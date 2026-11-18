export interface User {
  id: string;
  email: string;
  full_name?: string;
  role: string;
  is_active: boolean;
  created_at: string;
}

export interface UserPreferences {
  id?: string;
  user_id?: string;
  preferred_brands: string[];
  budget_max?: number;
  preferred_ram?: string;
  preferred_storage?: string;
  avoid_refurbished: boolean;
  excluded_keywords: string[];
  currency: string;
}

export interface ProductSpec {
  ram_gb?: number;
  storage_gb?: number;
  cpu?: string;
  gpu?: string;
  screen_size_inches?: number;
  battery_life_hours?: number;
  os?: string;
  weight_kg?: number;
  warranty_months?: number;
  raw_specs?: Record<string, any>;
}

export interface SellerPrice {
  id: string;
  seller_name: string;
  platform: string;
  seller_rating: number;
  current_price: number;
  original_price?: number;
  discount_percentage: number;
  currency: string;
  availability: string;
  shipping_cost: number;
  estimated_delivery: string;
}

export interface Product {
  id: string;
  name: string;
  brand?: string;
  model?: string;
  category: string;
  description?: string;
  main_image?: string;
  product_url?: string;
  source: string;
  rating: number;
  review_count: number;
  trust_score: number;
  trust_warning?: string;
  is_verified: boolean;
  best_price?: number;
  currency: string;
  availability: string;
  specs?: ProductSpec;
  last_checked?: string;
}

export interface RecommendationItem {
  id: string;
  name: string;
  brand?: string;
  price: number;
  original_price?: number;
  score_overall: number;
  score_match: number;
  score_price: number;
  score_performance: number;
  score_reviews: number;
  badge?: "Best Overall" | "Best Value" | "Best Performance" | "Cheapest Suitable" | string;
  budget_status: "Within Budget" | "Near Budget" | "Over Budget";
  budget_note?: string;
  recommendation_explanation: string;
  specifications: ProductSpec;
  image_url?: string;
  seller?: string;
  warranty?: string;
  product_url?: string;
  trust_score?: number;
}

export interface ShoppingPlan {
  category: string;
  budget_max?: number;
  required_features: string[];
  preferred_features: string[];
  optional_features: string[];
  excluded_features: string[];
  preferred_brands: string[];
  original_query: string;
}

export interface SearchWorkflowResult {
  session_id: string;
  request_id: string;
  query: string;
  plan: ShoppingPlan;
  ranked_products: RecommendationItem[];
  flagged_products: any[];
  comparison_matrix: Array<{ feature: string; key?: string; values: Record<string, string> }>;
  comparison_highlights: Record<string, string>;
  rag_insight?: {
    answer: string;
    citations: Array<{ title: string; source: string; score: number }>;
    confidence: number;
  };
}

export interface AgentEvent {
  session_id: string;
  agent_name: string;
  status: "started" | "progress" | "completed" | "warning" | "error";
  message: string;
  step_index: number;
  timestamp: string;
  payload?: any;
}

export interface ReviewAnalysis {
  product_id: string;
  sentiment_positive_pct: number;
  sentiment_neutral_pct: number;
  sentiment_negative_pct: number;
  positive_themes: string[];
  negative_themes: string[];
  common_complaints: string[];
  important_warnings: string[];
  aspect_scores: Record<string, number>;
  analyzed_review_count: number;
  last_analyzed: string;
}

export interface AgentStep {
  agent: string;
  status: string;
  message: string;
  timestamp: string;
}

export interface SourceStatus {
  name: string;
  type: string;
  status: string;
  products_count?: number;
  reason?: string;
}

export interface ProductSellerOption {
  source: string;
  seller_name: string;
  seller_rating: number;
  price: number;
  original_price: number;
  discount_percent: number;
  availability: string;
  delivery_info: string;
  product_url: string;
  condition: string;
}

export interface ProductVariant {
  name: string;
  price: number;
  mrp?: number;
  sku: string;
}

export interface ChatProductItem {
  id?: string;
  product_id?: string;
  name: string;
  product_name?: string;
  brand?: string;
  model?: string;
  category: string;
  subcategory?: string;
  variant?: string;
  variants?: ProductVariant[];
  sku?: string;
  gtin_upc_ean?: string;
  price: number;
  current_price?: number;
  mrp?: number;
  original_price?: number;
  discount_percentage?: number;
  currency?: string;
  rating: number;
  review_count: number;
  availability: string;
  shipping?: string;
  delivery_info?: string;
  warranty?: string;
  return_policy?: string;
  source_website?: string;
  product_url?: string;
  url?: string;
  affiliate_url?: string;
  image_url?: string;
  image?: string;
  images?: string[];
  source?: string;
  seller?: string;
  seller_rating?: number;
  badge?: string;
  score_overall?: number;
  score_match?: number;
  score_price?: number;
  score_performance?: number;
  score_reviews?: number;
  recommendation_explanation?: string;
  budget_status?: string;
  budget_note?: string;
  specifications?: ProductSpec | Record<string, any>;
  sellers?: ProductSellerOption[];
  lowest_price?: number;
  lowest_price_seller?: string;
  lowest_price_url?: string;
  verification?: {
    is_verified: boolean;
    claims_checked: string[];
    warnings: string[];
    confidence_score: number;
    verification_badge: string;
  };
}

export interface ChatMessage {
  id: string;
  conversation_id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  request_id?: string;
  agent_steps?: AgentStep[];
  sources_status?: SourceStatus[];
  products_payload?: ChatProductItem[];
  total_products_found?: number;
  comparison_payload?: {
    matrix?: any[];
    highlights?: Record<string, any>;
  };
  follow_up_suggestions?: string[];
  created_at: string;
}

export interface ConversationSummary {
  id: string;
  title: string;
  search_mode: string;
  created_at: string;
  updated_at: string;
  message_count: number;
}

export interface ConversationDetail {
  id: string;
  title: string;
  search_mode: string;
  active_constraints: Record<string, any>;
  created_at: string;
  updated_at: string;
  messages: ChatMessage[];
}

export interface CheckoutManifest {
  confirmation_required: boolean;
  notice: string;
  product_name: string;
  price: number;
  seller_name: string;
  shipping_cost: number;
  total_cost: number;
  currency: string;
  checkout_url: string;
  security_guarantee: string;
}
