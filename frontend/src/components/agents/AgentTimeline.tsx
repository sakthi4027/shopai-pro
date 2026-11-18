import React from 'react';
import { 
  CheckCircle, 
  Clock, 
  AlertCircle, 
  Loader2, 
  Cpu, 
  Terminal, 
  ShieldCheck, 
  Layers 
} from 'lucide-react';
import { AgentEvent } from '../../types';

interface AgentTimelineProps {
  events: AgentEvent[];
  activeAgent?: string;
  isComplete?: boolean;
}

export const AgentTimeline: React.FC<AgentTimelineProps> = ({
  events,
  activeAgent,
  isComplete
}) => {
  const agentRoster = [
    { name: 'Shopping Planner', role: 'Deconstructs requirements & user shopping memory' },
    { name: 'Product Search Agent', role: 'Live multi-source authorized search & URL deduplication' },
    { name: 'Product Extraction Agent', role: 'Normalizes structured specifications & hardware metrics' },
    { name: 'Product Safety / Trust Agent', role: 'Checks authenticity, seller ratings & warranty terms' },
    { name: 'Budget Intelligence Agent', role: 'Enforces budget ceiling and evaluates cost-benefit' },
    { name: 'Review Analysis Agent', role: 'Aspect sentiment analysis & buyer warning extraction' },
    { name: 'Price Intelligence Agent', role: 'Tracks observed price drops & cross-seller variances' },
    { name: 'Product Comparison Agent', role: 'Builds side-by-side matrices & evaluates winners' },
    { name: 'Recommendation Agent', role: 'Computes multi-factor scores & grounded rationale' },
    { name: 'Human-In-The-Loop Checkout Agent', role: 'Generates verified pre-checkout manifest' },
  ];

  return (
    <div className="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
      {/* Header */}
      <div className="p-5 border-b border-slate-100 flex items-center justify-between bg-slate-50/50">
        <div className="flex items-center gap-2.5">
          <div className="w-8 h-8 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center">
            <Cpu className="w-4 h-4" />
          </div>
          <div>
            <h3 className="font-bold text-slate-900 text-sm">Real-Time Shopping AI Agent</h3>
            <p className="text-xs text-slate-500">Autonomous cooperative pipeline with live telemetry</p>
          </div>
        </div>
        <div>
          {isComplete ? (
            <span className="inline-flex items-center gap-1 px-2.5 py-1 rounded-full text-xs font-semibold bg-emerald-100 text-emerald-800">
              <CheckCircle className="w-3.5 h-3.5" /> Pipeline Completed
            </span>
          ) : (
            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-semibold bg-indigo-100 text-indigo-700 animate-pulse">
              <Loader2 className="w-3.5 h-3.5 animate-spin" /> Shopping AI Active
            </span>
          )}
        </div>
      </div>

      <div className="p-5 grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Left: Agent Roster Status Matrix */}
        <div className="space-y-3">
          <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2">Agent Roster & State</h4>
          {agentRoster.map((agent, idx) => {
            const hasStarted = events.some(e => e.agent_name.toLowerCase().includes(agent.name.toLowerCase()));
            const isCompleted = events.some(e => e.agent_name.toLowerCase().includes(agent.name.toLowerCase()) && (e.status === 'completed' || isComplete));
            const isRunning = hasStarted && !isCompleted && !isComplete;

            return (
              <div
                key={agent.name}
                className={`p-3 rounded-xl border transition-all flex items-center justify-between text-xs ${
                  isCompleted
                    ? 'bg-emerald-50/40 border-emerald-200/60 text-emerald-950'
                    : isRunning
                    ? 'bg-indigo-50/80 border-indigo-200 text-indigo-950 shadow-sm'
                    : 'bg-slate-50/60 border-slate-200/60 text-slate-500'
                }`}
              >
                <div className="flex items-center gap-2.5">
                  <div className="w-5 text-slate-400 font-mono font-bold text-[10px]">
                    0{idx + 1}
                  </div>
                  <div>
                    <span className="font-bold text-slate-900 block text-xs">{agent.name}</span>
                    <span className="text-[11px] text-slate-500 line-clamp-1">{agent.role}</span>
                  </div>
                </div>

                <div className="flex items-center gap-1.5 shrink-0">
                  {isCompleted ? (
                    <span className="flex items-center gap-1 text-emerald-700 font-semibold bg-emerald-100/80 px-2 py-0.5 rounded-md text-[11px]">
                      <CheckCircle className="w-3 h-3 text-emerald-600" /> Done
                    </span>
                  ) : isRunning ? (
                    <span className="flex items-center gap-1 text-indigo-700 font-semibold bg-indigo-100 px-2 py-0.5 rounded-md text-[11px] animate-pulse">
                      <Loader2 className="w-3 h-3 animate-spin" /> Running
                    </span>
                  ) : (
                    <span className="text-slate-400 text-[11px] bg-slate-200/60 px-2 py-0.5 rounded-md">
                      Pending
                    </span>
                  )}
                </div>
              </div>
            );
          })}
        </div>

        {/* Right: Live Event Telemetry Stream */}
        <div className="flex flex-col h-full">
          <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-2 flex items-center gap-1.5">
            <Terminal className="w-3.5 h-3.5" /> Live Workflow Stream
          </h4>
          <div className="flex-1 bg-slate-900 rounded-xl p-4 font-mono text-xs text-slate-200 overflow-y-auto max-h-[460px] border border-slate-800 space-y-2.5">
            {events.length === 0 ? (
              <div className="text-slate-500 py-10 text-center flex flex-col items-center">
                <Loader2 className="w-6 h-6 animate-spin mb-2 text-indigo-400" />
                <span>Waiting for orchestrator dispatch...</span>
              </div>
            ) : (
              events.map((ev, i) => (
                <div key={i} className="flex items-start gap-2 border-b border-slate-800/60 pb-2">
                  <span className="text-indigo-400 font-semibold shrink-0">[{ev.agent_name}]:</span>
                  <span className={ev.status === 'error' ? 'text-rose-400' : ev.status === 'completed' ? 'text-emerald-400' : 'text-slate-300'}>
                    {ev.message}
                  </span>
                </div>
              ))
            )}
          </div>
        </div>
      </div>
    </div>
  );
};
