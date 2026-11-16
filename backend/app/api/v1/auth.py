from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.models.preference import UserPreference
from backend.app.models.agent_log import AuditLog
from backend.app.schemas.auth import RegisterRequest, LoginRequest, Token, UserResponse
from backend.app.security.password import get_password_hash, verify_password
from backend.app.security.jwt import create_access_token
from backend.app.security.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=Token)
async def register(req: RegisterRequest, db: AsyncSession = Depends(get_db)):
    # Check if email exists
    stmt = select(User).where(User.email == req.email)
    res = await db.execute(stmt)
    if res.scalar_one_or_none():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An account with this email address already exists."
        )

    new_user = User(
        email=req.email,
        hashed_password=get_password_hash(req.password),
        full_name=req.full_name or req.email.split("@")[0].capitalize(),
        role="user",
        is_active=True
    )
    db.add(new_user)
    await db.flush()

    # Create default empty shopping preferences
    pref = UserPreference(user_id=new_user.id)
    db.add(pref)

    # Log audit event
    audit = AuditLog(
        user_id=new_user.id,
        action="USER_REGISTRATION",
        resource_type="User",
        resource_id=new_user.id,
        details={"email": new_user.email}
    )
    db.add(audit)
    await db.commit()
    await db.refresh(new_user)

    token = create_access_token({"sub": new_user.id, "role": new_user.role})
    return Token(
        access_token=token,
        token_type="bearer",
        user_id=new_user.id,
        email=new_user.email,
        full_name=new_user.full_name
    )


@router.post("/login", response_model=Token)
async def login(req: LoginRequest, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == req.email)
    res = await db.execute(stmt)
    user = res.scalar_one_or_none()

    if not user or not verify_password(req.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if not user.is_active:
        raise HTTPException(status_code=403, detail="User account is deactivated")

    audit = AuditLog(
        user_id=user.id,
        action="USER_LOGIN",
        resource_type="User",
        resource_id=user.id,
        details={"email": user.email}
    )
    db.add(audit)
    await db.commit()

    token = create_access_token({"sub": user.id, "role": user.role})
    return Token(
        access_token=token,
        token_type="bearer",
        user_id=user.id,
        email=user.email,
        full_name=user.full_name
    )


@router.get("/me", response_model=UserResponse)
async def get_me(current_user: User = Depends(get_current_user)):
    return current_user
