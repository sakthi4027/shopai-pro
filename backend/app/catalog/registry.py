import re
from typing import Dict, Any, List, Optional
from datetime import datetime

# ==============================================================================
# SHOPAI PRO — COMPREHENSIVE MULTI-CATEGORY PRODUCT REGISTRY (ALL 17 CATEGORIES)
# Every product implements all 28 canonical e-commerce fields and hierarchical variants.
# ==============================================================================

UNIVERSAL_PRODUCT_CATALOG: List[Dict[str, Any]] = [
    # --------------------------------------------------------------------------
    # 1. ELECTRONICS: Laptops
    # --------------------------------------------------------------------------
    {
        "product_id": "ELEC-LAP-ASUS-F15",
        "product_name": "ASUS TUF Gaming F15 (15.6 inch FHD 144Hz, Intel Core i7-13620H, 16GB RAM, 1TB SSD, NVIDIA RTX 4060 8GB, Win 11)",
        "category": "electronics",
        "subcategory": "laptops",
        "brand": "ASUS",
        "model": "TUF Gaming F15 FX507ZV",
        "variant": "16GB RAM / 1TB SSD / Mecha Gray",
        "sku": "FX507ZV-LP094W",
        "gtin_upc_ean": "4711387123456",
        "product_description": "High-performance gaming and AI engineering laptop equipped with 10-core 13th Gen Intel Core i7-13620H processor, 140W max TGP NVIDIA GeForce RTX 4060 GPU with MUX Switch, 16GB high-speed DDR5 RAM (expandable to 32GB), 1TB NVMe PCIe 4.0 SSD, and 90Wh all-day battery life with fast charge.",
        "images": [
            "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.youtube.com/watch?v=FX507ZV_demo"],
        "specifications": {
            "ram_gb": 16,
            "storage_gb": 1024,
            "cpu": "Intel Core i7-13620H 13th Gen (10 Cores, 16 Threads)",
            "gpu": "NVIDIA GeForce RTX 4060 8GB GDDR6 (140W TGP)",
            "screen_size_inches": 15.6,
            "refresh_rate_hz": 144,
            "display_panel": "FHD IPS Anti-Glare 100% sRGB",
            "battery_life_hours": 7.5,
            "battery_capacity_wh": 90,
            "weight_kg": 2.2,
            "os": "Windows 11 Home",
            "ports": "Thunderbolt 4, USB 3.2 Gen 2 Type-C, HDMI 2.1, RJ45 LAN",
            "cooling": "Dual Arc Flow Fans with 4 Exhaust Vents",
            "warranty_months": 12
        },
        "variants": [
            {"name": "16GB RAM / 512GB SSD", "price": 74990.0, "mrp": 89990.0, "sku": "FX507ZV-512G"},
            {"name": "16GB RAM / 1TB SSD", "price": 79990.0, "mrp": 94990.0, "sku": "FX507ZV-1TB"},
            {"name": "32GB RAM / 1TB SSD", "price": 86990.0, "mrp": 104990.0, "sku": "FX507ZV-32G"}
        ],
        "current_price": 79990.0,
        "mrp": 94990.0,
        "discount_percentage": 15.8,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 18942,
        "seller": "Amazon India",
        "seller_rating": 4.6,
        "availability": "In Stock",
        "delivery_info": "Free Express Next-Day Delivery with Prime",
        "warranty": "1 Year Onsite Manufacturer Warranty + 1 Year Accidental Damage Protection",
        "return_policy": "7 Days Service Center Replacement",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B0D9BMBP3H",
        "affiliate_url": "https://www.amazon.in/dp/B0D9BMBP3H?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Appario Retail Pvt Ltd",
                "seller_rating": 4.6,
                "price": 79990.0,
                "original_price": 94990.0,
                "discount_percent": 15.8,
                "availability": "In Stock",
                "delivery_info": "Free Express Delivery",
                "product_url": "https://www.amazon.in/dp/B0D9BMBP3H",
                "condition": "Brand New with Manufacturer Warranty"
            },
            {
                "source": "Flipkart",
                "seller_name": "RetailNet Verified",
                "seller_rating": 4.5,
                "price": 81990.0,
                "original_price": 94990.0,
                "discount_percent": 13.7,
                "availability": "In Stock",
                "delivery_info": "Standard Delivery (2 Days)",
                "product_url": "https://www.flipkart.com/asus-tuf-gaming-f15-intel-core-i7-13th-gen-16-gb-1-tb-ssd-windows-11-home-8-gb-graphics-nvidia-geforce-rtx-4060-144-hz-fx507zv-lp094w-laptop/p/itm7e7ba0ad9bmbp",
                "condition": "Brand New"
            },
            {
                "source": "Croma",
                "seller_name": "Croma Electronics Official",
                "seller_rating": 4.4,
                "price": 82990.0,
                "original_price": 94990.0,
                "discount_percent": 12.6,
                "availability": "In Stock",
                "delivery_info": "Same Day Store Pickup Available",
                "product_url": "https://www.croma.com/asus-tuf-gaming-f15-intel-core-i7-13th-gen-gaming-laptop/p/274819",
                "condition": "Brand New Official Box"
            }
        ]
    },
    {
        "product_id": "ELEC-LAP-LENOVO-LOQ",
        "product_name": "Lenovo LOQ 15IRX9 (15.6 inch FHD 144Hz, Intel Core i7-13650HX, 16GB DDR5, 512GB SSD, NVIDIA RTX 4060 8GB 115W, Win 11)",
        "category": "electronics",
        "subcategory": "laptops",
        "brand": "Lenovo",
        "model": "LOQ 15IRX9",
        "variant": "16GB RAM / 512GB SSD / Luna Grey",
        "sku": "83DV00BEIN",
        "gtin_upc_ean": "197532890123",
        "product_description": "Powered by Intel 13th Gen Core i7-13650HX with 14 cores, paired with full 115W TGP RTX 4060, Lenovo LA1 AI chip for dynamic load balancing, hyperchamber thermal design, and 100% sRGB color calibrated screen.",
        "images": [
            "https://m.media-amazon.com/images/I/71c5W9NxN5L._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/81xU+c8F4KL._SL1500_.jpg"
        ],
        "videos": ["https://www.youtube.com/watch?v=LOQ_15IRX9"],
        "specifications": {
            "ram_gb": 16,
            "storage_gb": 512,
            "cpu": "Intel Core i7-13650HX 13th Gen (14 Cores, 20 Threads)",
            "gpu": "NVIDIA GeForce RTX 4060 8GB GDDR6 (115W TGP)",
            "screen_size_inches": 15.6,
            "refresh_rate_hz": 144,
            "display_panel": "FHD IPS 300 nits 100% sRGB G-Sync",
            "battery_life_hours": 6.0,
            "battery_capacity_wh": 60,
            "weight_kg": 2.38,
            "os": "Windows 11 Home",
            "warranty_months": 12
        },
        "variants": [
            {"name": "16GB RAM / 512GB SSD", "price": 77490.0, "mrp": 92990.0, "sku": "83DV00BEIN-512"},
            {"name": "16GB RAM / 1TB SSD", "price": 82990.0, "mrp": 98990.0, "sku": "83DV00BEIN-1TB"},
            {"name": "24GB RAM / 1TB SSD", "price": 87990.0, "mrp": 104990.0, "sku": "83DV00BEIN-24G"}
        ],
        "current_price": 77490.0,
        "mrp": 92990.0,
        "discount_percentage": 16.7,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 9280,
        "seller": "Flipkart",
        "seller_rating": 4.5,
        "availability": "In Stock",
        "delivery_info": "Free Standard 2-Day Delivery",
        "warranty": "1 Year Onsite + 1 Year Premium Care",
        "return_policy": "7 Days Replacement Policy",
        "source_website": "Flipkart",
        "product_url": "https://www.flipkart.com/lenovo-loq-intel-core-i7-13th-gen-13650hx-16-gb-512-gb-ssd-windows-11-home-8-graphics-nvidia-geforce-rtx-4060-15irx9-gaming-laptop/p/itmc5e0e0e0e0e0e",
        "affiliate_url": "https://www.flipkart.com/lenovo-loq-15irx9?affid=shopaipro",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Flipkart",
                "seller_name": "RetailNet Verified",
                "seller_rating": 4.5,
                "price": 77490.0,
                "original_price": 92990.0,
                "discount_percent": 16.7,
                "availability": "In Stock",
                "delivery_info": "Free Express Delivery",
                "product_url": "https://www.flipkart.com/lenovo-loq-intel-core-i7-13th-gen-13650hx-16-gb-512-gb-ssd-windows-11-home-8-graphics-nvidia-geforce-rtx-4060-15irx9-gaming-laptop/p/itmc5e0e0e0e0e0e",
                "condition": "Brand New"
            },
            {
                "source": "Amazon",
                "seller_name": "Appario Retail Pvt Ltd",
                "seller_rating": 4.6,
                "price": 78990.0,
                "original_price": 92990.0,
                "discount_percent": 15.1,
                "availability": "In Stock",
                "delivery_info": "Free Prime Delivery",
                "product_url": "https://www.amazon.in/dp/B0CX8XNVF3",
                "condition": "Brand New with Manufacturer Warranty"
            }
        ]
    },
    {
        "product_id": "ELEC-LAP-ACER-NITRO-32G",
        "product_name": "Acer Nitro V 15 Gaming Laptop (15.6 inch FHD 144Hz, 13th Gen Intel Core i7-13620H, 32GB DDR5 RAM, 1TB SSD, RTX 4060 8GB, Win 11)",
        "category": "electronics",
        "subcategory": "laptops",
        "brand": "Acer",
        "model": "Nitro V 15 ANV15-51",
        "variant": "32GB RAM / 1TB SSD / Obsidian Black",
        "sku": "ANV15-51-789X",
        "gtin_upc_ean": "4711121543219",
        "product_description": "Pre-configured with 32GB dual-channel DDR5 RAM specifically for demanding machine learning workloads, LLM inference, and AAA gaming. Includes 1TB NVMe Gen4 SSD and NVIDIA RTX 4060 8GB GDDR6.",
        "images": [
            "https://m.media-amazon.com/images/I/71czGb00k5L._SL1500_.jpg"
        ],
        "videos": [],
        "specifications": {
            "ram_gb": 32,
            "storage_gb": 1024,
            "cpu": "Intel Core i7-13620H 13th Gen",
            "gpu": "NVIDIA GeForce RTX 4060 8GB GDDR6",
            "screen_size_inches": 15.6,
            "refresh_rate_hz": 144,
            "display_panel": "FHD IPS 144Hz Slim Bezel",
            "battery_life_hours": 8.0,
            "battery_capacity_wh": 57,
            "weight_kg": 2.1,
            "os": "Windows 11 Home",
            "warranty_months": 12
        },
        "variants": [
            {"name": "16GB RAM / 512GB SSD", "price": 72990.0, "mrp": 87990.0, "sku": "ANV15-16G-512"},
            {"name": "32GB RAM / 1TB SSD", "price": 79990.0, "mrp": 94990.0, "sku": "ANV15-32G-1TB"}
        ],
        "current_price": 79990.0,
        "mrp": 94990.0,
        "discount_percentage": 15.8,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 8120,
        "seller": "Amazon India",
        "seller_rating": 4.6,
        "availability": "In Stock",
        "delivery_info": "Free Express Delivery",
        "warranty": "1 Year International Travelers Warranty",
        "return_policy": "7 Days Return/Exchange",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B0CKYM56NP",
        "affiliate_url": "https://www.amazon.in/dp/B0CKYM56NP?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Appario Retail Pvt Ltd",
                "seller_rating": 4.6,
                "price": 79990.0,
                "original_price": 94990.0,
                "discount_percent": 15.8,
                "availability": "In Stock",
                "delivery_info": "Free Express Delivery",
                "product_url": "https://www.amazon.in/dp/B0CKYM56NP",
                "condition": "Brand New with Manufacturer Warranty"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 1. ELECTRONICS: Mobile Phones
    # --------------------------------------------------------------------------
    {
        "product_id": "ELEC-MOB-IPHONE-15",
        "product_name": "Apple iPhone 15 (128 GB) - Black",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "Apple",
        "model": "iPhone 15",
        "variant": "128GB / Black",
        "sku": "MTP03HN/A",
        "gtin_upc_ean": "0195949038235",
        "product_description": "Dynamic Island brings alerts and Live Activities right to the top of your screen. 48MP Main camera with 2x Telephoto lens captures super-high-resolution photos with next-generation portraits. Powered by the A16 Bionic chip with USB-C universal charging port.",
        "images": [
            "https://m.media-amazon.com/images/I/71657TiFeHL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/71d7rfSl0wL._SL1500_.jpg"
        ],
        "videos": ["https://www.apple.com/iphone-15/video"],
        "specifications": {
            "display": "6.1-inch Super Retina XDR OLED (2556 x 1179) 2000 nits peak",
            "processor": "Apple A16 Bionic (6-core CPU, 5-core GPU, 16-core Neural Engine)",
            "ram_gb": 6,
            "storage_gb": 128,
            "camera": "48MP Main (f/1.6 OIS) + 12MP Ultra-Wide (f/2.4) + 12MP TrueDepth Front",
            "battery_mah": 3349,
            "charging": "USB-C, 20W Fast Charging, 15W MagSafe Wireless",
            "water_resistance": "IP68 (6 meters up to 30 mins)",
            "os": "iOS 17 (Upgradable to iOS 18)",
            "warranty_months": 12
        },
        "variants": [
            {"name": "128GB / Black", "price": 65999.0, "mrp": 79900.0, "sku": "IPH15-128-BLK"},
            {"name": "256GB / Black", "price": 75999.0, "mrp": 89900.0, "sku": "IPH15-256-BLK"},
            {"name": "512GB / Black", "price": 95999.0, "mrp": 109900.0, "sku": "IPH15-512-BLK"},
            {"name": "128GB / Blue", "price": 65999.0, "mrp": 79900.0, "sku": "IPH15-128-BLU"},
            {"name": "128GB / Pink", "price": 65999.0, "mrp": 79900.0, "sku": "IPH15-128-PNK"}
        ],
        "current_price": 65999.0,
        "mrp": 79900.0,
        "discount_percentage": 17.4,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 42180,
        "seller": "Amazon India",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Prime One-Day Delivery",
        "warranty": "1 Year Apple Limited Warranty with AppleCare Support",
        "return_policy": "7 Days Replacement Policy",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B0CHX1W1XY",
        "affiliate_url": "https://www.amazon.in/dp/B0CHX1W1XY?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Appario Retail Pvt Ltd",
                "seller_rating": 4.8,
                "price": 65999.0,
                "original_price": 79900.0,
                "discount_percent": 17.4,
                "availability": "In Stock",
                "delivery_info": "Next Day Delivery",
                "product_url": "https://www.amazon.in/dp/B0CHX1W1XY",
                "condition": "Brand New Sealed Official Indian Unit"
            },
            {
                "source": "Flipkart",
                "seller_name": "SuperComNet Official",
                "seller_rating": 4.7,
                "price": 66499.0,
                "original_price": 79900.0,
                "discount_percent": 16.8,
                "availability": "In Stock",
                "delivery_info": "Free Standard 2-Day Delivery",
                "product_url": "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4",
                "condition": "Brand New Official Box"
            },
            {
                "source": "Croma",
                "seller_name": "Croma Apple Authorized Reseller",
                "seller_rating": 4.6,
                "price": 66990.0,
                "original_price": 79900.0,
                "discount_percent": 16.2,
                "availability": "In Stock",
                "delivery_info": "Same Day In-Store Pickup",
                "product_url": "https://www.croma.com/apple-iphone-15-128gb-black/p/300652",
                "condition": "Brand New"
            }
        ]
    },
    {
        "product_id": "ELEC-MOB-SAMS-S24",
        "product_name": "Samsung Galaxy S24 5G (8GB RAM, 256GB Storage, Onyx Black)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "Samsung",
        "model": "Galaxy S24",
        "variant": "8GB RAM / 256GB / Onyx Black",
        "sku": "SM-S921B",
        "gtin_upc_ean": "8806095345678",
        "product_description": "Powered by Galaxy AI: Circle to Search with Google, Live Translate voice calls in real time, Note Assist, and Photo Assist. 50MP ProVisual Engine camera system, Dynamic AMOLED 2X 120Hz display with 2600 nits peak brightness and 7 years of Android OS updates.",
        "images": [
            "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.samsung.com/galaxy-s24"],
        "specifications": {
            "display": "6.2-inch Dynamic AMOLED 2X FHD+ (1-120Hz LTPO, 2600 nits peak)",
            "processor": "Samsung Exynos 2400 Deca-Core 4nm AI Processor",
            "ram_gb": 8,
            "storage_gb": 256,
            "camera": "50MP Dual Pixel OIS + 12MP Ultra-Wide + 10MP 3x Optical Telephoto",
            "battery_mah": 4000,
            "charging": "25W Super Fast Charging + 15W Fast Wireless Charging 2.0",
            "os": "One UI 6.1 based on Android 14 (7 Years OS Upgrades)",
            "warranty_months": 12
        },
        "variants": [
            {"name": "8GB / 128GB Onyx Black", "price": 64999.0, "mrp": 74999.0, "sku": "S24-128-BLK"},
            {"name": "8GB / 256GB Onyx Black", "price": 69999.0, "mrp": 79999.0, "sku": "S24-256-BLK"},
            {"name": "8GB / 256GB Cobalt Violet", "price": 69999.0, "mrp": 79999.0, "sku": "S24-256-VLT"}
        ],
        "current_price": 69999.0,
        "mrp": 79999.0,
        "discount_percentage": 12.5,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 28430,
        "seller": "Amazon India",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Next-Day Delivery",
        "warranty": "1 Year Comprehensive Manufacturer Warranty on Phone, 6 Months on Accessories",
        "return_policy": "7 Days Replacement",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B0CS5X8T1C",
        "affiliate_url": "https://www.amazon.in/dp/B0CS5X8T1C?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "STPL Exclusive",
                "seller_rating": 4.7,
                "price": 69999.0,
                "original_price": 79999.0,
                "discount_percent": 12.5,
                "availability": "In Stock",
                "delivery_info": "Express Delivery",
                "product_url": "https://www.amazon.in/dp/B0CS5X8T1C",
                "condition": "Brand New Sealed"
            },
            {
                "source": "Flipkart",
                "seller_name": "RetailNet Samsung Store",
                "seller_rating": 4.6,
                "price": 70499.0,
                "original_price": 79999.0,
                "discount_percent": 11.9,
                "availability": "In Stock",
                "delivery_info": "2 Days Delivery",
                "product_url": "https://www.flipkart.com/samsung-galaxy-s24-5g-onyx-black-256-gb/p/itm5b94c4bbbbbb0",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 2. FASHION: Footwear (Running Shoes)
    # --------------------------------------------------------------------------
    {
        "product_id": "FASH-FOOT-NIKE-PEGASUS",
        "product_name": "Nike Air Zoom Pegasus 40 Men's Road Running Shoes",
        "category": "fashion",
        "subcategory": "footwear",
        "brand": "Nike",
        "model": "Air Zoom Pegasus 40",
        "variant": "Size UK 9 / Black & White",
        "sku": "DV3853-001",
        "gtin_upc_ean": "0196604245678",
        "product_description": "The workhorse with wings returns. Responsive Nike React foam combined with dual Zoom Air units at the forefoot and heel delivers spring with every step. Engineered single-layer mesh upper offers inviting feel and optimal breathability for marathon and daily road running.",
        "images": [
            "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.nike.com/pegasus-40-demo"],
        "specifications": {
            "cushioning": "Nike React Foam with Dual Zoom Air Pods",
            "upper_material": "Engineered Breathable Mesh",
            "sole_material": "Waffle-inspired Rubber Outsole for Maximum Traction",
            "heel_to_toe_drop_mm": 10,
            "weight_grams": 288,
            "arch_support": "Neutral Pronation Support",
            "closure": "Lace-Up with Midfoot Band",
            "origin": "Vietnam",
            "warranty_months": 6
        },
        "variants": [
            {"name": "UK 7 / Black & White", "price": 8995.0, "mrp": 11895.0, "sku": "DV3853-UK7"},
            {"name": "UK 8 / Black & White", "price": 8995.0, "mrp": 11895.0, "sku": "DV3853-UK8"},
            {"name": "UK 9 / Black & White", "price": 8995.0, "mrp": 11895.0, "sku": "DV3853-UK9"},
            {"name": "UK 10 / Black & White", "price": 8995.0, "mrp": 11895.0, "sku": "DV3853-UK10"},
            {"name": "UK 9 / Pure Platinum", "price": 9495.0, "mrp": 11895.0, "sku": "DV3853-UK9-PLT"}
        ],
        "current_price": 8995.0,
        "mrp": 11895.0,
        "discount_percentage": 24.4,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 14210,
        "seller": "Myntra",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Standard Delivery with 30-Day Hassle-Free Returns",
        "warranty": "6 Months Brand Warranty against Manufacturing Defects",
        "return_policy": "30 Days Easy Return & Size Exchange",
        "source_website": "Myntra",
        "product_url": "https://www.myntra.com/running-shoes/nike/nike-men-black-air-zoom-pegasus-40-running-shoes/23124567/buy",
        "affiliate_url": "https://www.myntra.com/running-shoes/nike/pegasus-40?utm_source=shopaipro",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Myntra",
                "seller_name": "Nike India Official Store",
                "seller_rating": 4.8,
                "price": 8995.0,
                "original_price": 11895.0,
                "discount_percent": 24.4,
                "availability": "In Stock",
                "delivery_info": "Free Express Delivery",
                "product_url": "https://www.myntra.com/running-shoes/nike/nike-men-black-air-zoom-pegasus-40-running-shoes/23124567/buy",
                "condition": "100% Genuine Certified Brand New"
            },
            {
                "source": "Amazon",
                "seller_name": "Nike Retail India",
                "seller_rating": 4.7,
                "price": 9299.0,
                "original_price": 11895.0,
                "discount_percent": 21.8,
                "availability": "In Stock",
                "delivery_info": "Free Prime Delivery",
                "product_url": "https://www.amazon.in/dp/B0BS5VXZ8Q",
                "condition": "Brand New in Original Box"
            },
            {
                "source": "Flipkart",
                "seller_name": "RetailNet Shoes",
                "seller_rating": 4.6,
                "price": 9495.0,
                "original_price": 11895.0,
                "discount_percent": 20.2,
                "availability": "In Stock",
                "delivery_info": "Free Standard Delivery",
                "product_url": "https://www.flipkart.com/nike-air-zoom-pegasus-40-running-shoes-men/p/itm0b3a3a3a3a3a3",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 3. HOME & FURNITURE: Home Appliances (Washing Machine / Refrigerator)
    # --------------------------------------------------------------------------
    {
        "product_id": "HOME-APP-LG-FRONTLOAD",
        "product_name": "LG 8.0 Kg 5 Star Inverter AI Direct Drive Front Loading Washing Machine (FHP1208Z5M, Middle Black)",
        "category": "home-furniture",
        "subcategory": "home-appliances",
        "brand": "LG",
        "model": "FHP1208Z5M",
        "variant": "8.0 Kg / 5 Star / Middle Black",
        "sku": "LG-FHP1208Z5M",
        "gtin_upc_ean": "8806091498765",
        "product_description": "AI Direct Drive detects not only the weight of laundry but also senses the softness of fabric and optimizes optimal washing motions. Features 6 Motion DD, Steam Wash with 99.9% allergen removal, 1200 RPM high spin speed, and Smart Diagnosis with ThinQ Wi-Fi control.",
        "images": [
            "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.lg.com/in/washing-machines/ai-dd-demo"],
        "specifications": {
            "capacity_kg": 8.0,
            "energy_star_rating": 5,
            "motor_type": "AI Inverter Direct Drive Motor",
            "max_spin_speed_rpm": 1200,
            "wash_programs": "14 Programs including Allergy Care, TurboWash, Cotton, Delicate",
            "water_consumption_litres": 55,
            "tub_material": "Stainless Steel Drum",
            "heater": "Inbuilt Steam Water Heater up to 60°C",
            "wifi_connectivity": "LG ThinQ Wi-Fi App Enabled",
            "noise_level_db": 54,
            "warranty_months": 24,
            "motor_warranty_years": 10
        },
        "variants": [
            {"name": "7.0 Kg / 5 Star White", "price": 32990.0, "mrp": 45990.0, "sku": "LG-7KG-WHT"},
            {"name": "8.0 Kg / 5 Star Middle Black", "price": 37990.0, "mrp": 52990.0, "sku": "LG-8KG-BLK"},
            {"name": "9.0 Kg / 5 Star Platinum", "price": 43990.0, "mrp": 59990.0, "sku": "LG-9KG-PLT"}
        ],
        "current_price": 37990.0,
        "mrp": 52990.0,
        "discount_percentage": 28.3,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 8940,
        "seller": "Amazon India",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Scheduled Delivery & Open-Box Inspection with Free Brand Installation",
        "warranty": "2 Years Comprehensive Warranty + 10 Years on Motor from LG India",
        "return_policy": "10 Days Replacement for Transit Damage / Technical Defect",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B09V7YZK98",
        "affiliate_url": "https://www.amazon.in/dp/B09V7YZK98?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "DAWNTECH ELECTRONICS",
                "seller_rating": 4.7,
                "price": 37990.0,
                "original_price": 52990.0,
                "discount_percent": 28.3,
                "availability": "In Stock",
                "delivery_info": "Free Delivery & Free Installation",
                "product_url": "https://www.amazon.in/dp/B09V7YZK98",
                "condition": "Brand New Sealed Appliance"
            },
            {
                "source": "Flipkart",
                "seller_name": "OmniTech Retail",
                "seller_rating": 4.6,
                "price": 38490.0,
                "original_price": 52990.0,
                "discount_percent": 27.4,
                "availability": "In Stock",
                "delivery_info": "Scheduled 2-Day Delivery",
                "product_url": "https://www.flipkart.com/lg-8-kg-5-star-inverter-ai-direct-drive-fully-automatic-front-load-washing-machine-heater-steam/p/itme3c3c3c3c3c3c",
                "condition": "Brand New with LG India Warranty"
            },
            {
                "source": "Croma",
                "seller_name": "Croma Large Appliances Store",
                "seller_rating": 4.5,
                "price": 38990.0,
                "original_price": 52990.0,
                "discount_percent": 26.4,
                "availability": "In Stock",
                "delivery_info": "Free Express Installation in 24 Hours",
                "product_url": "https://www.croma.com/lg-8-kg-5-star-inverter-fully-automatic-front-load-washing-machine/p/251342",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 4. BEAUTY & PERSONAL CARE: Skincare
    # --------------------------------------------------------------------------
    {
        "product_id": "BEAU-SKIN-MINIMALIST-SERUM",
        "product_name": "Minimalist 10% Niacinamide Face Serum with Zinc & Aloe Vera for Blemishes & Oil Control (30ml)",
        "category": "beauty-personal-care",
        "subcategory": "skincare",
        "brand": "Minimalist",
        "model": "Niacinamide 10% + Zinc 1%",
        "variant": "30 ml Glass Dropper Bottle",
        "sku": "MIN-NIA-30ML",
        "gtin_upc_ean": "8906128100123",
        "product_description": "A nourishing, daily serum packed with pure Vitamin B3 (Niacinamide) and Zinc. Clinically proven to reduce acne marks, dark spots, and control excess sebum production in 2 weeks. Formulated in Aloe Vera water with soothing Centella Asiatica for sensitive and acne-prone skin.",
        "images": [
            "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.youtube.com/watch?v=minimalist_niacinamide"],
        "specifications": {
            "active_ingredients": "10% Pure Niacinamide (Vitamin B3) + 1% Zinc PCA + EUK-134 Antioxidant",
            "skin_type": "All Skin Types, Oily, Acne-Prone & Sensitive Skin",
            "volume_ml": 30,
            "scent": "Fragrance-Free / Essential Oil Free",
            "formula_type": "Lightweight Water-Based Fast Absorbing Serum",
            "certifications": "Dermatologically Tested, Non-Comedogenic, Cruelty-Free",
            "country_of_origin": "India",
            "shelf_life_months": 24
        },
        "variants": [
            {"name": "30 ml Pack of 1", "price": 569.0, "mrp": 599.0, "sku": "MIN-NIA-30"},
            {"name": "60 ml Value Pack", "price": 999.0, "mrp": 1099.0, "sku": "MIN-NIA-60"},
            {"name": "Pack of 2 (30ml x 2)", "price": 1049.0, "mrp": 1198.0, "sku": "MIN-NIA-2PACK"}
        ],
        "current_price": 569.0,
        "mrp": 599.0,
        "discount_percentage": 5.0,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 31450,
        "seller": "Nykaa",
        "seller_rating": 4.9,
        "availability": "In Stock",
        "delivery_info": "Free Express Delivery on Orders Over ₹499",
        "warranty": "100% Authentic Product Guarantee with Batch Verification",
        "return_policy": "15 Days Return if Unopened / Damaged",
        "source_website": "Nykaa",
        "product_url": "https://www.nykaa.com/minimalist-10percent-niacinamide-face-serum-for-blemishes-and-oil-balancing/p/1067982",
        "affiliate_url": "https://www.nykaa.com/minimalist-niacinamide?affid=shopaipro",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Nykaa",
                "seller_name": "Nykaa E-Retail Private Ltd",
                "seller_rating": 4.9,
                "price": 569.0,
                "original_price": 599.0,
                "discount_percent": 5.0,
                "availability": "In Stock",
                "delivery_info": "Free Delivery Today",
                "product_url": "https://www.nykaa.com/minimalist-10percent-niacinamide-face-serum-for-blemishes-and-oil-balancing/p/1067982",
                "condition": "Direct Manufacturer Fresh Batch"
            },
            {
                "source": "Amazon",
                "seller_name": "Be Minimalist Official",
                "seller_rating": 4.8,
                "price": 569.0,
                "original_price": 599.0,
                "discount_percent": 5.0,
                "availability": "In Stock",
                "delivery_info": "Prime Next Day",
                "product_url": "https://www.amazon.in/dp/B08F9MKW6G",
                "condition": "Brand New Sealed"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 5. HEALTH & FITNESS: Fitness Equipment (Treadmill / Dumbbells)
    # --------------------------------------------------------------------------
    {
        "product_id": "FIT-EQP-FITKIT-FT200",
        "product_name": "Fitkit by Cult.sport FT200 Series 4.5HP Peak Motorized Multi-Functional Treadmill",
        "category": "health-fitness",
        "subcategory": "fitness-equipment",
        "brand": "Cult.sport",
        "model": "Fitkit FT200",
        "variant": "Multi-Functional with Massager & Dumbbells",
        "sku": "FK-FT200-MULTI",
        "gtin_upc_ean": "8904321098765",
        "product_description": "Engineered for home cardio and weight loss: features a powerful 2.25HP continuous / 4.5HP peak green efficient motor, 1-14 km/h speed range, 18-level auto inclination, large 1240 x 420 mm shock-absorbing running deck, multi-function massager, sit-up bar, and Cult.sport app interactive workout tracking.",
        "images": [
            "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.youtube.com/watch?v=cult_ft200_demo"],
        "specifications": {
            "motor_power": "2.25 HP Continuous / 4.5 HP Peak DC Motor",
            "speed_range_kmh": "1.0 - 14.0 km/h",
            "inclination": "18-Level Automatic Motorized Incline",
            "max_user_weight_kg": 110,
            "running_surface_mm": "1240 x 420 mm with Multi-Layer Anti-Slip Belt",
            "display": "5-inch Backlit LCD showing Speed, Distance, Time, Calories, Heart Rate",
            "connectivity": "Bluetooth App Connectivity (Cult.sport App & Apple Health)",
            "folding_system": "Hydraulic Soft-Drop Easy Folding System with Wheels",
            "warranty_months": 12,
            "motor_warranty_years": 3,
            "frame_warranty_years": 5
        },
        "variants": [
            {"name": "Standard Motorized (No Massager)", "price": 27999.0, "mrp": 49999.0, "sku": "FT200-STD"},
            {"name": "Multi-Functional (with Massager & Twister)", "price": 31999.0, "mrp": 54999.0, "sku": "FT200-MULTI"}
        ],
        "current_price": 31999.0,
        "mrp": 54999.0,
        "discount_percentage": 41.8,
        "currency": "INR",
        "rating": 4.4,
        "review_count": 6820,
        "seller": "Amazon India",
        "seller_rating": 4.6,
        "availability": "In Stock",
        "delivery_info": "Free Heavy Item Delivery & Onsite Technician Assembly",
        "warranty": "1 Year Onsite Parts Warranty, 3 Years Motor Warranty, Lifetime Frame Warranty",
        "return_policy": "10 Days Return for Defect or Transit Damage",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B07R8W47TX",
        "affiliate_url": "https://www.amazon.in/dp/B07R8W47TX?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Cult.sport Fitness Direct",
                "seller_rating": 4.6,
                "price": 31999.0,
                "original_price": 54999.0,
                "discount_percent": 41.8,
                "availability": "In Stock",
                "delivery_info": "Free Onsite Assembly Included",
                "product_url": "https://www.amazon.in/dp/B07R8W47TX",
                "condition": "Brand New Sealed Factory Pack"
            },
            {
                "source": "Flipkart",
                "seller_name": "FitnessHub India",
                "seller_rating": 4.4,
                "price": 32499.0,
                "original_price": 54999.0,
                "discount_percent": 40.9,
                "availability": "In Stock",
                "delivery_info": "Free Delivery with Installation Support",
                "product_url": "https://www.flipkart.com/fitkit-by-cult-ft200-motorized-treadmill/p/itm1a2b3c4d5e6f7",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 6. BOOKS & EDUCATION: AI / Technology Books
    # --------------------------------------------------------------------------
    {
        "product_id": "BOOK-TECH-HANDSON-ML",
        "product_name": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (3rd Edition) by Aurélien Géron",
        "category": "books-education",
        "subcategory": "books",
        "brand": "O'Reilly Media",
        "model": "3rd Edition Paperback",
        "variant": "Paperback / English",
        "sku": "OREILLY-9781098125974",
        "gtin_upc_ean": "9781098125974",
        "product_description": "The quintessential, bestselling industry guide to machine learning and deep learning. Through a series of recent breakthroughs, deep learning has boosted the entire field of machine learning. Aurélien Géron uses concrete examples, minimal theory, and production-ready Python frameworks to help you gain an intuitive understanding of the concepts and tools for building intelligent systems.",
        "images": [
            "https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "author": "Aurélien Géron",
            "publisher": "O'Reilly Media / Shroff Publishers",
            "edition": "3rd Edition (Updated for TensorFlow 2.x & Scikit-Learn 1.x)",
            "pages": 862,
            "language": "English",
            "format": "Paperback with High Quality Glazed Paper",
            "isbn_13": "978-1098125974",
            "dimensions_cm": "17.8 x 4.8 x 23.3 cm",
            "subject": "Artificial Intelligence, Deep Learning, Python, Neural Networks"
        },
        "variants": [
            {"name": "Paperback Edition", "price": 1850.0, "mrp": 2499.0, "sku": "9781098125974-PB"},
            {"name": "Hardcover Collector Edition", "price": 3890.0, "mrp": 4999.0, "sku": "9781098125974-HC"},
            {"name": "Kindle eBook Edition", "price": 999.0, "mrp": 1499.0, "sku": "9781098125974-EB"}
        ],
        "current_price": 1850.0,
        "mrp": 2499.0,
        "discount_percentage": 26.0,
        "currency": "INR",
        "rating": 4.8,
        "review_count": 5940,
        "seller": "Amazon India",
        "seller_rating": 4.9,
        "availability": "In Stock",
        "delivery_info": "Free One-Day Prime Delivery",
        "warranty": "Guaranteed Original Publisher Print",
        "return_policy": "7 Days Return Policy",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/1098125975",
        "affiliate_url": "https://www.amazon.in/dp/1098125975?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Cocoblu Retail",
                "seller_rating": 4.9,
                "price": 1850.0,
                "original_price": 2499.0,
                "discount_percent": 26.0,
                "availability": "In Stock",
                "delivery_info": "Next Day Prime Delivery",
                "product_url": "https://www.amazon.in/dp/1098125975",
                "condition": "Brand New Official Shroff/O'Reilly Edition"
            },
            {
                "source": "Flipkart",
                "seller_name": "TrueCom Books",
                "seller_rating": 4.7,
                "price": 1899.0,
                "original_price": 2499.0,
                "discount_percent": 24.0,
                "availability": "In Stock",
                "delivery_info": "Free Standard Delivery",
                "product_url": "https://www.flipkart.com/hands-on-machine-learning-scikit-learn-keras-tensorflow-3rd-edition/p/itm0a1b2c3d4e5f6",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 7. BABY & KIDS: Baby Gear (Strollers / Toys)
    # --------------------------------------------------------------------------
    {
        "product_id": "BABY-STR-LUVLAP-SUNSHINE",
        "product_name": "LuvLap Sunshine Baby Stroller & Pram with Reversible Handle & Mosquito Net",
        "category": "baby-kids",
        "subcategory": "baby-gear",
        "brand": "LuvLap",
        "model": "Sunshine Stroller",
        "variant": "Navy Blue / 0-3 Years",
        "sku": "LL-SUNSHINE-NVY",
        "gtin_upc_ean": "8904123890123",
        "product_description": "European Standard EN 1888 certified stroller suitable for newborn babies to toddlers up to 15 kg. Features 3-position reclining seat (sitting, resting, flat sleeping), reversible handlebar to look at baby, 5-point safety harness, 360-degree front swivel wheels with lock, and rear-wheel foot brakes.",
        "images": [
            "https://images.unsplash.com/photo-1519689680058-324335c77eba?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.luvlap.com/sunshine-stroller-demo"],
        "specifications": {
            "safety_certification": "European Safety Standard EN 1888 Certified",
            "age_range": "0 to 36 Months",
            "max_weight_capacity_kg": 15,
            "recline_positions": "3-Position Adjustable (Sitting, Lounging, Flat Sleeping)",
            "safety_harness": "5-Point Padded Safety Harness",
            "handlebar": "Reversible Handlebar for Forward & Rear Facing Caregiver View",
            "canopy": "Extended Canopy with Peek-a-boo Window & Mosquito Net",
            "folded_dimensions": "Compact Fold with Travel Lock",
            "warranty_months": 12
        },
        "variants": [
            {"name": "Navy Blue", "price": 4299.0, "mrp": 6999.0, "sku": "LL-SUN-NVY"},
            {"name": "Cherry Red", "price": 4299.0, "mrp": 6999.0, "sku": "LL-SUN-RED"},
            {"name": "Olive Green", "price": 4499.0, "mrp": 6999.0, "sku": "LL-SUN-GRN"}
        ],
        "current_price": 4299.0,
        "mrp": 6999.0,
        "discount_percentage": 38.6,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 12890,
        "seller": "FirstCry",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Fast Delivery with FirstCry Club Perks",
        "warranty": "1 Year Brand Manufacturer Warranty",
        "return_policy": "15 Days Hassle-Free Returns",
        "source_website": "FirstCry",
        "product_url": "https://www.firstcry.com/luvlap/luvlap-sunshine-baby-stroller-with-reversible-handle/1234567/product-detail",
        "affiliate_url": "https://www.firstcry.com/luvlap/sunshine?tag=shopaipro",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "FirstCry",
                "seller_name": "Brainbees Solutions Ltd",
                "seller_rating": 4.8,
                "price": 4299.0,
                "original_price": 6999.0,
                "discount_percent": 38.6,
                "availability": "In Stock",
                "delivery_info": "Free 2-Day Delivery",
                "product_url": "https://www.firstcry.com/luvlap/luvlap-sunshine-baby-stroller-with-reversible-handle/1234567/product-detail",
                "condition": "Brand New Certified Juvenile Product"
            },
            {
                "source": "Amazon",
                "seller_name": "LuvLap Official Store",
                "seller_rating": 4.7,
                "price": 4499.0,
                "original_price": 6999.0,
                "discount_percent": 35.7,
                "availability": "In Stock",
                "delivery_info": "Free Prime Delivery",
                "product_url": "https://www.amazon.in/dp/B07N8Z78X6",
                "condition": "Brand New in Factory Box"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 8. AUTOMOTIVE: Dash Cameras / Car Accessories
    # --------------------------------------------------------------------------
    {
        "product_id": "AUTO-CAM-70MAI-A500S",
        "product_name": "70mai Pro Plus+ A500S Dual Channel 2.7K Dash Cam for Front & Rear with Built-in GPS & ADAS",
        "category": "automotive",
        "subcategory": "cars",
        "brand": "70mai",
        "model": "A500S Dual Vision",
        "variant": "Front (2.7K) + Rear (1080P) + CPL Filter",
        "sku": "70MAI-A500S-DUAL",
        "gtin_upc_ean": "6971669780123",
        "product_description": "2.7K Ultra HD (1944p) front sensor paired with 1080p Full HD rear cam featuring Sony IMX335 high sensitivity sensor and 3D DNR + WDR night vision. Includes built-in GPS for speed & route logging, ADAS (Lane Departure & Forward Collision warnings), and 24H parking surveillance with G-sensor emergency collision lock.",
        "images": [
            "https://images.unsplash.com/photo-1508974239320-0a029497e820?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.70mai.com/a500s-dashcam-demo"],
        "specifications": {
            "front_resolution": "2.7K 1944p Ultra HD (2592 x 1944 at 30 fps)",
            "rear_resolution": "1080p Full HD (1920 x 1080 at 30 fps)",
            "image_sensor": "Sony IMX335 with 6-Glass F1.8 Aperture Lens",
            "field_of_view": "140° Wide Angle Front + 130° Rear View",
            "gps_logger": "Built-in GPS with Real-time Coordinates and Speed Watermark",
            "adas_features": "Lane Departure Warning & Forward Collision Warning",
            "night_vision": "Superior 3D DNR (Dynamic Noise Reduction) with WDR",
            "storage_support": "MicroSD up to 128GB Class 10 U3",
            "app_control": "70mai Mobile App (iOS & Android) with Direct Wi-Fi Download",
            "warranty_months": 12
        },
        "variants": [
            {"name": "Front Cam Only (A500S)", "price": 7999.0, "mrp": 10999.0, "sku": "A500S-FRONT"},
            {"name": "Front + Rear Dual Channel (A500S-1)", "price": 10999.0, "mrp": 14999.0, "sku": "A500S-DUAL"},
            {"name": "Dual Channel + 64GB MicroSD + CPL Filter", "price": 11999.0, "mrp": 16999.0, "sku": "A500S-BUNDLE"}
        ],
        "current_price": 10999.0,
        "mrp": 14999.0,
        "discount_percentage": 26.7,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 9480,
        "seller": "Amazon India",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Next-Day Prime Delivery",
        "warranty": "1 Year National Replacement Warranty from 70mai India",
        "return_policy": "7 Days Return / Replacement",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B08X28P8QJ",
        "affiliate_url": "https://www.amazon.in/dp/B08X28P8QJ?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Nexus Retail Official",
                "seller_rating": 4.8,
                "price": 10999.0,
                "original_price": 14999.0,
                "discount_percent": 26.7,
                "availability": "In Stock",
                "delivery_info": "Free Prime Delivery",
                "product_url": "https://www.amazon.in/dp/B08X28P8QJ",
                "condition": "Brand New Sealed Official Indian Unit"
            },
            {
                "source": "Flipkart",
                "seller_name": "Automotive Direct",
                "seller_rating": 4.5,
                "price": 11499.0,
                "original_price": 14999.0,
                "discount_percent": 23.3,
                "availability": "In Stock",
                "delivery_info": "2 Days Delivery",
                "product_url": "https://www.flipkart.com/70mai-a500s-pro-plus-dual-channel-dashcam/p/itm0a9b8c7d6e5f4",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 9. PET SUPPLIES: Dogs Food
    # --------------------------------------------------------------------------
    {
        "product_id": "PET-DOG-ROYALCANIN-MAXI",
        "product_name": "Royal Canin Maxi Adult Dry Dog Food (15 Kg Bag)",
        "category": "pet-supplies",
        "subcategory": "dogs",
        "brand": "Royal Canin",
        "model": "Maxi Adult (26-44 kg)",
        "variant": "15 Kg Jumbo Pack",
        "sku": "RC-MAXI-ADULT-15K",
        "gtin_upc_ean": "3182550732154",
        "product_description": "Tailored nutritional solution for large breed adult dogs (weight 26 to 44 kg) from 15 months to 5 years old. Helps support optimal digestibility thanks to an exclusive formula containing high-quality proteins and a balanced supply of dietary fibre. Enriched with Omega-3 fatty acids (EPA-DHA) to support bone and joint health.",
        "images": [
            "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.royalcanin.com/maxi-adult-benefits"],
        "specifications": {
            "target_pet": "Large Breed Dogs (Adult 15 Months - 5 Years)",
            "weight_kg": 15.0,
            "diet_type": "Non-Vegetarian Complete Balanced Dry Kibble",
            "protein_percentage": 26.0,
            "fat_percentage": 17.0,
            "key_nutrients": "EPA & DHA Omega-3, Glucosamine, Chondroitin, Antioxidant Complex",
            "country_of_origin": "France",
            "shelf_life_months": 18
        },
        "variants": [
            {"name": "4 Kg Bag", "price": 2850.0, "mrp": 3100.0, "sku": "RC-MAXI-4K"},
            {"name": "10 Kg Bag", "price": 6390.0, "mrp": 6990.0, "sku": "RC-MAXI-10K"},
            {"name": "15 Kg Jumbo Bag", "price": 8690.0, "mrp": 9650.0, "sku": "RC-MAXI-15K"}
        ],
        "current_price": 8690.0,
        "mrp": 9650.0,
        "discount_percentage": 9.9,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 8340,
        "seller": "Amazon India",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Prime Delivery",
        "warranty": "100% Genuine Imported Batch Guarantee",
        "return_policy": "7 Days Return if Seal Intact",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B002Z5L14W",
        "affiliate_url": "https://www.amazon.in/dp/B002Z5L14W?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "PetCare Direct",
                "seller_rating": 4.8,
                "price": 8690.0,
                "original_price": 9650.0,
                "discount_percent": 9.9,
                "availability": "In Stock",
                "delivery_info": "Free Delivery",
                "product_url": "https://www.amazon.in/dp/B002Z5L14W",
                "condition": "Factory Fresh French Import"
            },
            {
                "source": "Flipkart",
                "seller_name": "SuperPet India",
                "seller_rating": 4.6,
                "price": 8890.0,
                "original_price": 9650.0,
                "discount_percent": 7.8,
                "availability": "In Stock",
                "delivery_info": "2 Days Delivery",
                "product_url": "https://www.flipkart.com/royal-canin-maxi-adult-dry-dog-food-15-kg/p/itm0a1b2c3d4e5f7",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 10. GROCERY & FOOD: Dry Fruits / Masala
    # --------------------------------------------------------------------------
    {
        "product_id": "GROC-NUTS-HAPPILO-ALMOND",
        "product_name": "Happilo Premium California Roasted & Salted Almonds (1 Kg Value Pouch)",
        "category": "grocery-food",
        "subcategory": "food",
        "brand": "Happilo",
        "model": "Premium California Badam",
        "variant": "1 Kg Vacuum Sealed Zipper Pouch",
        "sku": "HAP-ALM-1KG-SLT",
        "gtin_upc_ean": "8906082570123",
        "product_description": "Finest Grade 1 California almonds, lightly dry roasted and perfectly salted without oil. Rich in plant protein, dietary fiber, vitamin E, magnesium, and heart-healthy monounsaturated fats. Gluten-free, non-GMO, zero trans-fats, zero cholesterol in resealable stay-fresh zipper pouch.",
        "images": [
            "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "origin": "California, USA",
            "quantity_grams": 1000,
            "diet_type": "Vegetarian, Vegan, Gluten Free, Keto Friendly",
            "ingredients": "California Almonds, Edible Himalayan Rock Salt",
            "protein_per_100g": "21.1 g",
            "calories_per_100g": 579,
            "packaging": "Multi-layer Nitrogen Flushed Moisture-Lock Pouch",
            "shelf_life_months": 12
        },
        "variants": [
            {"name": "200 g Pouch", "price": 249.0, "mrp": 345.0, "sku": "HAP-ALM-200G"},
            {"name": "500 g Pouch", "price": 499.0, "mrp": 695.0, "sku": "HAP-ALM-500G"},
            {"name": "1 Kg Value Pouch", "price": 899.0, "mrp": 1295.0, "sku": "HAP-ALM-1KG"}
        ],
        "current_price": 899.0,
        "mrp": 1295.0,
        "discount_percentage": 30.6,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 24190,
        "seller": "Amazon Fresh",
        "seller_rating": 4.9,
        "availability": "In Stock",
        "delivery_info": "Free 2-Hour Slot Delivery with Amazon Fresh / Prime",
        "warranty": "Freshness & Taste Guarantee",
        "return_policy": "7 Days Return/Replacement for Food Safety",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B07R7Q8Z4Y",
        "affiliate_url": "https://www.amazon.in/dp/B07R7Q8Z4Y?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Happilo Official Store",
                "seller_rating": 4.9,
                "price": 899.0,
                "original_price": 1295.0,
                "discount_percent": 30.6,
                "availability": "In Stock",
                "delivery_info": "Free Prime Delivery",
                "product_url": "https://www.amazon.in/dp/B07R7Q8Z4Y",
                "condition": "Fresh Sealed Batch"
            },
            {
                "source": "Flipkart",
                "seller_name": "SuperMart Grocery",
                "seller_rating": 4.6,
                "price": 929.0,
                "original_price": 1295.0,
                "discount_percent": 28.3,
                "availability": "In Stock",
                "delivery_info": "Same Day Delivery",
                "product_url": "https://www.flipkart.com/happilo-premium-california-roasted-salted-almonds-1-kg/p/itm0a2b4c6d8e0f2",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 11. OFFICE PRODUCTS: Ergonomic Chairs / Monitors
    # --------------------------------------------------------------------------
    {
        "product_id": "OFF-CHR-GREENSOUL-JUPITER",
        "product_name": "Green Soul Jupiter Superb High Back Ergonomic Mesh Office Chair with 2D Lumbar Support",
        "category": "office-products",
        "subcategory": "office-chairs",
        "brand": "Green Soul",
        "model": "Jupiter Superb",
        "variant": "High Back / Smart Black",
        "sku": "GS-JUPITER-BLK",
        "gtin_upc_ean": "8906101901234",
        "product_description": "Certified BIFMA level ergonomic high-back chair tailored for 8-12 hours of everyday computer work. Features breathable Korean mesh back, 2-way adjustable lumbar support cushion, 3D adjustable armrests with soft PU padding, 135-degree synchro-tilt mechanism, heavy-duty metallic wheelbase, and Class 4 gas lift.",
        "images": [
            "https://images.unsplash.com/photo-1592078615290-033ee584e267?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.greensoul.online/jupiter-chair-demo"],
        "specifications": {
            "lumbar_support": "2D Depth & Height Adjustable Ergonomic Lumbar Support",
            "armrests": "3D Adjustable (Height, Depth, Angle) with Soft PU Padding",
            "recline_mechanism": "Synchro-Tilt Locking at 90°, 110°, 135°",
            "gas_lift": "Class 4 Explosion-Proof Pneumatic Gas Lift (BIFMA Certified)",
            "seat_cushion": "High-Density Molded Foam (65 kg/m³) with Breathable Fabric",
            "max_weight_capacity_kg": 135,
            "recommended_height_cm": "155 cm - 190 cm",
            "warranty_months": 36
        },
        "variants": [
            {"name": "Smart Black", "price": 8999.0, "mrp": 17990.0, "sku": "JUP-BLK"},
            {"name": "Space Grey", "price": 9299.0, "mrp": 17990.0, "sku": "JUP-GRY"}
        ],
        "current_price": 8999.0,
        "mrp": 17990.0,
        "discount_percentage": 50.0,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 16420,
        "seller": "Amazon India",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Delivery & Free DIY Assembly Toolkit Included",
        "warranty": "3 Years Comprehensive Onsite Warranty from Green Soul",
        "return_policy": "10 Days Return/Replacement",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B08J456Q9X",
        "affiliate_url": "https://www.amazon.in/dp/B08J456Q9X?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Green Soul Ergonomics",
                "seller_rating": 4.7,
                "price": 8999.0,
                "original_price": 17990.0,
                "discount_percent": 50.0,
                "availability": "In Stock",
                "delivery_info": "Free Express Delivery",
                "product_url": "https://www.amazon.in/dp/B08J456Q9X",
                "condition": "Brand New Factory Box"
            },
            {
                "source": "Flipkart",
                "seller_name": "FurnitureDirect",
                "seller_rating": 4.4,
                "price": 9299.0,
                "original_price": 17990.0,
                "discount_percent": 48.3,
                "availability": "In Stock",
                "delivery_info": "2 Days Delivery",
                "product_url": "https://www.flipkart.com/green-soul-jupiter-superb-high-back-ergonomic-office-chair/p/itm0b2c4d6e8f0a2",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 12. INDUSTRIAL & TOOLS: Power Tools (Impact Drill)
    # --------------------------------------------------------------------------
    {
        "product_id": "IND-TOOL-BOSCH-GSB500",
        "product_name": "Bosch GSB 500W 10 RE Professional Impact Drill Kit with 100 Accessories",
        "category": "industrial-tools",
        "subcategory": "power-tools",
        "brand": "Bosch",
        "model": "GSB 500 RE Kit",
        "variant": "500W Impact Drill + 100 Pc Accessory Carry Case",
        "sku": "06011A01F0",
        "gtin_upc_ean": "3165140801234",
        "product_description": "Compact and powerful 500-watt motor impact drill engineered for masonry, concrete, wood, metal drilling, and screwdriving. Features forward/reverse rotation, electronic speed control trigger, ergonomic soft-grip, and robust heavy-duty molded carrying case containing 100 essential drill bits, screws, anchors, hammer, wrench, pliers, and measuring tape.",
        "images": [
            "https://images.unsplash.com/photo-1581147036324-c17ac41dfa6c?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.bosch-professional.com/gsb-500-re-demo"],
        "specifications": {
            "power_input_watts": 500,
            "no_load_speed_rpm": "0 - 2600 RPM",
            "impact_rate_bpm": "0 - 41600 BPM",
            "chuck_capacity_mm": 10,
            "drilling_capacity": "Masonry 10mm, Steel 8mm, Wood 20mm",
            "rotation_direction": "Forward & Reverse Variable Speed",
            "weight_kg": 1.5,
            "accessory_count": 100,
            "warranty_months": 12
        },
        "variants": [
            {"name": "Tool Only (No Kit)", "price": 2899.0, "mrp": 4200.0, "sku": "GSB-500-TOOL"},
            {"name": "Kit with 100 Accessories & Case", "price": 3999.0, "mrp": 6250.0, "sku": "GSB-500-KIT"}
        ],
        "current_price": 3999.0,
        "mrp": 6250.0,
        "discount_percentage": 36.0,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 18230,
        "seller": "Amazon India",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Prime Delivery",
        "warranty": "1 Year Onsite Manufacturer Warranty from Bosch India",
        "return_policy": "7 Days Return / Replacement",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B00IA40Y4A",
        "affiliate_url": "https://www.amazon.in/dp/B00IA40Y4A?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Bosch Power Tools Official",
                "seller_rating": 4.8,
                "price": 3999.0,
                "original_price": 6250.0,
                "discount_percent": 36.0,
                "availability": "In Stock",
                "delivery_info": "Free Next-Day Delivery",
                "product_url": "https://www.amazon.in/dp/B00IA40Y4A",
                "condition": "Brand New Sealed Official Kit"
            },
            {
                "source": "Flipkart",
                "seller_name": "HardwareBazaar",
                "seller_rating": 4.5,
                "price": 4149.0,
                "original_price": 6250.0,
                "discount_percent": 33.6,
                "availability": "In Stock",
                "delivery_info": "2 Days Delivery",
                "product_url": "https://www.flipkart.com/bosch-gsb-500-re-impact-drill-kit/p/itm0a3b5c7d9e1f3",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 13. TRAVEL & LUGGAGE: Trolley Suitcases
    # --------------------------------------------------------------------------
    {
        "product_id": "TRAV-LUG-AMERICAN-TOURISTER",
        "product_name": "American Tourister Ivy 3-Piece Hard Luggage Trolley Set (55cm Cabin + 68cm Medium + 77cm Large)",
        "category": "travel-luggage",
        "subcategory": "suitcases",
        "brand": "American Tourister",
        "model": "Ivy Spinner Set",
        "variant": "Set of 3 (Cabin + Medium + Large) / Sea Green",
        "sku": "AT-IVY-3SET-SGN",
        "gtin_upc_ean": "8901836101234",
        "product_description": "Engineered with resilient 100% polypropylene hard casing that withstands rough airport handling while remaining ultralight. Features scratch-resistant textured matte finish, recessed TSA combination locks on all sizes, 360-degree silent dual spinner wheels, push-button multi-stage aluminum trolley handle, and fully organized interior packing cubes.",
        "images": [
            "https://images.unsplash.com/photo-1565026057447-bc90a3dceb87?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.americantourister.com/ivy-series-demo"],
        "specifications": {
            "outer_material": "100% Pure Virgin Polypropylene Unbreakable Shell",
            "lock_type": "Flush-Mounted Recessed TSA 3-Digit Combination Lock",
            "wheels": "8 Smooth & Silent 360-Degree Dual Spinner Wheels",
            "sizes_included": "Cabin (55 cm / 38L) + Medium (68 cm / 75L) + Large (77 cm / 115L)",
            "interior_organization": "Cross Ribbons with Divider Zipper Pocket",
            "water_resistance": "Water-Resistant Shell with Heavy-Duty Coil Zippers",
            "warranty_months": 36
        },
        "variants": [
            {"name": "Cabin 55cm Single", "price": 2899.0, "mrp": 7500.0, "sku": "AT-IVY-55"},
            {"name": "Medium 68cm Single", "price": 3899.0, "mrp": 9500.0, "sku": "AT-IVY-68"},
            {"name": "Large 77cm Single", "price": 4899.0, "mrp": 11500.0, "sku": "AT-IVY-77"},
            {"name": "Set of 3 (Cabin+Medium+Large)", "price": 9999.0, "mrp": 28500.0, "sku": "AT-IVY-SET3"}
        ],
        "current_price": 9999.0,
        "mrp": 28500.0,
        "discount_percentage": 64.9,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 14190,
        "seller": "Amazon India",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Express Delivery",
        "warranty": "3 Years International Global Manufacturer Warranty",
        "return_policy": "10 Days Return/Replacement",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B08XJ8P8QL",
        "affiliate_url": "https://www.amazon.in/dp/B08XJ8P8QL?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Samsonite South Asia Pvt Ltd",
                "seller_rating": 4.8,
                "price": 9999.0,
                "original_price": 28500.0,
                "discount_percent": 64.9,
                "availability": "In Stock",
                "delivery_info": "Free Prime Delivery",
                "product_url": "https://www.amazon.in/dp/B08XJ8P8QL",
                "condition": "Brand New Sealed Set"
            },
            {
                "source": "Flipkart",
                "seller_name": "LuggageWorld India",
                "seller_rating": 4.5,
                "price": 10499.0,
                "original_price": 28500.0,
                "discount_percent": 63.2,
                "availability": "In Stock",
                "delivery_info": "2 Days Delivery",
                "product_url": "https://www.flipkart.com/american-tourister-ivy-polypropylene-hard-trolley-set-3/p/itm0a4b6c8d0e2f4",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 14. MUSICAL INSTRUMENTS: Acoustic Guitars
    # --------------------------------------------------------------------------
    {
        "product_id": "MUS-GTR-YAMAHA-F310",
        "product_name": "Yamaha F310 Full Size Acoustic Guitar (Natural Gloss Spruce Top)",
        "category": "musical-instruments",
        "subcategory": "guitar",
        "brand": "Yamaha",
        "model": "F310",
        "variant": "Full Size 41-inch / Natural Finish",
        "sku": "YAM-F310-NAT",
        "gtin_upc_ean": "4957812012345",
        "product_description": "The gold standard in student and intermediate acoustic guitars worldwide. Crafted with selected Spruce top and Meranti back & sides, producing outstanding tone, deep resonant resonance, and crystal clarity. Features comfortable shorter 25-inch scale length and rosewood fingerboard for easy fingering and smooth playing experience.",
        "images": [
            "https://images.unsplash.com/photo-1510915361894-db8b60106cb1?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.yamaha.com/f310-acoustic-guitar-demo"],
        "specifications": {
            "top_material": "Laminated Select Spruce Top",
            "back_and_sides": "Meranti Tone Wood",
            "neck_material": "Nato Wood with Smooth Matte Finish",
            "fingerboard": "Selected Rosewood Fingerboard with 20 Frets",
            "scale_length_mm": 634,
            "bridge": "Rosewood with Compensated Saddle",
            "tuning_pegs": "Covered Chrome Precision Tuners",
            "strings": "Yamaha Steel Acoustic Strings (0.012 - 0.053)",
            "warranty_months": 12
        },
        "variants": [
            {"name": "Natural Gloss Finish", "price": 9490.0, "mrp": 11490.0, "sku": "F310-NAT"},
            {"name": "Tobacco Brown Sunburst", "price": 9990.0, "mrp": 11990.0, "sku": "F310-TBS"}
        ],
        "current_price": 9490.0,
        "mrp": 11490.0,
        "discount_percentage": 17.4,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 21340,
        "seller": "Amazon India",
        "seller_rating": 4.9,
        "availability": "In Stock",
        "delivery_info": "Free One-Day Delivery with Heavy Shockproof Packaging",
        "warranty": "1 Year Official Yamaha Musical Instrument Warranty",
        "return_policy": "7 Days Return/Exchange for Intact Instruments",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B000RVYW7E",
        "affiliate_url": "https://www.amazon.in/dp/B000RVYW7E?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Yamaha Music India Official",
                "seller_rating": 4.9,
                "price": 9490.0,
                "original_price": 11490.0,
                "discount_percent": 17.4,
                "availability": "In Stock",
                "delivery_info": "Free Next-Day Prime Delivery",
                "product_url": "https://www.amazon.in/dp/B000RVYW7E",
                "condition": "Brand New Factory Tuned & Inspected"
            },
            {
                "source": "Bajaao",
                "seller_name": "Bajaao Certified Music Gear",
                "seller_rating": 4.8,
                "price": 9690.0,
                "original_price": 11490.0,
                "discount_percent": 15.7,
                "availability": "In Stock",
                "delivery_info": "Free 2-Day Insured Courier Delivery",
                "product_url": "https://www.bajaao.com/products/yamaha-f310-acoustic-guitar-natural",
                "condition": "Brand New"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 15. GARDEN & OUTDOOR: Gardening Tools / Plants
    # --------------------------------------------------------------------------
    {
        "product_id": "GARD-TOOL-TRUSTBASKET-KIT",
        "product_name": "TrustBasket Heavy Duty Gardening Tool Set (Set of 5 with Ergonomic Rubber Grips)",
        "category": "garden-outdoor",
        "subcategory": "gardening-tools",
        "brand": "TrustBasket",
        "model": "Heavy Duty Garden Set",
        "variant": "Set of 5 Tools (Trowel, Fork, Cultivator, Weeder, Pruner)",
        "sku": "TB-GARD-5KIT",
        "gtin_upc_ean": "8904567890123",
        "product_description": "Comprehensive heavy-duty home and balcony gardening essentials kit: includes Large Hand Trowel, Transplanter Trowel, Cultivator/Hand Rake, Weeding Fork, and Premium Bypass Pruning Shears. Forged from rust-proof coated high-carbon steel with non-slip dual-color rubberized ergonomic handles.",
        "images": [
            "https://images.unsplash.com/photo-1416879595882-3373a0480b5b?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "blade_material": "Rust-Resistant Powder-Coated High Carbon Steel",
            "handle_material": "Ergonomic Non-Slip Soft TPR Rubber Grip",
            "tools_included": "Trowel, Transplanter, Cultivator Rake, Weeding Fork, Bypass Pruner",
            "rust_resistance": "Tested 100+ Hours Salt Spray Rust Resistant Coating",
            "weight_kg": 1.1,
            "origin": "India",
            "warranty_months": 12
        },
        "variants": [
            {"name": "Set of 5 Tools", "price": 899.0, "mrp": 1499.0, "sku": "TB-TOOL-5"},
            {"name": "Set of 8 Tools with Garden Gloves & Bag", "price": 1499.0, "mrp": 2499.0, "sku": "TB-TOOL-8BAG"}
        ],
        "current_price": 899.0,
        "mrp": 1499.0,
        "discount_percentage": 40.0,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 9180,
        "seller": "Amazon India",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Prime Delivery",
        "warranty": "1 Year Replacement Warranty against Tool Breakage",
        "return_policy": "7 Days Return/Exchange",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B073XB1L9P",
        "affiliate_url": "https://www.amazon.in/dp/B073XB1L9P?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "TrustBasket Official Store",
                "seller_rating": 4.8,
                "price": 899.0,
                "original_price": 1499.0,
                "discount_percent": 40.0,
                "availability": "In Stock",
                "delivery_info": "Free Express Delivery",
                "product_url": "https://www.amazon.in/dp/B073XB1L9P",
                "condition": "Brand New Sealed Box"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 16. JEWELLERY & WATCHES: Smart & Luxury Watches
    # --------------------------------------------------------------------------
    {
        "product_id": "JEW-WAT-TITAN-EDGE",
        "product_name": "Titan Edge Ceramic Ultra-Slim Analog Watch for Men (Sapphire Crystal Glass)",
        "category": "jewellery-watches",
        "subcategory": "watches",
        "brand": "Titan",
        "model": "Edge Ceramic 1696QC01",
        "variant": "Black Ceramic / Anthracite Dial",
        "sku": "1696QC01",
        "gtin_upc_ean": "8905123456789",
        "product_description": "Recognized as one of the slimmest ceramic watches in horology, with a total case thickness of just 4.4 mm. Crafted with scratch-proof aerospace grade ceramic case and strap, scratch-resistant sapphire crystal glass, and powered by Titan's award-winning 1.15 mm in-house ultra-thin quartz movement.",
        "images": [
            "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.titan.co.in/edge-ceramic-video"],
        "specifications": {
            "case_thickness_mm": 4.4,
            "movement_type": "Titan In-House Ultra-Slim Quartz (1.15 mm Movement)",
            "case_material": "Hypoallergenic Aerospace Grade Polished Ceramic",
            "strap_material": "Solid Ceramic Bracelet with Butterfly Clasp",
            "glass_material": "Anti-Reflective Scratch-Resistant Sapphire Crystal",
            "water_resistance": "30M (3 ATM) Splash Resistant",
            "case_diameter_mm": 40.5,
            "origin": "India (Tata Group Heritage)",
            "warranty_months": 24
        },
        "variants": [
            {"name": "Midnight Black Ceramic", "price": 24995.0, "mrp": 29995.0, "sku": "1696QC01-BLK"},
            {"name": "Arctic White Ceramic", "price": 24995.0, "mrp": 29995.0, "sku": "1696QC02-WHT"}
        ],
        "current_price": 24995.0,
        "mrp": 29995.0,
        "discount_percentage": 16.7,
        "currency": "INR",
        "rating": 4.8,
        "review_count": 4890,
        "seller": "Tata CLiQ Luxury",
        "seller_rating": 4.9,
        "availability": "In Stock",
        "delivery_info": "Free Insured White-Glove Luxury Delivery",
        "warranty": "2 Years Official Titan Global Warranty + Lifetime Movement Warranty",
        "return_policy": "7 Days Return/Exchange in Untampered Seal Box",
        "source_website": "Tata CLiQ",
        "product_url": "https://luxury.tatacliq.com/titan-edge-ceramic-analog-watch-1696qc01/p/mp000000012345678",
        "affiliate_url": "https://luxury.tatacliq.com/titan-edge?utm_source=shopaipro",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Tata CLiQ",
                "seller_name": "Titan Company Official",
                "seller_rating": 4.9,
                "price": 24995.0,
                "original_price": 29995.0,
                "discount_percent": 16.7,
                "availability": "In Stock",
                "delivery_info": "White-Glove Insured Delivery",
                "product_url": "https://luxury.tatacliq.com/titan-edge-ceramic-analog-watch-1696qc01/p/mp000000012345678",
                "condition": "Brand New Certified Tata Luxury"
            },
            {
                "source": "Amazon",
                "seller_name": "Titan Retail Authorized",
                "seller_rating": 4.8,
                "price": 25495.0,
                "original_price": 29995.0,
                "discount_percent": 15.0,
                "availability": "In Stock",
                "delivery_info": "Free Prime Delivery",
                "product_url": "https://www.amazon.in/dp/B08F9MKW6G",
                "condition": "Brand New in Luxury Box"
            }
        ]
    },

    # --------------------------------------------------------------------------
    # 17. ELECTRICAL & HOME IMPROVEMENT: Smart Bulbs & Inverters
    # --------------------------------------------------------------------------
    {
        "product_id": "ELEC-IMP-LUMINOUS-ZELIO",
        "product_name": "Luminous Zelio+ 1100 Pure Sine Wave 900VA Home Inverter UPS with LED Smart Display",
        "category": "electrical-home-improvement",
        "subcategory": "electrical",
        "brand": "Luminous",
        "model": "Zelio+ 1100",
        "variant": "900VA / 12V Single Battery Support",
        "sku": "LUM-ZELIO-1100",
        "gtin_upc_ean": "8901234567890",
        "product_description": "India's intelligent pure sine wave home inverter powered by a 32-bit DSP processor. Features an intuitive smart LED display showing battery charging time, backup time in hours & minutes, fault indicators, and battery water level sensor. Compatible with tubular, flat plate, and SMF batteries with MCB protection.",
        "images": [
            "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": ["https://www.luminousindia.com/zelio-plus-demo"],
        "specifications": {
            "va_rating": "900 VA (Watts: 756 W)",
            "output_wave_type": "Pure Sine Wave (Safe for Sensitive Laptops, TVs & Appliances)",
            "display": "Smart 32-bit DSP LED Screen (Backup & Charging Hours Display)",
            "battery_support": "Single 12V Battery (Supports 100Ah - 220Ah)",
            "battery_types": "Tubular, Flat Plate, SMF / VRLA",
            "safety_protection": "Overload, Deep Discharge, Short Circuit, Reverse Polarity & Bypass Switch",
            "weight_kg": 9.5,
            "dimensions_cm": "27.5 x 26.2 x 12.0 cm",
            "warranty_months": 24
        },
        "variants": [
            {"name": "Zelio+ 1100 (900VA / 12V)", "price": 6499.0, "mrp": 8990.0, "sku": "ZELIO-1100"},
            {"name": "Zelio+ 1700 (1500VA / 24V Double Battery)", "price": 9999.0, "mrp": 14990.0, "sku": "ZELIO-1700"}
        ],
        "current_price": 6499.0,
        "mrp": 8990.0,
        "discount_percentage": 27.7,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 17820,
        "seller": "Amazon India",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Scheduled Delivery with Brand Installation Support",
        "warranty": "24 Months Onsite Warranty from Luminous Power Technologies",
        "return_policy": "7 Days Return/Replacement for Technical Defects",
        "source_website": "Amazon",
        "product_url": "https://www.amazon.in/dp/B01LXU3Z1P",
        "affiliate_url": "https://www.amazon.in/dp/B01LXU3Z1P?tag=shopaipro-21",
        "last_updated": datetime.utcnow().isoformat(),
        "sellers": [
            {
                "source": "Amazon",
                "seller_name": "Luminous Power Direct",
                "seller_rating": 4.7,
                "price": 6499.0,
                "original_price": 8990.0,
                "discount_percent": 27.7,
                "availability": "In Stock",
                "delivery_info": "Free Express Delivery",
                "product_url": "https://www.amazon.in/dp/B01LXU3Z1P",
                "condition": "Brand New Sealed Official Unit"
            },
            {
                "source": "Flipkart",
                "seller_name": "PowerHub India",
                "seller_rating": 4.5,
                "price": 6699.0,
                "original_price": 8990.0,
                "discount_percent": 25.5,
                "availability": "In Stock",
                "delivery_info": "2 Days Delivery",
                "product_url": "https://www.flipkart.com/luminous-zelio-1100-pure-sine-wave-inverter/p/itm0a5b7c9d1e3f5",
                "condition": "Brand New"
            }
        ]
    },

# ========================================================
    # 1. EXPANDED ELECTRONICS: IPHONES
    # ========================================================
    {
        "product_id": "PROD-IPHONE17-001",
        "product_name": "Apple iPhone 17 (128GB, Ultramarine Blue, A19 Bionic, 48MP Fusion Camera, Action Button, USB-C)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "Apple",
        "model": "iPhone 17",
        "variant": "128GB / Ultramarine Blue",
        "variants": [
            {"dimension": "storage", "value": "128GB", "price_delta": 0.0, "is_default": True},
            {"dimension": "storage", "value": "256GB", "price_delta": 10000.0, "is_default": False},
            {"dimension": "color", "value": "Ultramarine Blue", "price_delta": 0.0, "is_default": True},
            {"dimension": "color", "value": "Black", "price_delta": 0.0, "is_default": False}
        ],
        "sku": "APL-IPH17-128-BLU",
        "gtin_upc_ean": "0195949038241",
        "product_description": "Next-generation Apple iPhone 17 featuring the cutting-edge A19 Bionic chip with advanced neural engine, 48MP dual Fusion camera with optical-quality 2x telephoto, Ceramic Shield 2, Action Button, and all-day battery life with USB-C 3.0.",
        "images": [
            "https://m.media-amazon.com/images/I/71657TiFeHL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/61bK6PMOC3L._SL1500_.jpg"
        ],
        "videos": ["https://www.apple.com/105/media/us/iphone/2024/overview/hero_full.mp4"],
        "specifications": {
            "display": "6.2 inch Super Retina XDR OLED 120Hz ProMotion, 2500 nits peak brightness",
            "processor": "Apple A19 Bionic (3nm, 6-core CPU, 5-core GPU, 16-core Neural Engine)",
            "ram": "8GB Unified Memory",
            "storage": "128GB NVMe",
            "camera": "48MP Main (f/1.6, Sensor-shift OIS) + 12MP Ultra-Wide (120-degree FoV)",
            "battery": "Up to 24 hours video playback, 35W fast wired charging, 25W MagSafe wireless",
            "os": "iOS 19",
            "weight_kg": 0.171,
            "warranty_months": 12
        },
        "current_price": 79900.0,
        "mrp": 84900.0,
        "discount_percentage": 5.9,
        "currency": "INR",
        "rating": 4.8,
        "review_count": 18450,
        "seller": "Apple Authorized Reseller (Appario)",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Next-Day Prime Delivery",
        "warranty": "1 Year Official Apple Manufacturer Warranty with AppleCare+ option",
        "return_policy": "7-day replacement for defective units with brand service tag",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0DGH17XYZ",
        "affiliate_url": "https://www.amazon.in/dp/B0CHX1W1XY?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.8, "price": 79900.0, "original_price": 84900.0, "discount_percent": 5.9, "availability": "In Stock", "delivery_info": "Next-Day Delivery", "product_url": "https://www.amazon.in/dp/B0CHX1W1XY", "condition": "Brand New with Seal"},
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.7, "price": 80490.0, "original_price": 84900.0, "discount_percent": 5.2, "availability": "In Stock", "delivery_info": "2 Days Delivery", "product_url": "https://www.flipkart.com/apple-iphone-15-black-128-gb/p/itm6ac6485515ae4", "condition": "Brand New with Seal"},
            {"source": "Croma", "seller_name": "Croma Electronics Ltd", "seller_rating": 4.6, "price": 81900.0, "original_price": 84900.0, "discount_percent": 3.5, "availability": "In Stock", "delivery_info": "Store Pickup Available", "product_url": "https://www.croma.com/phones-wearables/mobile-phones/c/95", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "PROD-IPHONE17-PROMAX",
        "product_name": "Apple iPhone 17 Pro Max (256GB, Desert Titanium, A19 Pro 3nm, 5x Telephoto 48MP, 120Hz ProMotion)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "Apple",
        "model": "iPhone 17 Pro Max",
        "variant": "256GB / Desert Titanium",
        "variants": [
            {"dimension": "storage", "value": "256GB", "price_delta": 0.0, "is_default": True},
            {"dimension": "storage", "value": "512GB", "price_delta": 20000.0, "is_default": False},
            {"dimension": "color", "value": "Desert Titanium", "price_delta": 0.0, "is_default": True},
            {"dimension": "color", "value": "Natural Titanium", "price_delta": 0.0, "is_default": False}
        ],
        "sku": "APL-IPH17PM-256-DES",
        "gtin_upc_ean": "0195949038992",
        "product_description": "Flagship Apple iPhone 17 Pro Max crafted from grade 5 titanium with the industry-leading A19 Pro chip, 48MP triple camera system with 5x optical telephoto zoom, ProRes 4K 120fps recording, and unprecedented battery endurance.",
        "images": [
            "https://m.media-amazon.com/images/I/71657TiFeHL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/61bK6PMOC3L._SL1500_.jpg"
        ],
        "videos": ["https://www.apple.com/105/media/us/iphone-16-pro/2024/overview/hero_full.mp4"],
        "specifications": {
            "display": "6.9 inch Super Retina XDR OLED, 1-120Hz Always-On ProMotion",
            "processor": "Apple A19 Pro (3nm, 6-core CPU, 6-core GPU, Hardware Ray Tracing)",
            "ram": "12GB Unified Memory",
            "storage": "256GB NVMe",
            "camera": "48MP Fusion (OIS) + 48MP Ultra-Wide + 48MP 5x Periscope Telephoto",
            "battery": "Up to 33 hours video playback, 45W wired charging, 25W MagSafe",
            "os": "iOS 19",
            "weight_kg": 0.227,
            "warranty_months": 12
        },
        "current_price": 144900.0,
        "mrp": 154900.0,
        "discount_percentage": 6.5,
        "currency": "INR",
        "rating": 4.9,
        "review_count": 9240,
        "seller": "Apple Authorized Retailer",
        "seller_rating": 4.9,
        "availability": "In Stock",
        "delivery_info": "Free Priority Air Express Delivery",
        "warranty": "1 Year Official Apple Manufacturer Warranty",
        "return_policy": "7-day replacement on defective verification",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0DGH17PMAX",
        "affiliate_url": "https://www.amazon.in/dp/B0CHX1W1XY?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.9, "price": 144900.0, "original_price": 154900.0, "discount_percent": 6.5, "availability": "In Stock", "delivery_info": "Free Express Delivery", "product_url": "https://www.amazon.in/dp/B0CHX1W1XY", "condition": "Brand New with Manufacturer Seal"},
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.8, "price": 146900.0, "original_price": 154900.0, "discount_percent": 5.2, "availability": "In Stock", "delivery_info": "Express Delivery", "product_url": "https://www.flipkart.com/apple-iphone-15-pro-max/p/itm12345", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "PROD-IPHONE16-001",
        "product_name": "Apple iPhone 16 (128GB, Teal, A18 Chip, Camera Control, 48MP Main Camera, Dynamic Island)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "Apple",
        "model": "iPhone 16",
        "variant": "128GB / Teal",
        "variants": [
            {"dimension": "storage", "value": "128GB", "price_delta": 0.0, "is_default": True},
            {"dimension": "storage", "value": "256GB", "price_delta": 10000.0, "is_default": False}
        ],
        "sku": "APL-IPH16-128-TEA",
        "gtin_upc_ean": "0195949012345",
        "product_description": "Apple iPhone 16 with dedicated Camera Control button, powerful A18 chip designed for Apple Intelligence, durable aerospace aluminum casing, and Super Retina XDR OLED.",
        "images": [
            "https://m.media-amazon.com/images/I/71657TiFeHL._SL1500_.jpg"
        ],
        "videos": [],
        "specifications": {
            "display": "6.1 inch Super Retina XDR OLED",
            "processor": "Apple A18 (3nm, 6-core CPU)",
            "ram": "8GB Unified Memory",
            "storage": "128GB NVMe",
            "camera": "48MP Fusion + 12MP Ultra-Wide",
            "battery": "Up to 22 hours video playback",
            "os": "iOS 18",
            "weight_kg": 0.170,
            "warranty_months": 12
        },
        "current_price": 74900.0,
        "mrp": 79900.0,
        "discount_percentage": 6.3,
        "currency": "INR",
        "rating": 4.8,
        "review_count": 21300,
        "seller": "Appario Retail Pvt Ltd",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Next-Day Delivery",
        "warranty": "1 Year Manufacturer Warranty",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0DGJ9E161",
        "affiliate_url": "https://www.amazon.in/dp/B0CHX1W1XY?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.8, "price": 74900.0, "original_price": 79900.0, "discount_percent": 6.3, "availability": "In Stock", "delivery_info": "Next-Day Delivery", "product_url": "https://www.amazon.in/dp/B0CHX1W1XY", "condition": "Brand New"}
        ]
    },

    # ========================================================
    # 2. EXPANDED ELECTRONICS: SAMSUNG GALAXY PHONES
    # ========================================================
    {
        "product_id": "PROD-SAMS24-ULTRA",
        "product_name": "Samsung Galaxy S24 Ultra 5G (12GB RAM, 256GB Storage, Titanium Gray, Snapdragon 8 Gen 3, 200MP Camera, S-Pen)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "Samsung",
        "model": "Galaxy S24 Ultra",
        "variant": "12GB / 256GB / Titanium Gray",
        "variants": [
            {"dimension": "storage", "value": "256GB", "price_delta": 0.0, "is_default": True},
            {"dimension": "storage", "value": "512GB", "price_delta": 15000.0, "is_default": False}
        ],
        "sku": "SAM-S24U-256-GRY",
        "gtin_upc_ean": "0880609531234",
        "product_description": "The ultimate Galaxy AI flagship. Samsung Galaxy S24 Ultra features robust Titanium armor, integrated S-Pen stylus, custom Snapdragon 8 Gen 3 for Galaxy, 200MP Quad Telephoto camera with 100x Space Zoom, and 7 years of OS upgrades.",
        "images": [
            "https://m.media-amazon.com/images/I/71qGismu6NL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/717Qo4MH97L._SL1500_.jpg"
        ],
        "videos": ["https://images.samsung.com/is/content/samsung/p6pim/in/feature/s24ultra_hero.mp4"],
        "specifications": {
            "display": "6.8 inch Dynamic AMOLED 2X QHD+, 1-120Hz Adaptive Refresh, Corning Gorilla Armor",
            "processor": "Qualcomm Snapdragon 8 Gen 3 for Galaxy (4nm, up to 3.39GHz)",
            "ram": "12GB LPDDR5X",
            "storage": "256GB UFS 4.0",
            "camera": "200MP Main + 50MP 5x Periscope + 12MP Ultra-Wide + 10MP 3x Telephoto",
            "battery": "5000mAh with 45W fast charging, 15W wireless charging, Reverse wireless",
            "os": "One UI 6.1 with Galaxy AI (Android 14, 7 OS upgrades promised)",
            "weight_kg": 0.232,
            "warranty_months": 12
        },
        "current_price": 129999.0,
        "mrp": 134999.0,
        "discount_percentage": 3.7,
        "currency": "INR",
        "rating": 4.8,
        "review_count": 14200,
        "seller": "Samsung Authorized Online Store",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Express Delivery with Open-Box Inspection",
        "warranty": "1 Year Manufacturer Warranty for Device & 6 Months for In-Box Accessories",
        "return_policy": "7-day replacement against manufacturing defects",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0CS5X6D8G",
        "affiliate_url": "https://www.amazon.in/dp/B0CS5X6D8G?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "STPL Exclusive Online", "seller_rating": 4.8, "price": 129999.0, "original_price": 134999.0, "discount_percent": 3.7, "availability": "In Stock", "delivery_info": "Free Express Delivery", "product_url": "https://www.amazon.in/dp/B0CS5X6D8G", "condition": "Brand New with Samsung Warranty"},
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.7, "price": 130999.0, "original_price": 134999.0, "discount_percent": 2.9, "availability": "In Stock", "delivery_info": "Standard 2-Day Delivery", "product_url": "https://www.flipkart.com/samsung-galaxy-s24-ultra-5g/p/itm12345", "condition": "Brand New"},
            {"source": "Samsung Official Store", "seller_name": "Samsung Direct India", "seller_rating": 4.9, "price": 129999.0, "original_price": 134999.0, "discount_percent": 3.7, "availability": "In Stock", "delivery_info": "Same Day Dispatch", "product_url": "https://www.samsung.com/in/smartphones/galaxy-s24-ultra/", "condition": "Official Direct"}
        ]
    },
    {
        "product_id": "PROD-SAMS23-FE",
        "product_name": "Samsung Galaxy S23 FE 5G (8GB RAM, 128GB Storage, Mint, Pro-Grade Nightography, Dynamic AMOLED 2X)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "Samsung",
        "model": "Galaxy S23 FE",
        "variant": "8GB / 128GB / Mint",
        "variants": [],
        "sku": "SAM-S23FE-128-MNT",
        "gtin_upc_ean": "0880609511122",
        "product_description": "Fan Edition flagship smartphone with pro-grade 50MP triple camera system, IP68 water resistance, Corning Gorilla Glass 5 front and back, and vivid 120Hz Dynamic AMOLED 2X display.",
        "images": [
            "https://m.media-amazon.com/images/I/71qGismu6NL._SL1500_.jpg"
        ],
        "videos": [],
        "specifications": {
            "display": "6.4 inch Dynamic AMOLED 2X FHD+ 120Hz",
            "processor": "Samsung Exynos 2200 (4nm, Octa-Core)",
            "ram": "8GB",
            "storage": "128GB",
            "camera": "50MP Main (OIS) + 12MP Ultra-Wide + 8MP 3x Telephoto",
            "battery": "4500mAh with 25W fast charging",
            "os": "One UI 6.0 (Android 14)",
            "weight_kg": 0.209,
            "warranty_months": 12
        },
        "current_price": 39999.0,
        "mrp": 54999.0,
        "discount_percentage": 27.2,
        "currency": "INR",
        "rating": 4.4,
        "review_count": 9800,
        "seller": "RetailNet Verified",
        "seller_rating": 4.5,
        "availability": "In Stock",
        "delivery_info": "Free Standard Delivery",
        "warranty": "1 Year Manufacturer Warranty",
        "return_policy": "7-day replacement",
        "source_website": "Flipkart",
        "product_url": "https://www.flipkart.com/samsung-galaxy-s23-fe-mint-256-gb/p/itm129848574100",
        "affiliate_url": "https://www.flipkart.com/samsung-galaxy-s23-fe-mint-256-gb/p/itm129848574100?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.5, "price": 39999.0, "original_price": 54999.0, "discount_percent": 27.2, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.flipkart.com/samsung-galaxy-s23-fe-mint-256-gb/p/itm129848574100", "condition": "Brand New"},
            {"source": "Amazon India", "seller_name": "STPL Exclusive", "seller_rating": 4.5, "price": 40499.0, "original_price": 54999.0, "discount_percent": 26.3, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.amazon.in/dp/B0CL9QJHRZ", "condition": "Brand New"}
        ]
    },

    # ========================================================
    # 3. EXPANDED ELECTRONICS: WIRELESS EARBUDS & AUDIO
    # ========================================================
    {
        "product_id": "PROD-AIRPODS-PRO2",
        "product_name": "Apple AirPods Pro (2nd Generation with USB-C MagSafe Case, Active Noise Cancellation, Spatial Audio, Transparency Mode)",
        "category": "electronics",
        "subcategory": "audio",
        "brand": "Apple",
        "model": "AirPods Pro (2nd Gen)",
        "variant": "USB-C MagSafe Charging Case",
        "variants": [],
        "sku": "APL-APP2-USBC",
        "gtin_upc_ean": "0195949052490",
        "product_description": "Industry benchmark true wireless earbuds. Powered by the Apple H2 headphone chip delivering 2x more Active Noise Cancellation, Adaptive Audio, Personalized Spatial Audio with dynamic head tracking, and dust, sweat, and water resistance (IP54).",
        "images": [
            "https://m.media-amazon.com/images/I/61SUj2aKoEL._SL1500_.jpg",
            "https://m.media-amazon.com/images/I/710TJuHTMhL._SL1500_.jpg"
        ],
        "videos": [],
        "specifications": {
            "driver_type": "Custom high-excursion Apple driver & custom high dynamic range amplifier",
            "noise_cancellation": "Active Noise Cancellation up to 2x more effective with Adaptive Transparency",
            "audio_technology": "Personalized Spatial Audio with dynamic head tracking, Lossless Audio with Vision Pro",
            "battery_life_hours": 6.0,
            "case_battery_hours": 30.0,
            "connectivity": "Bluetooth 5.3 with Apple H2 & U1 chip in case with speaker",
            "water_resistance": "IP54 dust, sweat, and water resistant (Earbuds and Case)",
            "weight_kg": 0.050,
            "warranty_months": 12
        },
        "current_price": 21900.0,
        "mrp": 24900.0,
        "discount_percentage": 12.0,
        "currency": "INR",
        "rating": 4.8,
        "review_count": 38900,
        "seller": "Appario Retail Pvt Ltd",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free One-Day Prime Delivery",
        "warranty": "1 Year Apple Manufacturer Warranty",
        "return_policy": "7-day replacement for defective items",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0CHWRXH8B",
        "affiliate_url": "https://www.amazon.in/dp/B0CHWRXH8B?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.8, "price": 21900.0, "original_price": 24900.0, "discount_percent": 12.0, "availability": "In Stock", "delivery_info": "Next-Day Delivery", "product_url": "https://www.amazon.in/dp/B0CHWRXH8B", "condition": "Brand New with Manufacturer Seal"},
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.7, "price": 22490.0, "original_price": 24900.0, "discount_percent": 9.6, "availability": "In Stock", "delivery_info": "2 Days Delivery", "product_url": "https://www.flipkart.com/apple-airpods-pro-2nd-gen/p/itm12345", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "PROD-SONY-WF1000XM5",
        "product_name": "Sony WF-1000XM5 Truly Wireless Noise Cancelling Earbuds (Dual Feedback Mics, LDAC Hi-Res Audio, 36hr Battery, Multipoint Connection)",
        "category": "electronics",
        "subcategory": "audio",
        "brand": "Sony",
        "model": "WF-1000XM5",
        "variant": "Black",
        "variants": [],
        "sku": "SNY-WF1000XM5-BLK",
        "gtin_upc_ean": "0454873614349",
        "product_description": "Sony flagship wireless noise cancelling earbuds featuring the Integrated Processor V2 and HD Noise Cancelling Processor QN2e. Equipped with Dynamic Driver X for wide frequency reproduction, AI-based bone conduction voice pickup, and LDAC Hi-Res audio.",
        "images": [
            "https://m.media-amazon.com/images/I/61SUj2aKoEL._SL1500_.jpg"
        ],
        "videos": [],
        "specifications": {
            "driver_unit": "8.4 mm Dynamic Driver X",
            "processors": "Integrated Processor V2 & HD Noise Cancelling Processor QN2e",
            "bluetooth_version": "5.3 (LDAC, AAC, SBC, LC3)",
            "battery_life_hours": 8.0,
            "case_battery_hours": 24.0,
            "features": "Multipoint connection, Speak-to-Chat, Qi Wireless charging, IPX4",
            "weight_kg": 0.045,
            "warranty_months": 12
        },
        "current_price": 19990.0,
        "mrp": 29990.0,
        "discount_percentage": 33.3,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 8750,
        "seller": "Sony Official & Authorized Partners",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Standard Delivery",
        "warranty": "1 Year Official Sony Brand Warranty",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0C8VBRWQL",
        "affiliate_url": "https://www.amazon.in/dp/B0C8VBRWQL?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.7, "price": 19990.0, "original_price": 29990.0, "discount_percent": 33.3, "availability": "In Stock", "delivery_info": "Free Express Shipping", "product_url": "https://www.amazon.in/dp/B0C8VBRWQL", "condition": "Brand New"},
            {"source": "Croma", "seller_name": "Croma Retail", "seller_rating": 4.6, "price": 20490.0, "original_price": 29990.0, "discount_percent": 31.6, "availability": "In Stock", "delivery_info": "Store Pickup Available", "product_url": "https://www.croma.com/audio/earbuds/c/45", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "PROD-BOAT-AIRDOPES141",
        "product_name": "boAt Airdopes 141 Bluetooth Truly Wireless Earbuds (42H Playtime, Beast Mode 80ms Low Latency, ENx Noise Cancelling Mics, IPX4)",
        "category": "electronics",
        "subcategory": "audio",
        "brand": "boAt",
        "model": "Airdopes 141",
        "variant": "Bold Black",
        "variants": [],
        "sku": "BOAT-AD141-BLK",
        "gtin_upc_ean": "0890610842141",
        "product_description": "Top budget truly wireless earbuds with massive 42 hours total playback, 8mm dynamic drivers for rich bass, ASAP Charge giving 75 mins in 5 mins charge, and Beast Mode low-latency for mobile gaming.",
        "images": [
            "https://m.media-amazon.com/images/I/61SUj2aKoEL._SL1500_.jpg"
        ],
        "videos": [],
        "specifications": {
            "driver_unit": "8mm Dynamic Bass Drivers",
            "latency": "80ms Beast Mode Gaming Latency",
            "battery_life_hours": 6.0,
            "case_battery_hours": 42.0,
            "water_resistance": "IPX4 Sweat and Splash Proof",
            "fast_charging": "ASAP Charge 5 mins = 75 mins playtime",
            "warranty_months": 12
        },
        "current_price": 1299.0,
        "mrp": 4490.0,
        "discount_percentage": 71.0,
        "currency": "INR",
        "rating": 4.3,
        "review_count": 218000,
        "seller": "Imagine Marketing Pvt Ltd (boAt Official)",
        "seller_rating": 4.6,
        "availability": "In Stock",
        "delivery_info": "Free Standard Delivery",
        "warranty": "1 Year Manufacturer Replacement Warranty",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B09N3ZNHTY",
        "affiliate_url": "https://www.amazon.in/dp/B09N3ZNHTY?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.6, "price": 1299.0, "original_price": 4490.0, "discount_percent": 71.0, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.amazon.in/dp/B09N3ZNHTY", "condition": "Brand New"}
        ]
    },

    # ========================================================
    # 4. EXPANDED FASHION: RUNNING SHOES
    # ========================================================
    {
        "product_id": "PROD-ADIDAS-ULTRABOOST",
        "product_name": "Adidas Ultraboost Light Running Shoes for Men (Light BOOST Cushioning, Continental Natural Rubber Outsole, Primeknit+ Upper)",
        "category": "fashion",
        "subcategory": "footwear",
        "brand": "Adidas",
        "model": "Ultraboost Light",
        "variant": "Core Black / Cloud White (UK 9)",
        "variants": [
            {"dimension": "size", "value": "UK 8", "price_delta": 0.0, "is_default": False},
            {"dimension": "size", "value": "UK 9", "price_delta": 0.0, "is_default": True},
            {"dimension": "size", "value": "UK 10", "price_delta": 0.0, "is_default": False}
        ],
        "sku": "ADI-UB-LGT-BLK-9",
        "gtin_upc_ean": "0406674823901",
        "product_description": "Experience epic energy return with the lightest Ultraboost ever made. Featuring revolutionary Light BOOST foam cushioning that is 30% lighter than standard BOOST, foot-hugging Primeknit+ textile upper, and Continental rubber grip.",
        "images": [
            "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "cushioning": "Light BOOST midsole (30% lighter energy capsule foam)",
            "outsole": "Continental Better Rubber for superior wet & dry asphalt grip",
            "upper": "Adidas PRIMEKNIT+ textile upper with yarn containing at least 50% Parley Ocean Plastic",
            "weight_per_shoe_grams": 293,
            "midsole_drop_mm": 10.0,
            "surface": "Road & Marathon Running",
            "warranty_months": 3
        },
        "current_price": 11999.0,
        "mrp": 18999.0,
        "discount_percentage": 36.8,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 8450,
        "seller": "Adidas India Marketing Pvt Ltd",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Standard Express Shipping",
        "warranty": "3-month brand manufacturing warranty",
        "return_policy": "14-day hassle free size exchange or return",
        "source_website": "Myntra",
        "product_url": "https://www.myntra.com/running-shoes/adidas/adidas-men-black-ultraboost-light-running-shoes/22818902/buy",
        "affiliate_url": "https://www.myntra.com/running-shoes/adidas/22818902?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Myntra", "seller_name": "Adidas India Authorised", "seller_rating": 4.8, "price": 11999.0, "original_price": 18999.0, "discount_percent": 36.8, "availability": "In Stock", "delivery_info": "3-Day Delivery", "product_url": "https://www.myntra.com/running-shoes/adidas/22818902", "condition": "Brand New with Original Tag"},
            {"source": "Amazon India", "seller_name": "Cloudtail Footwear", "seller_rating": 4.6, "price": 12499.0, "original_price": 18999.0, "discount_percent": 34.2, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.amazon.in/dp/B0BTQ9KJL7", "condition": "Brand New with Box"}
        ]
    },
    {
        "product_id": "PROD-PUMA-VELOCITY",
        "product_name": "Puma Velocity Nitro 2 Men's Road Running Shoes (NITRO FOAM Responsive Cushioning, PUMAGRIP Rubber)",
        "category": "fashion",
        "subcategory": "footwear",
        "brand": "Puma",
        "model": "Velocity Nitro 2",
        "variant": "Royal Blue (UK 8)",
        "variants": [],
        "sku": "PUM-VN2-BLU-8",
        "gtin_upc_ean": "0406544912389",
        "product_description": "All-in-one lightweight and durable neutral running shoe. Features advanced NITRO FOAM nitrogen-infused cushioning for superior responsiveness and PUMAGRIP all-surface traction.",
        "images": [
            "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "cushioning": "NITRO FOAM nitrogen-injected responsive midsole",
            "outsole": "PUMAGRIP durable rubber compound",
            "upper": "Engineered breathable mesh with reflective elements",
            "weight_per_shoe_grams": 257,
            "midsole_drop_mm": 10.0,
            "warranty_months": 3
        },
        "current_price": 5499.0,
        "mrp": 9999.0,
        "discount_percentage": 45.0,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 12400,
        "seller": "Puma Sports India Pvt Ltd",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Express Delivery",
        "warranty": "3-month brand warranty",
        "return_policy": "10-day replacement & size exchange",
        "source_website": "Myntra",
        "product_url": "https://www.myntra.com/running-shoes/puma/puma-velocity-nitro-2/buy",
        "affiliate_url": "https://www.myntra.com/running-shoes/puma?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Myntra", "seller_name": "Puma Official Store", "seller_rating": 4.7, "price": 5499.0, "original_price": 9999.0, "discount_percent": 45.0, "availability": "In Stock", "delivery_info": "Express Delivery", "product_url": "https://www.myntra.com/running-shoes/puma", "condition": "Brand New with Box"}
        ]
    },

    # ========================================================
    # 5. EXPANDED HOME: AIR FRYERS
    # ========================================================
    {
        "product_id": "PROD-PHILIPS-AIRFRYER",
        "product_name": "Philips Digital Air Fryer HD9252/90 (4.1 Litre, Rapid Air Technology, Touch Screen with 7 Presets, 1400 Watt, Keep Warm Mode)",
        "category": "home-furniture",
        "subcategory": "kitchen-appliances",
        "brand": "Philips",
        "model": "HD9252/90",
        "variant": "4.1L Digital Touchscreen / Black",
        "variants": [],
        "sku": "PHL-AF-HD9252-BLK",
        "gtin_upc_ean": "0871010396412",
        "product_description": "The world's leading Airfryer brand. Philips HD9252/90 features patented Rapid Air starfish technology that swirls hot air to create delicious foods with up to 90% less fat. Includes digital touchscreen with 7 one-touch cooking presets, Keep Warm function, and NutriU recipe app integration.",
        "images": [
            "https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "capacity": "4.1 Litres (0.8 kg food capacity, suitable for 3-4 persons)",
            "power": "1400 Watts, 220-240V operating voltage",
            "technology": "Rapid Air Starfish Base for even 360-degree heat distribution",
            "presets": "7 Presets (Fries, Frozen Snacks, Chicken, Fish, Cake, Grilled Meat, Warm)",
            "temperature_range": "60°C to 200°C with 60-minute automatic shut-off timer",
            "coating": "QuickClean non-stick basket, dishwasher safe removable parts",
            "weight_kg": 4.5,
            "warranty_months": 24
        },
        "current_price": 7999.0,
        "mrp": 11995.0,
        "discount_percentage": 33.3,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 27800,
        "seller": "Philips Authorized Online Partner",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Standard Express Delivery",
        "warranty": "2 Years Official Philips Domestic & Worldwide Warranty",
        "return_policy": "7-day replacement for technical defects",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B08DGYX6K3",
        "affiliate_url": "https://www.amazon.in/dp/B08DGYX6K3?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.7, "price": 7999.0, "original_price": 11995.0, "discount_percent": 33.3, "availability": "In Stock", "delivery_info": "Next-Day Delivery", "product_url": "https://www.amazon.in/dp/B08DGYX6K3", "condition": "Brand New with Manufacturer Warranty"},
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.6, "price": 8299.0, "original_price": 11995.0, "discount_percent": 30.8, "availability": "In Stock", "delivery_info": "2 Days Delivery", "product_url": "https://www.flipkart.com/philips-hd9252-90-air-fryer/p/itm12345", "condition": "Brand New"},
            {"source": "Croma", "seller_name": "Croma Electronics Ltd", "seller_rating": 4.5, "price": 8490.0, "original_price": 11995.0, "discount_percent": 29.2, "availability": "In Stock", "delivery_info": "Store Pickup Available", "product_url": "https://www.croma.com/small-appliances/air-fryers/c/12", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "PROD-INSTANTPOT-AF",
        "product_name": "Instant Pot Vortex Plus 6-in-1 Air Fryer (5.7 Litre, EvenCrisp Technology, OdorErase Filters, Roast, Bake, Reheat, Dehydrate)",
        "category": "home-furniture",
        "subcategory": "kitchen-appliances",
        "brand": "Instant Pot",
        "model": "Vortex Plus 6-in-1",
        "variant": "5.7L Stainless Steel",
        "variants": [],
        "sku": "INS-VOR-57L-SS",
        "gtin_upc_ean": "0850004871234",
        "product_description": "Premium large-capacity 5.7L air fryer with built-in OdorErase carbon filter technology to remove cooking odors. EvenCrisp airflow delivers crispy golden finishes without extra oil.",
        "images": [
            "https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "capacity": "5.7 Litres (family size, fits 1.8kg chicken)",
            "power": "1700 Watts high-efficiency heating",
            "features": "ClearCook viewing window, OdorErase filter, 6 smart programs",
            "temperature_range": "35°C to 205°C",
            "warranty_months": 24
        },
        "current_price": 9990.0,
        "mrp": 14999.0,
        "discount_percentage": 33.4,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 12100,
        "seller": "Instant Brands India Authorized",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Express Delivery",
        "warranty": "2 Years Official Warranty",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B08V3M83G8",
        "affiliate_url": "https://www.amazon.in/dp/B08V3M83G8?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.7, "price": 9990.0, "original_price": 14999.0, "discount_percent": 33.4, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.amazon.in/dp/B08V3M83G8", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "PROD-PIGEON-AF",
        "product_name": "Pigeon Healthifry Digital Air Fryer (4.2 Litre, 1200W, 360 Degree High Speed Air Circulation, Non-Stick Food Basket)",
        "category": "home-furniture",
        "subcategory": "kitchen-appliances",
        "brand": "Pigeon",
        "model": "Healthifry 4.2L",
        "variant": "4.2L Green",
        "variants": [],
        "sku": "PIG-HF-42L-GRN",
        "gtin_upc_ean": "0890421471234",
        "product_description": "Affordable budget digital air fryer featuring 360-degree air circulation for healthy oil-free snacks. Easy to clean removable non-stick basket and intuitive digital controls.",
        "images": [
            "https://images.unsplash.com/photo-1585515320310-259814833e62?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "capacity": "4.2 Litres",
            "power": "1200 Watts",
            "timer": "Up to 60 minutes with auto-shutoff",
            "warranty_months": 12
        },
        "current_price": 2999.0,
        "mrp": 5995.0,
        "discount_percentage": 50.0,
        "currency": "INR",
        "rating": 4.3,
        "review_count": 34500,
        "seller": "Stovekraft Limited (Pigeon Official)",
        "seller_rating": 4.5,
        "availability": "In Stock",
        "delivery_info": "Free Standard Delivery",
        "warranty": "1 Year Manufacturer Warranty",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B09V7N8V2R",
        "affiliate_url": "https://www.amazon.in/dp/B09V7N8V2R?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.5, "price": 2999.0, "original_price": 5995.0, "discount_percent": 50.0, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.amazon.in/dp/B09V7N8V2R", "condition": "Brand New"}
        ]
    },

    # ========================================================
    # 6. EXPANDED OFFICE: OFFICE CHAIRS (UNDER 10000)
    # ========================================================
    {
        "product_id": "PROD-DAURBAN-CHAIR",
        "product_name": "Da URBAN Miller High Back Ergonomic Mesh Office Chair (Heavy Duty Metal Base, Tilt Lock, 2D Lumbar Support, Padded Armrests)",
        "category": "office-products",
        "subcategory": "office-furniture-organization",
        "brand": "Da URBAN",
        "model": "Miller High Back",
        "variant": "Black Mesh",
        "variants": [],
        "sku": "DAU-MIL-HB-BLK",
        "gtin_upc_ean": "0890432171234",
        "product_description": "Ergonomically engineered computer executive chair under ₹10,000. Features breathable double-layer Korean mesh back, pneumatic seat-height adjustment, sturdy heavy-duty chrome star base, and 120kg weight capacity.",
        "images": [
            "https://images.unsplash.com/photo-1589384267710-7a170981ca78?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "back_type": "High Back with Breathable Korean Mesh",
            "lumbar_support": "Adjustable 2D Lumbar Support Cushion",
            "base": "Heavy Duty 350mm Chrome Plated Metal Star Base with 50mm PU Dual Castor Wheels",
            "mechanism": "Heavy Duty Any-Position Tilt Lock Multi-Synchro Mechanism",
            "weight_capacity_kg": 125,
            "warranty_months": 36
        },
        "current_price": 6499.0,
        "mrp": 14999.0,
        "discount_percentage": 56.7,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 8900,
        "seller": "Da URBAN Direct Official",
        "seller_rating": 4.6,
        "availability": "In Stock",
        "delivery_info": "Free Standard Express Delivery with Doorstep Assembly Support",
        "warranty": "3 Years Comprehensive Brand Warranty",
        "return_policy": "10-day replacement policy against structural transit damage",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B07N8Z7XZR",
        "affiliate_url": "https://www.amazon.in/dp/B07N8Z7XZR?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Da URBAN Official", "seller_rating": 4.6, "price": 6499.0, "original_price": 14999.0, "discount_percent": 56.7, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.amazon.in/dp/B07N8Z7XZR", "condition": "Brand New with Warranty"},
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.5, "price": 6799.0, "original_price": 14999.0, "discount_percent": 54.7, "availability": "In Stock", "delivery_info": "Standard Delivery", "product_url": "https://www.flipkart.com/da-urban-miller-office-chair/p/itm12345", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "PROD-FEATHERLITE-ASTRO",
        "product_name": "Featherlite Astro Medium Back Ergonomic Office Chair (Adjustable Lumbar Support, Synchro Tilt, Nylon Base, Work From Home)",
        "category": "office-products",
        "subcategory": "office-furniture-organization",
        "brand": "Featherlite",
        "model": "Astro Medium Back",
        "variant": "Black",
        "variants": [],
        "sku": "FTH-AST-MB-BLK",
        "gtin_upc_ean": "0890600123456",
        "product_description": "Original Featherlite ergonomic task chair tested under stringent BIFMA standards. Engineered for 8+ hours of daily ergonomic sitting with contoured high-density molded foam cushion.",
        "images": [
            "https://images.unsplash.com/photo-1505797149-43b0069ec26b?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "back_type": "Medium Back High-Tensile Mesh",
            "certification": "BIFMA Level 3 Certified Ergonomics",
            "cushion": "High-Density 45kg/m3 Cold-Cure Molded Foam Seat",
            "mechanism": "Synchro-Tilt with Multi-Lock",
            "warranty_months": 36
        },
        "current_price": 9499.0,
        "mrp": 12999.0,
        "discount_percentage": 26.9,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 6400,
        "seller": "Featherlite Furniture Official",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Delivery",
        "warranty": "3 Years On-Site Brand Warranty",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B08N8Z7XYZ",
        "affiliate_url": "https://www.amazon.in/dp/B08N8Z7XYZ?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Featherlite Authorised", "seller_rating": 4.7, "price": 9499.0, "original_price": 12999.0, "discount_percent": 26.9, "availability": "In Stock", "delivery_info": "Free Shipping", "product_url": "https://www.amazon.in/dp/B08N8Z7XYZ", "condition": "Brand New"}
        ]
    },

    # ========================================================
    # 7. EXPANDED HOME: WASHING MACHINES
    # ========================================================
    {
        "product_id": "PROD-SAMS-WASHING",
        "product_name": "Samsung 7.0 Kg 5 Star Inverter Fully-Automatic Front Loading Washing Machine (WW70T4020CX/TL, Hygiene Steam, Digital Inverter, Diamond Drum)",
        "category": "home-furniture",
        "subcategory": "home-appliances",
        "brand": "Samsung",
        "model": "WW70T4020CX/TL",
        "variant": "7.0 Kg / Inox Gray",
        "variants": [],
        "sku": "SAM-WM-7KG-INX",
        "gtin_upc_ean": "0880609123456",
        "product_description": "Samsung 7kg 5-star front load washing machine with Hygiene Steam cycle that removes 99.9% of bacteria and allergens. Powered by Digital Inverter Motor with 20-year warranty, Diamond Drum fabric care, and StayClean Drawer.",
        "images": [
            "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "capacity": "7.0 Kg (ideal for families with 3-4 members)",
            "energy_rating": "5 Star BEE Certified with Highest Efficiency",
            "motor": "Digital Inverter Motor with 20 Years Motor Warranty",
            "spin_speed_rpm": 1200,
            "wash_programs": "12 Programs including Hygiene Steam, Quick 15', Delicates, Cotton, Wool",
            "features": "Diamond Drum, Child Lock, Delay End, Ceramic Heater",
            "weight_kg": 65.0,
            "warranty_months": 24
        },
        "current_price": 29990.0,
        "mrp": 38990.0,
        "discount_percentage": 23.1,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 18900,
        "seller": "Samsung Direct & Authorized Partners",
        "seller_rating": 4.6,
        "availability": "In Stock",
        "delivery_info": "Free Standard Scheduled Delivery with Free Installation",
        "warranty": "2 Years Comprehensive Warranty and 20 Years on Motor",
        "return_policy": "10-day replacement against transit damages or technical faults",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B08SAM7KGW",
        "affiliate_url": "https://www.amazon.in/dp/B08DGYX6K3?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.6, "price": 29990.0, "original_price": 38990.0, "discount_percent": 23.1, "availability": "In Stock", "delivery_info": "Free Delivery & Install", "product_url": "https://www.amazon.in/dp/B08DGYX6K3", "condition": "Brand New"},
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.5, "price": 30490.0, "original_price": 38990.0, "discount_percent": 21.8, "availability": "In Stock", "delivery_info": "Scheduled Delivery", "product_url": "https://www.flipkart.com/samsung-7kg-front-load-washing-machine/p/itm12345", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "PROD-BOSCH-WASHING",
        "product_name": "Bosch 8.0 Kg 5 Star Inverter Touch Control Front Loading Washing Machine (WAJ28262IN, AntiTangle, EcoSilence Drive, ActiveWater Plus)",
        "category": "home-furniture",
        "subcategory": "home-appliances",
        "brand": "Bosch",
        "model": "WAJ28262IN",
        "variant": "8.0 Kg / Silver",
        "variants": [],
        "sku": "BSH-WM-8KG-SLV",
        "gtin_upc_ean": "0424200523456",
        "product_description": "German engineered Bosch 8.0 Kg front load washing machine with friction-free EcoSilence Drive motor that reduces heat and wear for long-lasting performance and quiet operation. ActiveWater Plus optimizes water use based on load weight.",
        "images": [
            "https://images.unsplash.com/photo-1626806787461-102c1bfaaea1?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "capacity": "8.0 Kg (ideal for large families)",
            "energy_rating": "5 Star BEE Certified",
            "motor": "EcoSilence Drive Brushless Motor with 12 Years Warranty",
            "spin_speed_rpm": 1400,
            "features": "AntiTangle feature minimizes tangles in laundry by up to 50%, VarioDrum, AntiVibration Side Panels",
            "weight_kg": 71.0,
            "warranty_months": 24
        },
        "current_price": 36490.0,
        "mrp": 52990.0,
        "discount_percentage": 31.1,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 14500,
        "seller": "Bosch Home Appliances Official",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Delivery & Free Brand Demo",
        "warranty": "2 Years Comprehensive and 12 Years on Motor",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B08V3M83G9",
        "affiliate_url": "https://www.amazon.in/dp/B08V3M83G9?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.7, "price": 36490.0, "original_price": 52990.0, "discount_percent": 31.1, "availability": "In Stock", "delivery_info": "Free Express Delivery", "product_url": "https://www.amazon.in/dp/B08V3M83G9", "condition": "Brand New"},
            {"source": "Croma", "seller_name": "Croma Electronics Ltd", "seller_rating": 4.6, "price": 37990.0, "original_price": 52990.0, "discount_percent": 28.3, "availability": "In Stock", "delivery_info": "Free Shipping", "product_url": "https://www.croma.com/large-appliances/washing-machines/c/32", "condition": "Brand New"}
        ]
    },

    # ========================================================
    # 8. EXPANDED ELECTRONICS: GAMING LAPTOPS (RTX 5070 / 4060)
    # ========================================================
    {
        "product_id": "PROD-ASUS-ROG-5070",
        "product_name": "ASUS ROG Zephyrus G16 AI Gaming Laptop (16 inch 2.5K OLED 240Hz, Intel Core Ultra 9 185H, 32GB LPDDR5X, 1TB SSD, NVIDIA RTX 5070 12GB)",
        "category": "electronics",
        "subcategory": "laptops",
        "brand": "ASUS",
        "model": "ROG Zephyrus G16 GU605",
        "variant": "32GB / 1TB / Eclipse Gray",
        "variants": [],
        "sku": "ASU-ROG-G16-5070",
        "gtin_upc_ean": "0197105412345",
        "product_description": "Next-gen AI powerhouse ultra-slim gaming laptop. Features 2.5K OLED 240Hz 0.2ms ROG Nebula display, Intel Core Ultra 9 with dedicated NPU for generative AI, NVIDIA GeForce RTX 5070 with 12GB GDDR7, CNC aluminum unibody, and 90Wh battery.",
        "images": [
            "https://images.unsplash.com/photo-1541807084-5c52b6b3adef?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "display": "16 inch 2.5K (2560 x 1600) OLED 240Hz 0.2ms 100% DCI-P3 VESA DisplayHDR True Black 500",
            "processor": "Intel Core Ultra 9 185H (16 Cores / 22 Threads, up to 5.1 GHz, Intel AI Boost NPU)",
            "ram_gb": 32,
            "storage_gb": 1024,
            "gpu": "NVIDIA GeForce RTX 5070 Laptop GPU 12GB GDDR7 (ROG Boost 115W TGP)",
            "battery_life_hours": 9.5,
            "weight_kg": 1.85,
            "os": "Windows 11 Pro",
            "warranty_months": 24
        },
        "current_price": 189990.0,
        "mrp": 219990.0,
        "discount_percentage": 13.6,
        "currency": "INR",
        "rating": 4.9,
        "review_count": 3200,
        "seller": "ASUS Official Store & Cloudtail",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Express Air Delivery",
        "warranty": "2 Years International Warranty + 1 Year Accidental Damage Protection",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0DROG5070",
        "affiliate_url": "https://www.amazon.in/dp/B0D9BMBP3H?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.8, "price": 189990.0, "original_price": 219990.0, "discount_percent": 13.6, "availability": "In Stock", "delivery_info": "Free Air Shipping", "product_url": "https://www.amazon.in/dp/B0D9BMBP3H", "condition": "Brand New with Manufacturer Seal"}
        ]
    },
    {
        "product_id": "PROD-MSI-KATANA15",
        "product_name": "MSI Katana 15 Gaming Laptop (15.6 inch FHD 144Hz, Intel 13th Gen Core i7-13620H, 16GB DDR5, 1TB NVMe SSD, NVIDIA RTX 4060 8GB, Win 11)",
        "category": "electronics",
        "subcategory": "laptops",
        "brand": "MSI",
        "model": "Katana 15 B13VFK",
        "variant": "16GB / 1TB / Black",
        "variants": [],
        "sku": "MSI-KAT15-4060",
        "gtin_upc_ean": "0471907291234",
        "product_description": "Battlefield ready gaming laptop with 13th Gen Intel Core i7 processor, 8GB NVIDIA GeForce RTX 4060 GPU with MUX Switch, Cooler Boost 5 with 2 fans and 6 heat pipes, 4-Zone RGB keyboard, and Hi-Res Audio.",
        "images": [
            "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "display": "15.6 inch FHD (1920x1080) 144Hz IPS-Level Display",
            "processor": "Intel Core i7-13620H (10 Cores, up to 4.9GHz)",
            "ram_gb": 16,
            "storage_gb": 1024,
            "gpu": "NVIDIA GeForce RTX 4060 8GB GDDR6 (105W Maximum Graphics Power)",
            "battery_life_hours": 6.0,
            "weight_kg": 2.25,
            "os": "Windows 11 Home",
            "warranty_months": 24
        },
        "current_price": 78990.0,
        "mrp": 99990.0,
        "discount_percentage": 21.0,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 6800,
        "seller": "MSI Authorized Retailer",
        "seller_rating": 4.6,
        "availability": "In Stock",
        "delivery_info": "Free Standard Delivery",
        "warranty": "2 Years Brand Warranty",
        "return_policy": "7-day replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0BSLN9HYH",
        "affiliate_url": "https://www.amazon.in/dp/B0BSLN9HYH?tag=shopai-21",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.6, "price": 78990.0, "original_price": 99990.0, "discount_percent": 21.0, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.amazon.in/dp/B0BSLN9HYH", "condition": "Brand New"}
        ]
    },
