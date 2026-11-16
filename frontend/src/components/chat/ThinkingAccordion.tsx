import React, { useState } from 'react';
import { ChevronDown, ChevronUp, CheckCircle, Clock, AlertTriangle, Cpu } from 'lucide-react';
import { AgentStep } from '../../types';

interface ThinkingAccordionProps {
  steps: AgentStep[];
  isStreaming?: boolean;
}

export function ThinkingAccordion({ steps, isStreaming = false }: ThinkingAccordionProps) {
  const [isOpen, setIsOpen] = useState<boolean>(isStreaming || false);

  if (!steps || steps.length === 0) return null;

  const completedCount = steps.filter(s => s.status === 'completed' || s.status === 'progress').length;

  return (
    <div className="mb-4 rounded-xl border border-slate-200 bg-slate-50/80 overflow-hidden shadow-xs">
      <button
        type="button"
        onClick={() => setIsOpen(!isOpen)}
        className="w-full px-4 py-2.5 flex items-center justify-between text-left hover:bg-slate-100/70 transition-colors cursor-pointer"
      >
        <div className="flex items-center space-x-2.5">
          <div className="p-1 rounded-md bg-indigo-100 text-indigo-700">
            <Cpu className={`h-4 w-4 ${isStreaming ? 'animate-pulse' : ''}`} />
          </div>
          <span className="text-xs font-semibold text-slate-800 tracking-wide uppercase">
            {isStreaming ? 'Agents Researching Live...' : 'Multi-Agent Research Completed'}
          </span>
          <span className="px-2 py-0.5 rounded-full text-[11px] font-medium bg-slate-200 text-slate-700">
            {steps.length} steps
          </span>
        </div>
        <div className="flex items-center space-x-2 text-slate-500 text-xs">
          <span>{isOpen ? 'Hide reasoning' : 'View reasoning'}</span>
          {isOpen ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </div>
      </button>

      {isOpen && (
        <div className="px-4 py-3 border-t border-slate-200/80 bg-white/70 space-y-2 max-h-72 overflow-y-auto">
          {steps.map((step, idx) => {
            const isCompleted = step.status === 'completed';
            const isError = step.status === 'error';
            const isWarning = step.status === 'warning';

            return (
              <div key={idx} className="flex items-start space-x-2.5 text-xs text-slate-600">
                <div className="mt-0.5 shrink-0">
                  {isCompleted ? (
                    <CheckCircle className="h-3.5 w-3.5 text-emerald-600" />
                  ) : isWarning ? (
                    <AlertTriangle className="h-3.5 w-3.5 text-amber-500" />
                  ) : isError ? (
                    <AlertTriangle className="h-3.5 w-3.5 text-rose-500" />
                  ) : (
                    <Clock className="h-3.5 w-3.5 text-indigo-500 animate-spin" />
                  )}
                </div>
                <div className="flex-1 leading-relaxed">
                  <span className="font-semibold text-slate-800 mr-1.5">
                    {step.agent}:
                  </span>
                  <span>{step.message}</span>
                </div>
              </div>
            );
          })}
        </div>
      )}
    </div>
  );
}
