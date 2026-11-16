import asyncio
import json
from typing import Dict, List, Any
from fastapi import WebSocket


class AgentStreamManager:
    """
    Broadcasts real-time multi-agent execution events to active SSE connections and WebSockets.
    """
    def __init__(self):
        self.active_websockets: Dict[str, List[WebSocket]] = {}
        self.active_sse_queues: Dict[str, List[asyncio.Queue]] = {}
        self.session_events: Dict[str, List[Dict[str, Any]]] = {}

    def connect_websocket(self, session_id: str, websocket: WebSocket):
        if session_id not in self.active_websockets:
            self.active_websockets[session_id] = []
        self.active_websockets[session_id].append(websocket)

    def disconnect_websocket(self, session_id: str, websocket: WebSocket):
        if session_id in self.active_websockets:
            self.active_websockets[session_id] = [ws for ws in self.active_websockets[session_id] if ws != websocket]

    def register_sse_queue(self, session_id: str) -> asyncio.Queue:
        q = asyncio.Queue()
        if session_id not in self.active_sse_queues:
            self.active_sse_queues[session_id] = []
        self.active_sse_queues[session_id].append(q)
        
        # Replay past events if any
        if session_id in self.session_events:
            for ev in self.session_events[session_id]:
                q.put_nowait(ev)
        return q

    def unregister_sse_queue(self, session_id: str, queue: asyncio.Queue):
        if session_id in self.active_sse_queues:
            self.active_sse_queues[session_id] = [q for q in self.active_sse_queues[session_id] if q != queue]

    async def broadcast_event(self, session_id: str, event_data: Dict[str, Any]):
        if session_id not in self.session_events:
            self.session_events[session_id] = []
        self.session_events[session_id].append(event_data)

        # 1. Broadcast to WebSockets
        if session_id in self.active_websockets:
            dead_ws = []
            for ws in self.active_websockets[session_id]:
                try:
                    await ws.send_text(json.dumps(event_data))
                except Exception:
                    dead_ws.append(ws)
            for d in dead_ws:
                self.active_websockets[session_id].remove(d)

        # 2. Broadcast to SSE queues
        if session_id in self.active_sse_queues:
            for q in self.active_sse_queues[session_id]:
                try:
                    q.put_nowait(event_data)
                except Exception:
                    pass


stream_manager = AgentStreamManager()
