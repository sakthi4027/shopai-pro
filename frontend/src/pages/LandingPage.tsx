import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
  Bot, 
  Sparkles, 
  Search, 
  ArrowRight, 
  CheckCircle2, 
  ShieldCheck, 
  TrendingDown, 
  Cpu, 
  Layers, 
  Star 
} from 'lucide-react';

export const LandingPage: React.FC = () => {
  const navigate = useNavigate();
  const [quickQuery, setQuickQuery] = React.useState('');

  const sampleQueries = [
    "Find me a laptop under ₹80,000 with 32GB RAM, 1TB SSD, good battery life, and suitable for AI development.",
    "Best gaming laptop under ₹1 lakh with RTX GPU and high refresh display",
    "Lightweight coding laptop under ₹75,000 with minimum 16GB RAM and long battery"
  ];

  const handleSearch = (q: string) => {
    navigate(`/search?q=${encodeURIComponent(q)}`);
  };

  return (
    <div className="space-y-24 py-8">
      {/* Hero Section */}
      <section className="text-center max-w-4xl mx-auto px-4">
        <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-indigo-50 border border-indigo-100 text-indigo-700 text-xs font-semibold mb-6 shadow-sm">
          <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
          Autonomous 10-Agent Swarm Intelligence
        </div>

        <h1 className="text-4xl sm:text-6xl font-black text-slate-900 tracking-tight leading-[1.15] mb-6">
          The Intelligent Shopping Swarm That{' '}
          <span className="bg-gradient-to-r from-indigo-600 via-violet-600 to-indigo-700 bg-clip-text text-transparent">
            Thinks, Verifies & Compares
          </span>
        </h1>

        <p className="text-lg text-slate-600 max-w-2xl mx-auto mb-10 leading-relaxed font-normal">
          Tell our AI swarm what you need in plain English. Ten specialized agents dissect hardware specs, search live merchant sources, audit customer reviews, track price trends, and rank recommendations — with strict human approval before purchase.
        </p>

        {/* Big Search Input */}
        <div className="max-w-2xl mx-auto bg-white p-2 rounded-2xl shadow-xl shadow-indigo-100/50 border border-slate-200/80 mb-6">
          <form
            onSubmit={(e) => {
              e.preventDefault();
              if (quickQuery.trim()) handleSearch(quickQuery);
            }}
            className="flex items-center gap-2"
          >
            <div className="pl-3 text-slate-400">
              <Search className="w-5 h-5 text-indigo-500" />
            </div>
            <input
              type="text"
              value={quickQuery}
              onChange={(e) => setQuickQuery(e.target.value)}
              placeholder="e.g. Find me a laptop under ₹80,000 with 32GB RAM and 1TB SSD for AI..."
              className="flex-1 py-3 px-2 text-sm text-slate-800 placeholder-slate-400 focus:outline-none"
            />
            <button
              type="submit"
              className="px-6 py-3 bg-indigo-600 hover:bg-indigo-700 text-white font-semibold text-sm rounded-xl shadow-md shadow-indigo-200 flex items-center gap-2 transition-colors"
            >
              Ask AI <ArrowRight className="w-4 h-4" />
            </button>
          </form>
        </div>

        {/* Quick Sample Prompts */}
        <div className="flex flex-wrap items-center justify-center gap-2 text-xs text-slate-500">
          <span className="font-semibold text-slate-700">Try asking:</span>
          {sampleQueries.map((q, idx) => (
            <button
              key={idx}
              onClick={() => handleSearch(q)}
              className="px-3 py-1 bg-white hover:bg-indigo-50 hover:text-indigo-700 border border-slate-200 rounded-lg text-slate-600 transition-colors text-left"
            >
              "{q.slice(0, 48)}..."
            </button>
          ))}
        </div>
      </section>

      {/* 10-Agent Swarm Section */}
      <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center max-w-2xl mx-auto mb-16">
          <h2 className="text-3xl font-extrabold text-slate-900 tracking-tight mb-3">
            Ten Specialized Agents Working in Harmony
          </h2>
          <p className="text-slate-600 text-sm">
            Rather than relying on a single prompt, our architecture decomposes your goal into specialized cooperative agents.
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[
            { title: "Shopping Planner", desc: "Transforms conversational input into precise structured constraints: category, budget ceiling, required vs preferred specs.", icon: Bot },
            { title: "Product Search & Deduplication", desc: "Searches authorized online store sources, detects duplicates, normalizes URLs, and verifies stock availability.", icon: Search },
            { title: "Product Extraction Agent", desc: "Extracts normalized hardware specifications (RAM, SSD, CPU, GPU, thermals, display, official warranty).", icon: Cpu },
            { title: "Product Safety / Trust Agent", desc: "Audits seller credentials, catches deceptive discount inflation, and flags unverified hardware claims.", icon: ShieldCheck },
            { title: "Review Analysis Agent", desc: "Synthesizes genuine buyer sentiment across battery, thermals, software, and build quality without fabricating reviews.", icon: Star },
            { title: "Price Intelligence Agent", desc: "Analyzes historical price trends, calculates discounts, and audits cross-merchant price variances.", icon: TrendingDown },
            { title: "Product Comparison Agent", desc: "Generates feature delta matrices and highlights category champions (Best Value, Best Perf, Cheapest Suitable).", icon: Layers },
            { title: "Recommendation Agent", desc: "Computes weighted multi-factor recommendation scores with transparent, grounded rationales.", icon: Sparkles },
            { title: "Human-In-The-Loop Checkout", desc: "Zero autonomous financial transactions. Every purchase requires explicit itemized human confirmation.", icon: CheckCircle2 }
          ].map((ag, i) => {
            const Icon = ag.icon;
            return (
              <div key={i} className="p-6 bg-white rounded-2xl border border-slate-200/80 shadow-sm hover:shadow-md transition-shadow">
                <div className="w-10 h-10 rounded-xl bg-indigo-50 text-indigo-600 flex items-center justify-center mb-4">
                  <Icon className="w-5 h-5" />
                </div>
                <h3 className="font-bold text-slate-900 text-base mb-2">{ag.title}</h3>
                <p className="text-xs text-slate-500 leading-relaxed">{ag.desc}</p>
              </div>
            );
          })}
        </div>
      </section>

      {/* Safety & Isolation Guarantee */}
      <section className="max-w-5xl mx-auto px-4 bg-gradient-to-tr from-slate-900 to-indigo-950 text-white rounded-3xl p-8 sm:p-12 shadow-2xl">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
          <div>
            <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-semibold mb-4 border border-emerald-500/30">
              <ShieldCheck className="w-4 h-4" /> Ironclad Security & Privacy
            </div>
            <h2 className="text-2xl sm:text-3xl font-extrabold mb-4 leading-tight">
              AI Never Purchases Without Explicit Confirmation
            </h2>
            <p className="text-sm text-slate-300 leading-relaxed mb-6">
              Financial safety is our core constraint. The system cannot make autonomous transactions or store payment cards. Every purchase requires an itemized visual confirmation with clear seller, tax, and shipping breakdowns.
            </p>
            <div className="space-y-2 text-xs text-slate-300">
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>Isolated user memory, searches, and price alerts</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>No credit card or payment details stored anywhere</span>
              </div>
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400" />
                <span>Anti-bot & CAPTCHA respect with safe human pauses</span>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/80 rounded-2xl p-6 border border-slate-700/80 backdrop-blur-md">
            <div className="text-xs font-mono text-amber-300 mb-2">⚠️ HUMAN CONFIRMATION REQUIRED</div>
            <div className="bg-slate-900/90 rounded-xl p-4 text-xs font-mono space-y-2 border border-slate-700">
              <div className="flex justify-between text-slate-400">
                <span>Product:</span>
                <span className="text-white font-semibold">Lenovo Legion Slim 5</span>
              </div>
              <div className="flex justify-between text-slate-400">
                <span>Price:</span>
                <span className="text-white font-semibold">₹79,990</span>
              </div>
              <div className="flex justify-between text-slate-400">
                <span>Seller:</span>
                <span className="text-white font-semibold">Lenovo Official Store</span>
              </div>
              <div className="flex justify-between text-slate-400">
                <span>Shipping:</span>
                <span className="text-emerald-400 font-semibold">₹0 (Free)</span>
              </div>
              <div className="pt-2 border-t border-slate-700 flex justify-between font-bold text-sm">
                <span>Total:</span>
                <span className="text-indigo-400">₹79,990</span>
              </div>
            </div>
            <div className="flex gap-2 mt-4 text-xs">
              <button className="flex-1 py-2 bg-slate-700 text-slate-300 rounded-lg text-center font-semibold">Cancel</button>
              <button className="flex-1 py-2 bg-indigo-600 text-white rounded-lg text-center font-semibold">Confirm</button>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};