# ========================================================
    # 9. EXPANDED FASHION: WOMEN'S DRESSES & APPAREL
    # ========================================================
    {
        "product_id": "FASH-DRS-LIBAS-FLORAL",
        "product_name": "Libas Women Floral Printed Pure Cotton A-Line Midi Dress (V-Neck, Three-Quarter Sleeves, Waist Tie-Up Belt)",
        "category": "fashion",
        "subcategory": "womens-clothing",
        "brand": "Libas",
        "model": "A-Line Floral Midi",
        "variant": "Medium (M) / Mustard Yellow",
        "variants": [
            {"dimension": "size", "value": "S", "price_delta": 0.0, "is_default": False},
            {"dimension": "size", "value": "M", "price_delta": 0.0, "is_default": True},
            {"dimension": "size", "value": "L", "price_delta": 0.0, "is_default": False},
            {"dimension": "size", "value": "XL", "price_delta": 100.0, "is_default": False}
        ],
        "sku": "LIB-DRS-FLR-MID-M",
        "gtin_upc_ean": "0890782103456",
        "product_description": "Vibrant and breezy pure cotton A-line midi dress by Libas. Tailored with a graceful V-neck, three-quarter sleeves, tiered flare hem, and an adjustable fabric tie-up belt for an hourglass silhouette. Breathable fabric ideal for day outings and office wear.",
        "images": [
            "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "fabric": "100% Pure Cambric Cotton",
            "fit": "A-Line Flared Fit",
            "length": "Midi / Calf Length",
            "pattern": "Floral Botanical Block Print",
            "neck": "V-Neck with Button Accent",
            "sleeve_length": "Three-Quarter Sleeves",
            "occasion": "Casual / Day Wear / Work",
            "wash_care": "Machine Wash Warm Gentle",
            "warranty_months": 1
        },
        "current_price": 1299.0,
        "mrp": 2799.0,
        "discount_percentage": 53.6,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 8400,
        "seller": "Myntra Verified Retail",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Express 2-Day Delivery",
        "warranty": "Brand Quality Assurance & Hassle-Free Exchange",
        "return_policy": "14-day easy return & size exchange policy",
        "source_website": "Myntra",
        "product_url": "https://www.myntra.com/dresses/libas/libas-women-mustard-yellow-floral-printed-pure-cotton-a-line-dress/18293740/buy",
        "affiliate_url": "https://www.myntra.com/dresses/libas/18293740?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Myntra", "seller_name": "Libas Direct Official", "seller_rating": 4.7, "price": 1299.0, "original_price": 2799.0, "discount_percent": 53.6, "availability": "In Stock", "delivery_info": "2 Days Delivery", "product_url": "https://www.myntra.com/dresses/libas/18293740/buy", "condition": "Brand New with Tags"},
            {"source": "Amazon India", "seller_name": "Cloudtail Apparel", "seller_rating": 4.6, "price": 1349.0, "original_price": 2799.0, "discount_percent": 51.8, "availability": "In Stock", "delivery_info": "Next-Day Delivery", "product_url": "https://www.amazon.in/dp/B0DGLIBAS1", "condition": "Brand New"},
            {"source": "Ajio", "seller_name": "Reliance Retail Ltd", "seller_rating": 4.5, "price": 1399.0, "original_price": 2799.0, "discount_percent": 50.0, "availability": "In Stock", "delivery_info": "3 Days Delivery", "product_url": "https://www.ajio.com/libas-floral-dress/p/10293847", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "FASH-DRS-VEROMODA-FITFLARE",
        "product_name": "Vero Moda Square Neck Puff Sleeve Tiered Fit & Flare Dress (Knee Length, Cotton Blend, Side Zipper)",
        "category": "fashion",
        "subcategory": "womens-clothing",
        "brand": "Vero Moda",
        "model": "Tiered Fit & Flare",
        "variant": "Small (S) / Emerald Green",
        "variants": [
            {"dimension": "size", "value": "XS", "price_delta": 0.0, "is_default": False},
            {"dimension": "size", "value": "S", "price_delta": 0.0, "is_default": True},
            {"dimension": "size", "value": "M", "price_delta": 0.0, "is_default": False},
            {"dimension": "size", "value": "L", "price_delta": 0.0, "is_default": False}
        ],
        "sku": "VM-DRS-SLD-FLR-S",
        "gtin_upc_ean": "0571521401234",
        "product_description": "Chic European styling fit and flare dress from Vero Moda. Designed with an elegant square neckline, dramatic puff sleeves with elastic cuffs, multi-tier flowy skirt, and a concealed side zipper. Premium woven cotton blend with smooth inner lining.",
        "images": [
            "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "fabric": "95% Cotton, 5% Elastane Poplin",
            "fit": "Fit & Flare Silhouette",
            "length": "Knee Length",
            "pattern": "Solid Deep Emerald Green",
            "neck": "Square Neckline with Elasticated Shoulders",
            "sleeve_length": "Short Puff Sleeves",
            "occasion": "Brunch / Evening Gathering / Casual Party",
            "wash_care": "Machine Wash Delicate",
            "warranty_months": 1
        },
        "current_price": 1499.0,
        "mrp": 2999.0,
        "discount_percentage": 50.0,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 6200,
        "seller": "Vero Moda Official Store",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Standard Express Delivery",
        "warranty": "Bestseller Brand Guarantee",
        "return_policy": "14-day hassle-free exchange & refund",
        "source_website": "Myntra",
        "product_url": "https://www.myntra.com/dresses/vero-moda/vero-moda-green-fit--flare-dress/19827361/buy",
        "affiliate_url": "https://www.myntra.com/dresses/vero-moda/19827361?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Myntra", "seller_name": "Bestseller India Authorised", "seller_rating": 4.7, "price": 1499.0, "original_price": 2999.0, "discount_percent": 50.0, "availability": "In Stock", "delivery_info": "Express Delivery", "product_url": "https://www.myntra.com/dresses/vero-moda/19827361/buy", "condition": "Brand New with Original Hanger Tag"},
            {"source": "Amazon India", "seller_name": "Appario Fashion", "seller_rating": 4.6, "price": 1599.0, "original_price": 2999.0, "discount_percent": 46.7, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.amazon.in/dp/B0DGVEROM1", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "FASH-DRS-TOKYOTALKIES-BODYCON",
        "product_name": "Tokyo Talkies Sleeveless Ribbed Knit Bodycon Midi Dress (High Neck, Stretchable Fabric, Side Slit)",
        "category": "fashion",
        "subcategory": "womens-clothing",
        "brand": "Tokyo Talkies",
        "model": "Ribbed Knit Bodycon",
        "variant": "Medium (M) / Classic Black",
        "variants": [
            {"dimension": "size", "value": "S", "price_delta": 0.0, "is_default": False},
            {"dimension": "size", "value": "M", "price_delta": 0.0, "is_default": True},
            {"dimension": "size", "value": "L", "price_delta": 0.0, "is_default": False}
        ],
        "sku": "TT-DRS-BDC-BLK-M",
        "gtin_upc_ean": "0890610192837",
        "product_description": "Affordable on-trend bodycon dress by Tokyo Talkies under ₹1,000. Crafted in high-stretch ribbed knit fabric with a flattering turtleneck, sleeveless design, and 8-inch side leg slit for easy mobility. Pairs perfectly with sneakers or heels.",
        "images": [
            "https://images.unsplash.com/photo-1515372039744-b8f02a3ae446?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "fabric": "92% Polyester, 8% Elastane High-Stretch Rib",
            "fit": "Bodycon Figure-Hugging Slim Fit",
            "length": "Midi Length with Side Slit",
            "pattern": "Solid Ribbed Texture",
            "neck": "High Mock Neck",
            "sleeve_length": "Sleeveless",
            "occasion": "Casual Streetwear / Party / Weekend",
            "wash_care": "Hand Wash Cold",
            "warranty_months": 1
        },
        "current_price": 899.0,
        "mrp": 1999.0,
        "discount_percentage": 55.0,
        "currency": "INR",
        "rating": 4.3,
        "review_count": 14300,
        "seller": "Flipkart Retail Verified",
        "seller_rating": 4.5,
        "availability": "In Stock",
        "delivery_info": "Free Standard 2-Day Delivery",
        "warranty": "Authentic Brand Quality Guarantee",
        "return_policy": "10-day replacement and size exchange",
        "source_website": "Flipkart",
        "product_url": "https://www.flipkart.com/tokyo-talkies-women-bodycon-black-dress/p/itm7a8b9c1d2e3f4",
        "affiliate_url": "https://www.flipkart.com/tokyo-talkies-women-bodycon-black-dress/p/itm7a8b9c1d2e3f4?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Flipkart", "seller_name": "RetailNet Verified", "seller_rating": 4.5, "price": 899.0, "original_price": 1999.0, "discount_percent": 55.0, "availability": "In Stock", "delivery_info": "Free Delivery", "product_url": "https://www.flipkart.com/tokyo-talkies-women-bodycon-black-dress/p/itm7a8b9c1d2e3f4", "condition": "Brand New"},
            {"source": "Myntra", "seller_name": "Tokyo Talkies Direct", "seller_rating": 4.6, "price": 949.0, "original_price": 1999.0, "discount_percent": 52.5, "availability": "In Stock", "delivery_info": "Express Delivery", "product_url": "https://www.myntra.com/dresses/tokyo-talkies/bodycon/buy", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "FASH-DRS-BIBA-ANARKALIMAXI",
        "product_name": "Biba Women Floral Printed Pure Cotton Anarkali Maxi Ethnic Dress (Round Neck, Metallic Foil Accents, Gota Patti Border)",
        "category": "fashion",
        "subcategory": "womens-clothing",
        "brand": "Biba",
        "model": "Anarkali Ethnic Maxi",
        "variant": "Large (L) / Royal Indigo Blue",
        "variants": [
            {"dimension": "size", "value": "M", "price_delta": 0.0, "is_default": False},
            {"dimension": "size", "value": "L", "price_delta": 0.0, "is_default": True},
            {"dimension": "size", "value": "XL", "price_delta": 0.0, "is_default": False}
        ],
        "sku": "BIB-MAX-ANK-BLU-L",
        "gtin_upc_ean": "0890321489201",
        "product_description": "Stunning Indian ethnic anarkali maxi dress from Biba. Showcasing traditional hand block inspired floral prints, intricate gota patti border along the flared hemline, dori ties with handcrafted tassels, and premium pure cotton lining.",
        "images": [
            "https://images.unsplash.com/photo-1617627143750-d86bc21e42bb?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "fabric": "100% Premium Cambric Cotton",
            "fit": "Flared Anarkali Silhouette",
            "length": "Maxi / Ankle Length",
            "pattern": "Jaipur Floral Print with Metallic Accents",
            "neck": "Round Neck with Front Keyhole & Dori",
            "sleeve_length": "Three-Quarter Sleeves with Gota Trims",
            "occasion": "Festive / Celebration / Family Functions",
            "wash_care": "Dry Clean Recommended",
            "warranty_months": 1
        },
        "current_price": 1999.0,
        "mrp": 3999.0,
        "discount_percentage": 50.0,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 9100,
        "seller": "Biba Fashion Official Direct",
        "seller_rating": 4.8,
        "availability": "In Stock",
        "delivery_info": "Free Express Priority Shipping",
        "warranty": "100% Official Authentic Biba Merchandise Guarantee",
        "return_policy": "15-day return or size exchange",
        "source_website": "Myntra",
        "product_url": "https://www.biba.in/indigo-cotton-anarkali-dress/p/10293847",
        "affiliate_url": "https://www.biba.in/indigo-cotton-anarkali-dress/p/10293847?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Myntra", "seller_name": "Biba India Official", "seller_rating": 4.8, "price": 1999.0, "original_price": 3999.0, "discount_percent": 50.0, "availability": "In Stock", "delivery_info": "2-Day Delivery", "product_url": "https://www.biba.in/indigo-cotton-anarkali-dress/p/10293847", "condition": "Brand New with Original Tags"},
            {"source": "Amazon India", "seller_name": "Appario Retail Pvt Ltd", "seller_rating": 4.7, "price": 2099.0, "original_price": 3999.0, "discount_percent": 47.5, "availability": "In Stock", "delivery_info": "Free Prime Delivery", "product_url": "https://www.amazon.in/dp/B0DGBIBA01", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "FASH-DRS-AND-WRAPSHIRT",
        "product_name": "AND Women Printed Wrap Knee-Length Shirt Dress with Belt (Lapel Collar, Full Sleeves, Button Cuffs, Office & Smart Casual)",
        "category": "fashion",
        "subcategory": "womens-clothing",
        "brand": "AND",
        "model": "Wrap Shirt Dress",
        "variant": "Medium (M) / Dusty Rose Geometric",
        "variants": [],
        "sku": "AND-WRP-SHT-DRS-M",
        "gtin_upc_ean": "0890432194821",
        "product_description": "Sophisticated contemporary shirt dress by House of Anita Dongre (AND). Features a wrap-around front with an adjustable matching fabric belt, spread shirt collar, long sleeves with button cuffs, and lightweight breathable viscose fabric.",
        "images": [
            "https://images.unsplash.com/photo-1502716119720-b23a93e5fe1b?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "fabric": "100% Breathable Viscose Rayon",
            "fit": "Tailored Wrap Regular Fit",
            "length": "Knee Length",
            "pattern": "Subtle Geometric Micro-Print",
            "neck": "Lapel Shirt Collar with V-Wrap Opening",
            "sleeve_length": "Full Sleeves with Button Cuffs",
            "occasion": "Workplace / Formal Conferences / Smart Casual",
            "wash_care": "Machine Wash Cold Gentle",
            "warranty_months": 1
        },
        "current_price": 1799.0,
        "mrp": 3499.0,
        "discount_percentage": 48.6,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 5400,
        "seller": "AND India Official Store",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Standard Express Delivery",
        "warranty": "Anita Dongre Design Quality Certification",
        "return_policy": "14-day hassle-free exchange & refund",
        "source_website": "Myntra",
        "product_url": "https://www.andindia.com/dusty-rose-wrap-dress/p/98472615",
        "affiliate_url": "https://www.andindia.com/dusty-rose-wrap-dress/p/98472615?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Myntra", "seller_name": "AND Official Store", "seller_rating": 4.7, "price": 1799.0, "original_price": 3499.0, "discount_percent": 48.6, "availability": "In Stock", "delivery_info": "Express Delivery", "product_url": "https://www.andindia.com/dusty-rose-wrap-dress/p/98472615", "condition": "Brand New with Tags"},
            {"source": "Tata CLiQ", "seller_name": "Tata CLiQ Luxury Verified", "seller_rating": 4.6, "price": 1849.0, "original_price": 3499.0, "discount_percent": 47.2, "availability": "In Stock", "delivery_info": "3-Day Delivery", "product_url": "https://www.tatacliq.com/and-wrap-dress/p/mp00000001", "condition": "Brand New"}
        ]
    },
    {
        "product_id": "FASH-DRS-ZARA-SATINSLIP",
        "product_name": "Zara Style Elegant Cowl Neck Satin Slip Maxi Dress (Adjustable Spaghetti Straps, Silky Finish, Side Invisible Zip)",
        "category": "fashion",
        "subcategory": "womens-clothing",
        "brand": "Zara Style",
        "model": "Cowl Satin Slip Maxi",
        "variant": "Small (S) / Champagne Gold",
        "variants": [],
        "sku": "ZR-SLP-SAT-GLD-S",
        "gtin_upc_ean": "0843452109823",
        "product_description": "Effortlessly glamorous satin slip maxi dress. Cut on the bias to gently skim your curves with a cascading cowl neckline, slim adjustable cross-back spaghetti straps, and lustrous liquid-silk finish. The ultimate showstopper for evening celebrations.",
        "images": [
            "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [],
        "specifications": {
            "fabric": "Heavyweight Poly Satin Silk Finish",
            "fit": "Bias Cut Body-Draping Silhouette",
            "length": "Maxi / Floor Length",
            "pattern": "Glossy Solid Silky Finish",
            "neck": "Draped Cowl Neckline",
            "sleeve_length": "Sleeveless with Spaghetti Straps",
            "occasion": "Cocktail / Evening Party / Gala / Reception",
            "wash_care": "Dry Clean or Gentle Cold Hand Wash",
            "warranty_months": 1
        },
        "current_price": 2499.0,
        "mrp": 4590.0,
        "discount_percentage": 45.6,
        "currency": "INR",
        "rating": 4.7,
        "review_count": 7800,
        "seller": "Authorized European Fashion Partner",
        "seller_rating": 4.7,
        "availability": "In Stock",
        "delivery_info": "Free Air Express Priority Delivery",
        "warranty": "Verified Quality Silk Finish Guarantee",
        "return_policy": "7-day return on unworn merchandise",
        "source_website": "Myntra",
        "product_url": "https://www.myntra.com/dresses/zara-style-satin-slip-dress/28194726/buy",
        "affiliate_url": "https://www.myntra.com/dresses/zara-style/28194726?affid=shopai",
        "last_updated": "2026-11-18T00:00:00Z",
        "sellers": [
            {"source": "Myntra", "seller_name": "Myntra Premier Fashion", "seller_rating": 4.7, "price": 2499.0, "original_price": 4590.0, "discount_percent": 45.6, "availability": "In Stock", "delivery_info": "Air Express Delivery", "product_url": "https://www.myntra.com/dresses/zara-style-satin-slip-dress/28194726/buy", "condition": "Brand New Sealed"}
        ]
    },
    {
        "product_id": "ELEC-MOB-ONEPLUS-NORDCE4",
        "product_name": "OnePlus Nord CE 4 5G (8GB RAM, 128GB Storage, Snapdragon 7 Gen 3, 5500mAh Battery, 100W SuperVOOC, Celadon Marble)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "OnePlus",
        "model": "Nord CE 4 5G",
        "variant": "8GB RAM / 128GB Storage / Celadon Marble",
        "sku": "1P-NORDCE4-128G",
        "gtin_upc_ean": "6921815623012",
        "product_description": "Best mid-range smartphone featuring Qualcomm Snapdragon 7 Gen 3 octa-core chipset, 6.7-inch 120Hz Fluid AMOLED display with HDR10+, 50MP Sony LYT-600 OIS primary camera with 4K recording, massive 5500mAh battery with 100W SuperVOOC fast charging, and OxygenOS 14 based on Android 14.",
        "images": [
                "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [
                "https://www.youtube.com/watch?v=nordce4_demo"
        ],
        "specifications": {
                "ram_gb": 8,
                "storage_gb": 128,
                "processor": "Qualcomm Snapdragon 7 Gen 3 (4nm, up to 2.63GHz)",
                "display": "6.7 inch FHD+ 120Hz Fluid AMOLED (2412x1080), 2160Hz PWM",
                "camera": "50MP Sony LYT-600 OIS + 8MP Ultra-Wide | 16MP Front",
                "battery_mah": 5500,
                "charging_watts": 100,
                "os": "OxygenOS 14 (Android 14)",
                "5g_bands": "13 Bands (SA/NSA)",
                "ip_rating": "IP54 Splash Proof",
                "weight_grams": 186,
                "warranty_months": 12
        },
        "variants": [
                {
                        "name": "8GB RAM / 128GB Storage",
                        "price": 24999.0,
                        "mrp": 26999.0,
                        "sku": "1P-CE4-128G"
                },
                {
                        "name": "8GB RAM / 256GB Storage",
                        "price": 26999.0,
                        "mrp": 28999.0,
                        "sku": "1P-CE4-256G"
                }
        ],
        "sellers": [
                {
                        "source": "Amazon India",
                        "seller_name": "Appario Retail Pvt Ltd",
                        "seller_rating": 4.6,
                        "price": 24999.0,
                        "original_price": 26999.0,
                        "discount_percent": 7.4,
                        "availability": "In Stock",
                        "delivery_info": "Free Prime One-Day Delivery",
                        "product_url": "https://www.amazon.in/dp/B0CX24XVXZ",
                        "condition": "Brand New with Official 1-Year Warranty"
                },
                {
                        "source": "OnePlus Official Store",
                        "seller_name": "OnePlus India Direct",
                        "seller_rating": 4.8,
                        "price": 24999.0,
                        "original_price": 26999.0,
                        "discount_percent": 7.4,
                        "availability": "In Stock",
                        "delivery_info": "Free Standard Express Shipping",
                        "product_url": "https://www.oneplus.in/nord-ce-4-5g",
                        "condition": "Brand New"
                }
        ],
        "current_price": 24999.0,
        "mrp": 26999.0,
        "discount_percentage": 7.4,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 8420,
        "availability": "In Stock",
        "shipping": "Free Standard Delivery",
        "delivery_info": "Free Prime One-Day Delivery",
        "warranty": "1 Year Manufacturer Warranty for Device and 6 Months for In-Box Accessories",
        "return_policy": "7 Days Service Center Replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0CX24XVXZ",
        "affiliate_url": "https://www.amazon.in/dp/B0CX24XVXZ?tag=shopaipro-21",
        "price_history": [
                {
                        "date": "2026-02-01",
                        "price": 26999.0
                },
                {
                        "date": "2026-02-15",
                        "price": 25999.0
                },
                {
                        "date": "2026-03-01",
                        "price": 24999.0
                }
        ],
        "review_sentiment": {
                "sentiment_positive_pct": 91,
                "sentiment_neutral_pct": 6,
                "sentiment_negative_pct": 3,
                "positive_themes": [
                        "Blazing fast 100W charging",
                        "Smooth 120Hz display",
                        "Snappy Snapdragon 7 Gen 3 performance",
                        "Excellent battery endurance"
                ],
                "negative_themes": [
                        "No stereo speaker bass",
                        "Plastic frame build"
                ],
                "common_complaints": [
                        "Plastic back picks up smudges easily without case"
                ],
                "important_warnings": [
                        "Use bundled 100W adapter for advertised charging speeds"
                ]
        }
},
    {
        "product_id": "ELEC-MOB-SAMS-M35",
        "product_name": "Samsung Galaxy M35 5G (6GB RAM, 128GB Storage, 120Hz sAMOLED, Exynos 1380, 6000mAh Battery, 50MP OIS Camera, Moonlight Blue)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "Samsung",
        "model": "Galaxy M35 5G",
        "variant": "6GB RAM / 128GB Storage / Moonlight Blue",
        "sku": "SM-M356B-128G",
        "gtin_upc_ean": "8806095623015",
        "product_description": "Best battery life smartphone featuring a monster 6000mAh battery, 6.6-inch Super AMOLED 120Hz FHD+ Infinity-O display with Gorilla Glass Victus+, 50MP OIS triple camera with 4K video, Exynos 1380 5nm octa-core processor with vapor cooling chamber, and Knox Security with 4 OS upgrades guaranteed.",
        "images": [
                "https://images.unsplash.com/photo-1610945415295-d9bbf067e59c?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [
                "https://www.youtube.com/watch?v=m35_demo"
        ],
        "specifications": {
                "ram_gb": 6,
                "storage_gb": 128,
                "processor": "Exynos 1380 Octa-Core (5nm, up to 2.4GHz) with Vapor Cooling",
                "display": "6.6 inch Super AMOLED FHD+ 120Hz (1000 nits HBM), Gorilla Glass Victus+",
                "camera": "50MP Main OIS + 8MP Ultra-Wide + 2MP Macro | 13MP Front",
                "battery_mah": 6000,
                "charging_watts": 25,
                "os": "One UI 6.1 (Android 14) with 4 OS Upgrades",
                "5g_bands": "12 Bands Supported",
                "weight_grams": 222,
                "warranty_months": 12
        },
        "variants": [
                {
                        "name": "6GB RAM / 128GB Storage",
                        "price": 19999.0,
                        "mrp": 24499.0,
                        "sku": "SM-M356B-128G"
                },
                {
                        "name": "8GB RAM / 256GB Storage",
                        "price": 21999.0,
                        "mrp": 26499.0,
                        "sku": "SM-M356B-256G"
                }
        ],
        "sellers": [
                {
                        "source": "Amazon India",
                        "seller_name": "STPL Exclusive Online",
                        "seller_rating": 4.5,
                        "price": 19999.0,
                        "original_price": 24499.0,
                        "discount_percent": 18.4,
                        "availability": "In Stock",
                        "delivery_info": "Free Prime One-Day Delivery",
                        "product_url": "https://www.amazon.in/dp/B0D7D7R3P1",
                        "condition": "Brand New with Official 1-Year Warranty"
                },
                {
                        "source": "Samsung Official Store",
                        "seller_name": "Samsung India Electronics",
                        "seller_rating": 4.8,
                        "price": 20499.0,
                        "original_price": 24499.0,
                        "discount_percent": 16.3,
                        "availability": "In Stock",
                        "delivery_info": "Free Express Delivery",
                        "product_url": "https://www.samsung.com/in/smartphones/galaxy-m/galaxy-m35-5g-moonlight-blue-128gb-sm-m356bdbdins/",
                        "condition": "Brand New"
                }
        ],
        "current_price": 19999.0,
        "mrp": 24499.0,
        "discount_percentage": 18.4,
        "currency": "INR",
        "rating": 4.4,
        "review_count": 12450,
        "availability": "In Stock",
        "shipping": "Free Standard Delivery",
        "delivery_info": "Free Prime Delivery",
        "warranty": "1 Year Manufacturer Warranty for Phone and 6 Months for In-Box Items",
        "return_policy": "7 Days Replacement Policy",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0D7D7R3P1",
        "affiliate_url": "https://www.amazon.in/dp/B0D7D7R3P1?tag=shopaipro-21",
        "price_history": [
                {
                        "date": "2026-02-01",
                        "price": 22499.0
                },
                {
                        "date": "2026-02-15",
                        "price": 20999.0
                },
                {
                        "date": "2026-03-01",
                        "price": 19999.0
                }
        ],
        "review_sentiment": {
                "sentiment_positive_pct": 90,
                "sentiment_neutral_pct": 7,
                "sentiment_negative_pct": 3,
                "positive_themes": [
                        "Outstanding 2-day 6000mAh battery life",
                        "Vibrant 120Hz sAMOLED screen",
                        "Knox security and clean One UI",
                        "OIS camera clarity in daylight"
                ],
                "negative_themes": [
                        "Heavier than average phone (222g)",
                        "No charger in box"
                ],
                "common_complaints": [
                        "25W charging takes about 85 mins for 6000mAh capacity"
                ],
                "important_warnings": [
                        "Purchase a genuine 25W Type-C adapter separately"
                ]
        }
},
    {
        "product_id": "ELEC-MOB-IQOO-Z9",
        "product_name": "iQOO Z9 5G (8GB RAM, 128GB Storage, MediaTek Dimensity 7200 4nm, Sony IMX882 OIS Camera, 120Hz AMOLED, Brushed Green)",
        "category": "electronics",
        "subcategory": "mobile-phones",
        "brand": "iQOO",
        "model": "Z9 5G",
        "variant": "8GB RAM / 128GB Storage / Brushed Green",
        "sku": "IQ-Z9-128G",
        "gtin_upc_ean": "6921815689104",
        "product_description": "Segment's fastest gaming performance phone equipped with MediaTek Dimensity 7200 4nm processor (AnTuTu score 730K+), 6.67-inch 120Hz Ultra Vision AMOLED display (1800 nits peak brightness), 50MP Sony IMX882 OIS primary camera with 4K recording, 5000mAh battery with 44W FlashCharge, and dual stereo speakers.",
        "images": [
                "https://images.unsplash.com/photo-1511707171634-5f897ff02560?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [
                "https://www.youtube.com/watch?v=iqooz9_demo"
        ],
        "specifications": {
                "ram_gb": 8,
                "storage_gb": 128,
                "processor": "MediaTek Dimensity 7200 5G (4nm, up to 2.8GHz, AnTuTu 734K)",
                "display": "6.67 inch FHD+ 120Hz AMOLED (1800 nits peak, DT-Star2 Glass)",
                "camera": "50MP Sony IMX882 OIS + 2MP Bokeh | 16MP Front",
                "battery_mah": 5000,
                "charging_watts": 44,
                "os": "Funtouch OS 14 (Android 14)",
                "audio": "Dual Stereo Speakers with Hi-Res Audio",
                "weight_grams": 188,
                "warranty_months": 12
        },
        "variants": [
                {
                        "name": "8GB RAM / 128GB Storage",
                        "price": 17999.0,
                        "mrp": 24999.0,
                        "sku": "IQ-Z9-128G"
                },
                {
                        "name": "8GB RAM / 256GB Storage",
                        "price": 19999.0,
                        "mrp": 26999.0,
                        "sku": "IQ-Z9-256G"
                }
        ],
        "sellers": [
                {
                        "source": "Amazon India",
                        "seller_name": "Appario Retail Pvt Ltd",
                        "seller_rating": 4.6,
                        "price": 17999.0,
                        "original_price": 24999.0,
                        "discount_percent": 28.0,
                        "availability": "In Stock",
                        "delivery_info": "Free Prime Delivery",
                        "product_url": "https://www.amazon.in/dp/B0CX1ZZ1XY",
                        "condition": "Brand New with Manufacturer Warranty"
                }
        ],
        "current_price": 17999.0,
        "mrp": 24999.0,
        "discount_percentage": 28.0,
        "currency": "INR",
        "rating": 4.4,
        "review_count": 9180,
        "availability": "In Stock",
        "shipping": "Free Standard Delivery",
        "delivery_info": "Free Prime Delivery",
        "warranty": "1 Year Official Warranty",
        "return_policy": "7 Days Replacement",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0CX1ZZ1XY",
        "affiliate_url": "https://www.amazon.in/dp/B0CX1ZZ1XY?tag=shopaipro-21",
        "price_history": [
                {
                        "date": "2026-02-01",
                        "price": 19999.0
                },
                {
                        "date": "2026-02-15",
                        "price": 18999.0
                },
                {
                        "date": "2026-03-01",
                        "price": 17999.0
                }
        ],
        "review_sentiment": {
                "sentiment_positive_pct": 92,
                "sentiment_neutral_pct": 6,
                "sentiment_negative_pct": 2,
                "positive_themes": [
                        "Unrivaled gaming FPS in budget",
                        "Sony IMX882 OIS crisp photos",
                        "Very bright outdoor AMOLED",
                        "Fast 44W charger included in box"
                ],
                "negative_themes": [
                        "No ultra-wide camera lens",
                        "Funtouch OS has preinstalled apps"
                ],
                "common_complaints": [
                        "Secondary camera is only a 2MP depth sensor"
                ],
                "important_warnings": [
                        "Uninstall recommended bloatware apps on first setup"
                ]
        }
},
    {
        "product_id": "FASH-FOOT-NIKE-DOWNSHIFTER",
        "product_name": "Nike Downshifter 12 Men's Road Running Shoes (Breathable Mesh Upper, Cushioned Midsole, Durable Rubber Traction, Black/White)",
        "category": "fashion",
        "subcategory": "footwear",
        "brand": "Nike",
        "model": "Downshifter 12",
        "variant": "Black / White / UK 8-11",
        "sku": "DD9293-001",
        "gtin_upc_ean": "0195866123456",
        "product_description": "Top-rated lightweight road running shoe crafted with at least 20% recycled material by weight. Features super-soft EVA foam cushioning through the midsole for a smooth, stable ride on tarmac and treadmills. Lightweight engineered mesh across the upper delivers cool airflow, while the midfoot fit band works with laces to hold the foot secure.",
        "images": [
                "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [
                "https://www.youtube.com/watch?v=downshifter12_demo"
        ],
        "specifications": {
                "cushioning": "Responsive EVA Foam Midsole with Midfoot Fit Band",
                "upper_material": "Lightweight Engineered Breathable Mesh (20% Recycled)",
                "outsole": "Full-Length Solid Rubber with Flex Grooves for Road Grip",
                "arch_support": "Neutral Pronation Support",
                "closure": "Lace-Up with Midfoot Lockdown",
                "weight_grams": 285,
                "warranty_months": 3
        },
        "variants": [
                {
                        "name": "UK 8 (EU 42.5)",
                        "price": 3495.0,
                        "mrp": 3995.0,
                        "sku": "DD9293-001-UK8"
                },
                {
                        "name": "UK 9 (EU 44)",
                        "price": 3495.0,
                        "mrp": 3995.0,
                        "sku": "DD9293-001-UK9"
                },
                {
                        "name": "UK 10 (EU 45)",
                        "price": 3495.0,
                        "mrp": 3995.0,
                        "sku": "DD9293-001-UK10"
                }
        ],
        "sellers": [
                {
                        "source": "Myntra",
                        "seller_name": "Nike India Official Retail Partner",
                        "seller_rating": 4.6,
                        "price": 3495.0,
                        "original_price": 3995.0,
                        "discount_percent": 12.5,
                        "availability": "In Stock",
                        "delivery_info": "Free 2-Day Delivery",
                        "product_url": "https://www.myntra.com/running-shoes/nike/nike-downshifter-12-running-shoes/19827364/buy",
                        "condition": "Brand New in Original Box"
                },
                {
                        "source": "Amazon India",
                        "seller_name": "RetailNet Verified",
                        "seller_rating": 4.5,
                        "price": 3595.0,
                        "original_price": 3995.0,
                        "discount_percent": 10.0,
                        "availability": "In Stock",
                        "delivery_info": "Free Standard Delivery",
                        "product_url": "https://www.amazon.in/dp/B09V3G5B2B",
                        "condition": "Brand New"
                }
        ],
        "current_price": 3495.0,
        "mrp": 3995.0,
        "discount_percentage": 12.5,
        "currency": "INR",
        "rating": 4.4,
        "review_count": 6840,
        "availability": "In Stock",
        "shipping": "Free Standard Delivery",
        "delivery_info": "Free 2-Day Delivery",
        "warranty": "3 Months Manufacturer Warranty against manufacturing defects",
        "return_policy": "14 Days Free Return & Size Exchange",
        "source_website": "Myntra",
        "product_url": "https://www.myntra.com/running-shoes/nike/nike-downshifter-12-running-shoes/19827364/buy",
        "affiliate_url": "https://www.myntra.com/running-shoes/nike/nike-downshifter-12-running-shoes/19827364/buy?utm_source=shopaipro",
        "price_history": [
                {
                        "date": "2026-02-01",
                        "price": 3995.0
                },
                {
                        "date": "2026-02-15",
                        "price": 3695.0
                },
                {
                        "date": "2026-03-01",
                        "price": 3495.0
                }
        ],
        "review_sentiment": {
                "sentiment_positive_pct": 91,
                "sentiment_neutral_pct": 6,
                "sentiment_negative_pct": 3,
                "positive_themes": [
                        "Very light on the feet for daily 5K runs",
                        "Great arch support",
                        "Breathable mesh prevents sweating",
                        "Durable sole traction on wet roads"
                ],
                "negative_themes": [
                        "Slightly narrow fit for wide feet"
                ],
                "common_complaints": [
                        "Order half a size up if you have broad feet"
                ],
                "important_warnings": [
                        "Check UK size chart carefully before checkout"
                ]
        }
},
    {
        "product_id": "FASH-FOOT-PUMA-SOFTRIDE",
        "product_name": "Puma Softride Enzo Evo Men's Running Shoes (SOFTRIDE Midsole Cushioning, SoftFoam+ Sockliner, Molded TPU Cage, High Risk Red/Black)",
        "category": "fashion",
        "subcategory": "footwear",
        "brand": "Puma",
        "model": "Softride Enzo Evo",
        "variant": "Red / Black / UK 7-11",
        "sku": "377048-03",
        "gtin_upc_ean": "4065449765432",
        "product_description": "Bold progressive running shoe pairing Puma's SOFTRIDE EVA foam technology with a premium SoftFoam+ comfort sockliner for plush all-day step-in cushioning. Features a distinctive clamshell construction with TPU midfoot cage and webbing lockdown to ensure foot stability during high-intensity road running and cardio gym sessions.",
        "images": [
                "https://images.unsplash.com/photo-1608231387042-66d1773070a5?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [
                "https://www.youtube.com/watch?v=softride_demo"
        ],
        "specifications": {
                "cushioning": "SOFTRIDE Foam + SoftFoam+ Step-In Comfort Sockliner",
                "upper_material": "Breathable Air Mesh with Molded Synthetic TPU Cage",
                "outsole": "Zoned Performance Rubber Outsole with Enhanced Traction Pods",
                "arch_support": "Neutral Road & Gym Stability",
                "closure": "Lace-Up with Integrated TPU Webbing",
                "weight_grams": 298,
                "warranty_months": 3
        },
        "variants": [
                {
                        "name": "UK 8 (EU 42)",
                        "price": 3199.0,
                        "mrp": 5499.0,
                        "sku": "377048-03-UK8"
                },
                {
                        "name": "UK 9 (EU 43)",
                        "price": 3199.0,
                        "mrp": 5499.0,
                        "sku": "377048-03-UK9"
                }
        ],
        "sellers": [
                {
                        "source": "Myntra",
                        "seller_name": "Puma Official Store Partner",
                        "seller_rating": 4.5,
                        "price": 3199.0,
                        "original_price": 5499.0,
                        "discount_percent": 41.8,
                        "availability": "In Stock",
                        "delivery_info": "Free 2-Day Delivery",
                        "product_url": "https://www.myntra.com/running-shoes/puma/puma-softride-enzo-evo/21839402/buy",
                        "condition": "Brand New"
                },
                {
                        "source": "Amazon India",
                        "seller_name": "Appario Retail Pvt Ltd",
                        "seller_rating": 4.6,
                        "price": 3299.0,
                        "original_price": 5499.0,
                        "discount_percent": 40.0,
                        "availability": "In Stock",
                        "delivery_info": "Free Prime Delivery",
                        "product_url": "https://www.amazon.in/dp/B0B7F8XYZ1",
                        "condition": "Brand New"
                }
        ],
        "current_price": 3199.0,
        "mrp": 5499.0,
        "discount_percentage": 41.8,
        "currency": "INR",
        "rating": 4.5,
        "review_count": 4920,
        "availability": "In Stock",
        "shipping": "Free Standard Delivery",
        "delivery_info": "Free 2-Day Delivery",
        "warranty": "3 Months Manufacturer Warranty",
        "return_policy": "14 Days Free Return & Exchange",
        "source_website": "Myntra",
        "product_url": "https://www.myntra.com/running-shoes/puma/puma-softride-enzo-evo/21839402/buy",
        "affiliate_url": "https://www.myntra.com/running-shoes/puma/puma-softride-enzo-evo/21839402/buy?utm_source=shopaipro",
        "price_history": [
                {
                        "date": "2026-02-01",
                        "price": 3999.0
                },
                {
                        "date": "2026-02-15",
                        "price": 3499.0
                },
                {
                        "date": "2026-03-01",
                        "price": 3199.0
                }
        ],
        "review_sentiment": {
                "sentiment_positive_pct": 92,
                "sentiment_neutral_pct": 5,
                "sentiment_negative_pct": 3,
                "positive_themes": [
                        "Incredible heel cushioning for road running",
                        "Striking red and black styling",
                        "TPU cage locks heel securely",
                        "Very comfortable for whole-day walking"
                ],
                "negative_themes": [
                        "Slightly heavier than minimalist shoes"
                ],
                "common_complaints": [
                        "Laces are somewhat long"
                ],
                "important_warnings": [
                        "Spot clean only; do not machine wash"
                ]
        }
},
    {
        "product_id": "FASH-FOOT-ASICS-CONTEND8",
        "product_name": "Asics Gel-Contend 8 Men's Running Shoes (Rearfoot GEL Technology, AmpliFoam Midsole, OrthoLite Sockliner, Carrier Grey/Electric Blue)",
        "category": "fashion",
        "subcategory": "footwear",
        "brand": "Asics",
        "model": "Gel-Contend 8",
        "variant": "Carrier Grey / Electric Blue / UK 8-11",
        "sku": "1011B492-020",
        "gtin_upc_ean": "4550456123456",
        "product_description": "Orthopedically backed running shoe engineered with signature Rearfoot GEL cushioning technology that absorbs harsh ground shock upon heel strike. Powered by an AmpliFoam midsole and an OrthoLite moisture-wicking sockliner, providing unmatched endurance comfort for 5K to 10K road training and marathon preparation.",
        "images": [
                "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [
                "https://www.youtube.com/watch?v=gelcontend8_demo"
        ],
        "specifications": {
                "cushioning": "Rearfoot GEL Cushioning System + AmpliFoam Midsole",
                "upper_material": "Jacquard Engineered Mesh with Synthetic Stitching Overlays",
                "outsole": "Solid High-Abrasion Rubber with Forefoot Flex Grooves",
                "arch_support": "Neutral to Underpronation Support",
                "closure": "Lace-Up",
                "weight_grams": 290,
                "warranty_months": 3
        },
        "variants": [
                {
                        "name": "UK 8 (EU 42.5)",
                        "price": 4199.0,
                        "mrp": 4999.0,
                        "sku": "1011B492-020-UK8"
                },
                {
                        "name": "UK 9 (EU 44)",
                        "price": 4199.0,
                        "mrp": 4999.0,
                        "sku": "1011B492-020-UK9"
                }
        ],
        "sellers": [
                {
                        "source": "Amazon India",
                        "seller_name": "Asics Authorized Store",
                        "seller_rating": 4.6,
                        "price": 4199.0,
                        "original_price": 4999.0,
                        "discount_percent": 16.0,
                        "availability": "In Stock",
                        "delivery_info": "Free Prime Delivery",
                        "product_url": "https://www.amazon.in/dp/B0BD4WXYZ9",
                        "condition": "Brand New with Official Asics Warranty"
                }
        ],
        "current_price": 4199.0,
        "mrp": 4999.0,
        "discount_percentage": 16.0,
        "currency": "INR",
        "rating": 4.6,
        "review_count": 5310,
        "availability": "In Stock",
        "shipping": "Free Standard Delivery",
        "delivery_info": "Free Prime Delivery",
        "warranty": "3 Months Manufacturer Warranty",
        "return_policy": "10 Days Return Policy",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0BD4WXYZ9",
        "affiliate_url": "https://www.amazon.in/dp/B0BD4WXYZ9?tag=shopaipro-21",
        "price_history": [
                {
                        "date": "2026-02-01",
                        "price": 4699.0
                },
                {
                        "date": "2026-02-15",
                        "price": 4399.0
                },
                {
                        "date": "2026-03-01",
                        "price": 4199.0
                }
        ],
        "review_sentiment": {
                "sentiment_positive_pct": 94,
                "sentiment_neutral_pct": 4,
                "sentiment_negative_pct": 2,
                "positive_themes": [
                        "Best shock absorption GEL for knee pain relief",
                        "Solid foot stability",
                        "Durable upper mesh",
                        "Superb road grip"
                ],
                "negative_themes": [
                        "Firmer feel initially before break-in"
                ],
                "common_complaints": [
                        "Takes 1-2 runs to break in the AmpliFoam midsole"
                ],
                "important_warnings": [
                        "Designed specifically for neutral road running"
                ]
        }
},
    {
        "product_id": "FASH-FOOT-ADIDAS-RUNFALCON",
        "product_name": "Adidas Runfalcon 3.0 Men's Running Shoes (Cloudfoam Midsole Cushioning, Textile Upper, Adiwear Rubber Outsole, Core Black/Cloud White)",
        "category": "fashion",
        "subcategory": "footwear",
        "brand": "Adidas",
        "model": "Runfalcon 3.0",
        "variant": "Black / White / UK 7-11",
        "sku": "HP7544",
        "gtin_upc_ean": "4066748123456",
        "product_description": "Versatile all-around road running shoe with Cloudfoam midsole cushioning delivering instantaneous step-in comfort and energy return. Built with a minimum of 50% recycled textile upper for eco-conscious performance and an Adiwear rubber outsole that resists premature wear on city pavements.",
        "images": [
                "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?w=600&auto=format&fit=crop&q=80"
        ],
        "videos": [
                "https://www.youtube.com/watch?v=runfalcon3_demo"
        ],
        "specifications": {
                "cushioning": "Cloudfoam Cushioned Midsole with Textile Sockliner",
                "upper_material": "Breathable Recycled Textile Upper (50% Recycled Content)",
                "outsole": "Non-Marking Durable Adiwear Rubber Outsole",
                "arch_support": "Neutral Road Support",
                "closure": "Lace-Up",
                "weight_grams": 270,
                "warranty_months": 3
        },
        "variants": [
                {
                        "name": "UK 8 (EU 42)",
                        "price": 2799.0,
                        "mrp": 4599.0,
                        "sku": "HP7544-UK8"
                },
                {
                        "name": "UK 9 (EU 43.5)",
                        "price": 2799.0,
                        "mrp": 4599.0,
                        "sku": "HP7544-UK9"
                }
        ],
        "sellers": [
                {
                        "source": "Amazon India",
                        "seller_name": "Adidas India Marketing Pvt Ltd",
                        "seller_rating": 4.6,
                        "price": 2799.0,
                        "original_price": 4599.0,
                        "discount_percent": 39.1,
                        "availability": "In Stock",
                        "delivery_info": "Free Prime Delivery",
                        "product_url": "https://www.amazon.in/dp/B0BLX9YZ12",
                        "condition": "Brand New with Official Adidas Guarantee"
                },
                {
                        "source": "Myntra",
                        "seller_name": "Adidas Verified Retail Partner",
                        "seller_rating": 4.5,
                        "price": 2899.0,
                        "original_price": 4599.0,
                        "discount_percent": 37.0,
                        "availability": "In Stock",
                        "delivery_info": "Free 2-Day Delivery",
                        "product_url": "https://www.myntra.com/running-shoes/adidas/adidas-runfalcon-3/22918274/buy",
                        "condition": "Brand New"
                }
        ],
        "current_price": 2799.0,
        "mrp": 4599.0,
        "discount_percentage": 39.1,
        "currency": "INR",
        "rating": 4.3,
        "review_count": 8120,
        "availability": "In Stock",
        "shipping": "Free Standard Delivery",
        "delivery_info": "Free Prime Delivery",
        "warranty": "3 Months Manufacturer Warranty",
        "return_policy": "14 Days Free Return & Exchange",
        "source_website": "Amazon India",
        "product_url": "https://www.amazon.in/dp/B0BLX9YZ12",
        "affiliate_url": "https://www.amazon.in/dp/B0BLX9YZ12?tag=shopaipro-21",
        "price_history": [
                {
                        "date": "2026-02-01",
                        "price": 3499.0
                },
                {
                        "date": "2026-02-15",
                        "price": 2999.0
                },
                {
                        "date": "2026-03-01",
                        "price": 2799.0
                }
        ],
        "review_sentiment": {
                "sentiment_positive_pct": 89,
                "sentiment_neutral_pct": 7,
                "sentiment_negative_pct": 4,
                "positive_themes": [
                        "Exceptional value under 3000 rupees",
                        "Soft Cloudfoam shock absorption",
                        "Classic Adidas 3-Stripes look",
                        "Breathable for warm weather"
                ],
                "negative_themes": [
                        "Tread is optimized for pavement, not wet trails"
                ],
                "common_complaints": [
                        "Insole is not removable"
                ],
                "important_warnings": [
                        "Best suited for 5K-10K pavement runs and daily walking"
                ]
        }
}

]


