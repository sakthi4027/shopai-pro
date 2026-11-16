import React, { useState } from 'react';
import { Scale, ChevronDown, ChevronUp, Check, X } from 'lucide-react';
import { ChatProductItem } from '../../types';

interface ChatComparisonMatrixProps {
  products: ChatProductItem[];
  matrix?: Array<{ feature: string; key?: string; values: Record<string, string> }>;
}

export function ChatComparisonMatrix({ products, matrix }: ChatComparisonMatrixProps) {
  const [isExpanded, setIsExpanded] = useState(false);

  if (!products || products.length < 2) return null;

  const compareItems = products.slice(0, 3);

  // If matrix rows not provided by backend, build dynamic rows from products specs
  const rows = matrix && matrix.length > 0 ? matrix : [
    { feature: 'Price', values: Object.fromEntries(compareItems.map(p => [p.name, `₹${(p.lowest_price || p.price).toLocaleString()}`])) },
    { feature: 'RAM', values: Object.fromEntries(compareItems.map(p => [p.name, p.specifications?.ram_gb ? `${p.specifications.ram_gb}GB` : 'Standard'])) },
    { feature: 'Storage', values: Object.fromEntries(compareItems.map(p => [p.name, p.specifications?.storage_gb ? `${p.specifications.storage_gb >= 1000 ? `${(p.specifications.storage_gb/1024).toFixed(0)}TB` : `${p.specifications.storage_gb}GB`} SSD` : 'SSD'])) },
    { feature: 'GPU', values: Object.fromEntries(compareItems.map(p => [p.name, p.specifications?.gpu || 'Integrated'])) },
    { feature: 'Rating', values: Object.fromEntries(compareItems.map(p => [p.name, `${p.rating?.toFixed(1) || '4.4'} ★ (${p.review_count || 400})`])) },
    { feature: 'Best Seller', values: Object.fromEntries(compareItems.map(p => [p.name, p.lowest_price_seller || p.seller || 'Official'])) },
    { feature: 'AI Match', values: Object.fromEntries(compareItems.map(p => [p.name, `${Math.round(p.score_overall || 90)}%`])) },
  ];

  return (
    <div className="my-4 rounded-xl border border-slate-200 bg-white overflow-hidden shadow-xs">
      <button
        type="button"
        onClick={() => setIsExpanded(!isExpanded)}
        className="w-full px-4 py-2.5 bg-slate-50 border-b border-slate-200 flex items-center justify-between text-left hover:bg-slate-100 transition-colors cursor-pointer"
      >
        <div className="flex items-center space-x-2 text-xs font-bold text-slate-800">
          <Scale className="h-4 w-4 text-indigo-600" />
          <span>Side-by-Side Product Comparison ({compareItems.length} Products)</span>
        </div>
        <div className="flex items-center space-x-1 text-slate-500 text-xs">
          <span>{isExpanded ? 'Collapse matrix' : 'Expand matrix'}</span>
          {isExpanded ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
        </div>
      </button>

      {isExpanded && (
        <div className="overflow-x-auto">
          <table className="w-full text-xs text-left border-collapse">
            <thead>
              <tr className="bg-slate-50 border-b border-slate-200 text-slate-700">
                <th className="p-2.5 font-semibold w-28 shrink-0">Feature</th>
                {compareItems.map((p, idx) => (
                  <th key={idx} className="p-2.5 font-bold text-slate-900 min-w-36">
                    <div className="line-clamp-1">{p.name}</div>
                    <div className="text-[11px] font-normal text-indigo-600">
                      {p.badge || `Option ${idx + 1}`}
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100 text-slate-700">
              {rows.map((row, rIdx) => (
                <tr key={rIdx} className={rIdx % 2 === 0 ? 'bg-white' : 'bg-slate-50/50'}>
                  <td className="p-2.5 font-semibold text-slate-800 bg-slate-50/80">
                    {row.feature}
                  </td>
                  {compareItems.map((p, cIdx) => (
                    <td key={cIdx} className="p-2.5">
                      {row.values[p.name] || '—'}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}
