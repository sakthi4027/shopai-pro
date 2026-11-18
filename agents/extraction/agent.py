import datetime
from typing import Dict, Any, Optional, List
from agents.base_agent import AbstractAgent


class ProductExtractionAgent(AbstractAgent):
    """
    Universal Multi-Category Product Extraction Agent:
    Extracts all 28 canonical e-commerce schema fields from raw product candidates:
    Product ID, Product Name, Category, Subcategory, Brand, Model, Variant,
    SKU, GTIN/UPC/EAN, Product Description, Images, Videos, Dynamic Specifications,
    Current Price, MRP, Discount, Currency, Rating, Review Count, Seller,
    Seller Rating, Availability, Delivery Info, Warranty, Return Policy,
    Source Website, Product URL, Affiliate URL, and Last Updated.
    """
    def __init__(self):
        super().__init__(
            name="Product Extraction Agent",
            description="Extracts normalized structured specifications and 28 canonical e-commerce metadata fields across all categories"
        )

    async def _execute(
        self, 
        context: Dict[str, Any], 
        on_progress: Optional[Any] = None
    ) -> Dict[str, Any]:
        search_data = context.get("search_results", {})
        raw_candidates = search_data.get("products", [])

        extracted = []
        now_iso = datetime.datetime.utcnow().isoformat()

        for c in raw_candidates:
            specs = dict(c.get("specs", {}))
            if "warranty_months" not in specs:
                specs["warranty_months"] = 12

            price = float(c.get("price", 0.0))
            orig_price = float(c.get("original_price", price))
            discount = float(c.get("discount_percentage", 0.0))
            if discount == 0.0 and orig_price > price:
                discount = round(((orig_price - price) / orig_price) * 100, 1)

            images = c.get("images", [])
            primary_img = c.get("image") or (images[0] if images else "")

            # Ensure all 28 canonical fields + backwards compatibility fields
            item = {
                "product_id": c.get("product_id") or f"PROD-{abs(hash(str(c.get('raw_name') or c.get('title')))) % 1000000:06d}",
                "product_name": c.get("raw_name") or c.get("title"),
                "name": c.get("raw_name") or c.get("title"),
                "category": c.get("category", "electronics"),
                "subcategory": c.get("subcategory", "general"),
                "brand": c.get("brand"),
                "model": c.get("model"),
                "variant": c.get("variant", ""),
                "variants": c.get("variants", []),
                "sku": c.get("sku", ""),
                "gtin_upc_ean": c.get("gtin_upc_ean", ""),
                "product_description": c.get("snippet", ""),
                "description": c.get("snippet", ""),
                "images": images if images else ([primary_img] if primary_img else []),
                "videos": c.get("videos", []),
                "specifications": specs,
                "current_price": price,
                "price": price,
                "mrp": orig_price,
                "original_price": orig_price,
                "discount_percentage": discount,
                "currency": "INR",
                "rating": float(c.get("rating", 4.5)),
                "review_count": int(c.get("review_count", 100)),
                "seller": c.get("source"),
                "seller_rating": float(c.get("seller_rating", 4.5)),
                "availability": c.get("availability", "In Stock"),
                "delivery_info": c.get("delivery_info", c.get("shipping", "Free Standard Delivery")),
                "shipping": c.get("shipping", "Free Standard Delivery"),
                "warranty": c.get("warranty", f"{specs.get('warranty_months', 12)} Months Official Warranty"),
                "return_policy": c.get("return_policy", "7 Days Service Center Replacement"),
                "source_website": c.get("source", "Amazon"),
                "source": c.get("source"),
                "product_url": c.get("product_url", c.get("url")),
                "url": c.get("url", c.get("product_url")),
                "affiliate_url": c.get("affiliate_url", ""),
                "last_updated": now_iso,
                "last_checked_timestamp": now_iso,
                "image_url": primary_img,
                "image": primary_img,
                "sellers": c.get("sellers", []),
                "lowest_price": c.get("lowest_price", price),
                "lowest_price_seller": c.get("lowest_price_seller", c.get("source")),
                "lowest_price_url": c.get("lowest_price_url", c.get("url"))
            }
            extracted.append(item)

        if on_progress:
            await on_progress(self.name, "progress", f"Extracted structured 28-field specifications across {len(extracted)} candidate products.", None)

        return {"extracted_products": extracted}
