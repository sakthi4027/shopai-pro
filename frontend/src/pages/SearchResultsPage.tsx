import React, { useEffect, useState } from 'react';
import { useLocation } from 'react-router-dom';
import { Search, SlidersHorizontal, Loader2 } from 'lucide-react';
import { api } from '../services/api';
import { ProductCard } from '../components/products/ProductCard';

export const SearchResultsPage: React.FC = () => {
  const location = useLocation();
  const [loading, setLoading] = useState(true);
  const [products, setProducts] = useState<any[]>([]);
  const [filterBrand, setFilterBrand] = useState<string>('All');

  useEffect(() => {
    api.search("laptop 32GB RAM")
      .then(res => setProducts(res.ranked_products || []))
      .catch(console.error)
      .finally(() => setLoading(false));
  }, [location.search]);

  const brands = ['All', 'Lenovo', 'ASUS', 'HP', 'Acer'];

  const filtered = filterBrand === 'All'
    ? products
    : products.filter(p => p.brand?.toLowerCase() === filterBrand.toLowerCase());

  if (loading) {
    return (
      <div className="py-24 text-center flex flex-col items-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
        <p className="text-sm text-slate-500 font-medium">Filtering catalog products...</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
            Search Results ({filtered.length})
          </h1>
          <p className="text-sm text-slate-500">
            Verified hardware candidates satisfying baseline performance requirements.
          </p>
        </div>

        {/* Brand Filter Pills */}
        <div className="flex items-center gap-1.5 overflow-x-auto pb-1">
          {brands.map(b => (
            <button
              key={b}
              onClick={() => setFilterBrand(b)}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-colors ${
                filterBrand === b
                  ? 'bg-indigo-600 text-white shadow-sm'
                  : 'bg-white border border-slate-200 text-slate-600 hover:bg-slate-50'
              }`}
            >
              {b}
            </button>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filtered.map((product, idx) => (
          <ProductCard key={idx} product={product} />
        ))}
      </div>
    </div>
  );
};
