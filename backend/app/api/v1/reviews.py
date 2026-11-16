from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db
from backend.app.models.review import Review, ReviewAnalysis
from backend.app.schemas.review import ReviewSchema, ReviewAnalysisResponse

router = APIRouter(prefix="/reviews", tags=["Review Intelligence"])


@router.get("/{product_id}", response_model=List[ReviewSchema])
async def get_product_reviews(product_id: str, db: AsyncSession = Depends(get_db)):
    stmt = select(Review).where(Review.product_id == product_id).order_by(Review.review_date.desc())
    res = await db.execute(stmt)
    reviews = res.scalars().all()
    return reviews


@router.get("/{product_id}/analysis", response_model=ReviewAnalysisResponse)
async def get_review_analysis(product_id: str, db: AsyncSession = Depends(get_db)):
    stmt = select(ReviewAnalysis).where(ReviewAnalysis.product_id == product_id)
    res = await db.execute(stmt)
    analysis = res.scalar_one_or_none()

    if not analysis:
        raise HTTPException(status_code=404, detail="Review analysis not available for this product.")
    return analysis
