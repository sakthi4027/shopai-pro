import React, { useEffect, useState } from 'react';
import { Settings, Save, RotateCcw, CheckCircle2, ShieldCheck, Cpu, HardDrive, DollarSign, Tag, Loader2 } from 'lucide-react';
import { api } from '../services/api';
import { UserPreferences } from '../types';

export const SettingsPage: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [successMsg, setSuccessMsg] = useState<string | null>(null);

  const [preferences, setPreferences] = useState<UserPreferences>({
    preferred_brands: ['Lenovo', 'ASUS'],
    budget_max: 80000,
    preferred_ram: '32GB',
    preferred_storage: '1TB',
    avoid_refurbished: true,
    excluded_keywords: ['Refurbished', 'Open Box'],
    currency: 'INR'
  });

  const [brandInput, setBrandInput] = useState('');

  useEffect(() => {
    api.getPreferences()
      .then(pref => {
        if (pref) {
          setPreferences({
            preferred_brands: pref.preferred_brands || ['Lenovo', 'ASUS'],
            budget_max: pref.budget_max || 80000,
            preferred_ram: pref.preferred_ram || '32GB',
            preferred_storage: pref.preferred_storage || '1TB',
            avoid_refurbished: pref.avoid_refurbished !== false,
            excluded_keywords: pref.excluded_keywords || ['Refurbished', 'Open Box'],
            currency: pref.currency || 'INR'
          });
        }
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaving(true);
    try {
      await api.updatePreferences(preferences);
      setSuccessMsg("Shopping memory preferences updated successfully!");
      setTimeout(() => setSuccessMsg(null), 4000);
    } catch (err: any) {
      alert("Save failed: " + err.message);
    } finally {
      setSaving(false);
    }
  };

  const handleReset = async () => {
    if (!confirm("Are you sure you want to reset your shopping memory preferences?")) return;
    setSaving(true);
    try {
      await api.resetPreferences();
      setPreferences({
        preferred_brands: [],
        budget_max: undefined,
        preferred_ram: undefined,
        preferred_storage: undefined,
        avoid_refurbished: true,
        excluded_keywords: [],
        currency: 'INR'
      });
      setSuccessMsg("Shopping memory reset to default.");
      setTimeout(() => setSuccessMsg(null), 4000);
    } catch (err: any) {
      alert("Reset failed: " + err.message);
    } finally {
      setSaving(false);
    }
  };

  const addBrand = () => {
    if (brandInput.trim() && !preferences.preferred_brands.includes(brandInput.trim())) {
      setPreferences(prev => ({
        ...prev,
        preferred_brands: [...prev.preferred_brands, brandInput.trim()]
      }));
      setBrandInput('');
    }
  };

  const removeBrand = (brand: string) => {
    setPreferences(prev => ({
      ...prev,
      preferred_brands: prev.preferred_brands.filter(b => b !== brand)
    }));
  };

  if (loading) {
    return (
      <div className="py-24 text-center flex flex-col items-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
        <p className="text-sm text-slate-500 font-medium">Loading user shopping memory...</p>
      </div>
    );
  }

  return (
    <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div>
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-700 text-xs font-bold mb-2">
          <Settings className="w-3.5 h-3.5" /> Persistent Shopping Memory
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
          AI Shopping Memory & User Preferences
        </h1>
        <p className="text-sm text-slate-500">
          Customize your default constraints. The shopping planner agent consults this memory to filter future searches automatically.
        </p>
      </div>

      {successMsg && (
        <div className="p-4 bg-emerald-50 border border-emerald-200 rounded-2xl text-xs text-emerald-800 font-semibold flex items-center gap-2">
          <CheckCircle2 className="w-4 h-4 text-emerald-600 shrink-0" />
          <span>{successMsg}</span>
        </div>
      )}

      <form onSubmit={handleSave} className="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200 shadow-sm space-y-6">
        {/* Preferred Brands */}
        <div>
          <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
            Preferred Brands
          </label>
          <div className="flex gap-2 mb-2">
            <input
              type="text"
              value={brandInput}
              onChange={(e) => setBrandInput(e.target.value)}
              placeholder="e.g. Lenovo, ASUS, Apple, Dell"
              className="flex-1 px-4 py-2 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500/20"
            />
            <button
              type="button"
              onClick={addBrand}
              className="px-4 py-2 bg-slate-900 text-white rounded-xl text-xs font-semibold hover:bg-black"
            >
              Add Brand
            </button>
          </div>
          <div className="flex flex-wrap gap-2">
            {preferences.preferred_brands.map((b) => (
              <span key={b} className="inline-flex items-center gap-1.5 px-3 py-1 bg-indigo-50 text-indigo-700 rounded-xl text-xs font-semibold">
                {b}
                <button type="button" onClick={() => removeBrand(b)} className="hover:text-red-600 text-indigo-400">
                  ×
                </button>
              </span>
            ))}
          </div>
        </div>

        {/* Default Budget */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
              Default Budget Ceiling (₹ INR)
            </label>
            <input
              type="number"
              value={preferences.budget_max || ''}
              onChange={(e) => setPreferences({ ...preferences, budget_max: e.target.value ? Number(e.target.value) : undefined })}
              placeholder="e.g. 80000"
              className="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500/20"
            />
          </div>

          <div>
            <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
              Preferred RAM
            </label>
            <input
              type="text"
              value={preferences.preferred_ram || ''}
              onChange={(e) => setPreferences({ ...preferences, preferred_ram: e.target.value })}
              placeholder="e.g. 32GB"
              className="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500/20"
            />
          </div>
        </div>

        {/* Preferred Storage & Avoid Refurbished */}
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <div>
            <label className="block text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
              Preferred Storage
            </label>
            <input
              type="text"
              value={preferences.preferred_storage || ''}
              onChange={(e) => setPreferences({ ...preferences, preferred_storage: e.target.value })}
              placeholder="e.g. 1TB SSD"
              className="w-full px-4 py-2.5 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-indigo-500/20"
            />
          </div>

          <div className="flex items-center gap-3 pt-6">
            <input
              type="checkbox"
              id="avoidRefurbished"
              checked={preferences.avoid_refurbished}
              onChange={(e) => setPreferences({ ...preferences, avoid_refurbished: e.target.checked })}
              className="w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500"
            />
            <label htmlFor="avoidRefurbished" className="text-xs font-semibold text-slate-800">
              Avoid Refurbished / Open-Box Products (Always recommend Brand New)
            </label>
          </div>
        </div>

        {/* Isolation Notice */}
        <div className="bg-slate-50 p-4 rounded-2xl border border-slate-200 text-xs text-slate-500 flex items-center gap-2">
          <ShieldCheck className="w-4 h-4 text-emerald-600 shrink-0" />
          <span>User isolation enabled: Your shopping memory is strictly encrypted and isolated to your user account.</span>
        </div>

        {/* Actions */}
        <div className="pt-4 border-t border-slate-100 flex items-center justify-between">
          <button
            type="button"
            onClick={handleReset}
            disabled={saving}
            className="px-4 py-2.5 border border-slate-200 text-slate-600 hover:text-red-600 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-colors"
          >
            <RotateCcw className="w-3.5 h-3.5" /> Reset Preferences
          </button>

          <button
            type="submit"
            disabled={saving}
            className="px-6 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl text-xs font-bold shadow-md shadow-indigo-100 flex items-center gap-1.5 transition-colors"
          >
            {saving ? <Loader2 className="w-4 h-4 animate-spin" /> : <Save className="w-3.5 h-3.5" />}
            Save Shopping Memory
          </button>
        </div>
      </form>
    </div>
  );
};
