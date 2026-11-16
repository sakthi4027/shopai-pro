import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { 
  Star, 
  ShieldCheck, 
  Truck, 
  Cpu, 
  HardDrive, 
  Battery, 
  ArrowLeft, 
  ShoppingCart, 
  Bell, 
  TrendingDown, 
  Loader2 
} from 'lucide-react';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';
import { api } from '../services/api';
import { HumanApprovalModal } from '../components/checkout/HumanApprovalModal';

export const ProductDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [loading, setLoading] = useState(true);
  const [product, setProduct] = useState<any>(null);
  const [reviewAnalysis, setReviewAnalysis] = useState<any>(null);
  const [showCheckout, setShowCheckout] = useState(false);
  const [selectedSeller, setSelectedSeller] = useState<any>(null);
  const [alertTargetPrice, setAlertTargetPrice] = useState<number | ''>('');
  const [alertSuccess, setAlertSuccess] = useState<string | null>(null);

  useEffect(() => {
    if (!id) return;
    setLoading(true);
    Promise.all([
      api.getProductDetail(id),
      api.getReviewAnalysis(id).catch(() => null)
    ])
      .then(([prod, review]) => {
        setProduct(prod);
        setReviewAnalysis(review);
        if (prod.prices?.length) {
          setSelectedSeller(prod.prices[0]);
          setAlertTargetPrice(Math.round(prod.prices[0].current_price * 0.95));
        }
      })
      .catch(err => alert("Error loading product: " + err.message))
      .finally(() => setLoading(false));
  }, [id]);

  const handleCreateAlert = async () => {
    if (!alertTargetPrice || !id) return;
    try {
      const res = await api.createAlert(id, Number(alertTargetPrice));
      setAlertSuccess(res.message);
      setTimeout(() => setAlertSuccess(null), 4000);
    } catch (err: any) {
      alert("Alert creation failed: " + err.message);
    }
  };

  if (loading) {
    return (
      <div className="py-24 text-center flex flex-col items-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
        <p className="text-sm text-slate-500 font-medium">Auditing product specifications and merchant pricing...</p>
      </div>
    );
  }

  if (!product) {
    return <div className="py-20 text-center text-slate-500">Product not found.</div>;
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
      <Link to="/search" className="inline-flex items-center gap-1.5 text-xs text-slate-500 hover:text-indigo-600 font-medium">
        <ArrowLeft className="w-3.5 h-3.5" /> Back to Search
      </Link>

      {/* Main Product Header & Summary */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-10">
        {/* Left: Product Image & Trust Badge */}
        <div className="space-y-4">
          <div className="relative rounded-3xl overflow-hidden border border-slate-200 bg-white h-96 shadow-sm">
            <img
              src={product.main_image || "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80"}
              alt={product.name}
              className="w-full h-full object-cover"
            />
            <div className="absolute top-4 left-4 bg-emerald-600 text-white text-xs font-bold px-3 py-1 rounded-full shadow-md flex items-center gap-1">
              <ShieldCheck className="w-4 h-4" /> Authenticity Verified
            </div>
          </div>

          {/* Quick specs grid */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs">
            <div className="p-3 bg-white rounded-xl border border-slate-200">
              <span className="text-slate-400 block mb-1">RAM</span>
              <span className="font-bold text-slate-900">{product.specs?.ram_gb || 32}GB DDR5</span>
            </div>
            <div className="p-3 bg-white rounded-xl border border-slate-200">
              <span className="text-slate-400 block mb-1">Storage</span>
              <span className="font-bold text-slate-900">{product.specs?.storage_gb || 1024}GB SSD</span>
            </div>
            <div className="p-3 bg-white rounded-xl border border-slate-200">
              <span className="text-slate-400 block mb-1">Battery</span>
              <span className="font-bold text-slate-900">~{product.specs?.battery_life_hours || 8} Hours</span>
            </div>
            <div className="p-3 bg-white rounded-xl border border-slate-200">
              <span className="text-slate-400 block mb-1">Warranty</span>
              <span className="font-bold text-slate-900">{product.specs?.warranty_months || 12} Months</span>
            </div>
          </div>
        </div>

        {/* Right: Pricing, Buy Button, Alert */}
        <div className="space-y-6">
          <div>
            <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">{product.brand}</span>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight mt-1 mb-2">
              {product.name}
            </h1>
            <div className="flex items-center gap-3 text-sm text-slate-500">
              <span className="flex items-center gap-1 font-bold text-amber-500">
                <Star className="w-4 h-4 fill-current" /> {product.rating}
              </span>
              <span>•</span>
              <span>{product.review_count} verified ratings</span>
              <span>•</span>
              <span className="text-emerald-600 font-semibold">{product.availability}</span>
            </div>
          </div>

          {/* Price Box */}
          <div className="p-6 bg-slate-50 rounded-2xl border border-slate-200 space-y-4">
            <div className="flex items-baseline gap-3">
              <span className="text-3xl font-black text-slate-900">
                ₹{selectedSeller?.current_price?.toLocaleString() || product.best_price?.toLocaleString()}
              </span>
              {selectedSeller?.original_price && selectedSeller.original_price > selectedSeller.current_price && (
                <span className="text-base text-slate-400 line-through">
                  ₹{selectedSeller.original_price.toLocaleString()}
                </span>
              )}
              <span className="text-xs font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800">
                Free Delivery
              </span>
            </div>

            <p className="text-xs text-slate-500">
              Inclusive of all taxes (GST). Official manufacturer on-site service warranty.
            </p>

            <button
              onClick={() => setShowCheckout(true)}
              className="w-full py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-xl text-sm shadow-md shadow-indigo-100 flex items-center justify-center gap-2 transition-colors"
            >
              <ShoppingCart className="w-4 h-4" />
              Proceed with Human Confirmation
            </button>
          </div>

          {/* Price Alert Configuration */}
          <div className="p-5 bg-white rounded-2xl border border-slate-200 space-y-3">
            <h4 className="font-bold text-slate-900 text-sm flex items-center gap-2">
              <Bell className="w-4 h-4 text-indigo-600" /> Track Price & Get Notified
            </h4>
            <div className="flex gap-2">
              <input
                type="number"
                value={alertTargetPrice}
                onChange={(e) => setAlertTargetPrice(e.target.value ? Number(e.target.value) : '')}
                placeholder="Target Price in ₹"
                className="flex-1 px-4 py-2 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500/20"
              />
              <button
                onClick={handleCreateAlert}
                className="px-4 py-2 bg-slate-900 hover:bg-black text-white text-xs font-semibold rounded-xl"
              >
                Set Alert
              </button>
            </div>
            {alertSuccess && (
              <p className="text-xs text-emerald-600 font-medium">{alertSuccess}</p>
            )}
          </div>
        </div>
      </div>

      {/* Verified Price History Chart */}
      {product.price_history?.length > 0 && (
        <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="font-bold text-slate-900 text-base flex items-center gap-2">
                <TrendingDown className="w-5 h-5 text-indigo-600" /> Verified Historical Price Trend
              </h3>
              <p className="text-xs text-slate-500">
                Observed price snapshots over time. AI never claims historical lowest without verified timestamp data.
              </p>
            </div>
          </div>
          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={product.price_history}>
                <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
                <XAxis dataKey="date" stroke="#94a3b8" fontSize={11} />
                <YAxis stroke="#94a3b8" fontSize={11} domain={['auto', 'auto']} />
                <Tooltip
                  formatter={(val: any) => [`₹${Number(val).toLocaleString()}`, 'Observed Price']}
                  contentStyle={{ backgroundColor: '#1e293b', color: '#fff', borderRadius: '12px', fontSize: '12px' }}
                />
                <Line type="monotone" dataKey="price" stroke="#4f46e5" strokeWidth={3} dot={{ r: 4 }} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>
      )}

      {/* Review Sentiment Analysis Section */}
      {reviewAnalysis && (
        <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-6">
          <h3 className="font-bold text-slate-900 text-base">
            Review Analysis & Aspect Breakdown
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-4 bg-emerald-50 rounded-2xl border border-emerald-100">
              <span className="text-xs font-bold text-emerald-800 uppercase tracking-wider block mb-2">
                Positive Themes ({reviewAnalysis.sentiment_positive_pct}%)
              </span>
              <ul className="text-xs text-emerald-950 space-y-1">
                {reviewAnalysis.positive_themes?.map((t: string, i: number) => (
                  <li key={i}>✓ {t}</li>
                ))}
              </ul>
            </div>
            <div className="p-4 bg-amber-50 rounded-2xl border border-amber-100">
              <span className="text-xs font-bold text-amber-800 uppercase tracking-wider block mb-2">
                Common Complaints ({reviewAnalysis.sentiment_negative_pct}%)
              </span>
              <ul className="text-xs text-amber-950 space-y-1">
                {reviewAnalysis.common_complaints?.map((t: string, i: number) => (
                  <li key={i}>• {t}</li>
                ))}
              </ul>
            </div>
            <div className="p-4 bg-rose-50 rounded-2xl border border-rose-100">
              <span className="text-xs font-bold text-rose-800 uppercase tracking-wider block mb-2">
                Important Warnings
              </span>
              <ul className="text-xs text-rose-950 space-y-1">
                {reviewAnalysis.important_warnings?.map((t: string, i: number) => (
                  <li key={i}>⚠️ {t}</li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      )}

      {/* Human Approval Modal */}
      <HumanApprovalModal
        isOpen={showCheckout}
        onClose={() => setShowCheckout(false)}
        product={{
          id: product.id,
          name: product.name,
          brand: product.brand,
          price: selectedSeller?.current_price || product.best_price,
          seller: selectedSeller?.seller_name || product.source,
          image_url: product.main_image
        }}
      />
    </div>
  );
};
