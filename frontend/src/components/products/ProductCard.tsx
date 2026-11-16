import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { 
  Star, 
  ShieldCheck, 
  Bookmark, 
  Bell, 
  Layers, 
  ShoppingCart, 
  CheckCircle2, 
  Cpu, 
  HardDrive, 
  Battery, 
  Zap,
  TrendingDown
} from 'lucide-react';
import { RecommendationItem } from '../../types';
import { api } from '../../services/api';
import { HumanApprovalModal } from '../checkout/HumanApprovalModal';

interface ProductCardProps {
  product: RecommendationItem;
  onCompareToggle?: (productId: string) => void;
  isCompared?: boolean;
}

export const ProductCard: React.FC<ProductCardProps> = ({
  product,
  onCompareToggle,
  isCompared
}) => {
  const [saved, setSaved] = useState(false);
  const [showCheckoutModal, setShowCheckoutModal] = useState(false);
  const [savingLoading, setSavingLoading] = useState(false);

  const handleSave = async () => {
    setSavingLoading(true);
    try {
      if (saved) {
        await api.removeSavedProduct(product.id || product.product_url || "");
        setSaved(false);
      } else {
        await api.saveProduct(product.id || product.product_url || "");
        setSaved(true);
      }
    } catch {
      // optimistic toggle
      setSaved(!saved);
    } finally {
      setSavingLoading(false);
    }
  };

  const badgeColor = {
    'Best Overall': 'bg-amber-100 text-amber-800 border-amber-300',
    'Best Value': 'bg-emerald-100 text-emerald-800 border-emerald-300',
    'Best Performance': 'bg-indigo-100 text-indigo-800 border-indigo-300',
    'Cheapest Suitable': 'bg-blue-100 text-blue-800 border-blue-300',
  }[product.badge || ''] || 'bg-slate-100 text-slate-700 border-slate-200';

  return (
    <>
      <div className="bg-white rounded-2xl border border-slate-200 hover:border-indigo-300 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col overflow-hidden group">
        {/* Top Image & Badges */}
        <div className="relative h-52 bg-slate-100 overflow-hidden">
          <img
            src={product.image_url || "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80"}
            alt={product.name}
            className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
          />
          
          {/* Badge & Match Score */}
          <div className="absolute top-3 left-3 flex flex-wrap gap-1.5 items-center">
            {product.badge && (
              <span className={`px-2.5 py-1 text-xs font-bold rounded-lg border shadow-sm ${badgeColor}`}>
                {product.badge}
              </span>
            )}
            <span className="px-2.5 py-1 text-xs font-bold rounded-lg bg-indigo-600 text-white shadow-sm flex items-center gap-1">
              <Zap className="w-3 h-3 fill-current" />
              {product.score_overall}% AI Match
            </span>
          </div>

          {/* Quick Save Action */}
          <button
            onClick={handleSave}
            disabled={savingLoading}
            className={`absolute top-3 right-3 p-2 rounded-xl backdrop-blur-md shadow-sm transition-colors ${
              saved ? 'bg-amber-500 text-white' : 'bg-white/80 hover:bg-white text-slate-600 hover:text-amber-500'
            }`}
            title="Save for Later"
          >
            <Bookmark className={`w-4 h-4 ${saved ? 'fill-current' : ''}`} />
          </button>
        </div>

        {/* Card Body */}
        <div className="p-5 flex-1 flex flex-col justify-between">
          <div>
            {/* Brand & Seller */}
            <div className="flex items-center justify-between text-xs text-slate-500 mb-1.5">
              <span className="font-semibold uppercase tracking-wider text-indigo-600">{product.brand || 'Verified Brand'}</span>
              <span className="truncate max-w-[150px]">{product.seller || 'Authorized Partner'}</span>
            </div>

            {/* Product Title */}
            <h3 className="font-bold text-slate-900 text-base leading-snug line-clamp-2 mb-2 group-hover:text-indigo-600 transition-colors">
              {product.name}
            </h3>

            {/* Price & Budget Status */}
            <div className="flex items-baseline gap-2 mb-3">
              <span className="text-2xl font-extrabold text-slate-900">
                ₹{product.price.toLocaleString()}
              </span>
              {product.original_price && product.original_price > product.price && (
                <span className="text-sm text-slate-400 line-through">
                  ₹{product.original_price.toLocaleString()}
                </span>
              )}
              <span className={`text-[11px] font-semibold px-2 py-0.5 rounded-full ${
                product.budget_status === 'Within Budget'
                  ? 'bg-emerald-50 text-emerald-700'
                  : 'bg-amber-50 text-amber-700'
              }`}>
                {product.budget_status}
              </span>
            </div>

            {/* Key Specs Pills */}
            <div className="grid grid-cols-2 gap-2 mb-3.5 text-xs text-slate-600">
              <div className="flex items-center gap-1.5 bg-slate-50 p-1.5 rounded-lg border border-slate-100">
                <Cpu className="w-3.5 h-3.5 text-indigo-500 shrink-0" />
                <span className="truncate font-medium">{product.specifications?.ram_gb || 32}GB DDR5 RAM</span>
              </div>
              <div className="flex items-center gap-1.5 bg-slate-50 p-1.5 rounded-lg border border-slate-100">
                <HardDrive className="w-3.5 h-3.5 text-indigo-500 shrink-0" />
                <span className="truncate font-medium">{product.specifications?.storage_gb || 1024}GB NVMe SSD</span>
              </div>
              <div className="flex items-center gap-1.5 bg-slate-50 p-1.5 rounded-lg border border-slate-100">
                <Zap className="w-3.5 h-3.5 text-amber-500 shrink-0" />
                <span className="truncate font-medium">{product.specifications?.gpu || 'RTX 4060 GPU'}</span>
              </div>
              <div className="flex items-center gap-1.5 bg-slate-50 p-1.5 rounded-lg border border-slate-100">
                <Battery className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                <span className="truncate font-medium">~{product.specifications?.battery_life_hours || 8}h Battery</span>
              </div>
            </div>

            {/* AI Recommendation Reason */}
            {product.recommendation_explanation && (
              <div className="bg-indigo-50/60 border border-indigo-100 rounded-xl p-3 mb-4 text-xs text-indigo-950 leading-relaxed">
                <span className="font-bold text-indigo-700 block mb-0.5 flex items-center gap-1">
                  <CheckCircle2 className="w-3.5 h-3.5 text-indigo-600" />
                  Why AI Recommends This:
                </span>
                <p className="line-clamp-2">{product.recommendation_explanation}</p>
              </div>
            )}
          </div>

          {/* Action Buttons */}
          <div className="pt-3 border-t border-slate-100 flex items-center gap-2">
            <button
              onClick={() => onCompareToggle && onCompareToggle(product.id)}
              className={`p-2.5 rounded-xl border text-xs font-semibold flex items-center justify-center gap-1 transition-colors ${
                isCompared
                  ? 'bg-indigo-50 border-indigo-300 text-indigo-700'
                  : 'border-slate-200 text-slate-700 hover:bg-slate-50'
              }`}
              title="Add to Comparison"
            >
              <Layers className="w-4 h-4" />
              <span className="hidden sm:inline">Compare</span>
            </button>

            <Link
              to={`/products/${product.id || 'prod_lenovo_legion_slim5'}`}
              className="flex-1 py-2.5 px-3 bg-slate-100 hover:bg-slate-200 text-slate-800 rounded-xl text-xs font-semibold text-center transition-colors"
            >
              View Details
            </Link>

            <button
              onClick={() => setShowCheckoutModal(true)}
              className="py-2.5 px-3.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-semibold shadow-sm shadow-indigo-100 flex items-center justify-center gap-1.5 transition-colors"
            >
              <ShoppingCart className="w-3.5 h-3.5" />
              Buy
            </button>
          </div>
        </div>
      </div>

      {/* Human In The Loop Checkout Gate */}
      <HumanApprovalModal
        isOpen={showCheckoutModal}
        onClose={() => setShowCheckoutModal(false)}
        product={{
          id: product.id,
          name: product.name,
          brand: product.brand,
          price: product.price,
          seller: product.seller,
          image_url: product.image_url
        }}
      />
    </>
  );
};
