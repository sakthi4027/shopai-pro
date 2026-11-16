import React, { useState, useEffect } from 'react';
import { useLocation, Link } from 'react-router-dom';
import { Layers, Award, Check, X, ArrowLeft, Loader2, Zap } from 'lucide-react';
import { api } from '../services/api';

export const ProductComparisonPage: React.FC = () => {
  const location = useLocation();
  const [loading, setLoading] = useState(true);
  const [compareData, setCompareData] = useState<any>(null);

  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const idsParam = params.get('ids');
    let ids = idsParam ? idsParam.split(',').filter(Boolean) : [];

    if (ids.length === 0) {
      // Default to top 3 products in DB
      ids = ['prod_lenovo_legion_slim5', 'prod_asus_tuf_a15', 'prod_acer_nitro_v15'];
    }

    api.compareProducts(ids)
      .then(data => setCompareData(data))
      .catch(err => alert("Comparison error: " + err.message))
      .finally(() => setLoading(false));
  }, [location.search]);

  if (loading) {
    return (
      <div className="py-24 text-center flex flex-col items-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
        <p className="text-sm text-slate-500 font-medium">Constructing side-by-side spec comparison...</p>
      </div>
    );
  }

  if (!compareData || !compareData.products?.length) {
    return (
      <div className="py-20 text-center max-w-md mx-auto">
        <Layers className="w-12 h-12 text-slate-300 mx-auto mb-3" />
        <h3 className="text-lg font-bold text-slate-900 mb-1">No Products to Compare</h3>
        <p className="text-sm text-slate-500 mb-6">Select products from the search results to see a side-by-side comparison.</p>
        <Link to="/search" className="px-5 py-2.5 bg-indigo-600 text-white rounded-xl text-sm font-semibold">
          Go to Search
        </Link>
      </div>
    );
  }

  const { products, comparison_matrix, highlights } = compareData;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <Link to="/search" className="inline-flex items-center gap-1.5 text-xs text-slate-500 hover:text-indigo-600 font-medium mb-2">
            <ArrowLeft className="w-3.5 h-3.5" /> Back to Search
          </Link>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
            Side-by-Side Product Comparison
          </h1>
          <p className="text-xs text-slate-500">
            Comparing {products.length} products against technical constraints, battery, warranty, and price.
          </p>
        </div>
      </div>

      {/* Highlights / Category Winners Bar */}
      {highlights && (
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-indigo-50/60 p-4 rounded-2xl border border-indigo-100">
          <div className="p-3 bg-white rounded-xl border border-indigo-100/80 shadow-sm">
            <span className="text-[10px] uppercase font-bold text-amber-600 block mb-0.5">🏆 Best Overall</span>
            <span className="text-xs font-bold text-slate-900 line-clamp-1">{highlights.best_overall}</span>
          </div>
          <div className="p-3 bg-white rounded-xl border border-indigo-100/80 shadow-sm">
            <span className="text-[10px] uppercase font-bold text-emerald-600 block mb-0.5">💰 Best Value</span>
            <span className="text-xs font-bold text-slate-900 line-clamp-1">{highlights.best_value}</span>
          </div>
          <div className="p-3 bg-white rounded-xl border border-indigo-100/80 shadow-sm">
            <span className="text-[10px] uppercase font-bold text-indigo-600 block mb-0.5">⚡ Best Performance</span>
            <span className="text-xs font-bold text-slate-900 line-clamp-1">{highlights.best_performance}</span>
          </div>
          <div className="p-3 bg-white rounded-xl border border-indigo-100/80 shadow-sm">
            <span className="text-[10px] uppercase font-bold text-blue-600 block mb-0.5">💵 Cheapest Suitable</span>
            <span className="text-xs font-bold text-slate-900 line-clamp-1">{highlights.cheapest_suitable}</span>
          </div>
        </div>
      )}

      {/* Comparison Table */}
      <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-x-auto">
        <table className="w-full text-left border-collapse text-sm">
          <thead>
            <tr className="border-b border-slate-200 bg-slate-50">
              <th className="p-4 font-bold text-slate-600 text-xs uppercase tracking-wider w-48">
                Feature
              </th>
              {products.map((p: any) => (
                <th key={p.id} className="p-4 min-w-[240px]">
                  <div className="space-y-1.5">
                    <img
                      src={p.main_image || "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80"}
                      alt={p.name}
                      className="w-full h-28 object-cover rounded-xl border border-slate-200 mb-2"
                    />
                    <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">{p.brand}</span>
                    <h4 className="font-bold text-slate-900 text-sm line-clamp-2">{p.name}</h4>
                    <span className="text-lg font-extrabold text-slate-900 block">
                      ₹{p.best_price?.toLocaleString()}
                    </span>
                    <Link
                      to={`/products/${p.id}`}
                      className="inline-block text-xs text-indigo-600 font-semibold hover:underline"
                    >
                      View Details →
                    </Link>
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100 text-xs">
            {comparison_matrix.map((row: any, i: number) => (
              <tr key={i} className={i % 2 === 0 ? 'bg-white' : 'bg-slate-50/50'}>
                <td className="p-4 font-semibold text-slate-700 bg-slate-50/80">
                  {row.feature}
                </td>
                {products.map((p: any) => (
                  <td key={p.id} className="p-4 text-slate-800 font-medium">
                    {row.values[p.id] || "—"}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
