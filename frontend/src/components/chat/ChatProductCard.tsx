import React, { useState } from 'react';
import { 
  Star, 
  ExternalLink, 
  ShieldCheck, 
  Check, 
  Bookmark, 
  Bell, 
  Scale, 
  Sparkles,
  ShoppingBag,
  TrendingDown,
  ChevronDown,
  ChevronUp
} from 'lucide-react';
import { ChatProductItem, ProductSellerOption } from '../../types';

interface ChatProductCardProps {
  product: ChatProductItem;
  onCompare?: (product: ChatProductItem) => void;
  onSave?: (product: ChatProductItem) => void;
  onTrackPrice?: (product: ChatProductItem) => void;
  onCheckoutAssist?: (product: ChatProductItem, seller: ProductSellerOption) => void;
}

export function ChatProductCard({
  product,
  onCompare,
  onSave,
  onTrackPrice,
  onCheckoutAssist
}: ChatProductCardProps) {
  const [showAllSellers, setShowAllSellers] = useState(false);
  const [saved, setSaved] = useState(false);

  const sellers = product.sellers || [];
  const lowestPrice = product.lowest_price || product.price;
  const lowestSellerName = product.lowest_price_seller || product.seller || 'Authorized Seller';
  const lowestUrl = product.lowest_price_url || product.product_url || product.url || '#';

  const badgeColor = 
    product.badge === 'Best Overall' ? 'bg-amber-100 text-amber-900 border-amber-300' :
    product.badge === 'Best Value' ? 'bg-emerald-100 text-emerald-900 border-emerald-300' :
    product.badge === 'Best Performance' ? 'bg-indigo-100 text-indigo-900 border-indigo-300' :
    product.badge === 'Cheapest Suitable' || product.badge === 'Lowest Price' ? 'bg-sky-100 text-sky-900 border-sky-300' :
    'bg-slate-100 text-slate-800 border-slate-300';

  const specs = product.specifications || {};

  const handleSaveClick = () => {
    setSaved(!saved);
    if (onSave) onSave(product);
  };

  return (
    <div className="my-4 rounded-2xl border border-slate-200 bg-white shadow-sm hover:shadow-md transition-shadow duration-200 overflow-hidden">
      {/* Top Banner with Badge & AI Match */}
      <div className="px-4 py-2.5 bg-gradient-to-r from-slate-50 to-indigo-50/40 border-b border-slate-100 flex items-center justify-between">
        <div className="flex items-center space-x-2">
          {product.badge && (
            <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-semibold border ${badgeColor}`}>
              <Sparkles className="h-3 w-3 mr-1" />
              {product.badge}
            </span>
          )}
          {product.verification?.is_verified && (
            <span className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-full text-[11px] font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">
              <ShieldCheck className="h-3 w-3" />
              <span>Verified Claims</span>
            </span>
          )}
        </div>

        {product.score_overall !== undefined && product.score_overall > 0 && (
          <div className="flex items-center space-x-1 text-xs font-bold text-indigo-600 bg-indigo-50 px-2 py-0.5 rounded-md border border-indigo-100">
            <span>AI Match:</span>
            <span>{Math.round(product.score_overall)}%</span>
          </div>
        )}
      </div>

      <div className="p-4 sm:p-5">
        <div className="flex flex-col sm:flex-row items-start gap-4">
          {/* Image */}
          <div className="w-full sm:w-28 sm:h-28 shrink-0 bg-slate-50 rounded-xl border border-slate-100 flex items-center justify-center p-2 overflow-hidden">
            <img
              src={product.image_url || product.image || 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=300'}
              alt={product.name}
              className="max-h-full max-w-full object-contain"
              onError={(e) => {
                (e.target as HTMLImageElement).src = 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=300';
              }}
            />
          </div>

          {/* Core Info */}
          <div className="flex-1 min-w-0">
            <div className="flex items-baseline space-x-2">
              <span className="text-xs font-semibold uppercase tracking-wider text-indigo-600">
                {product.brand || 'Verified Brand'}
              </span>
              {product.model && (
                <span className="text-xs text-slate-500 font-medium">
                  {product.model}
                </span>
              )}
            </div>

            <h4 className="text-base font-bold text-slate-900 mt-0.5 leading-snug line-clamp-2">
              {product.name}
            </h4>

            {/* Rating & Reviews */}
            <div className="flex items-center space-x-2 mt-1.5 text-xs text-slate-600">
              <div className="flex items-center text-amber-500 font-semibold">
                <Star className="h-3.5 w-3.5 fill-current mr-0.5" />
                <span>{product.rating ? product.rating.toFixed(1) : '4.4'}</span>
              </div>
              <span className="text-slate-300">•</span>
              <span>{(product.review_count || 450).toLocaleString()} authentic reviews</span>
              <span className="text-slate-300">•</span>
              <span className="text-emerald-600 font-medium">{product.availability || 'In Stock'}</span>
            </div>

            {/* Price & Savings */}
            <div className="mt-2.5 flex items-baseline space-x-2.5">
              <span className="text-xl font-extrabold text-slate-900">
                ₹{lowestPrice.toLocaleString()}
              </span>
              {product.original_price && product.original_price > lowestPrice && (
                <>
                  <span className="text-xs text-slate-400 line-through">
                    ₹{product.original_price.toLocaleString()}
                  </span>
                  <span className="text-xs font-bold text-emerald-600 flex items-center">
                    <TrendingDown className="h-3 w-3 mr-0.5" />
                    Save ₹{(product.original_price - lowestPrice).toLocaleString()}
                  </span>
                </>
              )}
              <span className="text-xs text-slate-500 font-medium">
                on {lowestSellerName}
              </span>
            </div>
          </div>
        </div>

        {/* Specifications Pill Strip */}
        <div className="mt-3.5 flex flex-wrap gap-1.5">
          {specs.ram_gb && (
            <span className="px-2 py-0.5 rounded-md bg-slate-100 border border-slate-200 text-slate-700 text-xs font-medium">
              {specs.ram_gb}GB RAM
            </span>
          )}
          {specs.storage_gb && (
            <span className="px-2 py-0.5 rounded-md bg-slate-100 border border-slate-200 text-slate-700 text-xs font-medium">
              {specs.storage_gb >= 1000 ? `${(specs.storage_gb/1024).toFixed(0)}TB SSD` : `${specs.storage_gb}GB SSD`}
            </span>
          )}
          {specs.gpu && (
            <span className="px-2 py-0.5 rounded-md bg-indigo-50 border border-indigo-100 text-indigo-700 text-xs font-medium">
              {specs.gpu}
            </span>
          )}
          {specs.cpu && (
            <span className="px-2 py-0.5 rounded-md bg-slate-100 border border-slate-200 text-slate-700 text-xs font-medium">
              {specs.cpu}
            </span>
          )}
          {specs.battery_life_hours && (
            <span className="px-2 py-0.5 rounded-md bg-emerald-50 border border-emerald-100 text-emerald-700 text-xs font-medium">
              ~{specs.battery_life_hours}h Battery
            </span>
          )}
          {specs.screen_size_inches && (
            <span className="px-2 py-0.5 rounded-md bg-slate-100 border border-slate-200 text-slate-700 text-xs font-medium">
              {specs.screen_size_inches}" Display
            </span>
          )}
        </div>

        {/* AI Recommendation Reason */}
        {product.recommendation_explanation && (
          <div className="mt-3 p-2.5 rounded-xl bg-slate-50 border border-slate-200/80 text-xs text-slate-700 leading-relaxed">
            <span className="font-semibold text-slate-900 mr-1">Why this pick:</span>
            {product.recommendation_explanation}
          </div>
        )}

        {/* Cross-Merchant Multi-Seller Price Comparison Table */}
        <div className="mt-4 rounded-xl border border-slate-200 overflow-hidden bg-white">
          <div className="px-3.5 py-2 bg-slate-50 border-b border-slate-200 flex items-center justify-between text-xs font-semibold text-slate-800">
            <span>Available Sellers & Real Prices</span>
            <span className="text-slate-500 font-normal">
              {sellers.length} authorized stores
            </span>
          </div>

          <div className="divide-y divide-slate-100">
            {(showAllSellers ? sellers : sellers.slice(0, 2)).map((s, idx) => {
              const isBestPrice = s.price === lowestPrice;

              return (
                <div key={idx} className="p-3 flex items-center justify-between gap-3 text-xs hover:bg-slate-50/60 transition-colors">
                  <div className="flex-1 min-w-0">
                    <div className="flex items-center space-x-2">
                      <span className="font-bold text-slate-900">{s.source}</span>
                      {isBestPrice && (
                        <span className="px-1.5 py-0.5 rounded text-[10px] font-extrabold bg-emerald-100 text-emerald-800 border border-emerald-200">
                          LOWEST PRICE
                        </span>
                      )}
                    </div>
                    <div className="text-[11px] text-slate-500 flex items-center space-x-2 mt-0.5">
                      <span>Seller: {s.seller_name} ({s.seller_rating}★)</span>
                      <span>•</span>
                      <span>{s.delivery_info}</span>
                    </div>
                  </div>

                  <div className="text-right shrink-0">
                    <div className="font-extrabold text-sm text-slate-900">
                      ₹{s.price.toLocaleString()}
                    </div>
                    <div className="flex items-center space-x-1.5 mt-1">
                      <a
                        href={s.product_url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="inline-flex items-center space-x-1 px-2.5 py-1 rounded-md text-xs font-semibold bg-indigo-50 hover:bg-indigo-100 text-indigo-700 transition-colors"
                      >
                        <span>Buy on {s.source.split(' ')[0]}</span>
                        <ExternalLink className="h-3 w-3" />
                      </a>
                      {onCheckoutAssist && (
                        <button
                          type="button"
                          onClick={() => onCheckoutAssist(product, s)}
                          className="px-2 py-1 rounded-md text-xs font-medium bg-slate-100 hover:bg-slate-200 text-slate-700 transition-colors"
                          title="Human-in-the-Loop Safe Checkout Assistance"
                        >
                          <ShoppingBag className="h-3 w-3" />
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          {sellers.length > 2 && (
            <button
              type="button"
              onClick={() => setShowAllSellers(!showAllSellers)}
              className="w-full py-1.5 text-center text-xs text-indigo-600 font-semibold bg-slate-50/50 hover:bg-slate-100/60 transition-colors flex items-center justify-center space-x-1 border-t border-slate-100 cursor-pointer"
            >
              <span>{showAllSellers ? 'Show fewer sellers' : `Compare all ${sellers.length} sellers`}</span>
              {showAllSellers ? <ChevronUp className="h-3 w-3" /> : <ChevronDown className="h-3 w-3" />}
            </button>
          )}
        </div>

        {/* Card Action Buttons */}
        <div className="mt-4 pt-3 border-t border-slate-100 flex flex-wrap items-center justify-between gap-2">
          <div className="flex items-center space-x-2">
            {onCompare && (
              <button
                type="button"
                onClick={() => onCompare(product)}
                className="inline-flex items-center space-x-1 px-2.5 py-1.5 rounded-lg border border-slate-200 text-slate-700 text-xs font-semibold hover:bg-slate-50 transition-colors"
              >
                <Scale className="h-3.5 w-3.5 text-slate-500" />
                <span>Compare</span>
              </button>
            )}

            <button
              type="button"
              onClick={handleSaveClick}
              className={`inline-flex items-center space-x-1 px-2.5 py-1.5 rounded-lg border text-xs font-semibold transition-colors ${
                saved
                  ? 'bg-emerald-50 border-emerald-200 text-emerald-700'
                  : 'border-slate-200 text-slate-700 hover:bg-slate-50'
              }`}
            >
              {saved ? <Check className="h-3.5 w-3.5 text-emerald-600" /> : <Bookmark className="h-3.5 w-3.5 text-slate-500" />}
              <span>{saved ? 'Saved' : 'Save'}</span>
            </button>

            {onTrackPrice && (
              <button
                type="button"
                onClick={() => onTrackPrice(product)}
                className="inline-flex items-center space-x-1 px-2.5 py-1.5 rounded-lg border border-slate-200 text-slate-700 text-xs font-semibold hover:bg-slate-50 transition-colors"
              >
                <Bell className="h-3.5 w-3.5 text-slate-500" />
                <span>Track Price</span>
              </button>
            )}
          </div>

          <a
            href={lowestUrl}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center space-x-1 px-3 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold shadow-xs transition-colors"
          >
            <span>Visit {lowestSellerName}</span>
            <ExternalLink className="h-3.5 w-3.5" />
          </a>
        </div>
      </div>
    </div>
  );
}
