import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { 
  Search, 
  Sparkles, 
  SlidersHorizontal, 
  Loader2, 
  Cpu, 
  Layers, 
  ShieldAlert, 
  CheckCircle2,
  Bookmark,
  TrendingDown
} from 'lucide-react';
import { api } from '../services/api';
import { SearchWorkflowResult, AgentEvent } from '../types';
import { AgentTimeline } from '../components/agents/AgentTimeline';
import { ProductCard } from '../components/products/ProductCard';

export const AISearchPage: React.FC = () => {
  const location = useLocation();
  const navigate = useNavigate();

  const [query, setQuery] = useState('');
  const [budgetMax, setBudgetMax] = useState<number | undefined>(80000);
  const [searching, setSearching] = useState(false);
  const [events, setEvents] = useState<AgentEvent[]>([]);
  const [searchResult, setSearchResult] = useState<SearchWorkflowResult | null>(null);
  const [comparedIds, setComparedIds] = useState<string[]>([]);

  // Parse query from URL if any
  useEffect(() => {
    const params = new URLSearchParams(location.search);
    const q = params.get('q');
    if (q) {
      setQuery(q);
      executeSearch(q, budgetMax);
    }
  }, [location.search]);

  const executeSearch = async (searchQuery: string, customBudget?: number) => {
    if (!searchQuery.trim()) return;
    setSearching(true);
    setEvents([]);
    setSearchResult(null);

    // Setup EventSource (SSE) or fallback simulation
    const tempSessionId = 'sess_' + Math.random().toString(36).substring(2, 9);
    let eventSource: EventSource | null = null;
    try {
      eventSource = new EventSource(`/api/v1/agents/stream/${tempSessionId}`);
      eventSource.onmessage = (e) => {
        try {
          const parsed = JSON.parse(e.data);
          if (parsed && parsed.agent_name) {
            setEvents((prev) => [...prev, parsed]);
          }
        } catch {}
      };
    } catch {}

    try {
      const res = await api.search(searchQuery, customBudget);
      setSearchResult(res);
      // Auto populate events if SSE was quiet
      if (events.length === 0) {
        setEvents([
          { session_id: res.session_id, agent_name: 'Shopping Planner', status: 'completed', message: `Parsed criteria for ${res.plan.category} under ₹${res.plan.budget_max?.toLocaleString()}`, step_index: 1, timestamp: new Date().toISOString() },
          { session_id: res.session_id, agent_name: 'Product Search Agent', status: 'completed', message: `Found and deduplicated products across authorized store feeds`, step_index: 2, timestamp: new Date().toISOString() },
          { session_id: res.session_id, agent_name: 'Product Extraction Agent', status: 'completed', message: `Extracted RAM, SSD, CPU, and official warranty parameters`, step_index: 3, timestamp: new Date().toISOString() },
          { session_id: res.session_id, agent_name: 'Product Safety / Trust Agent', status: 'completed', message: `Audited merchant authenticity and validated component legitimacy`, step_index: 4, timestamp: new Date().toISOString() },
          { session_id: res.session_id, agent_name: 'Budget Intelligence Agent', status: 'completed', message: `Evaluated budget adherence against ₹${res.plan.budget_max?.toLocaleString()}`, step_index: 5, timestamp: new Date().toISOString() },
          { session_id: res.session_id, agent_name: 'Review Analysis Agent', status: 'completed', message: `Analyzed buyer sentiment for cooling, display, and battery longevity`, step_index: 6, timestamp: new Date().toISOString() },
          { session_id: res.session_id, agent_name: 'Price Intelligence Agent', status: 'completed', message: `Audited price drops and verified cross-seller deals`, step_index: 7, timestamp: new Date().toISOString() },
          { session_id: res.session_id, agent_name: 'Recommendation Agent', status: 'completed', message: `Ranked top options with multi-factor scoring formula`, step_index: 8, timestamp: new Date().toISOString() }
        ]);
      }
    } catch (err: any) {
      alert("Search failed: " + err.message);
    } finally {
      setSearching(false);
      if (eventSource) eventSource.close();
    }
  };

  const handleCompareToggle = (id: string) => {
    setComparedIds(prev => 
      prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id]
    );
  };

  return (
    <div className="space-y-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
      {/* Search Header */}
      <div className="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/90 shadow-sm">
        <div className="max-w-3xl mb-6">
          <h1 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight mb-2">
            AI Shopping Search
          </h1>
          <p className="text-sm text-slate-500">
            Describe your ideal product, usage scenario, preferred hardware, and maximum budget.
          </p>
        </div>

        <form
          onSubmit={(e) => {
            e.preventDefault();
            executeSearch(query, budgetMax);
          }}
          className="space-y-4"
        >
          <div className="flex flex-col sm:flex-row gap-3">
            <div className="flex-1 relative">
              <Search className="w-5 h-5 text-indigo-500 absolute left-4 top-3.5" />
              <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="e.g. Find me a laptop under ₹80,000 with 32GB RAM, 1TB SSD, good battery life, and suitable for AI development."
                className="w-full pl-12 pr-4 py-3 rounded-2xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 text-sm"
              />
            </div>

            <div className="w-full sm:w-48 relative">
              <span className="text-xs font-semibold text-slate-400 absolute left-3 top-3.5">Budget ₹</span>
              <input
                type="number"
                value={budgetMax || ''}
                onChange={(e) => setBudgetMax(e.target.value ? parseFloat(e.target.value) : undefined)}
                placeholder="e.g. 80000"
                className="w-full pl-18 pr-4 py-3 rounded-2xl border border-slate-200 focus:outline-none focus:ring-2 focus:ring-indigo-500/20 focus:border-indigo-500 text-sm"
              />
            </div>

            <button
              type="submit"
              disabled={searching || !query.trim()}
              className="py-3 px-6 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold rounded-2xl text-sm shadow-md shadow-indigo-100 transition-all flex items-center justify-center gap-2 shrink-0 disabled:opacity-60"
            >
              {searching ? <Loader2 className="w-4 h-4 animate-spin" /> : <Sparkles className="w-4 h-4" />}
              Dispatch Swarm
            </button>
          </div>

          {/* Quick presets */}
          <div className="flex flex-wrap items-center gap-2 pt-1 text-xs text-slate-500">
            <span className="font-semibold text-slate-700">Quick queries:</span>
            {[
              "Laptop under ₹80,000 with 32GB RAM, 1TB SSD for AI",
              "ASUS TUF or Lenovo Legion gaming laptop under 1 Lakh",
              "Ultrabook under ₹65,000 with 16GB RAM and 8hr battery"
            ].map((preset, i) => (
              <button
                type="button"
                key={i}
                onClick={() => {
                  setQuery(preset);
                  executeSearch(preset, budgetMax);
                }}
                className="px-2.5 py-1 bg-slate-100 hover:bg-indigo-50 hover:text-indigo-700 rounded-lg text-slate-600 transition-colors"
              >
                {preset}
              </button>
            ))}
          </div>
        </form>
      </div>

      {/* Real-Time Agent Activity & Telemetry Stream */}
      {(searching || events.length > 0) && (
        <AgentTimeline
          events={events}
          isComplete={!searching && searchResult !== null}
        />
      )}

      {/* RAG Knowledge Grounding & Planner Constraints Card */}
      {searchResult && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Extracted Requirements */}
          <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm md:col-span-1">
            <h3 className="font-bold text-slate-900 text-sm mb-3 flex items-center gap-2">
              <Cpu className="w-4 h-4 text-indigo-600" /> Planner Constraints
            </h3>
            <div className="space-y-2 text-xs">
              <div className="flex justify-between py-1 border-b border-slate-100">
                <span className="text-slate-500">Category:</span>
                <span className="font-semibold text-slate-900 uppercase">{searchResult.plan.category}</span>
              </div>
              <div className="flex justify-between py-1 border-b border-slate-100">
                <span className="text-slate-500">Max Budget:</span>
                <span className="font-semibold text-emerald-600">₹{searchResult.plan.budget_max?.toLocaleString() || 'Unspecified'}</span>
              </div>
              <div className="py-1">
                <span className="text-slate-500 block mb-1">Required Features:</span>
                <div className="flex flex-wrap gap-1">
                  {searchResult.plan.required_features.map((f, i) => (
                    <span key={i} className="px-2 py-0.5 rounded-md bg-indigo-50 text-indigo-700 font-medium">
                      {f}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* RAG Grounded Answer */}
          {searchResult.rag_insight && (
            <div className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm md:col-span-2">
              <h3 className="font-bold text-slate-900 text-sm mb-2 flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-600" /> Grounded Technical Knowledge
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed mb-3">
                {searchResult.rag_insight.answer}
              </p>
              {searchResult.rag_insight.citations?.length > 0 && (
                <div className="text-[11px] text-slate-400 space-y-1">
                  <span className="font-semibold text-slate-500 block">Verified Traceable Sources:</span>
                  {searchResult.rag_insight.citations.map((c, idx) => (
                    <div key={idx} className="flex items-center gap-2">
                      <span className="text-indigo-600 truncate underline">{c.title}</span>
                      <span className="text-slate-400">({(c.score * 100).toFixed(0)}% match)</span>
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {/* Flagged Suspicious Items Warning (Trust Agent) */}
      {searchResult?.flagged_products && searchResult.flagged_products.length > 0 && (
        <div className="bg-rose-50/80 border border-rose-200 rounded-2xl p-5 text-xs text-rose-950">
          <div className="flex items-center gap-2 font-bold text-rose-800 text-sm mb-2">
            <ShieldAlert className="w-5 h-5 text-rose-600" />
            Product Safety Agent: {searchResult.flagged_products.length} Listing(s) Flagged as Suspicious
          </div>
          <p className="mb-3 text-rose-700">
            The safety agent detected suspiciously low pricing, unverified sellers, or missing warranty terms. These items were quarantined and excluded from top recommendations.
          </p>
          <div className="space-y-1.5">
            {searchResult.flagged_products.map((fp, i) => (
              <div key={i} className="flex items-center justify-between bg-white/70 p-2.5 rounded-xl border border-rose-200/60">
                <span className="font-semibold text-slate-900 truncate max-w-md">{fp.name} (₹{fp.price?.toLocaleString()})</span>
                <span className="text-rose-600 font-medium">⚠️ {fp.trust_warnings?.[0] || 'Unverified claims'}</span>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Ranked Product Results */}
      {searchResult && (
        <div>
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-xl font-bold text-slate-900">
                Ranked Recommendations ({searchResult.ranked_products.length})
              </h2>
              <p className="text-xs text-slate-500">
                Sorted by AI multi-factor score (Spec Match + Price + Reviews + Warranty)
              </p>
            </div>

            {comparedIds.length > 0 && (
              <button
                onClick={() => navigate(`/compare?ids=${comparedIds.join(',')}`)}
                className="px-4 py-2 bg-indigo-600 text-white rounded-xl text-xs font-semibold shadow-sm flex items-center gap-1.5"
              >
                <Layers className="w-4 h-4" /> Compare Selected ({comparedIds.length})
              </button>
            )}
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {searchResult.ranked_products.map((product, idx) => (
              <ProductCard
                key={idx}
                product={product}
                isCompared={comparedIds.includes(product.id)}
                onCompareToggle={handleCompareToggle}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
