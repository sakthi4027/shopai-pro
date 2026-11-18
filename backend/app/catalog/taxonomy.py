import re
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class SubcategoryDefinition(BaseModel):
    name: str
    slug: str
    keywords: List[str] = Field(default_factory=list)
    key_spec_fields: List[str] = Field(default_factory=list)
    common_brands: List[str] = Field(default_factory=list)
    default_warranty_months: int = 12


class CategoryDefinition(BaseModel):
    name: str
    slug: str
    description: str
    subcategories: List[SubcategoryDefinition] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)
    brands: List[str] = Field(default_factory=list)
    variant_dimensions: List[str] = Field(default_factory=list)


# ==============================================================================
# UNIVERSAL 17-CATEGORY TAXONOMY REGISTRY
# ==============================================================================
TAXONOMY_REGISTRY: Dict[str, CategoryDefinition] = {
    "electronics": CategoryDefinition(
        name="Electronics",
        slug="electronics",
        description="Mobile phones, computers, laptops, audio, cameras, wearables, gaming & home entertainment",
        variant_dimensions=["Color", "Storage", "RAM", "Configuration", "Screen Size"],
        brands=[
            "Apple", "Samsung", "Google", "OnePlus", "Xiaomi", "Redmi", "Realme", "Vivo", "Oppo",
            "Motorola", "Nothing", "Asus", "Sony", "Nokia", "Honor", "Poco", "Infinix", "Tecno",
            "Lenovo", "Dell", "HP", "Acer", "MSI", "LG", "Bose", "Sennheiser", "JBL", "Boat", "Noise",
            "Canon", "Nikon", "PlayStation", "Xbox", "Nintendo", "TP-Link", "Netgear", "Epson", "Crucial"
        ],
        keywords=["electronic", "gadget", "tech", "device", "smart"],
        subcategories=[
            SubcategoryDefinition(
                name="Mobile Phones",
                slug="mobile-phones",
                keywords=["phone", "smartphone", "iphone", "galaxy", "pixel", "android phone", "mobile", "5g phone"],
                key_spec_fields=["display", "ram_gb", "storage_gb", "camera", "battery_mah", "processor", "os"],
                common_brands=["Apple", "Samsung", "Google", "OnePlus", "Xiaomi", "Vivo", "Realme", "Motorola", "Nothing"]
            ),
            SubcategoryDefinition(
                name="Laptops",
                slug="laptops",
                keywords=["laptop", "notebook", "macbook", "ultrabook", "gaming laptop", "chromebook", "2-in-1 laptop", "ai laptop"],
                key_spec_fields=["ram_gb", "storage_gb", "cpu", "gpu", "screen_size_inches", "battery_life_hours", "os", "weight_kg"],
                common_brands=["Apple", "ASUS", "Lenovo", "Dell", "HP", "Acer", "MSI", "Samsung"]
            ),
            SubcategoryDefinition(
                name="Computers & Components",
                slug="computers-components",
                keywords=["desktop pc", "gaming pc", "workstation", "cpu", "gpu", "graphics card", "ram", "ssd", "nvme", "motherboard", "power supply"],
                key_spec_fields=["cpu", "gpu", "ram_gb", "storage_gb", "form_factor", "wattage", "socket"],
                common_brands=["Intel", "AMD", "NVIDIA", "Corsair", "Crucial", "Kingston", "Samsung", "Gigabyte", "Asus"]
            ),
            SubcategoryDefinition(
                name="Tablets",
                slug="tablets",
                keywords=["tablet", "ipad", "android tablet", "drawing tablet", "tab"],
                key_spec_fields=["screen_size_inches", "storage_gb", "ram_gb", "battery_mah", "stylus_support"],
                common_brands=["Apple", "Samsung", "Lenovo", "OnePlus", "Xiaomi", "Wacom"]
            ),
            SubcategoryDefinition(
                name="Audio",
                slug="audio",
                keywords=["headphone", "headphones", "earbuds", "tws", "earphones", "soundbar", "bluetooth speaker", "dac", "amplifier", "mic"],
                key_spec_fields=["driver_size_mm", "battery_hours", "noise_cancellation", "connectivity", "water_resistance"],
                common_brands=["Sony", "Bose", "Apple", "Sennheiser", "JBL", "Marshall", "Boat", "Noise"]
            ),
            SubcategoryDefinition(
                name="Wearables",
                slug="wearables",
                keywords=["smart watch", "smartwatch", "fitness band", "smart ring", "apple watch", "galaxy watch"],
                key_spec_fields=["display_type", "battery_days", "water_resistance", "sensors", "compatibility"],
                common_brands=["Apple", "Samsung", "Garmin", "Fitbit", "Noise", "Boat", "Amazfit"]
            ),
            SubcategoryDefinition(
                name="Cameras",
                slug="cameras",
                keywords=["dslr", "mirrorless camera", "action camera", "gopro", "vlog camera", "camera lens", "tripod"],
                key_spec_fields=["sensor_type", "megapixels", "video_resolution", "lens_mount", "stabilization"],
                common_brands=["Sony", "Canon", "Nikon", "Fujifilm", "GoPro", "DJI"]
            ),
            SubcategoryDefinition(
                name="TV & Entertainment",
                slug="tv-entertainment",
                keywords=["smart tv", "led tv", "oled tv", "qled tv", "projector", "4k tv", "streaming stick", "fire stick"],
                key_spec_fields=["screen_size_inches", "resolution", "display_tech", "refresh_rate_hz", "smart_os", "audio_watts"],
                common_brands=["Sony", "Samsung", "LG", "TCL", "Xiaomi", "Vu", "Hisense"]
            ),
            SubcategoryDefinition(
                name="Gaming",
                slug="gaming",
                keywords=["playstation", "ps5", "xbox", "nintendo switch", "gaming controller", "racing wheel", "vr headset"],
                key_spec_fields=["storage_gb", "resolution_support", "controller_included", "vr_compatible"],
                common_brands=["Sony", "Microsoft", "Nintendo", "Meta", "Logitech", "Razer"]
            ),
            SubcategoryDefinition(
                name="Networking & Printers",
                slug="networking-printers",
                keywords=["wifi router", "mesh router", "modem", "printer", "laser printer", "inkjet printer", "all-in-one printer", "3d printer"],
                key_spec_fields=["speed_mbps", "wifi_standard", "print_speed_ppm", "duplex_printing"],
                common_brands=["TP-Link", "Netgear", "Asus", "HP", "Canon", "Epson", "Brother"]
            )
        ]
    ),

    "fashion": CategoryDefinition(
        name="Fashion",
        slug="fashion",
        description="Men's, Women's and Kids' clothing, footwear, bags, watches and accessories",
        variant_dimensions=["Size", "Color", "Material", "Fit"],
        brands=[
            "Nike", "Adidas", "Puma", "Under Armour", "Asics", "Levi's", "Zara", "H&M", "Marks & Spencer",
            "Tommy Hilfiger", "Calvin Klein", "Manyavar", "Biba", "Fabindia", "W", "Allen Solly", "Van Heusen",
            "Louis Philippe", "Ray-Ban", "Fossil", "Titan", "Fastrack", "Bata", "Clarks", "Woodland", "Skechers"
        ],
        keywords=["clothing", "apparel", "wear", "outfit", "shoe", "shoes", "fashion", "dress"],
        subcategories=[
            SubcategoryDefinition(
                name="Footwear",
                slug="footwear",
                keywords=["shoes", "running shoes", "sneakers", "boots", "sandals", "slippers", "heels", "formal shoes", "walking shoes"],
                key_spec_fields=["material", "sole_type", "closure", "cushioning_level", "weight_g"],
                common_brands=["Nike", "Adidas", "Puma", "Asics", "Skechers", "Bata", "Clarks", "Woodland"]
            ),
            SubcategoryDefinition(
                name="Men's Clothing",
                slug="mens-clothing",
                keywords=["men shirt", "men t-shirt", "men jeans", "trousers", "blazer", "suit", "kurta", "jacket", "hoodie"],
                key_spec_fields=["fabric", "fit", "sleeve_length", "pattern", "wash_care"],
                common_brands=["Levi's", "Tommy Hilfiger", "Allen Solly", "Van Heusen", "Zara", "Manyavar"]
            ),
            SubcategoryDefinition(
                name="Women's Clothing",
                slug="womens-clothing",
                keywords=["saree", "kurti", "salwar suit", "dress", "lehenga", "women jeans", "gown", "top"],
                key_spec_fields=["fabric", "fit", "weave_type", "occasion", "length"],
                common_brands=["Biba", "W", "Fabindia", "Zara", "H&M", "Aurelia", "Forever New"]
            ),
            SubcategoryDefinition(
                name="Kids Clothing",
                slug="kids-clothing",
                keywords=["boys clothing", "girls clothing", "baby clothes", "kids wear", "infant wear"],
                key_spec_fields=["age_group", "material", "safety_tested", "closure"],
                common_brands=["Mothercare", "FirstCry", "Hopscotch", "H&M Kids", "Marks & Spencer"]
            ),
            SubcategoryDefinition(
                name="Fashion Accessories",
                slug="fashion-accessories",
                keywords=["handbag", "backpack", "wallet", "belt", "sunglasses", "scarf", "tie", "caps"],
                key_spec_fields=["material", "compartments", "uv_protection", "dimensions"],
                common_brands=["Ray-Ban", "Fossil", "Titan", "Wildcraft", "American Tourister", "Caprese"]
            )
        ]
    ),

    "home-furniture": CategoryDefinition(
        name="Home & Furniture",
        slug="home-furniture",
        description="Furniture, large home appliances, smart kitchen appliances, and home decor",
        variant_dimensions=["Color", "Size", "Capacity", "Material", "Configuration"],
        brands=[
            "LG", "Samsung", "Whirlpool", "Bosch", "IFB", "Haier", "Godrej", "Voltas", "Daikin",
            "Philips", "Morphy Richards", "Bajaj", "Prestige", "Hawkins", "Panasonic", "Dyson",
            "Sleepwell", "Wakefit", "IKEA", "Godrej Interio", "Green Soul", "Nilkamal", "Urban Ladder"
        ],
        keywords=["home", "furniture", "appliance", "kitchen", "living room", "decor", "sofa", "bed"],
        subcategories=[
            SubcategoryDefinition(
                name="Home Appliances",
                slug="home-appliances",
                keywords=["washing machine", "refrigerator", "fridge", "air conditioner", "ac", "dishwasher", "air purifier", "vacuum cleaner", "water heater", "geyser"],
                key_spec_fields=["capacity", "energy_rating_stars", "inverter_tech", "power_consumption_w", "warranty_years"],
                common_brands=["LG", "Samsung", "Whirlpool", "Bosch", "IFB", "Voltas", "Daikin", "Dyson"]
            ),
            SubcategoryDefinition(
                name="Kitchen Appliances",
                slug="kitchen-appliances",
                keywords=["microwave oven", "air fryer", "mixer grinder", "juicer", "blender", "food processor", "electric kettle", "coffee machine", "induction cooktop", "chimney"],
                key_spec_fields=["capacity_litres", "wattage", "speed_settings", "auto_programs", "warranty_months"],
                common_brands=["Philips", "Prestige", "Morphy Richards", "Bajaj", "Havells", "Pigeon", "Wonderchef"]
            ),
            SubcategoryDefinition(
                name="Furniture",
                slug="furniture",
                keywords=["sofa", "recliner", "bed", "mattress", "wardrobe", "study table", "office chair", "dining table", "bookshelf", "gaming chair"],
                key_spec_fields=["material", "dimensions_cm", "seating_capacity", "ergonomic_features", "warranty_years"],
                common_brands=["Wakefit", "Sleepwell", "IKEA", "Green Soul", "Urban Ladder", "Godrej Interio"]
            ),
            SubcategoryDefinition(
                name="Home Decor",
                slug="home-decor",
                keywords=["curtain", "carpet", "rug", "wall clock", "lamp", "vase", "bedsheet", "blanket", "cushion"],
                key_spec_fields=["fabric_type", "thread_count", "dimensions_inches", "care_instructions"],
                common_brands=["D'Decor", "Spaces", "Story@Home", "Bombay Dyeing", "Trident"]
            )
        ]
    ),

    "beauty-personal-care": CategoryDefinition(
        name="Beauty & Personal Care",
        slug="beauty-personal-care",
        description="Skincare, haircare, luxury fragrances, cosmetics and grooming appliances",
        variant_dimensions=["Volume", "Shade", "Skin Type", "Pack Size"],
        brands=[
            "Minimalist", "The Ordinary", "Cetaphil", "Neutrogena", "L'Oreal", "Maybelline", "MAC",
            "Estee Lauder", "Nykaa", "Clinique", "Davidoff", "Calvin Klein", "Dior", "Chanel", "Philips",
            "Braun", "Gillette", "Beardo", "Mamaearth", "Biotique", "Forest Essentials", "Kama Ayurveda"
        ],
        keywords=["beauty", "skin", "hair", "perfume", "grooming", "makeup", "lotion", "cosmetic"],
        subcategories=[
            SubcategoryDefinition(
                name="Skincare",
                slug="skincare",
                keywords=["face wash", "moisturizer", "sunscreen", "serum", "cleanser", "toner", "face mask", "body lotion"],
                key_spec_fields=["skin_type", "active_ingredients", "spf_rating", "volume_ml", "dermatologist_tested"],
                common_brands=["Minimalist", "Cetaphil", "The Ordinary", "Neutrogena", "Forest Essentials"]
            ),
            SubcategoryDefinition(
                name="Haircare & Styling",
                slug="haircare-styling",
                keywords=["shampoo", "conditioner", "hair oil", "hair serum", "hair dryer", "hair straightener"],
                key_spec_fields=["hair_type", "sulfate_free", "heat_settings", "wattage"],
                common_brands=["L'Oreal", "Philips", "Dyson", "Kérastase", "Mamaearth", "Tresemme"]
            ),
            SubcategoryDefinition(
                name="Makeup",
                slug="makeup",
                keywords=["foundation", "lipstick", "mascara", "eyeliner", "blush", "compact powder", "makeup kit"],
                key_spec_fields=["shade", "finish", "coverage", "longevity_hours"],
                common_brands=["Maybelline", "MAC", "Nykaa", "L'Oreal", "Sugar Cosmetics"]
            ),
            SubcategoryDefinition(
                name="Fragrance & Grooming",
                slug="fragrance-grooming",
                keywords=["perfume", "deodorant", "body spray", "attar", "electric shaver", "beard trimmer", "hair clipper"],
                key_spec_fields=["fragrance_family", "concentration", "battery_run_time_min", "waterproof"],
                common_brands=["Davidoff", "Calvin Klein", "Philips", "Braun", "Beardo", "Bombay Shaving Company"]
            )
        ]
    ),

    "health-fitness": CategoryDefinition(
        name="Health & Fitness",
        slug="health-fitness",
        description="Home gym equipment, sports gear, fitness trackers and accessories",
        variant_dimensions=["Weight", "Size", "Resistance Level"],
        brands=[
            "PowerMax", "Cultsport", "Boldfit", "Fitkit", "Decathlon", "Yonex", "Cosco",
            "Nivia", "Spalding", "Wilson", "Stag", "Garmin", "Optimum Nutrition", "MuscleBlaze"
        ],
        keywords=["fitness", "gym", "workout", "exercise", "sport", "sports", "treadmill", "dumbbells"],
        subcategories=[
            SubcategoryDefinition(
                name="Fitness Equipment",
                slug="fitness-equipment",
                keywords=["treadmill", "exercise bike", "dumbbells", "kettlebell", "barbell", "weight bench", "resistance bands", "pull-up bar"],
                key_spec_fields=["motor_hp", "max_user_weight_kg", "incline_levels", "weight_kg"],
                common_brands=["PowerMax", "Cultsport", "Fitkit", "Boldfit", "Decathlon"]
            ),
            SubcategoryDefinition(
                name="Sports Equipment",
                slug="sports-equipment",
                keywords=["cricket bat", "cricket ball", "football", "basketball", "tennis racket", "badminton racket", "shuttlecock"],
                key_spec_fields=["material", "string_tension_lbs", "size", "weight_g"],
                common_brands=["Yonex", "Cosco", "Nivia", "SS", "MRF", "Wilson"]
            ),
            SubcategoryDefinition(
                name="Fitness Accessories",
                slug="fitness-accessories",
                keywords=["yoga mat", "water bottle", "gym bag", "skipping rope", "foam roller", "knee support"],
                key_spec_fields=["thickness_mm", "material", "anti_slip", "capacity_ml"],
                common_brands=["Boldfit", "Decathlon", "Kobo", "Nivia"]
            )
        ]
    ),

    "books-education": CategoryDefinition(
        name="Books & Education",
        slug="books-education",
        description="Technical, programming, academic, non-fiction and children's literature, STEM kits",
        variant_dimensions=["Format", "Edition", "Language"],
        brands=[
            "O'Reilly", "Penguin", "HarperCollins", "Pearson", "McGraw Hill", "Packt",
            "Oxford", "Cambridge", "Scholastic", "LEGO", "Arduino", "Raspberry Pi"
        ],
        keywords=["book", "books", "reading", "textbook", "novel", "programming book", "stem kit", "learn"],
        subcategories=[
            SubcategoryDefinition(
                name="Books",
                slug="books",
                keywords=["programming book", "ai book", "machine learning", "machine learning book", "data science", "deep learning", "hands-on", "hands on", "fiction", "non-fiction", "self-help", "biography", "novel", "edition", "paperback"],
                key_spec_fields=["author", "publisher", "pages", "language", "format", "isbn"],
                common_brands=["O'Reilly", "Penguin", "HarperCollins", "Pearson", "Packt"]
            ),
            SubcategoryDefinition(
                name="Educational & STEM Kits",
                slug="educational-stem-kits",
                keywords=["stem kit", "robotics kit", "coding kit", "science kit", "arduino kit", "learning toys"],
                key_spec_fields=["recommended_age", "components_count", "curriculum_focus"],
                common_brands=["LEGO Education", "Arduino", "Raspberry Pi", "Smartivity"]
            )
        ]
    ),

    "baby-kids": CategoryDefinition(
        name="Baby & Kids",
        slug="baby-kids",
        description="Baby care essentials, strollers, car seats, infant toys and nursery furniture",
        variant_dimensions=["Age Group", "Size", "Color"],
        brands=["Pampers", "Huggies", "Chicco", "MamyPoko", "Fisher-Price", "LEGO", "Hot Wheels", "Barbie"],
        keywords=["baby", "infant", "toddler", "kids", "diaper", "stroller", "toys"],
        subcategories=[
            SubcategoryDefinition(
                name="Baby Care & Gear",
                slug="baby-care-gear",
                keywords=["baby diapers", "baby wipes", "stroller", "car seat", "baby cot", "feeding bottle"],
                key_spec_fields=["age_suitability", "weight_capacity_kg", "bpa_free", "safety_certification"],
                common_brands=["Pampers", "Chicco", "Huggies", "LuvLap", "Philips Avent"]
            ),
            SubcategoryDefinition(
                name="Toys & Games",
                slug="toys-games",
                keywords=["toys", "building blocks", "remote control car", "board game", "puzzle", "doll"],
                key_spec_fields=["recommended_age", "material", "battery_operated"],
                common_brands=["LEGO", "Fisher-Price", "Hot Wheels", "Hasbro", "Mattel"]
            )
        ]
    ),

    "automotive": CategoryDefinition(
        name="Automotive",
        slug="automotive",
        description="Car electronics, dash cams, bike riding gear, helmets, and vehicle maintenance",
        variant_dimensions=["Vehicle Fitment", "Size", "Voltage"],
        brands=["70mai", "Bosch", "Portronics", "Steelbird", "Vega", "Studds", "Michelin", "MRF", "Castrol"],
        keywords=["car", "bike", "motorcycle", "vehicle", "auto", "dash cam", "helmet", "tyres"],
        subcategories=[
            SubcategoryDefinition(
                name="Car Electronics & Accessories",
                slug="car-electronics-accessories",
                keywords=["dash camera", "dash cam", "car camera", "car charger", "car vacuum", "car cover", "floor mats", "tyre inflator"],
                key_spec_fields=["resolution", "power_input", "sensor", "fitment_type"],
                common_brands=["70mai", "Bosch", "Portronics", "Qubo", "Amkette"]
            ),
            SubcategoryDefinition(
                name="Motorcycle Riding Gear",
                slug="motorcycle-riding-gear",
                keywords=["helmet", "riding gloves", "riding jacket", "bike cover", "bike lock"],
                key_spec_fields=["safety_standard", "size", "material", "waterproof"],
                common_brands=["Steelbird", "Vega", "Studds", "Rynox", "Royal Enfield"]
            )
        ]
    ),

    "pet-supplies": CategoryDefinition(
        name="Pet Supplies",
        slug="pet-supplies",
        description="Nutritious pet food, grooming supplies, toys, beds and accessories for dogs, cats and birds",
        variant_dimensions=["Pet Size", "Weight / Quantity", "Flavor"],
        brands=["Royal Canin", "Pedigree", "Whiskas", "Drools", "Farmina N&D", "Himalaya Pet", "KONG"],
        keywords=["pet", "dog", "cat", "puppy", "kitten", "pet food", "dog food", "cat food", "aquarium"],
        subcategories=[
            SubcategoryDefinition(
                name="Dog Supplies",
                slug="dog-supplies",
                keywords=["dog food", "dog treats", "dog toy", "dog bed", "dog leash", "dog shampoo"],
                key_spec_fields=["life_stage", "breed_size", "diet_type", "weight_kg"],
                common_brands=["Royal Canin", "Pedigree", "Drools", "Farmina", "KONG"]
            ),
            SubcategoryDefinition(
                name="Cat Supplies",
                slug="cat-supplies",
                keywords=["cat food", "cat treats", "cat litter", "cat bed", "cat scratcher"],
                key_spec_fields=["life_stage", "flavor", "weight_kg", "clumping_type"],
                common_brands=["Whiskas", "Royal Canin", "Sheba", "Drools"]
            )
        ]
    ),

    "grocery-food": CategoryDefinition(
        name="Grocery & Food",
        slug="grocery-food",
        description="Pantry staples, organic foods, dry fruits, beverages and household essentials",
        variant_dimensions=["Pack Size", "Weight", "Flavor"],
        brands=["Tata", "Fortune", "Aashirvaad", "Nestle", "Cadbury", "Bru", "Tetley", "Surf Excel", "Vim"],
        keywords=["grocery", "food", "tea", "coffee", "rice", "dal", "oil", "biscuits", "detergent"],
        subcategories=[
            SubcategoryDefinition(
                name="Pantry Staples & Gourmet",
                slug="pantry-staples-gourmet",
                keywords=["basmati rice", "wheat flour", "cooking oil", "dry fruits", "spices", "olive oil"],
                key_spec_fields=["dietary_type", "pack_weight_kg", "shelf_life_months"],
                common_brands=["Tata Sampann", "Fortune", "Aashirvaad", "Daawat", "Happilo"]
            ),
            SubcategoryDefinition(
                name="Beverages & Snacks",
                slug="beverages-snacks",
                keywords=["tea", "coffee", "green tea", "cookies", "dark chocolate", "roasted almonds"],
                key_spec_fields=["roast_level", "organic_certified", "caffeine_content"],
                common_brands=["Nescafe", "Blue Tokai", "Tetley", "Cadbury", "Ferrero"]
            )
        ]
    ),

    "office-products": CategoryDefinition(
        name="Office Products",
        slug="office-products",
        description="Ergonomic workstations, desk organization, office electronics and writing supplies",
        variant_dimensions=["Size", "Color", "Configuration"],
        brands=["Featherlite", "Green Soul", "Logitech", "HP", "Epson", "Classmate", "Parker", "Faber-Castell"],
        keywords=["office", "stationery", "desk", "office chair", "calculator", "shredder", "whiteboard"],
        subcategories=[
            SubcategoryDefinition(
                name="Office Furniture & Organization",
                slug="office-furniture-organization",
                keywords=["office chair", "ergonomic chair", "standing desk", "file cabinet", "whiteboard"],
                key_spec_fields=["ergonomic_adjustment", "weight_capacity_kg", "dimensions_cm"],
                common_brands=["Featherlite", "Green Soul", "Wakefit", "IKEA"]
            )
        ]
    ),

    "industrial-tools": CategoryDefinition(
        name="Industrial & Tools",
        slug="industrial-tools",
        description="Power tools, hand tool kits, measurement devices and workshop safety gear",
        variant_dimensions=["Power / Voltage", "Set Size"],
        brands=["Bosch", "DeWalt", "Black+Decker", "Stanley", "Taparia", "Makita"],
        keywords=["tools", "power tool", "drill", "screwdriver", "welding", "safety gloves", "multimeter"],
        subcategories=[
            SubcategoryDefinition(
                name="Power & Hand Tools",
                slug="power-hand-tools",
                keywords=["drill machine", "cordless drill", "toolkit", "screwdriver set", "wrench", "measuring tape"],
                key_spec_fields=["voltage", "motor_power_w", "chuck_size_mm", "torque_nm", "cordless"],
                common_brands=["Bosch", "DeWalt", "Black+Decker", "Stanley", "Taparia"]
            )
        ]
    ),

    "travel-luggage": CategoryDefinition(
        name="Travel & Luggage",
        slug="travel-luggage",
        description="Cabin and check-in suitcases, laptop backpacks, duffels and travel accessories",
        variant_dimensions=["Size (Cabin/Medium/Large)", "Color", "Volume"],
        brands=["Samsonite", "American Tourister", "VIP", "Safari", "Mokobara", "Wildcraft", "Delsey"],
        keywords=["luggage", "suitcase", "trolley bag", "backpack", "travel bag", "duffel bag"],
        subcategories=[
            SubcategoryDefinition(
                name="Suitcases & Trolley Bags",
                slug="suitcases-trolley-bags",
                keywords=["trolley bag", "suitcase", "cabin luggage", "hard luggage", "check-in bag"],
                key_spec_fields=["size_inches", "volume_litres", "lock_type_tsa", "wheel_count", "material"],
                common_brands=["American Tourister", "Samsonite", "Mokobara", "Safari", "VIP"]
            )
        ]
    ),

    "musical-instruments": CategoryDefinition(
        name="Musical Instruments",
        slug="musical-instruments",
        description="Acoustic and electric guitars, digital pianos, studio microphones and audio monitors",
        variant_dimensions=["Color", "Size / Frets", "Type"],
        brands=["Yamaha", "Fender", "Gibson", "Casio", "Roland", "Shure", "Audio-Technica", "Focusrite"],
        keywords=["guitar", "keyboard", "piano", "drums", "violin", "microphone", "amplifier", "music"],
        subcategories=[
            SubcategoryDefinition(
                name="String & Key Instruments",
                slug="string-key-instruments",
                keywords=["acoustic guitar", "electric guitar", "digital piano", "synthesizer", "ukulele"],
                key_spec_fields=["fret_count", "body_wood", "keys_count", "connectivity"],
                common_brands=["Yamaha", "Fender", "Casio", "Roland", "Ibanez"]
            )
        ]
    ),

    "garden-outdoor": CategoryDefinition(
        name="Garden & Outdoor",
        slug="garden-outdoor",
        description="Gardening tools, planters, soil nutrients, camping tents and outdoor leisure",
        variant_dimensions=["Size", "Capacity", "Material"],
        brands=["TrustBasket", "Ugaoo", "Kraft Seeds", "Quechua", "Coleman", "Black+Decker"],
        keywords=["garden", "plants", "planter", "seeds", "camping", "tent", "sleeping bag", "outdoor"],
        subcategories=[
            SubcategoryDefinition(
                name="Gardening & Camping",
                slug="gardening-camping",
                keywords=["gardening tool kit", "plant pots", "flower seeds", "organic potting soil", "camping tent"],
                key_spec_fields=["material", "capacity_litres", "occupancy_persons", "weatherproof"],
                common_brands=["TrustBasket", "Ugaoo", "Quechua", "Coleman"]
            )
        ]
    ),

    "jewellery-watches": CategoryDefinition(
        name="Jewellery & Watches",
        slug="jewellery-watches",
        description="Gold, silver, diamond and fine jewellery, along with luxury, automatic and analog watches",
        variant_dimensions=["Metal Purity", "Gemstone", "Size", "Dial Color"],
        brands=["Tanishq", "Malabar Gold", "CaratLane", "Titan", "Fossil", "Seiko", "Citizen", "Casio", "Rolex"],
        keywords=["jewellery", "gold", "silver", "diamond", "watch", "analog watch", "ring", "necklace"],
        subcategories=[
            SubcategoryDefinition(
                name="Fine Jewellery",
                slug="fine-jewellery",
                keywords=["gold ring", "diamond necklace", "silver earrings", "bracelet", "pendant"],
                key_spec_fields=["metal_purity", "gross_weight_g", "certificate_authority", "gemstone_clarity"],
                common_brands=["Tanishq", "CaratLane", "Malabar Gold", "Giva"]
            ),
            SubcategoryDefinition(
                name="Watches",
                slug="watches",
                keywords=["analog watch", "automatic watch", "chronograph watch", "luxury watch", "titan watch"],
                key_spec_fields=["movement_type", "dial_diameter_mm", "water_resistance_atm", "strap_material"],
                common_brands=["Titan", "Fossil", "Seiko", "Casio", "Citizen", "Tommy Hilfiger"]
            )
        ]
    ),

    "electrical-home-improvement": CategoryDefinition(
        name="Electrical & Home Improvement",
        slug="electrical-home-improvement",
        description="Smart lighting, modular switches, power inverters, solar panels and home hardware",
        variant_dimensions=["Wattage", "Color Temp", "Capacity"],
        brands=["Philips", "Havells", "Luminous", "Microtek", "Schneider", "Wipro", "Anchor", "Syska"],
        keywords=["bulb", "smart bulb", "inverter", "solar panel", "switch", "socket", "electrical", "hardware"],
        subcategories=[
            SubcategoryDefinition(
                name="Smart Lighting & Power Inverters",
                slug="lighting-inverters",
                keywords=["smart led bulb", "ceiling light", "inverter", "tubular battery", "solar inverter", "modular switch"],
                key_spec_fields=["wattage", "lumens", "va_rating", "battery_capacity_ah", "color_temperature_k"],
                common_brands=["Philips", "Havells", "Luminous", "Microtek", "Wipro"]
            )
        ]
    )
}


