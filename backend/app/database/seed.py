import asyncio
import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from backend.app.database.session import AsyncSessionLocal, init_db
from backend.app.models.user import User
from backend.app.models.conversation import SearchSource
from backend.app.models.preference import UserPreference
from backend.app.models.product import Product, ProductVariant, ProductSpec
from backend.app.models.price import Seller, ProductPrice, PriceHistory
from backend.app.models.review import Review, ReviewAnalysis
from backend.app.security.password import get_password_hash


async def seed_database():
    await init_db()
    async with AsyncSessionLocal() as session:
        # Check if already seeded
        res = await session.execute(select(Product))
        if res.scalars().first():
            print("Database already contains product data.")
            return

        print("Seeding initial database data...")

        # 1. Default demo users
        demo_user = User(
            id="u_demo_user_001",
            email="demo@ecommerce-ai.com",
            hashed_password=get_password_hash("password123"),
            full_name="Alex Mercer",
            role="user",
            is_active=True
        )
        admin_user = User(
            id="u_admin_user_001",
            email="admin@ecommerce-ai.com",
            hashed_password=get_password_hash("admin123"),
            full_name="System Administrator",
            role="admin",
            is_active=True
        )
        session.add(demo_user)
        session.add(admin_user)
        await session.flush()

        # Demo user preferences / memory
        demo_pref = UserPreference(
            user_id=demo_user.id,
            preferred_brands=["Lenovo", "ASUS"],
            budget_max=80000.0,
            preferred_ram="32GB",
            preferred_storage="1TB",
            avoid_refurbished=True,
            excluded_keywords=["Refurbished", "Open Box"],
            currency="INR"
        )
        session.add(demo_pref)

        # 2. Verified Sellers
        seller_lenovo = Seller(
            id="s_lenovo_official",
            name="Lenovo Official Store",
            platform="Lenovo Direct",
            rating=4.8,
            review_count=15420,
            is_verified=True,
            policy_summary="30-day hassle-free replacement, 2-year on-site warranty"
        )
        seller_amazon = Seller(
            id="s_appario_amazon",
            name="Appario Retail (Amazon Authorized)",
            platform="Amazon India",
            rating=4.7,
            review_count=98200,
            is_verified=True,
            policy_summary="7-day service center return, GST invoice provided"
        )
        seller_croma = Seller(
            id="s_croma_retail",
            name="Croma Electronics Ltd.",
            platform="Croma",
            rating=4.6,
            review_count=34100,
            is_verified=True,
            policy_summary="Store pickup available in 2 hours, Tata brand assurance"
        )
        seller_flipkart = Seller(
            id="s_supercom_flipkart",
            name="SuperComNet (Flipkart Assured)",
            platform="Flipkart",
            rating=4.5,
            review_count=71200,
            is_verified=True,
            policy_summary="Flipkart Assured guarantee, Brand warranty"
        )
        session.add_all([seller_lenovo, seller_amazon, seller_croma, seller_flipkart])
        await session.flush()

        # 3. Products
        products_data = [
            {
                "id": "prod_lenovo_legion_slim5",
                "name": "Lenovo Legion Slim 5 AMD Ryzen 7 8845HS",
                "brand": "Lenovo",
                "model": "Legion Slim 5 16AHP9",
                "category": "laptop",
                "description": "High-performance AI development and gaming laptop featuring AMD Ryzen 7 8845HS with dedicated Ryzen AI NPU and NVIDIA RTX 4060 graphics.",
                "main_image": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80",
                "product_url": "https://www.lenovo.com/in/en/p/laptops/legion-laptops/legion-slim-series/legion-slim-5-gen-9-16-inch-amd/len101g0036",
                "source": "Lenovo Official & Authorized Partners",
                "rating": 4.6,
                "review_count": 842,
                "trust_score": 1.0,
                "is_verified": True,
                "specs": {
                    "ram_gb": 32, "storage_gb": 1024,
                    "cpu": "AMD Ryzen 7 8845HS (8C/16T, up to 5.1GHz, 38 TOPS NPU)",
                    "gpu": "NVIDIA GeForce RTX 4060 8GB GDDR6 (140W TGP)",
                    "screen_size_inches": 16.0, "battery_life_hours": 8.0,
                    "weight_kg": 2.3, "os": "Windows 11 Home", "warranty_months": 24,
                    "raw_specs": {"Display": "16\" WQXGA 165Hz 100% sRGB", "Ports": "USB-C USB4, HDMI 2.1, RJ-45", "Charger": "230W Slim Tip"}
                },
                "prices": [
                    {"seller_id": seller_lenovo.id, "current": 79990.0, "orig": 94990.0, "avail": "In Stock", "shipping": 0.0},
                    {"seller_id": seller_amazon.id, "current": 81490.0, "orig": 94990.0, "avail": "In Stock", "shipping": 0.0}
                ],
                "reviews": [
                    {"author": "Rohan M.", "rating": 5.0, "source": "Amazon India", "sentiment": "Positive", "text": "Runs local LLM quantizations (Llama 3 8B) on the RTX 4060 with zero throttling. 32GB RAM makes Docker and PyTorch effortless."},
                    {"author": "Vikram K.", "rating": 4.5, "source": "Lenovo Store", "sentiment": "Positive", "text": "Solid build quality and keyboard ergonomics. The screen resolution is crisp. Power brick is large but battery lasts 7+ hours in hybrid mode."}
                ],
                "analysis": {
                    "positive_pct": 88.0, "neutral_pct": 8.0, "negative_pct": 4.0,
                    "positive_themes": ["Exceptional PyTorch AI performance", "Superb 165Hz color-accurate display", "Effective dual-fan cooling", "Upgradable RAM slots"],
                    "negative_themes": ["Heavy power brick (230W)", "Speakers could have deeper bass"],
                    "common_complaints": ["Bulky adapter adds carrying weight for travel", "Slight fan whine under maximum synthetic stress"],
                    "warnings": ["Ensure BIOS update from Vantage app to optimize battery switching profile."],
                    "aspect_scores": {"battery": 4.2, "performance": 4.9, "heating": 4.5, "display": 4.8, "build_quality": 4.7, "software": 4.3}
                }
            },
            {
                "id": "prod_asus_tuf_a15",
                "name": "ASUS TUF Gaming A15 (2024) AMD Ryzen 7 7735HS",
                "brand": "ASUS",
                "model": "FA507NV-LP023W",
                "category": "laptop",
                "description": "Durable MIL-STD-810H certified gaming and programming laptop with massive 90WHr battery and NVIDIA GeForce RTX 4060.",
                "main_image": "https://images.unsplash.com/photo-1588872657578-7efd1f1555ed?auto=format&fit=crop&w=800&q=80",
                "product_url": "https://www.amazon.in/dp/B0CXF335N6",
                "source": "Amazon India (Authorized Cloudtail)",
                "rating": 4.4,
                "review_count": 1280,
                "trust_score": 0.95,
                "is_verified": True,
                "specs": {
                    "ram_gb": 32, "storage_gb": 1024,
                    "cpu": "AMD Ryzen 7 7735HS (8C/16T, up to 4.75GHz)",
                    "gpu": "NVIDIA GeForce RTX 4060 8GB GDDR6 (140W)",
                    "screen_size_inches": 15.6, "battery_life_hours": 7.5,
                    "weight_kg": 2.2, "os": "Windows 11 Home", "warranty_months": 12,
                    "raw_specs": {"Display": "15.6\" FHD 144Hz", "Battery": "90WHr 4-cell", "Keyboard": "RGB Backlit"}
                },
                "prices": [
                    {"seller_id": seller_amazon.id, "current": 74990.0, "orig": 86990.0, "avail": "In Stock", "shipping": 0.0},
                    {"seller_id": seller_croma.id, "current": 76990.0, "orig": 86990.0, "avail": "In Stock", "shipping": 0.0}
                ],
                "reviews": [
                    {"author": "Deepak S.", "rating": 4.5, "source": "Amazon India", "sentiment": "Positive", "text": "Best battery life among gaming laptops in this price bracket. The 90Wh battery easily gives 7 hours for coding."},
                    {"author": "Aditya V.", "rating": 4.0, "source": "Amazon India", "sentiment": "Neutral", "text": "Super performance in games and AI models. Screen is decent indoors, but slightly dim in direct sunlight."}
                ],
                "analysis": {
                    "positive_pct": 84.0, "neutral_pct": 11.0, "negative_pct": 5.0,
                    "positive_themes": ["Great battery life from 90WHr pack", "Excellent value for RTX 4060", "Durable military-spec chassis"],
                    "negative_themes": ["Display is 250 nits (average outdoors)", "Fans get audible under turbo mode"],
                    "common_complaints": ["Screen brightness is modest in sunlight", "Armoury Crate software can be bloated"],
                    "warnings": ["Check display color gamut (62.5% sRGB) if professional color grading is required."],
                    "aspect_scores": {"battery": 4.6, "performance": 4.7, "heating": 4.1, "display": 3.8, "build_quality": 4.4, "software": 3.9}
                }
            },
            {
                "id": "prod_acer_nitro_v15",
                "name": "Acer Nitro V 15 Intel Core i7-13620H",
                "brand": "Acer",
                "model": "ANV15-51",
                "category": "laptop",
                "description": "Budget-focused gaming and computing powerhouse featuring 13th Gen Intel Core i7 and RTX 4050.",
                "main_image": "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?auto=format&fit=crop&w=800&q=80",
                "product_url": "https://www.flipkart.com/acer-nitro-v-intel-core-i7-13th-gen",
                "source": "Flipkart (SuperComNet Verified)",
                "rating": 4.3,
                "review_count": 915,
                "trust_score": 0.90,
                "is_verified": True,
                "specs": {
                    "ram_gb": 16, "storage_gb": 1024,
                    "cpu": "Intel Core i7-13620H (10 Cores, 16 Threads)",
                    "gpu": "NVIDIA GeForce RTX 4050 6GB GDDR6",
                    "screen_size_inches": 15.6, "battery_life_hours": 5.0,
                    "weight_kg": 2.1, "os": "Windows 11 Home", "warranty_months": 12,
                    "raw_specs": {"Display": "15.6\" FHD 144Hz IPS", "Thermal": "Dual fan exhaust", "Audio": "DTS:X Ultra"}
                },
                "prices": [
                    {"seller_id": seller_flipkart.id, "current": 68990.0, "orig": 79990.0, "avail": "In Stock", "shipping": 0.0}
                ],
                "reviews": [
                    {"author": "Kunal P.", "rating": 4.0, "source": "Flipkart", "sentiment": "Neutral", "text": "Good raw CPU speed for compilation. You will definitely need to plug in the charger after 4 hours of development work."},
                    {"author": "Tanmay G.", "rating": 4.0, "source": "Flipkart", "sentiment": "Positive", "text": "Decent gaming and ML work on budget, but recommend upgrading to 32GB RAM."}
                ],
                "analysis": {
                    "positive_pct": 78.0, "neutral_pct": 14.0, "negative_pct": 8.0,
                    "positive_themes": ["Very affordable entry point for i7 13th gen", "Decent thermal airflow", "Good keyboard layout"],
                    "negative_themes": ["Battery life is only around 4.5 hours", "16GB RAM is single channel out of box"],
                    "common_complaints": ["Sub-5 hour battery life", "Plastic body feels less premium than metal competitors"],
                    "warnings": ["Needs a second RAM stick upgrade for optimal dual-channel memory bandwidth."],
                    "aspect_scores": {"battery": 3.2, "performance": 4.4, "heating": 3.9, "display": 4.0, "build_quality": 3.7, "software": 4.0}
                }
            },
            {
                "id": "prod_hp_victus_16",
                "name": "HP Victus Gaming Laptop 16 AMD Ryzen 7 7840HS",
                "brand": "HP",
                "model": "Victus 16-s0095AX",
                "category": "laptop",
                "description": "Sleek and professional design with AMD Ryzen 7 7840HS, 32GB RAM, and Omen Tempest Cooling architecture.",
                "main_image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=800&q=80",
                "product_url": "https://www.croma.com/hp-victus-16-gaming-laptop",
                "source": "Croma Electronics",
                "rating": 4.2,
                "review_count": 520,
                "trust_score": 0.92,
                "is_verified": True,
                "specs": {
                    "ram_gb": 32, "storage_gb": 1024,
                    "cpu": "AMD Ryzen 7 7840HS (8 Cores, 16 Threads)",
                    "gpu": "NVIDIA GeForce RTX 4050 6GB GDDR6",
                    "screen_size_inches": 16.1, "battery_life_hours": 6.5,
                    "weight_kg": 2.3, "os": "Windows 11 Home", "warranty_months": 12,
                    "raw_specs": {"Display": "16.1\" FHD 144Hz", "Cooling": "Omen Tempest", "Color": "Mica Silver"}
                },
                "prices": [
                    {"seller_id": seller_croma.id, "current": 76990.0, "orig": 89990.0, "avail": "In Stock", "shipping": 0.0}
                ],
                "reviews": [
                    {"author": "Amit R.", "rating": 4.0, "source": "Croma", "sentiment": "Positive", "text": "Looks very sleek for college and office. Fast enough for coding, though screen has slight wobble on moving desks."}
                ],
                "analysis": {
                    "positive_pct": 81.0, "neutral_pct": 13.0, "negative_pct": 6.0,
                    "positive_themes": ["Clean non-aggressive aesthetics suitable for office", "Quiet idle fans", "Comfortable keypad"],
                    "negative_themes": ["Noticeable screen wobble when typing vigorously", "RTX 4050 has lower VRAM (6GB)"],
                    "common_complaints": ["Hinge wobble", "Lower graphics headroom compared to 4060"],
                    "warnings": ["6GB VRAM may limit larger batch sizes during local deep learning training."],
                    "aspect_scores": {"battery": 4.1, "performance": 4.3, "heating": 4.2, "display": 4.0, "build_quality": 3.6, "software": 4.1}
                }
            }
        ]

        for p_data in products_data:
            p = Product(
                id=p_data["id"],
                name=p_data["name"],
                brand=p_data["brand"],
                model=p_data["model"],
                category=p_data["category"],
                description=p_data["description"],
                main_image=p_data["main_image"],
                product_url=p_data["product_url"],
                source=p_data["source"],
                rating=p_data["rating"],
                review_count=p_data["review_count"],
                trust_score=p_data["trust_score"],
                is_verified=p_data["is_verified"]
            )
            session.add(p)
            await session.flush()

            # Specs
            sp = p_data["specs"]
            spec_obj = ProductSpec(
                product_id=p.id,
                ram_gb=sp["ram_gb"],
                storage_gb=sp["storage_gb"],
                cpu=sp["cpu"],
                gpu=sp["gpu"],
                screen_size_inches=sp["screen_size_inches"],
                battery_life_hours=sp["battery_life_hours"],
                weight_kg=sp["weight_kg"],
                os=sp["os"],
                warranty_months=sp["warranty_months"],
                raw_specs=sp["raw_specs"]
            )
            session.add(spec_obj)

            # Prices & History
            for pr in p_data["prices"]:
                discount = round(((pr["orig"] - pr["current"]) / pr["orig"]) * 100, 1) if pr["orig"] > 0 else 0
                price_obj = ProductPrice(
                    product_id=p.id,
                    seller_id=pr["seller_id"],
                    current_price=pr["current"],
                    original_price=pr["orig"],
                    discount_percentage=discount,
                    currency="INR",
                    availability=pr["avail"],
                    shipping_cost=pr["shipping"]
                )
                session.add(price_obj)

                # History entries
                now = datetime.datetime.utcnow()
                session.add(PriceHistory(product_id=p.id, price=pr["orig"], recorded_at=now - datetime.timedelta(days=30)))
                session.add(PriceHistory(product_id=p.id, price=round(pr["orig"] * 0.98, -1), recorded_at=now - datetime.timedelta(days=20)))
                session.add(PriceHistory(product_id=p.id, price=round(pr["orig"] * 0.95, -1), recorded_at=now - datetime.timedelta(days=10)))
                session.add(PriceHistory(product_id=p.id, price=pr["current"], recorded_at=now))

            # Reviews
            for r in p_data["reviews"]:
                rev_obj = Review(
                    product_id=p.id,
                    author=r["author"],
                    rating=r["rating"],
                    source=r["source"],
                    sentiment=r["sentiment"],
                    review_text=r["text"]
                )
                session.add(rev_obj)

            # Review Analysis
            ana = p_data["analysis"]
            ana_obj = ReviewAnalysis(
                product_id=p.id,
                sentiment_positive_pct=ana["positive_pct"],
                sentiment_neutral_pct=ana["neutral_pct"],
                sentiment_negative_pct=ana["negative_pct"],
                positive_themes=ana["positive_themes"],
                negative_themes=ana["negative_themes"],
                common_complaints=ana["common_complaints"],
                important_warnings=ana["warnings"],
                aspect_scores=ana["aspect_scores"],
                analyzed_review_count=p_data["review_count"]
            )
            session.add(ana_obj)

        # 3. Seed Configured Authorized Search Sources
        initial_sources = [
            {"name": "Amazon India", "source_type": "marketplace", "base_url": "https://www.amazon.in", "health_status": "operational"},
            {"name": "Flipkart", "source_type": "marketplace", "base_url": "https://www.flipkart.com", "health_status": "operational"},
            {"name": "Croma", "source_type": "retailer", "base_url": "https://www.croma.com", "health_status": "operational"},
            {"name": "Reliance Digital", "source_type": "retailer", "base_url": "https://www.reliancedigital.in", "health_status": "operational"},
            {"name": "Tata CLiQ", "source_type": "retailer", "base_url": "https://www.tatacliq.com", "health_status": "operational"},
            {"name": "Vijay Sales", "source_type": "retailer", "base_url": "https://www.vijaysales.com", "health_status": "operational"},
            {"name": "Lenovo Official Store", "source_type": "brand", "base_url": "https://www.lenovo.com/in/en/", "health_status": "operational"},
            {"name": "ASUS Official Store", "source_type": "brand", "base_url": "https://in.store.asus.com", "health_status": "operational"},
            {"name": "Samsung Official Store", "source_type": "brand", "base_url": "https://www.samsung.com/in/", "health_status": "operational"},
            {"name": "Apple India Store", "source_type": "brand", "base_url": "https://www.apple.com/in/store", "health_status": "operational"},
        ]
        for src in initial_sources:
            session.add(SearchSource(
                name=src["name"],
                source_type=src["source_type"],
                base_url=src["base_url"],
                is_active=True,
                health_status=src["health_status"]
            ))

        await session.commit()
        print("Database seeded successfully with users, verified sellers, and products.")


if __name__ == "__main__":
    asyncio.run(seed_database())
