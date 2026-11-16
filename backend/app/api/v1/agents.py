import json
import asyncio
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.responses import StreamingResponse
from backend.app.services.stream_manager import stream_manager

router = APIRouter(prefix="/agents", tags=["AI Agent Activity & Monitoring"])


@router.get("/stream/{session_id}")
async def stream_agent_events_sse(session_id: str):
    """
    Server-Sent Events (SSE) endpoint providing real-time streaming updates
    as each agent in the multi-agent pipeline completes steps.
    """
    queue = stream_manager.register_sse_queue(session_id)

    async def event_generator():
        try:
            # Yield initial connection confirmation
            yield f"data: {json.dumps({'type': 'connected', 'session_id': session_id})}\n\n"
            while True:
                try:
                    event = await asyncio.wait_for(queue.get(), timeout=20.0)
                    yield f"data: {json.dumps(event)}\n\n"
                except asyncio.TimeoutError:
                    # Keep-alive heartbeat
                    yield ": ping\n\n"
        except asyncio.CancelledError:
            pass
        finally:
            stream_manager.unregister_sse_queue(session_id, queue)

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"
        }
    )


@router.websocket("/ws/{session_id}")
async def agent_websocket_endpoint(websocket: WebSocket, session_id: str):
    """
    WebSocket endpoint for bidirectional interactive agent telemetry.
    """
    await websocket.accept()
    stream_manager.connect_websocket(session_id, websocket)
    
    # Send backlog of events for this session
    backlog = stream_manager.session_events.get(session_id, [])
    for ev in backlog:
        await websocket.send_text(json.dumps(ev))

    try:
        while True:
            # Keep socket open and listen for any client messages
            msg = await websocket.receive_text()
    except WebSocketDisconnect:
        stream_manager.disconnect_websocket(session_id, websocket)


@router.get("/tasks/{session_id}")
async def get_agent_tasks(session_id: str):
    """
    Returns agent execution metrics, tool calls, and completion status.
    """
    events = stream_manager.session_events.get(session_id, [])
    agent_status_map = {}
    for ev in events:
        agent_status_map[ev["agent_name"]] = {
            "name": ev["agent_name"],
            "status": ev["status"],
            "last_message": ev["message"],
            "step_index": ev.get("step_index", 0),
            "timestamp": ev.get("timestamp")
        }
    return {
        "session_id": session_id,
        "agents": list(agent_status_map.values()),
        "raw_events_count": len(events)
    }