class TaxonomyClassifier:
    """Intelligent multi-category classifier that matches freeform user queries to category & subcategory."""
    
    @staticmethod
    def classify(query: str) -> Dict[str, Any]:
        q_lower = query.lower()

        # Check each category and subcategory
        best_category = "all"
        best_subcategory = "all"
        max_score = 0
        detected_brands = []

        # Direct product alias to brand mapping
        brand_aliases = {
            "iphone": "Apple",
            "ipad": "Apple",
            "macbook": "Apple",
            "airpods": "Apple",
            "galaxy": "Samsung",
            "thinkpad": "Lenovo",
            "legion": "Lenovo",
            "loq": "Lenovo",
            "yoga": "Lenovo",
            "tuf": "ASUS",
            "rog": "ASUS",
            "zenbook": "ASUS",
            "omen": "HP",
            "victus": "HP",
            "nitro": "Acer",
            "predator": "Acer",
            "katana": "MSI",
            "bravia": "Sony",
            "playstation": "Sony",
            "pegasus": "Nike",
            "ultraboost": "Adidas",
        }
        for alias, brand_name in brand_aliases.items():
            if re.search(rf'\b{re.escape(alias)}\b', q_lower):
                if brand_name not in detected_brands:
                    detected_brands.append(brand_name)

        for cat_slug, cat_def in TAXONOMY_REGISTRY.items():
            cat_score = 0
            # Check category keywords
            for kw in cat_def.keywords:
                if re.search(rf'\b{re.escape(kw)}\b', q_lower):
                    cat_score += 2

            # Check subcategory keywords
            for sub in cat_def.subcategories:
                sub_score = 0
                for skw in sub.keywords:
                    if re.search(rf'\b{re.escape(skw)}\b', q_lower):
                        sub_score += 4
                
                total_score = cat_score + sub_score
                if total_score > max_score:
                    max_score = total_score
                    best_category = cat_slug
                    best_subcategory = sub.slug

            # Check brands
            for b in cat_def.brands:
                if re.search(rf'\b{re.escape(b.lower())}\b', q_lower):
                    if b not in detected_brands:
                        detected_brands.append(b)
                        if cat_score == 0:
                            cat_score += 3
                            if cat_score > max_score:
                                max_score = cat_score
                                best_category = cat_slug

        return {
            "category": best_category if max_score > 0 else "all",
            "subcategory": best_subcategory if max_score > 0 else "all",
            "detected_brands": detected_brands,
            "confidence": min(1.0, max_score / 6.0) if max_score > 0 else 0.0
        }

    @staticmethod
    def get_category(slug: str) -> Optional[CategoryDefinition]:
        return TAXONOMY_REGISTRY.get(slug)

    @staticmethod
    def get_all_categories() -> List[Dict[str, str]]:
        return [{"name": c.name, "slug": c.slug, "description": c.description} for c in TAXONOMY_REGISTRY.values()]
