import React, { useEffect, useState } from 'react';
import { Bell, Trash2, CheckCircle2, AlertCircle, Loader2 } from 'lucide-react';
import { Link } from 'react-router-dom';
import { api } from '../services/api';

export const PriceAlertsPage: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [alerts, setAlerts] = useState<any[]>([]);

  const loadAlerts = () => {
    setLoading(true);
    api.getAlerts()
      .then(data => setAlerts(data))
      .catch(console.error)
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    loadAlerts();
  }, []);

  const handleDelete = async (id: string) => {
    try {
      await api.deleteAlert(id);
      setAlerts(prev => prev.filter(a => a.id !== id));
    } catch (err: any) {
      alert("Error deleting alert: " + err.message);
    }
  };

  if (loading) {
    return (
      <div className="py-24 text-center flex flex-col items-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
        <p className="text-sm text-slate-500 font-medium">Checking active price threshold monitors...</p>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div>
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-700 text-xs font-bold mb-2">
          <Bell className="w-3.5 h-3.5" /> Price Monitoring
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
          Active Price Alerts ({alerts.length})
        </h1>
        <p className="text-sm text-slate-500">
          Automated threshold monitoring. You will be alerted the moment verified prices meet your ceiling.
        </p>
      </div>

      {alerts.length === 0 ? (
        <div className="py-16 text-center max-w-sm mx-auto bg-white rounded-3xl p-8 border border-slate-200">
          <Bell className="w-12 h-12 text-slate-300 mx-auto mb-3" />
          <h3 className="font-bold text-slate-900 text-base mb-1">No Active Price Alerts</h3>
          <p className="text-xs text-slate-500 mb-6">Open any product page and enter your target price to activate an alert.</p>
          <Link to="/search" className="px-5 py-2.5 bg-indigo-600 text-white rounded-xl text-xs font-semibold">
            Browse Laptops
          </Link>
        </div>
      ) : (
        <div className="space-y-3">
          {alerts.map((al) => (
            <div key={al.id} className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div className="space-y-1">
                <Link to={`/products/${al.product_id}`} className="font-bold text-slate-900 text-sm hover:text-indigo-600">
                  {al.product_name}
                </Link>
                <div className="flex items-center gap-3 text-xs text-slate-500">
                  <span>Target Threshold: <strong className="text-indigo-600">₹{al.target_price?.toLocaleString()}</strong></span>
                  <span>•</span>
                  <span>Current Price: <strong>₹{al.current_price?.toLocaleString()}</strong></span>
                </div>
              </div>

              <div className="flex items-center gap-4">
                {al.is_triggered ? (
                  <span className="inline-flex items-center gap-1 px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full text-xs font-bold">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600" /> Price Target Reached!
                  </span>
                ) : (
                  <span className="inline-flex items-center gap-1 px-3 py-1 bg-slate-100 text-slate-600 rounded-full text-xs font-semibold">
                    <Bell className="w-3.5 h-3.5 text-slate-400" /> Monitoring (₹{al.difference?.toLocaleString()} away)
                  </span>
                )}

                <button
                  onClick={() => handleDelete(al.id)}
                  className="p-2 text-slate-400 hover:text-red-600 rounded-lg hover:bg-red-50 transition-colors"
                  title="Delete alert"
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
