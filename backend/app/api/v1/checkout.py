import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import get_db
from backend.app.models.user import User
from backend.app.models.product import Product
from backend.app.models.price import ProductPrice, Seller
from backend.app.models.agent_log import AuditLog
from backend.app.schemas.checkout import (
    CheckoutReviewRequest,
    CheckoutReviewResponse,
    CheckoutConfirmationRequest,
    CheckoutConfirmationResponse
)
from backend.app.security.dependencies import get_current_user

router = APIRouter(prefix="/checkout", tags=["Human-in-the-Loop Checkout Assistance"])


@router.post("/review", response_model=CheckoutReviewResponse)
async def generate_checkout_review(
    req: CheckoutReviewRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Step 1: Gathers itemized pricing, seller credentials, and shipping terms.
    Constructs the Human Confirmation manifest. Zero financial transactions can occur here.
    """
    stmt = select(Product).where(Product.id == req.product_id)
    res = await db.execute(stmt)
    prod = res.scalar_one_or_none()
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")

    # Seller & price
    if req.seller_id:
        price_stmt = (
            select(ProductPrice, Seller)
            .join(Seller, ProductPrice.seller_id == Seller.id)
            .where(ProductPrice.product_id == prod.id, ProductPrice.seller_id == req.seller_id)
        )
    else:
        price_stmt = (
            select(ProductPrice, Seller)
            .join(Seller, ProductPrice.seller_id == Seller.id)
            .where(ProductPrice.product_id == prod.id)
            .order_by(ProductPrice.current_price.asc())
        )
    price_res = await db.execute(price_stmt)
    row = price_res.first()

    if not row:
        raise HTTPException(status_code=400, detail="No active seller pricing available for this product.")

    pp, seller = row
    base_price = pp.current_price
    shipping_cost = pp.shipping_cost
    estimated_tax = 0.0  # Inclusive GST in Indian retail pricing
    total_cost = base_price + shipping_cost + estimated_tax

    # Audit log entry for review attempt
    audit = AuditLog(
        user_id=current_user.id,
        action="CHECKOUT_REVIEW_GENERATED",
        resource_type="Product",
        resource_id=prod.id,
        details={
            "product_name": prod.name,
            "seller_name": seller.name,
            "total_cost": total_cost,
            "human_approval_pending": True
        }
    )
    db.add(audit)
    await db.commit()

    return CheckoutReviewResponse(
        product_id=prod.id,
        product_name=prod.name,
        brand=prod.brand,
        model=prod.model,
        seller_id=seller.id,
        seller_name=seller.name,
        seller_rating=seller.rating,
        base_price=base_price,
        shipping_cost=shipping_cost,
        estimated_tax=estimated_tax,
        total_cost=total_cost,
        currency="INR",
        estimated_delivery=pp.estimated_delivery_days,
        human_confirmation_required=True,
        security_warning="⚠️ HUMAN CONFIRMATION REQUIRED: Review all details before approving. No payment occurs without your explicit confirmation. Card details are NEVER stored."
    )


@router.post("/confirm", response_model=CheckoutConfirmationResponse)
async def confirm_checkout(
    req: CheckoutConfirmationRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """
    Step 2: Explicit Human Approval Gate.
    User MUST click [Confirm] to proceed to external authorized store.
    If [Cancel] or not confirmed, aborts immediately without touching any service.
    """
    confirmation_id = str(uuid.uuid4())

    if not req.user_confirmed:
        audit = AuditLog(
            user_id=current_user.id,
            action="CHECKOUT_CANCELLED_BY_USER",
            resource_type="Product",
            resource_id=req.product_id,
            details={"confirmation_id": confirmation_id, "notes": req.user_notes}
        )
        db.add(audit)
        await db.commit()
        return CheckoutConfirmationResponse(
            confirmation_id=confirmation_id,
            status="CANCELLED",
            message="Purchase cancelled by user. No financial transaction or external redirection initiated.",
            external_checkout_url=None,
            audit_logged=True
        )

    # Fetch product link
    prod_stmt = select(Product).where(Product.id == req.product_id)
    prod_res = await db.execute(prod_stmt)
    prod = prod_res.scalar_one_or_none()
    target_url = prod.product_url if prod else "https://amazon.in"

    # User explicitly confirmed! Record immutable audit record.
    audit = AuditLog(
        user_id=current_user.id,
        action="CHECKOUT_APPROVED_BY_USER",
        resource_type="Product",
        resource_id=req.product_id,
        details={
            "confirmation_id": confirmation_id,
            "total_amount": req.total_amount,
            "seller_id": req.seller_id,
            "user_notes": req.user_notes
        }
    )
    db.add(audit)
    await db.commit()

    return CheckoutConfirmationResponse(
        confirmation_id=confirmation_id,
        status="APPROVED_READY_FOR_REDIRECT",
        message="Purchase approved! You will now be redirected securely to the merchant's official site to complete payment yourself.",
        external_checkout_url=target_url,
        audit_logged=True
    )
