import React from 'react';
import { ShieldCheck, Lock, Cpu, Sparkles } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="bg-white border-t border-slate-200 mt-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div className="md:col-span-2">
            <div className="flex items-center gap-2 mb-3">
              <span className="font-bold text-slate-900 text-base">Antigravity ShopAI Multi-Agent System</span>
              <span className="text-xs bg-indigo-100 text-indigo-700 font-medium px-2 py-0.5 rounded-full">v1.0 Production</span>
            </div>
            <p className="text-sm text-slate-500 max-w-md leading-relaxed">
              Autonomous 10-agent shopping swarm coordinating real-time requirement extraction, live multi-source searches, verified spec auditing, sentiment analysis, and grounded recommendations.
            </p>
            <div className="flex items-center gap-4 mt-4 text-xs text-slate-500">
              <span className="flex items-center gap-1 text-emerald-600 font-medium">
                <ShieldCheck className="w-4 h-4" /> Zero Autonomous Purchases
              </span>
              <span className="flex items-center gap-1 text-slate-600">
                <Lock className="w-3.5 h-3.5" /> No Card Storage
              </span>
              <span className="flex items-center gap-1 text-slate-600">
                <Cpu className="w-3.5 h-3.5" /> 10 Active Agents
              </span>
            </div>
          </div>

          <div>
            <h4 className="text-xs font-semibold text-slate-900 uppercase tracking-wider mb-3">Architecture</h4>
            <ul className="space-y-2 text-sm text-slate-500">
              <li>Shopping Planner & Budget Agents</li>
              <li>Live Multi-Source Search & Deduplication</li>
              <li>Review Sentiment & Theme Analysis</li>
              <li>Price Intelligence & Trend Tracking</li>
              <li>Human-in-the-Loop Checkout Gate</li>
            </ul>
          </div>

          <div>
            <h4 className="text-xs font-semibold text-slate-900 uppercase tracking-wider mb-3">Security & Compliance</h4>
            <ul className="space-y-2 text-sm text-slate-500">
              <li>Isolated User Workspaces</li>
              <li>JWT & Role-Based Access Control</li>
              <li>Model Context Protocol (MCP) Tools</li>
              <li>Playwright Anti-Bot Safe Pause</li>
              <li>Audit Trail Logging</li>
            </ul>
          </div>
        </div>

        <div className="mt-8 pt-8 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-400">
          <p>© 2026 Antigravity ShopAI. All rights reserved.</p>
          <p className="flex items-center gap-1 mt-2 sm:mt-0">
            Powered by <Sparkles className="w-3.5 h-3.5 text-indigo-500" /> Multi-Agent Swarm Intelligence
          </p>
        </div>
      </div>
    </footer>
  );
};