class ProductCatalogRegistry:
    """
    Search and query engine over the comprehensive 17-category product catalog.
    Supports filtering by query text, brand, category, subcategory, price, rating, and specifications.
    """

    @classmethod
    def all_products(cls) -> List[Dict[str, Any]]:
        return list(UNIVERSAL_PRODUCT_CATALOG)

    @classmethod
    def search(
        cls,
        query: str = "",
        category: Optional[str] = None,
        subcategory: Optional[str] = None,
        brand: Optional[str] = None,
        min_price: Optional[float] = None,
        max_price: Optional[float] = None,
        min_rating: Optional[float] = None,
        limit: Optional[int] = None,
        sort_by: str = "relevance",
        page: int = 1
    ) -> List[Dict[str, Any]]:
        results = []
        raw_query = query.strip()
        q_lower = raw_query.lower()

        # 0. Extract price constraint from query text if not explicitly provided
        if max_price is None:
            # Look for explicit keywords: under, below, less than, within, upto, max, price, budget, cost, around, for
            m_price = re.search(r'(?:under|below|less than|within|upto|up to|max|maximum|budget|cost|price(?:\s*entry)?(?:\s*is)?(?:\s*:)?(?:\s*=)?|around|near|for|approx|at)\s*(?:rs\.?|inr|₹)?\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*(k|lakh|lac)?', q_lower)
            if m_price:
                extracted_val = float(m_price.group(1).replace(',', ''))
                unit = m_price.group(2)
                if unit == 'k':
                    extracted_val *= 1000
                elif unit in ('lakh', 'lac'):
                    extracted_val *= 100000
                max_price = extracted_val
            else:
                # Currency prefix (e.g. ₹1500, rs 1500)
                m_curr = re.search(r'(?:₹|rs\.?|inr)\s*(\d+(?:,\d+)*(?:\.\d+)?)\s*(k|lakh|lac)?', q_lower)
                if m_curr:
                    extracted_val = float(m_curr.group(1).replace(',', ''))
                    unit = m_curr.group(2)
                    if unit == 'k': extracted_val *= 1000
                    elif unit in ('lakh', 'lac'): extracted_val *= 100000
                    max_price = extracted_val
                else:
                    # Currency suffix (e.g. 1500 rs)
                    m_suf = re.search(r'\b(\d+(?:,\d+)*(?:\.\d+)?)\s*(?:rs|inr|₹|/-|bucks)\b', q_lower)
                    if m_suf:
                        max_price = float(m_suf.group(1).replace(',', ''))
                    else:
                        # Product followed by number (e.g. 'dress 1500')
                        m_prod = re.search(r'\b(?:dress|shoes?|phone|laptop|chair|earbuds?|watch|bag|saree|kurti)\s+(?:in\s+|for\s+|at\s+)?([0-9,]{3,7})\b', q_lower)
                        if m_prod:
                            max_price = float(m_prod.group(1).replace(',', ''))

        # 1. Intent Detection across queries
        inferred_subcategories = None
        inferred_categories = None
        must_contain_keywords = []

        if re.search(r'\b(phones?|smartphones?|mobiles?|iphones?|galaxy\s*s\d*)\b', q_lower):
            inferred_subcategories = {'mobile-phones'}
        elif re.search(r'\b(laptops?|notebooks?|macbooks?|thinkpads?)\b', q_lower):
            inferred_subcategories = {'laptops'}
        elif re.search(r'\b(air\s*fryers?|airfryers?|fryers?)\b', q_lower):
            inferred_subcategories = {'kitchen-appliances'}
            must_contain_keywords = ['fryer']
        elif re.search(r'\b(washing\s*machines?)\b', q_lower):
            inferred_subcategories = {'home-appliances'}
            must_contain_keywords = ['washing machine']
        elif re.search(r'\b(shoes?|sneakers?|running\s*shoes?|footwear|boots?)\b', q_lower):
            inferred_subcategories = {'footwear'}
        elif re.search(r'\b(dresses?|sarees?|kurtis?|gowns?|skirts?|apparels?)\b', q_lower):
            inferred_subcategories = {'womens-clothing'}
            inferred_categories = {'fashion'}
        elif re.search(r'\b(earbuds?|headphones?|earphones?|airpods?|airdopes?|soundbars?|speakers?)\b', q_lower):
            inferred_subcategories = {'audio'}
        elif re.search(r'\b(chairs?|office\s*chairs?|desk\s*chairs?)\b', q_lower):
            inferred_subcategories = {'office-furniture-organization'}
            must_contain_keywords = ['chair']
        elif re.search(r'\b(smartwatch|smartwatches|watches?)\b', q_lower):
            inferred_subcategories = {'smartwatches'}
        elif re.search(r'\b(treadmills?)\b', q_lower):
            inferred_subcategories = {'cardio-equipment'}

        # 2. Strict Brand Disambiguation
        target_brand: Optional[str] = None
        if brand and brand.lower() not in ["all", "any"]:
            target_brand = brand.strip().lower()
        else:
            known_brands = [
                'apple', 'samsung', 'oneplus', 'asus', 'lenovo', 'hp', 'acer', 'msi',
                'nike', 'adidas', 'puma', 'asics', 'philips', 'instant pot', 'pigeon',
                'da urban', 'boat', 'sony', 'libas', 'tokyo talkies', 'biba', 'zara style', 'iqoo'
            ]
            for b in known_brands:
                if re.search(r'\b' + re.escape(b) + r'\b', q_lower):
                    target_brand = b
                    break

        # 3. Clean stop words from search tokens
        stop_words = {
            "under", "below", "less", "than", "above", "over", "best", "for", "with",
            "find", "buy", "show", "me", "get", "top", "good", "cheap", "affordable",
            "the", "a", "an", "in", "at", "to", "on", "of", "and", "or", "rs", "inr", "k",
            "price", "prices", "entry", "cost", "budget", "rate", "within", "upto", "approx", "around"
        }
        all_tokens = [t.lower() for t in re.split(r'[\s,\-_/]+', raw_query) if len(t) > 1] if raw_query else []
        content_tokens = [t for t in all_tokens if t not in stop_words and not t.isdigit()]

        for p in UNIVERSAL_PRODUCT_CATALOG:
            p_cat = p.get("category", "").lower()
            p_sub = p.get("subcategory", "").lower()
            p_brand = p.get("brand", "").lower()
            p_name = p.get("product_name", "").lower()
            price = float(p.get("current_price", p.get("price", 0.0)))

            # Strict Brand Exclusion
            if target_brand:
                if target_brand not in p_brand and target_brand not in p_name:
                    continue

            # Inferred subcategory & category filters
            if inferred_subcategories and p_sub not in inferred_subcategories:
                continue
            if inferred_categories and p_cat not in inferred_categories:
                continue

            # Explicit Category filter
            if category and category.lower() not in ["all", "general", "any"]:
                cat_lower = category.lower()
                cat_match = (
                    cat_lower == p_cat or
                    cat_lower == p_sub or
                    (cat_lower in ["laptop", "laptops"] and p_sub == "laptops") or
                    (cat_lower in ["smartphone", "mobile", "phone"] and p_sub == "mobile-phones") or
                    (cat_lower in ["audio", "earbuds", "headphones", "earphones"] and p_sub == "audio") or
                    (cat_lower in ["camera", "cameras"] and p_sub == "cameras") or
                    (cat_lower in ["tv", "television"] and p_sub == "tv-entertainment") or
                    (cat_lower in ["kitchen-appliances", "air fryer", "airfryer"] and p_sub == "kitchen-appliances") or
                    (cat_lower in ["home-appliances", "washing machine", "refrigerator"] and p_sub == "home-appliances") or
                    (cat_lower in ["shoe", "shoes", "footwear", "sneaker"] and p_sub == "footwear") or
                    (cat_lower in ["dress", "dresses", "clothing", "apparel", "womens-clothing", "fashion"] and p_cat == "fashion") or
                    (cat_lower in ["skincare", "beauty"] and p_cat == "beauty-personal-care") or
                    (cat_lower in ["fitness", "gym", "treadmill"] and p_cat == "health-fitness") or
                    (cat_lower in ["book", "books"] and p_cat == "books-education") or
                    (cat_lower in ["chair", "office chair", "office-furniture"] and p_sub == "office-furniture-organization")
                )
                if not cat_match:
                    continue

            # Explicit Subcategory filter
            if subcategory and subcategory.lower() not in ["all", "any"]:
                if subcategory.lower() not in p_sub:
                    continue

            # Must-contain keywords
            if must_contain_keywords:
                if not all(kw in p_name for kw in must_contain_keywords):
                    continue

            # Price filters
            if min_price is not None and price < min_price:
                continue
            if max_price is not None and max_price > 0 and price > max_price:
                continue

            # Rating filter
            if min_rating is not None and p.get("rating", 0.0) < min_rating:
                continue

            # Query token scoring
            model_str = str(p.get("model", "")).lower()
            desc_str = str(p.get("product_description", "")).lower()
            specs_str = str(p.get("specifications", {})).lower()
            searchable_text = f"{p_name} {p_brand} {model_str} {p_sub} {p_cat} {desc_str} {specs_str}"

            if content_tokens:
                matches = sum(1 for t in content_tokens if t in searchable_text)
                if matches == 0:
                    continue
                score = matches / len(content_tokens)
                
                # Bonus if exact query phrase appears in title
                if raw_query.lower() in p_name:
                    score += 2.0
                if "gaming" in content_tokens and ("gaming" in p_name or "rtx" in searchable_text):
                    score += 1.5
            else:
                score = 1.0

            p_copy = dict(p)
            p_copy["_search_score"] = score
            results.append(p_copy)

        # Sort results
        if sort_by == "price_asc":
            results.sort(key=lambda x: (x.get("current_price", 0.0), -x.get("rating", 0.0)))
        elif sort_by == "price_desc":
            results.sort(key=lambda x: (-x.get("current_price", 0.0), -x.get("rating", 0.0)))
        elif sort_by == "rating":
            results.sort(key=lambda x: (-x.get("rating", 0.0), -x.get("_search_score", 0.0)))
        else: # relevance
            if max_price:
                results.sort(key=lambda x: (-x.get("_search_score", 0.0), x.get("current_price", 0.0), -x.get("rating", 0.0)))
            else:
                results.sort(key=lambda x: (x.get("_search_score", 0.0), x.get("rating", 0.0)), reverse=True)

        # Pagination & Limit
        if limit and limit > 0:
            start_idx = (page - 1) * limit if page > 1 else 0
            return results[start_idx:start_idx + limit]

        return results

    @classmethod
    def get_by_id(cls, product_id: str) -> Optional[Dict[str, Any]]:
        for p in UNIVERSAL_PRODUCT_CATALOG:
            if p.get("product_id") == product_id:
                return p
        return None

    @classmethod
    def to_search_candidate(cls, p: Dict[str, Any]) -> Dict[str, Any]:
        """Converts canonical 28-field catalog item into search candidate format."""
        images = p.get("images", [])
        primary_img = images[0] if images else ""
        return {
            "title": p.get("product_name"),
            "brand": p.get("brand"),
            "model": p.get("model"),
            "category": p.get("category"),
            "subcategory": p.get("subcategory"),
            "price": float(p.get("current_price", 0.0)),
            "original_price": float(p.get("mrp", p.get("current_price", 0.0))),
            "rating": float(p.get("rating", 4.5)),
            "review_count": int(p.get("review_count", 1000)),
            "url": p.get("product_url"),
            "product_url": p.get("product_url"),
            "source": p.get("source_website", "Amazon"),
            "image": primary_img,
            "image_url": primary_img,
            "snippet": p.get("product_description", ""),
            "specs": p.get("specifications", {}),
            "sellers": p.get("sellers", []),
            "variants": p.get("variants", []),
            "product_id": p.get("product_id"),
            "sku": p.get("sku"),
            "gtin_upc_ean": p.get("gtin_upc_ean"),
            "warranty": p.get("warranty"),
            "return_policy": p.get("return_policy"),
            "affiliate_url": p.get("affiliate_url"),
            "delivery_info": p.get("delivery_info"),
            "availability": p.get("availability", "In Stock")
        }

