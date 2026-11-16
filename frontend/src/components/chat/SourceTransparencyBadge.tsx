import React from 'react';
import { CheckCircle2, AlertCircle, ShieldCheck } from 'lucide-react';
import { SourceStatus } from '../../types';

interface SourceTransparencyBadgeProps {
  sources: SourceStatus[];
}

export function SourceTransparencyBadge({ sources }: SourceTransparencyBadgeProps) {
  if (!sources || sources.length === 0) return null;

  const searched = sources.filter(s => s.status === 'searched');
  const unavailable = sources.filter(s => s.status !== 'searched');

  return (
    <div className="my-3 p-3 rounded-xl border border-slate-200 bg-slate-50 text-xs">
      <div className="flex items-center space-x-2 text-slate-700 font-semibold mb-2">
        <ShieldCheck className="h-4 w-4 text-indigo-600" />
        <span>Source Transparency Report ({searched.length} Active / {unavailable.length} Unavailable)</span>
      </div>

      <div className="flex flex-wrap gap-1.5">
        {searched.map((src, i) => (
          <span
            key={i}
            className="inline-flex items-center space-x-1 px-2.5 py-1 rounded-md bg-emerald-50 border border-emerald-200 text-emerald-800 text-[11px]"
            title={`Queried ${src.name}`}
          >
            <CheckCircle2 className="h-3 w-3 text-emerald-600" />
            <span className="font-medium">{src.name}</span>
            {src.products_count !== undefined && src.products_count > 0 && (
              <span className="text-[10px] text-emerald-600">({src.products_count})</span>
            )}
          </span>
        ))}

        {unavailable.map((src, i) => (
          <span
            key={`un-${i}`}
            className="inline-flex items-center space-x-1 px-2.5 py-1 rounded-md bg-amber-50 border border-amber-200 text-amber-800 text-[11px]"
            title={src.reason || 'Source temporarily unavailable'}
          >
            <AlertCircle className="h-3 w-3 text-amber-600" />
            <span className="font-medium">{src.name}</span>
            <span className="text-[10px] text-amber-600">(Protected)</span>
          </span>
        ))}
      </div>
      <p className="mt-1.5 text-[11px] text-slate-500 italic">
        *Zero fabricated results. Only authorized live sources are queried.
      </p>
    </div>
  );
}
