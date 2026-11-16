import React, { useEffect, useState } from 'react';
import { Star, ShieldAlert, CheckCircle2, MessageSquare, AlertTriangle, Loader2 } from 'lucide-react';
import { api } from '../services/api';

export const ReviewIntelligencePage: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [products, setProducts] = useState<any[]>([]);
  const [selectedProduct, setSelectedProduct] = useState<any>(null);
  const [analysis, setAnalysis] = useState<any>(null);
  const [reviews, setReviews] = useState<any[]>([]);

  useEffect(() => {
    api.getProducts()
      .then(prods => {
        setProducts(prods);
        if (prods.length > 0) {
          setSelectedProduct(prods[0]);
          return Promise.all([
            api.getReviewAnalysis(prods[0].id),
            api.getReviews(prods[0].id)
          ]);
        }
      })
      .then(res => {
        if (res) {
          setAnalysis(res[0] as any);
          setReviews(res[1] as any[]);
        }
      })
      .catch(console.error)
      .finally(() => setLoading(false));
  }, []);

  const handleSelect = async (p: any) => {
    setSelectedProduct(p);
    setLoading(true);
    try {
      const [ana, revs] = await Promise.all([
        api.getReviewAnalysis(p.id),
        api.getReviews(p.id)
      ]);
      setAnalysis(ana);
      setReviews(revs);
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
          <Star className="w-3.5 h-3.5" /> Review Analysis Agent
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
          Review Intelligence & Buyer Sentiment
        </h1>
        <p className="text-sm text-slate-500">
          Synthesizing genuine verified owner feedback across battery, thermals, display, and build quality.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Left: Product selector */}
        <div className="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
          <h3 className="font-bold text-slate-900 text-sm">Select Product</h3>
          <div className="space-y-2">
            {products.map(p => (
              <button
                key={p.id}
                onClick={() => handleSelect(p)}
                className={`w-full p-3 rounded-2xl border text-left transition-all flex items-center gap-3 ${
                  selectedProduct?.id === p.id
                    ? 'border-indigo-600 bg-indigo-50/50 shadow-sm'
                    : 'border-slate-200 hover:border-slate-300'
                }`}
              >
                <img src={p.main_image} alt={p.name} className="w-12 h-12 object-cover rounded-xl" />
                <div className="flex-1 min-w-0">
                  <h4 className="text-xs font-bold text-slate-900 truncate">{p.name}</h4>
                  <div className="flex items-center gap-1 text-xs text-amber-500 font-semibold mt-0.5">
                    <Star className="w-3.5 h-3.5 fill-current" /> {p.rating} ({p.review_count})
                  </div>
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* Right: Aspect Sentiment & Themes */}
        <div className="lg:col-span-2 space-y-6">
          {analysis && (
            <>
              {/* Sentiment Gauge Bar */}
              <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4">
                <div className="flex justify-between items-center">
                  <h3 className="font-bold text-slate-900 text-base">Overall Sentiment Distribution</h3>
                  <span className="text-xs text-slate-400">Audited across verified buyers</span>
                </div>
                <div className="h-4 w-full bg-slate-100 rounded-full flex overflow-hidden">
                  <div style={{ width: `${analysis.sentiment_positive_pct}%` }} className="bg-emerald-500" title={`Positive: ${analysis.sentiment_positive_pct}%`} />
                  <div style={{ width: `${analysis.sentiment_neutral_pct}%` }} className="bg-slate-400" title={`Neutral: ${analysis.sentiment_neutral_pct}%`} />
                  <div style={{ width: `${analysis.sentiment_negative_pct}%` }} className="bg-rose-500" title={`Negative: ${analysis.sentiment_negative_pct}%`} />
                </div>
                <div className="flex justify-between text-xs font-semibold">
                  <span className="text-emerald-600">● {analysis.sentiment_positive_pct}% Positive</span>
                  <span className="text-slate-500">● {analysis.sentiment_neutral_pct}% Neutral</span>
                  <span className="text-rose-600">● {analysis.sentiment_negative_pct}% Negative</span>
                </div>
              </div>

              {/* Aspect Scores Grid */}
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
                {Object.entries(analysis.aspect_scores || {}).map(([aspect, score]: any) => (
                  <div key={aspect} className="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm">
                    <span className="text-xs font-semibold text-slate-400 capitalize block mb-1">{aspect.replace('_', ' ')}</span>
                    <span className="text-lg font-black text-slate-900">⭐ {score} / 5.0</span>
                  </div>
                ))}
              </div>

              {/* Positive Themes & Warnings */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="bg-emerald-50/70 p-5 rounded-2xl border border-emerald-100 space-y-2">
                  <h4 className="text-xs font-bold text-emerald-800 uppercase tracking-wider flex items-center gap-1.5">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600" /> Positive Themes
                  </h4>
                  <ul className="text-xs text-emerald-950 space-y-1.5">
                    {analysis.positive_themes?.map((t: string, i: number) => (
                      <li key={i}>✓ {t}</li>
                    ))}
                  </ul>
                </div>

                <div className="bg-rose-50/70 p-5 rounded-2xl border border-rose-100 space-y-2">
                  <h4 className="text-xs font-bold text-rose-800 uppercase tracking-wider flex items-center gap-1.5">
                    <AlertTriangle className="w-4 h-4 text-rose-600" /> Buyer Warnings & Complaints
                  </h4>
                  <ul className="text-xs text-rose-950 space-y-1.5">
                    {analysis.important_warnings?.map((t: string, i: number) => (
                      <li key={i}>⚠️ {t}</li>
                    ))}
                    {analysis.common_complaints?.map((t: string, i: number) => (
                      <li key={i}>• {t}</li>
                    ))}
                  </ul>
                </div>
              </div>

              {/* Sample Authentic Reviews with clear source attribution */}
              <div className="bg-white p-6 rounded-3xl border border-slate-200 shadow-sm space-y-4">
                <h3 className="font-bold text-slate-900 text-sm">Verified Sample Customer Reviews</h3>
                <div className="space-y-3">
                  {reviews.map((r, idx) => (
                    <div key={idx} className="p-4 bg-slate-50 rounded-2xl border border-slate-200/80 text-xs space-y-1.5">
                      <div className="flex justify-between items-center text-slate-500">
                        <span className="font-bold text-slate-900">{r.author || 'Verified Purchaser'}</span>
                        <span className="text-[11px] bg-slate-200/60 px-2 py-0.5 rounded-md font-medium">Source: {r.source}</span>
                      </div>
                      <div className="text-amber-500 font-semibold">⭐ {r.rating} / 5.0</div>
                      <p className="text-slate-700 leading-relaxed">{r.review_text}</p>
                    </div>
                  ))}
                </div>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};
