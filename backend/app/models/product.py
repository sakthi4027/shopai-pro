import uuid
from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, Boolean, DateTime, ForeignKey, JSON, Text
from sqlalchemy.orm import relationship
from backend.app.database.session import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    name = Column(String(500), nullable=False, index=True)
    brand = Column(String(100), nullable=True, index=True)
    model = Column(String(100), nullable=True)
    category = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    main_image = Column(String(1000), nullable=True)
    product_url = Column(String(1000), nullable=True)
    source = Column(String(100), nullable=False, index=True)  # e.g. "Amazon India", "Flipkart", "Croma"
    
    # Aggregated metrics
    rating = Column(Float, default=0.0)
    review_count = Column(Integer, default=0)
    trust_score = Column(Float, default=1.0)  # 0.0 to 1.0 from Trust Agent
    trust_warning = Column(String(500), nullable=True)
    is_verified = Column(Boolean, default=True)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    last_checked = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    variants = relationship("ProductVariant", back_populates="product", cascade="all, delete-orphan")
    specs = relationship("ProductSpec", back_populates="product", cascade="all, delete-orphan")
    prices = relationship("ProductPrice", back_populates="product", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="product", cascade="all, delete-orphan")
    review_analyses = relationship("ReviewAnalysis", back_populates="product", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="product", cascade="all, delete-orphan")
    saved_by = relationship("SavedProduct", back_populates="product", cascade="all, delete-orphan")
    alerts = relationship("Alert", back_populates="product", cascade="all, delete-orphan")


class ProductVariant(Base):
    __tablename__ = "product_variants"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    product_id = Column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    sku = Column(String(100), nullable=True)
    title = Column(String(255), nullable=False)
    color = Column(String(50), nullable=True)
    storage_option = Column(String(50), nullable=True)
    ram_option = Column(String(50), nullable=True)
    extra_attributes = Column(JSON, default=dict)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    product = relationship("Product", back_populates="variants")


class ProductSpec(Base):
    __tablename__ = "product_specs"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    product_id = Column(String(36), ForeignKey("products.id", ondelete="CASCADE"), nullable=False, index=True)
    
    # Normalized critical technical specs
    ram_gb = Column(Integer, nullable=True, index=True)
    storage_gb = Column(Integer, nullable=True, index=True)
    cpu = Column(String(150), nullable=True)
    gpu = Column(String(150), nullable=True)
    screen_size_inches = Column(Float, nullable=True)
    battery_life_hours = Column(Float, nullable=True)
    os = Column(String(100), nullable=True)
    weight_kg = Column(Float, nullable=True)
    warranty_months = Column(Integer, nullable=True)
    
    # Raw extracted attributes
    raw_specs = Column(JSON, default=dict)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    product = relationship("Product", back_populates="specs")
