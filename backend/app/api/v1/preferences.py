from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.models.preference import UserPreference
from backend.app.schemas.preference import PreferenceUpdate, PreferenceResponse
from backend.app.security.dependencies import get_current_user

router = APIRouter(prefix="/preferences", tags=["Shopping Preferences / Memory"])


@router.get("", response_model=PreferenceResponse)
async def get_preferences(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(UserPreference).where(UserPreference.user_id == current_user.id)
    res = await db.execute(stmt)
    pref = res.scalar_one_or_none()

    if not pref:
        pref = UserPreference(user_id=current_user.id)
        db.add(pref)
        await db.commit()
        await db.refresh(pref)

    return pref


@router.put("", response_model=PreferenceResponse)
async def update_preferences(
    req: PreferenceUpdate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(UserPreference).where(UserPreference.user_id == current_user.id)
    res = await db.execute(stmt)
    pref = res.scalar_one_or_none()

    if not pref:
        pref = UserPreference(user_id=current_user.id)
        db.add(pref)

    if req.preferred_brands is not None:
        pref.preferred_brands = req.preferred_brands
    if req.budget_max is not None:
        pref.budget_max = req.budget_max
    if req.preferred_ram is not None:
        pref.preferred_ram = req.preferred_ram
    if req.preferred_storage is not None:
        pref.preferred_storage = req.preferred_storage
    if req.avoid_refurbished is not None:
        pref.avoid_refurbished = req.avoid_refurbished
    if req.excluded_keywords is not None:
        pref.excluded_keywords = req.excluded_keywords
    if req.currency is not None:
        pref.currency = req.currency

    await db.commit()
    await db.refresh(pref)
    return pref


@router.delete("", response_model=dict)
async def reset_preferences(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    stmt = select(UserPreference).where(UserPreference.user_id == current_user.id)
    res = await db.execute(stmt)
    pref = res.scalar_one_or_none()

    if pref:
        pref.preferred_brands = []
        pref.budget_max = None
        pref.preferred_ram = None
        pref.preferred_storage = None
        pref.avoid_refurbished = True
        pref.excluded_keywords = []
        await db.commit()

    return {"message": "Shopping memory preferences reset successfully"}
