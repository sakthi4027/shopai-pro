import React, { useState, useRef, useEffect } from 'react';
import { Send, Sparkles, Loader2, Zap, Search, BrainCircuit } from 'lucide-react';

interface ChatInputBoxProps {
  onSendMessage: (content: string) => void;
  isLoading?: boolean;
  searchMode: string;
  onSelectSearchMode: (mode: string) => void;
  placeholder?: string;
}

export function ChatInputBox({
  onSendMessage,
  isLoading = false,
  searchMode,
  onSelectSearchMode,
  placeholder = "Ask any shopping question (e.g., 'Find me a laptop under ₹80,000 for AI dev' or 'Cheapest 1TB SSD')..."
}: ChatInputBoxProps) {
  const [input, setInput] = useState('');
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-resize textarea height
  useEffect(() => {
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
      textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 160)}px`;
    }
  }, [input]);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;
    onSendMessage(input.trim());
    setInput('');
    if (textareaRef.current) {
      textareaRef.current.style.height = 'auto';
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <div className="w-full max-w-4xl mx-auto px-4 pb-4 pt-2">
      <form
        onSubmit={handleSubmit}
        className="relative rounded-2xl border border-slate-300 bg-white shadow-md focus-within:border-indigo-500 focus-within:ring-2 focus-within:ring-indigo-100 transition-all overflow-hidden"
      >
        <textarea
          ref={textareaRef}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          rows={1}
          disabled={isLoading}
          className="w-full resize-none border-0 bg-transparent px-4 pt-3.5 pb-12 text-sm text-slate-800 placeholder-slate-400 focus:outline-hidden focus:ring-0 leading-relaxed"
        />

        {/* Bottom Toolbar inside input box */}
        <div className="absolute bottom-2.5 left-3 right-3 flex items-center justify-between pointer-events-auto">
          {/* Search Depth Selector Pill */}
          <div className="flex items-center space-x-1 bg-slate-100 p-0.5 rounded-lg text-[11px] font-semibold text-slate-600">
            <button
              type="button"
              onClick={() => onSelectSearchMode('quick')}
              className={`px-2 py-1 rounded-md transition-colors flex items-center space-x-1 cursor-pointer ${
                searchMode === 'quick' ? 'bg-white text-indigo-700 shadow-xs' : 'hover:text-slate-900'
              }`}
            >
              <Zap className="h-3 w-3" />
              <span>Quick</span>
            </button>
            <button
              type="button"
              onClick={() => onSelectSearchMode('deep')}
              className={`px-2 py-1 rounded-md transition-colors flex items-center space-x-1 cursor-pointer ${
                searchMode === 'deep' ? 'bg-white text-indigo-700 shadow-xs' : 'hover:text-slate-900'
              }`}
            >
              <Search className="h-3 w-3" />
              <span>Deep</span>
            </button>
            <button
              type="button"
              onClick={() => onSelectSearchMode('maximum')}
              className={`px-2 py-1 rounded-md transition-colors flex items-center space-x-1 cursor-pointer ${
                searchMode === 'maximum' ? 'bg-white text-indigo-700 shadow-xs' : 'hover:text-slate-900'
              }`}
            >
              <BrainCircuit className="h-3 w-3" />
              <span>Max</span>
            </button>
          </div>

          {/* Send Button */}
          <button
            type="submit"
            disabled={!input.trim() || isLoading}
            className={`p-2 rounded-xl flex items-center justify-center transition-colors cursor-pointer ${
              input.trim() && !isLoading
                ? 'bg-indigo-600 hover:bg-indigo-700 text-white shadow-xs'
                : 'bg-slate-100 text-slate-400 cursor-not-allowed'
            }`}
            title="Send query (Enter)"
          >
            {isLoading ? (
              <Loader2 className="h-4 w-4 animate-spin text-indigo-600" />
            ) : (
              <Send className="h-4 w-4" />
            )}
          </button>
        </div>
      </form>

      <p className="mt-2 text-center text-[11px] text-slate-400">
        Strict Zero-Autonomous Purchase Guarantee. Human confirmation required before any checkout.
      </p>
    </div>
  );
}
