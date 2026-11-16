import React, { useState } from 'react';
import { Bot, User, Sparkles, Copy, Check, ChevronRight } from 'lucide-react';
import { ChatMessage, ChatProductItem, ProductSellerOption } from '../../types';
import { ThinkingAccordion } from './ThinkingAccordion';
import { SourceTransparencyBadge } from './SourceTransparencyBadge';
import { ChatProductCard } from './ChatProductCard';
import { ChatComparisonMatrix } from './ChatComparisonMatrix';

interface ChatMessageItemProps {
  message: ChatMessage;
  isStreaming?: boolean;
  onSuggestionClick?: (suggestion: string) => void;
  onCompareProduct?: (product: ChatProductItem) => void;
  onSaveProduct?: (product: ChatProductItem) => void;
  onTrackPriceProduct?: (product: ChatProductItem) => void;
  onCheckoutAssist?: (product: ChatProductItem, seller: ProductSellerOption) => void;
}

export function ChatMessageItem({
  message,
  isStreaming = false,
  onSuggestionClick,
  onCompareProduct,
  onSaveProduct,
  onTrackPriceProduct,
  onCheckoutAssist
}: ChatMessageItemProps) {
  const [copied, setCopied] = useState(false);
  const [visibleProductCount, setVisibleProductCount] = useState(3);

  const isUser = message.role === 'user';
  const products = message.products_payload || [];
  const totalFound = message.total_products_found || products.length;

  const handleCopy = () => {
    navigator.clipboard.writeText(message.content);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  if (isUser) {
    return (
      <div className="flex justify-end mb-6">
        <div className="flex items-start space-x-2.5 max-w-2xl">
          <div className="rounded-2xl bg-indigo-600 text-white px-4 py-3 shadow-xs">
            <p className="text-sm leading-relaxed whitespace-pre-wrap font-medium">
              {message.content}
            </p>
          </div>
          <div className="w-8 h-8 rounded-full bg-slate-200 border border-slate-300 flex items-center justify-center shrink-0 text-slate-600">
            <User className="h-4 w-4" />
          </div>
        </div>
      </div>
    );
  }

  const displayedProducts = products.slice(0, visibleProductCount);
  const hasMoreProducts = products.length > visibleProductCount;

  return (
    <div className="flex justify-start mb-8">
      <div className="flex items-start space-x-3 w-full max-w-4xl">
        <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-indigo-600 to-violet-600 text-white flex items-center justify-center shrink-0 shadow-sm mt-0.5">
          <Sparkles className="h-4 w-4" />
        </div>

        <div className="flex-1 min-w-0 bg-white rounded-2xl border border-slate-200 p-4 sm:p-6 shadow-xs">
          {/* Real-time Agent Thinking Progress */}
          {message.agent_steps && message.agent_steps.length > 0 && (
            <ThinkingAccordion steps={message.agent_steps} isStreaming={isStreaming} />
          )}

          {/* Sources Transparency Report */}
          {message.sources_status && message.sources_status.length > 0 && (
            <SourceTransparencyBadge sources={message.sources_status} />
          )}

          {/* Assistant Text Content / Markdown */}
          <div className="text-sm text-slate-800 leading-relaxed space-y-3 prose-sm max-w-none">
            {message.content.split('\n\n').map((paragraph, pIdx) => {
              if (paragraph.startsWith('### ')) {
                return (
                  <h4 key={pIdx} className="text-base font-bold text-slate-900 mt-4 mb-1">
                    {paragraph.replace('### ', '')}
                  </h4>
                );
              }
              return (
                <p key={pIdx} className="leading-relaxed">
                  {paragraph}
                </p>
              );
            })}
          </div>

          {/* Embedded Product Result Cards */}
          {displayedProducts.length > 0 && (
            <div className="mt-5 border-t border-slate-100 pt-3">
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-500">
                  Top Recommended Products ({totalFound} Available)
                </span>
                {totalFound > products.length && (
                  <span className="text-xs text-indigo-600 font-medium">
                    Showing strongest matches
                  </span>
                )}
              </div>

              <div className="space-y-4">
                {displayedProducts.map((p, idx) => (
                  <ChatProductCard
                    key={p.id || idx}
                    product={p}
                    onCompare={onCompareProduct}
                    onSave={onSaveProduct}
                    onTrackPrice={onTrackPriceProduct}
                    onCheckoutAssist={onCheckoutAssist}
                  />
                ))}
              </div>

              {/* Load More Button - Satisfies Section 3: No Artificial Limit */}
              {hasMoreProducts && (
                <button
                  type="button"
                  onClick={() => setVisibleProductCount(prev => prev + 5)}
                  className="mt-3 w-full py-2.5 rounded-xl border border-indigo-200 bg-indigo-50/50 hover:bg-indigo-100/70 text-indigo-700 text-xs font-bold transition-colors flex items-center justify-center space-x-1.5 cursor-pointer"
                >
                  <span>Load more products ({products.length - visibleProductCount} remaining)</span>
                  <ChevronRight className="h-4 w-4" />
                </button>
              )}
            </div>
          )}

          {/* Embedded Comparison Matrix */}
          {products.length >= 2 && (
            <ChatComparisonMatrix
              products={products}
              matrix={message.comparison_payload?.matrix}
            />
          )}

          {/* Follow-up Suggestion Pills */}
          {message.follow_up_suggestions && message.follow_up_suggestions.length > 0 && (
            <div className="mt-5 pt-3 border-t border-slate-100">
              <p className="text-xs font-semibold text-slate-600 mb-2">
                Suggested Follow-up Refinements:
              </p>
              <div className="flex flex-wrap gap-1.5">
                {message.follow_up_suggestions.map((suggestion, sIdx) => (
                  <button
                    key={sIdx}
                    type="button"
                    onClick={() => onSuggestionClick && onSuggestionClick(suggestion)}
                    className="px-3 py-1.5 rounded-full text-xs font-medium bg-slate-100 hover:bg-indigo-50 hover:text-indigo-700 hover:border-indigo-200 text-slate-700 border border-slate-200 transition-colors text-left cursor-pointer"
                  >
                    {suggestion}
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Message Footer & Copy */}
          <div className="mt-4 pt-2 flex items-center justify-between text-xs text-slate-400">
            <span>
              {new Date(message.created_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
            </span>
            <button
              type="button"
              onClick={handleCopy}
              className="flex items-center space-x-1 hover:text-slate-600 transition-colors cursor-pointer"
            >
              {copied ? <Check className="h-3 w-3 text-emerald-600" /> : <Copy className="h-3 w-3" />}
              <span>{copied ? 'Copied' : 'Copy'}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
