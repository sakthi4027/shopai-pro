from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.models.agent_log import AuditLog
from backend.app.security.dependencies import get_current_user

router = APIRouter(prefix="/audit", tags=["Security & Compliance Audit"])


@router.get("")
async def get_audit_logs(
    limit: int = Query(default=50, le=100),
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    # Admins see full system logs; standard users see only their own action logs
    if current_user.role == "admin":
        stmt = select(AuditLog).order_by(AuditLog.timestamp.desc()).limit(limit)
    else:
        stmt = (
            select(AuditLog)
            .where(AuditLog.user_id == current_user.id)
            .order_by(AuditLog.timestamp.desc())
            .limit(limit)
        )

    res = await db.execute(stmt)
    logs = res.scalars().all()

    return [
        {
            "id": log.id,
            "action": log.action,
            "resource_type": log.resource_type,
            "resource_id": log.resource_id,
            "details": log.details,
            "ip_address": log.ip_address,
            "timestamp": log.timestamp.isoformat()
        }
        for log in logs
    ]
