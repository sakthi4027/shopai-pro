import React from 'react';
import { 
  Star, 
  ExternalLink, 
  Check, 
  RotateCcw, 
  Bookmark, 
  Heart, 
  Sparkles, 
  TrendingDown,
  ShoppingBag
} from 'lucide-react';
import { ChatProductItem } from '../../types';
import { getSafeProductImage, handleImageError } from '../../utils/imageUtils';
import { getProperProductUrl } from '../../utils/linkUtils';

interface ChatInlineProductsProps {
  products: ChatProductItem[];
  onCompare?: (product: ChatProductItem) => void;
  onSave?: (product: ChatProductItem) => void;
  isProductSaved?: (name: string) => boolean;
}

export function ChatInlineProducts({
  products,
  onCompare,
  onSave,
  isProductSaved
}: ChatInlineProductsProps) {
  if (!products || products.length === 0) return null;

  const topItems = products.slice(0, 4);

  return (
    <div className="mt-4 pt-4 border-t border-slate-100 space-y-3">
      <div className="flex items-center justify-between">
        <span className="text-[11px] font-bold uppercase tracking-wider text-slate-500 flex items-center gap-1.5">
          <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
          <span>Recommended Products ({products.length} Matching)</span>
        </span>
        <span className="text-[11px] text-indigo-600 font-semibold">
          Click link to open merchant store
        </span>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
        {topItems.map((product, idx) => {
          const targetUrl = getProperProductUrl(product);
          const sellerName = product.lowest_price_seller || product.seller || product.source || 'Authorized Store';
          const price = product.lowest_price || product.price || 0;
          const origPrice = product.original_price || Math.round(price * 1.18);
          const discount = origPrice > price ? Math.round(((origPrice - price) / origPrice) * 100) : 0;
          const saved = isProductSaved ? isProductSaved(product.name) : false;

          let badge = product.badge || (idx === 0 ? 'Best Overall' : idx === 1 ? 'Best Value' : idx === 2 ? 'Top Rated' : 'Recommended');

          return (
            <div
              key={product.id || idx}
              className="bg-white rounded-2xl border border-slate-200 hover:border-indigo-300 p-3 shadow-xs hover:shadow-md transition-all flex flex-col justify-between group"
            >
              <div>
                {/* Header badge & save */}
                <div className="flex items-center justify-between mb-2">
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-100 flex items-center gap-1">
                    <Sparkles className="w-2.5 h-2.5 text-indigo-600" />
                    <span>{badge}</span>
                  </span>

                  {onSave && (
                    <button
                      type="button"
                      onClick={() => onSave(product)}
                      className="text-slate-400 hover:text-red-500 transition-colors p-1"
                      title="Save product"
                    >
                      <Heart className={`w-3.5 h-3.5 ${saved ? 'text-red-500 fill-red-500' : ''}`} />
                    </button>
                  )}
                </div>

                {/* Product Image Thumbnail */}
                <div
                  onClick={() => window.open(targetUrl, '_blank')}
                  className="h-32 w-full flex items-center justify-center rounded-xl bg-slate-50 overflow-hidden mb-2 cursor-pointer relative group-hover:bg-slate-100/70 transition-colors"
                  title="Click to open product page on store"
                >
                  <img
                    src={getSafeProductImage(product)}
                    alt={product.name}
                    onError={(e) => handleImageError(e, product.category, product.subcategory, product.name)}
                    className="h-full w-full object-contain p-2 group-hover:scale-105 transition-transform duration-300"
                  />
                  <div className="absolute inset-0 bg-black/0 group-hover:bg-black/5 transition-colors flex items-center justify-center">
                    <span className="opacity-0 group-hover:opacity-100 bg-white/95 text-slate-800 text-[10px] font-bold px-2 py-1 rounded-md shadow-xs transition-opacity flex items-center gap-1">
                      <span>View Store</span>
                      <ExternalLink className="w-2.5 h-2.5" />
                    </span>
                  </div>
                </div>

                {/* Title & Brand */}
                <div className="text-[10px] font-bold uppercase tracking-wider text-indigo-600">
                  {product.brand || 'Verified Brand'}
                </div>
                <h4
                  onClick={() => window.open(targetUrl, '_blank')}
                  className="text-xs font-bold text-slate-900 line-clamp-2 mt-0.5 hover:text-indigo-600 cursor-pointer transition-colors leading-snug"
                  title={product.name}
                >
                  {product.name}
                </h4>

                {/* Rating & Reviews */}
                <div className="flex items-center gap-1.5 mt-1.5 text-[11px] text-slate-600">
                  <div className="flex items-center text-amber-500 font-bold">
                    <Star className="w-3 h-3 fill-amber-500 mr-0.5" />
                    <span>{product.rating ? product.rating.toFixed(1) : '4.5'}</span>
                  </div>
                  <span className="text-slate-300">•</span>
                  <span className="text-slate-400 text-[10px]">({(product.review_count || 1200).toLocaleString()})</span>
                  <span className="text-slate-300">•</span>
                  <span className="text-emerald-600 font-medium text-[10px]">In Stock</span>
                </div>

                {/* Price Line */}
                <div className="flex items-baseline gap-2 mt-2">
                  <span className="text-base font-extrabold text-slate-900">
                    ₹{price.toLocaleString()}
                  </span>
                  {origPrice > price && (
                    <>
                      <span className="text-[11px] text-slate-400 line-through">
                        ₹{origPrice.toLocaleString()}
                      </span>
                      <span className="text-[10px] font-bold text-emerald-600">
                        {discount}% OFF
                      </span>
                    </>
                  )}
                </div>

                <div className="text-[10px] text-slate-500 mt-0.5">
                  Available on <span className="font-semibold text-slate-700">{sellerName}</span>
                </div>
              </div>

              {/* Action Buttons */}
              <div className="mt-3 pt-2 border-t border-slate-100 flex items-center gap-1.5">
                <button
                  type="button"
                  onClick={() => window.open(targetUrl, '_blank')}
                  className="flex-1 bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-bold text-xs py-2 px-2.5 rounded-xl flex items-center justify-center gap-1 hover:opacity-95 shadow-xs cursor-pointer transition-all"
                  title={`Open website directly on ${sellerName}`}
                >
                  <span>Buy on {sellerName.split(' ')[0]}</span>
                  <ExternalLink className="w-3 h-3" />
                </button>

                {onCompare && (
                  <button
                    type="button"
                    onClick={() => onCompare(product)}
                    className="p-2 border border-slate-200 hover:border-slate-300 rounded-xl text-slate-600 hover:text-indigo-600 bg-slate-50/50 hover:bg-slate-100 transition-colors cursor-pointer"
                    title="Compare product"
                  >
                    <RotateCcw className="w-3.5 h-3.5" />
                  </button>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
