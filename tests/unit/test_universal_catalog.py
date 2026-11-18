import pytest
from backend.app.catalog.taxonomy import TAXONOMY_REGISTRY, TaxonomyClassifier
from backend.app.catalog.registry import UNIVERSAL_PRODUCT_CATALOG, ProductCatalogRegistry
from agents.orchestrator.agent import orchestrator_agent


def test_taxonomy_has_all_17_categories():
    """Verify all 17 canonical e-commerce categories are present in the taxonomy registry."""
    expected_categories = [
        "electronics", "fashion", "home-furniture", "beauty-personal-care",
        "health-fitness", "books-education", "baby-kids", "automotive",
        "pet-supplies", "grocery-food", "office-products", "industrial-tools",
        "travel-luggage", "musical-instruments", "garden-outdoor",
        "jewellery-watches", "electrical-home-improvement"
    ]
    for cat in expected_categories:
        assert cat in TAXONOMY_REGISTRY, f"Category '{cat}' missing from TAXONOMY_REGISTRY"
        cat_def = TAXONOMY_REGISTRY[cat]
        assert len(cat_def.subcategories) > 0, f"Category '{cat}' has no subcategories"
        assert len(cat_def.brands) > 0, f"Category '{cat}' has no brands registered"
        assert len(cat_def.variant_dimensions) > 0, f"Category '{cat}' has no variant dimensions"


def test_taxonomy_classifier_multicategory():
    """Verify taxonomy classifier accurately categorizes diverse shopping queries."""
    test_cases = [
        ("running shoes under 10000", "fashion", "footwear"),
        ("front load washing machine 8kg", "home-furniture", "home-appliances"),
        ("minimalist niacinamide face serum", "beauty-personal-care", "skincare"),
        ("dual dash cam with gps for car", "automotive", "car-electronics-accessories"),
        ("acoustic guitar for beginners", "musical-instruments", "string-key-instruments"),
        ("motorized treadmill for home cardio", "health-fitness", "fitness-equipment"),
        ("hands on machine learning aurelien geron", "books-education", "books"),
        ("pure sine wave inverter 900va luminous", "electrical-home-improvement", "lighting-inverters"),
    ]

    for query, exp_cat, exp_sub in test_cases:
        res = TaxonomyClassifier.classify(query)
        assert res["category"] == exp_cat, f"For query '{query}', expected category '{exp_cat}', got '{res['category']}'"
        assert res["subcategory"] == exp_sub, f"For query '{query}', expected subcategory '{exp_sub}', got '{res['subcategory']}'"


def test_products_have_28_canonical_fields_and_no_mock_data():
    """Verify every catalog product contains all 28 canonical e-commerce data fields and authentic store URLs."""
    canonical_fields = [
        "product_id", "product_name", "category", "subcategory", "brand", "model",
        "variant", "sku", "gtin_upc_ean", "product_description", "images", "videos",
        "specifications", "current_price", "mrp", "discount_percentage", "currency",
        "rating", "review_count", "seller", "seller_rating", "availability",
        "delivery_info", "warranty", "return_policy", "source_website", "product_url",
        "affiliate_url", "last_updated"
    ]

    assert len(UNIVERSAL_PRODUCT_CATALOG) >= 17, "Catalog must span all 17 categories"

    for p in UNIVERSAL_PRODUCT_CATALOG:
        for f in canonical_fields:
            assert f in p, f"Product {p.get('product_id', 'Unknown')} missing required field '{f}'"
        
        # Verify valid non-empty real URLs
        assert p["product_url"].startswith("http"), f"Invalid product_url for {p['product_id']}"
        assert any(store in p["product_url"].lower() for store in ["amazon.in", "flipkart.com", "croma.com", "myntra.com", "nykaa.com", "firstcry.com", "tatacliq.com", "bajaao.com"]), (
            f"Product {p['product_id']} has unrecognized store domain in url: {p['product_url']}"
        )
        assert p["current_price"] > 0
        assert p["mrp"] >= p["current_price"]
        assert len(p["images"]) > 0
        assert p["images"][0].startswith("http")


def test_product_variants_dimensions():
    """Verify variant support for Color, Size, Storage, RAM, Capacity, Pack Size, etc."""
    for p in UNIVERSAL_PRODUCT_CATALOG:
        variants = p.get("variants", [])
        if variants:
            for v in variants:
                assert "name" in v
                assert "price" in v
                assert v["price"] > 0
                assert "sku" in v


@pytest.mark.asyncio
async def test_end_to_end_multicategory_search_shoes():
    """Verify end-to-end workflow execution for a non-tech category: running shoes."""
    result = await orchestrator_agent.execute_workflow(
        query="Find me Nike running shoes for road running under ₹10,000 with good cushioning"
    )
    assert len(result["ranked_products"]) > 0
    top = result["ranked_products"][0]
    assert "Nike" in top["brand"] or "Nike" in top["name"]
    assert top["price"] <= 10000.0
    assert len(top["recommendation_explanation"]) > 10
    assert top["product_url"].startswith("http")
