import React, { useState } from 'react';
import { Activity, Cpu, CheckCircle, Loader2, Clock, Wrench, ShieldCheck, Zap } from 'lucide-react';
import { AgentTimeline } from '../components/agents/AgentTimeline';

export const AIAgentActivityPage: React.FC = () => {
  const [activeTab, setActiveTab] = useState<'roster' | 'tools' | 'architecture'>('roster');

  const agents = [
    { name: 'Shopping Planner', status: 'Completed', latency: '210ms', tools: ['shopping_preferences'], confidence: '98%', tokens: 320, task: 'Parsed category, 80k budget ceiling, 32GB RAM, 1TB SSD constraints' },
    { name: 'Product Search Agent', status: 'Completed', latency: '440ms', tools: ['product_search'], confidence: '96%', tokens: 680, task: 'Retrieved and deduplicated live candidate feeds from Amazon & Flipkart' },
    { name: 'Product Extraction Agent', status: 'Completed', latency: '190ms', tools: ['product_details'], confidence: '99%', tokens: 410, task: 'Normalized CPU, GPU, RAM, screen size, and warranty attributes' },
    { name: 'Product Safety / Trust Agent', status: 'Completed', latency: '140ms', tools: ['seller_lookup'], confidence: '94%', tokens: 380, task: 'Audited seller reputation and quarantined 1 deceptive listing' },
    { name: 'Budget Intelligence Agent', status: 'Completed', latency: '90ms', tools: [], confidence: '100%', tokens: 190, task: 'Categorized items into Within Budget, Near Budget, and Over Budget' },
    { name: 'Review Analysis Agent', status: 'Completed', latency: '380ms', tools: ['review_search'], confidence: '92%', tokens: 840, task: 'Analyzed aspect sentiment for cooling, display brightness, and battery' },
    { name: 'Price Intelligence Agent', status: 'Completed', latency: '230ms', tools: ['price_lookup', 'price_history'], confidence: '95%', tokens: 490, task: 'Audited historical price drops and computed cross-merchant variances' },
    { name: 'Product Comparison Agent', status: 'Completed', latency: '180ms', tools: ['product_compare'], confidence: '97%', tokens: 520, task: 'Constructed comparative spec delta matrix and highlighted category winners' },
    { name: 'Recommendation Agent', status: 'Completed', latency: '290ms', tools: [], confidence: '96%', tokens: 650, task: 'Computed weighted multi-factor scores and grounded rationale' },
    { name: 'Human-In-The-Loop Checkout', status: 'Standby / Gated', latency: '80ms', tools: ['notification_service'], confidence: '100%', tokens: 120, task: 'Constructs verified manifest requiring explicit human [Confirm] click' },
  ];

  const mcpTools = [
    { name: 'product_search', desc: 'Searches verified authorized product sources based on query, constraints, and brands.' },
    { name: 'product_details', desc: 'Fetches complete structured product specifications, model attributes, and verification status.' },
    { name: 'price_lookup', desc: 'Retrieves current prices across verified sellers and checks best available deal.' },
    { name: 'review_search', desc: 'Retrieves authenticated customer reviews filtered by aspects like battery, heating, performance.' },
    { name: 'seller_lookup', desc: 'Inspects merchant credentials, trustworthiness score, and return policies.' },
    { name: 'availability_check', desc: 'Checks regional delivery turnaround and real-time inventory for a product.' },
    { name: 'product_compare', desc: 'Computes side-by-side specification diff matrix for up to 4 products.' },
    { name: 'price_history', desc: 'Fetches historical price timestamps and computes market trend.' },
    { name: 'shopping_preferences', desc: 'Reads or updates persistent user shopping preferences with strict user isolation.' },
    { name: 'notification_service', desc: 'Dispatches price-drop and back-in-stock alerts to authorized user channels.' }
  ];

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div>
        <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-indigo-50 border border-indigo-200 text-indigo-700 text-xs font-bold mb-2">
          <Activity className="w-3.5 h-3.5" /> Swarm Observability
        </div>
        <h1 className="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
          AI Agent Activity & Swarm Telemetry
        </h1>
        <p className="text-sm text-slate-500">
          Live monitoring of agent task execution, tool calls, token usage, latency, and confidence metrics.
        </p>
      </div>

      {/* Tabs */}
      <div className="flex gap-2 border-b border-slate-200 pb-3">
        <button
          onClick={() => setActiveTab('roster')}
          className={`px-4 py-2 rounded-xl text-xs font-bold transition-colors ${
            activeTab === 'roster' ? 'bg-indigo-600 text-white shadow-sm' : 'text-slate-600 hover:bg-slate-100'
          }`}
        >
          Active Agents ({agents.length})
        </button>
        <button
          onClick={() => setActiveTab('tools')}
          className={`px-4 py-2 rounded-xl text-xs font-bold transition-colors ${
            activeTab === 'tools' ? 'bg-indigo-600 text-white shadow-sm' : 'text-slate-600 hover:bg-slate-100'
          }`}
        >
          Model Context Protocol (MCP) Tools ({mcpTools.length})
        </button>
      </div>

      {activeTab === 'roster' ? (
        <div className="bg-white rounded-3xl border border-slate-200 shadow-sm overflow-hidden">
          <table className="w-full text-left border-collapse text-xs">
            <thead>
              <tr className="bg-slate-50 border-b border-slate-200 text-slate-500 uppercase font-bold text-[11px]">
                <th className="p-4">Agent Name</th>
                <th className="p-4">Status</th>
                <th className="p-4">Current / Last Task</th>
                <th className="p-4">Execution Time</th>
                <th className="p-4">Tool Calls</th>
                <th className="p-4">Confidence</th>
                <th className="p-4">Tokens</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              {agents.map((ag, i) => (
                <tr key={i} className="hover:bg-slate-50/60 transition-colors">
                  <td className="p-4 font-bold text-slate-900 flex items-center gap-2">
                    <div className="w-2 h-2 rounded-full bg-emerald-500" />
                    {ag.name}
                  </td>
                  <td className="p-4">
                    <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-emerald-100 text-emerald-800">
                      <CheckCircle className="w-3 h-3 text-emerald-600" /> {ag.status}
                    </span>
                  </td>
                  <td className="p-4 text-slate-600 max-w-xs truncate">{ag.task}</td>
                  <td className="p-4 font-mono text-slate-500">{ag.latency}</td>
                  <td className="p-4">
                    {ag.tools.length > 0 ? (
                      <div className="flex flex-wrap gap-1">
                        {ag.tools.map(t => (
                          <span key={t} className="px-2 py-0.5 bg-indigo-50 text-indigo-700 rounded font-mono text-[10px]">
                            {t}
                          </span>
                        ))}
                      </div>
                    ) : (
                      <span className="text-slate-400">—</span>
                    )}
                  </td>
                  <td className="p-4 font-bold text-slate-900">{ag.confidence}</td>
                  <td className="p-4 font-mono text-slate-500">{ag.tokens}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {mcpTools.map((tool, idx) => (
            <div key={idx} className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-2">
              <div className="flex items-center gap-2 text-indigo-600 font-mono font-bold text-sm">
                <Wrench className="w-4 h-4" /> {tool.name}
              </div>
              <p className="text-xs text-slate-600 leading-relaxed">{tool.desc}</p>
              <div className="flex items-center gap-2 pt-2 text-[11px] text-slate-400 font-medium">
                <ShieldCheck className="w-3.5 h-3.5 text-emerald-600" /> Pydantic v2 Schema Validated
                <span>•</span>
                <span>Timeout: 5.0s</span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
