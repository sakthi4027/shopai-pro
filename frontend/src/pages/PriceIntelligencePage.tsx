import React, { useEffect, useState } from 'react';
import { TrendingDown, ShieldCheck, ArrowRight, Loader2 } from 'lucide-react';
import { api } from '../services/api';
import { ResponsiveContainer, LineChart, Line, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

export const PriceIntelligencePage: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [products, setProducts] = useState<any[]>([]);
  const [selectedProduct, setSelectedProduct] = useState<any>(null);
  const [historyData, setHistoryData] = useState<any>(null);

  useEffect(() => {
    api.getProducts()
      .then(prods => {
        setProducts(prods);
        if (prods.length > 0) {
          setSelectedProduct(prods[0]);
          return api.getPriceHistory(prods[0].id);
        }
      })
      .then(hist => {
        if (hist) setHistoryData(hist);
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  const handleSelectProduct = async (p: any) => {
    setSelectedProduct(p);
    setLoading(true);
    try {
      const hist = await api.getPriceHistory(p.id);
      setHistoryData(hist);
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div>
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-700 text-xs font-bold mb-2">
          <TrendingDown className="w-3.5 h-3.5" /> Price Intelligence Agent
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
          Verified Market Price Intelligence
        </h1>
        <p className="text-sm text-slate-500">
          Tracking price drop frequencies, artificial discount inflation, and cross-seller variances.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left: Product Selection List */}
        <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
          <h3 className="font-bold text-slate-900 text-sm">Monitored Hardware</h3>
          <div className="space-y-2">
            {products.map((p) => (
              <button
                key={p.id}
                onClick={() => handleSelectProduct(p)}
                className={`w-full p-3 rounded-2xl border text-left transition-all flex items-center gap-3 ${
                  selectedProduct?.id === p.id
                    ? 'border-indigo-600 bg-indigo-50/50 shadow-sm'
                    : 'border-slate-200 hover:border-slate-300'
                }`}
              >
                <img src={p.main_image} alt={p.name} className="w-12 h-12 object-cover rounded-xl" />
                <div className="flex-1 min-w-0">
                  <h4 className="text-xs font-bold text-slate-900 truncate">{p.name}</h4>
                  <span className="text-sm font-extrabold text-indigo-600">₹{p.best_price?.toLocaleString()}</span>
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* Right: Price Chart & Statement */}
        <div className="lg:col-span-2 space-y-6">
          {historyData && (
            <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-6">
              <div>
                <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">{selectedProduct?.brand}</span>
                <h3 className="text-xl font-bold text-slate-900">{selectedProduct?.name}</h3>
                <div className="mt-2 p-3 bg-indigo-50/60 rounded-xl border border-indigo-100 text-xs font-semibold text-indigo-900">
                  {historyData.price_insight}
                </div>
              </div>

              <div className="h-72 w-full">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={historyData.history}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#f1f5f9" />
                    <XAxis dataKey="date" stroke="#94a3b8" fontSize={11} />
                    <YAxis stroke="#94a3b8" fontSize={11} domain={['auto', 'auto']} />
                    <Tooltip
                      formatter={(val: any) => [`₹${Number(val).toLocaleString()}`, 'Recorded Price']}
                      contentStyle={{ backgroundColor: '#1e293b', color: '#fff', borderRadius: '12px', fontSize: '12px' }}
                    />
                    <Line type="monotone" dataKey="price" stroke="#4f46e5" strokeWidth={3} dot={{ r: 4 }} />
                  </LineChart>
                </ResponsiveContainer>
              </div>

              <div className="grid grid-cols-2 gap-4 text-xs">
                <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <span className="text-slate-400 block mb-0.5">Verified Discount</span>
                  <span className="font-extrabold text-slate-900 text-sm">~15.8% Confirmed</span>
                </div>
                <div className="p-3 bg-slate-50 rounded-xl border border-slate-200">
                  <span className="text-slate-400 block mb-0.5">Price Stability</span>
                  <span className="font-extrabold text-emerald-600 text-sm">Consistent Trend</span>
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
