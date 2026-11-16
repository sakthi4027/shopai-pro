import React, { useEffect, useState } from 'react';
import { Bookmark, Trash2, ExternalLink, Loader2, Star, ShoppingBag } from 'lucide-react';
import { Link } from 'react-router-dom';
import { api } from '../services/api';

export const SavedProductsPage: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [savedItems, setSavedItems] = useState<any[]>([]);

  const loadSaved = () => {
    setLoading(true);
    api.getSavedProducts()
      .then(data => setSavedItems(data))
      .catch(console.error)
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    loadSaved();
  }, []);

  const handleRemove = async (productId: string) => {
    try {
      await api.removeSavedProduct(productId);
      setSavedItems(prev => prev.filter(item => item.product_id !== productId));
    } catch (err: any) {
      alert("Error removing item: " + err.message);
    }
  };

  if (loading) {
    return (
      <div className="py-24 text-center flex flex-col items-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
        <p className="text-sm text-slate-500 font-medium">Loading saved products...</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div>
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-700 text-xs font-bold mb-2">
          <Bookmark className="w-3.5 h-3.5" /> Bookmarks
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
          Saved Products ({savedItems.length})
        </h1>
        <p className="text-sm text-slate-500">
          Your bookmarked shortlist isolated to your authenticated account.
        </p>
      </div>

      {savedItems.length === 0 ? (
        <div className="py-16 text-center max-w-sm mx-auto bg-white rounded-3xl p-8 border border-slate-200">
          <ShoppingBag className="w-12 h-12 text-slate-300 mx-auto mb-3" />
          <h3 className="font-bold text-slate-900 text-base mb-1">No Saved Products Yet</h3>
          <p className="text-xs text-slate-500 mb-6">Click the bookmark icon on any product card in search results to save it here.</p>
          <Link to="/search" className="px-5 py-2.5 bg-indigo-600 text-white rounded-xl text-xs font-semibold">
            Explore Products
          </Link>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {savedItems.map((item) => (
            <div key={item.id} className="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm flex flex-col justify-between">
              <div>
                <img
                  src={item.main_image || "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80"}
                  alt={item.product_name}
                  className="w-full h-44 object-cover rounded-xl mb-3"
                />
                <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">{item.brand}</span>
                <h3 className="font-bold text-slate-900 text-sm line-clamp-2 mt-1 mb-2">{item.product_name}</h3>
                <div className="flex items-center gap-1 text-xs text-amber-500 font-semibold mb-3">
                  <Star className="w-3.5 h-3.5 fill-current" /> {item.rating}
                </div>
              </div>

              <div className="pt-3 border-t border-slate-100 flex items-center justify-between">
                <Link
                  to={`/products/${item.product_id}`}
                  className="text-xs font-semibold text-indigo-600 hover:underline flex items-center gap-1"
                >
                  View Details <ExternalLink className="w-3.5 h-3.5" />
                </Link>
                <button
                  onClick={() => handleRemove(item.product_id)}
                  className="p-2 text-slate-400 hover:text-red-600 rounded-lg hover:bg-red-50 transition-colors"
                  title="Remove from saved"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
