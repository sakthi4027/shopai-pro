import React, { useEffect, useState } from 'react';
import { Clock, Search, ArrowRight, Loader2 } from 'lucide-react';
import { Link } from 'react-router-dom';
import { api } from '../services/api';

export const ShoppingHistoryPage: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [history, setHistory] = useState<any[]>([]);

  useEffect(() => {
    api.getSearchHistory()
      .then(data => setHistory(data))
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="py-24 text-center flex flex-col items-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
        <p className="text-sm text-slate-500 font-medium">Retrieving past search sessions...</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div>
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-700 text-xs font-bold mb-2">
          <Clock className="w-3.5 h-3.5" /> Isolated History
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
          Shopping Search History ({history.length})
        </h1>
        <p className="text-sm text-slate-500">
          Your search sessions are strictly isolated to your authenticated account.
        </p>
      </div>

      {history.length === 0 ? (
        <div className="py-16 text-center max-w-sm mx-auto bg-white rounded-3xl p-8 border border-slate-200">
          <Clock className="w-12 h-12 text-slate-300 mx-auto mb-3" />
          <h3 className="font-bold text-slate-900 text-base mb-1">No Past Search Sessions</h3>
          <p className="text-xs text-slate-500 mb-6">Ask our multi-agent assistant to find products and your sessions will appear here.</p>
          <Link to="/search" className="px-5 py-2.5 bg-indigo-600 text-white rounded-xl text-xs font-semibold">
            Start a Search
          </Link>
        </div>
      ) : (
        <div className="bg-white rounded-3xl border border-slate-200 divide-y divide-slate-100 shadow-sm overflow-hidden">
          {history.map((s) => (
            <div key={s.id} className="p-5 flex items-center justify-between hover:bg-slate-50 transition-colors">
              <div className="space-y-1">
                <h4 className="font-bold text-slate-900 text-sm">{s.title}</h4>
                <div className="text-xs text-slate-400">
                  {new Date(s.created_at).toLocaleString()} • Status: <span className="text-emerald-600 font-semibold">{s.status}</span>
                </div>
              </div>
              <Link
                to={`/search?q=${encodeURIComponent(s.title)}`}
                className="px-4 py-2 bg-indigo-50 hover:bg-indigo-100 text-indigo-700 rounded-xl text-xs font-semibold flex items-center gap-1 transition-colors"
              >
                Re-run Swarm <ArrowRight className="w-3.5 h-3.5" />
              </Link>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
