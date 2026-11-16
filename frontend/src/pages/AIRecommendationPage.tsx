import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Award, Zap, TrendingUp, DollarSign, ArrowRight, Loader2 } from 'lucide-react';
import { api } from '../services/api';
import { ProductCard } from '../components/products/ProductCard';
import { RecommendationItem } from '../types';

export const AIRecommendationPage: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [recommendations, setRecommendations] = useState<RecommendationItem[]>([]);

  useEffect(() => {
    // Perform standard search query to get fresh recommendations
    api.search("Find me a laptop under ₹80,000 with 32GB RAM, 1TB SSD, good battery life, and suitable for AI development.")
      .then(res => setRecommendations(res.ranked_products || []))
      .catch(err => console.error(err))
      .finally(() => setLoading(false));
  }, []);

  if (loading) {
    return (
      <div className="py-24 text-center flex flex-col items-center">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-600 mb-2" />
        <p className="text-sm text-slate-500 font-medium">Computing multi-factor recommendation rankings...</p>
      </div>
    );
  }

  const bestOverall = recommendations.find(r => r.badge === 'Best Overall') || recommendations[0];
  const bestValue = recommendations.find(r => r.badge === 'Best Value') || recommendations[1];
  const bestPerf = recommendations.find(r => r.badge === 'Best Performance') || recommendations[2];
  const cheapest = recommendations.find(r => r.badge === 'Cheapest Suitable') || recommendations[3];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">
      <div>
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-amber-50 border border-amber-200 text-amber-800 text-xs font-bold mb-2">
          <Award className="w-3.5 h-3.5" /> AI Recommendation Engine
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
          Curated Category Champions
        </h1>
        <p className="text-sm text-slate-500 max-w-2xl">
          Multi-factor scored across requirement match (30%), price justification (25%), compute performance (20%), buyer sentiment (15%), and warranty (10%).
        </p>
      </div>

      {/* Hero Category Winners Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {[
          { item: bestOverall, title: "🏆 Best Overall", subtitle: "Top Balanced Choice", border: "border-amber-300 bg-amber-50/20" },
          { item: bestValue, title: "💰 Best Value", subtitle: "Maximum Spec per Rupee", border: "border-emerald-300 bg-emerald-50/20" },
          { item: bestPerf, title: "⚡ Best Performance", subtitle: "Maximum Compute & TGP", border: "border-indigo-300 bg-indigo-50/20" },
          { item: cheapest, title: "💵 Cheapest Suitable", subtitle: "Most Affordable Qualified", border: "border-blue-300 bg-blue-50/20" }
        ].map((card, idx) => card.item ? (
          <div key={idx} className={`rounded-3xl p-5 border-2 shadow-sm flex flex-col justify-between ${card.border}`}>
            <div>
              <div className="flex justify-between items-start mb-3">
                <span className="font-extrabold text-slate-900 text-base">{card.title}</span>
                <span className="text-xs font-bold px-2 py-0.5 rounded-full bg-white text-indigo-700 shadow-sm">
                  {card.item.score_overall}%
                </span>
              </div>
              <img
                src={card.item.image_url || "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=800&q=80"}
                alt={card.item.name}
                className="w-full h-36 object-cover rounded-xl mb-3 shadow-sm"
              />
              <span className="text-xs font-bold text-indigo-600 uppercase tracking-wider">{card.item.brand}</span>
              <h3 className="font-bold text-slate-900 text-sm line-clamp-2 mb-2">{card.item.name}</h3>
              <div className="text-xl font-extrabold text-slate-900 mb-3">
                ₹{card.item.price.toLocaleString()}
              </div>
              <p className="text-xs text-slate-600 line-clamp-3 bg-white/80 p-2.5 rounded-xl border border-slate-200/60 mb-4">
                {card.item.recommendation_explanation}
              </p>
            </div>
            <Link
              to={`/products/${card.item.id}`}
              className="w-full py-2 bg-indigo-600 text-white rounded-xl text-xs font-semibold text-center hover:bg-indigo-700 transition-colors shadow-sm"
            >
              View Full Audit →
            </Link>
          </div>
        ) : null)}
      </div>

      {/* All Scored Recommendations List */}
      <div className="pt-8 border-t border-slate-200">
        <h2 className="text-xl font-bold text-slate-900 mb-6">All Evaluated Candidates</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {recommendations.map((p, i) => (
            <ProductCard key={i} product={p} />
          ))}
        </div>
      </div>
    </div>
  );
};
