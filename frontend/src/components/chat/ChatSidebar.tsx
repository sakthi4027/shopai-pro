import React from 'react';
import { 
  Plus, 
  MessageSquare, 
  Trash2, 
  Sparkles, 
  Zap, 
  Search, 
  BrainCircuit, 
  Bookmark, 
  Bell, 
  SlidersHorizontal,
  X
} from 'lucide-react';
import { ConversationSummary } from '../../types';

interface ChatSidebarProps {
  conversations: ConversationSummary[];
  activeConversationId?: string;
  searchMode: string;
  onSelectConversation: (id: string) => void;
  onNewConversation: () => void;
  onDeleteConversation: (id: string, e: React.MouseEvent) => void;
  onSelectSearchMode: (mode: string) => void;
  onOpenPreferences?: () => void;
  isOpenMobile?: boolean;
  onCloseMobile?: () => void;
}

export function ChatSidebar({
  conversations,
  activeConversationId,
  searchMode,
  onSelectConversation,
  onNewConversation,
  onDeleteConversation,
  onSelectSearchMode,
  onOpenPreferences,
  isOpenMobile = false,
  onCloseMobile
}: ChatSidebarProps) {
  return (
    <aside
      className={`fixed inset-y-0 left-0 z-40 w-72 bg-slate-900 text-slate-200 flex flex-col transition-transform duration-300 md:static md:translate-x-0 ${
        isOpenMobile ? 'translate-x-0' : '-translate-x-full'
      }`}
    >
      {/* Top Header & Branding */}
      <div className="p-4 border-b border-slate-800 flex items-center justify-between">
        <div className="flex items-center space-x-2.5">
          <div className="w-8 h-8 rounded-lg bg-indigo-600 flex items-center justify-center text-white shadow-xs">
            <Sparkles className="h-4 w-4" />
          </div>
          <div>
            <h1 className="text-sm font-bold text-white tracking-tight">Shopping AI Agent</h1>
            <p className="text-[11px] text-slate-400">Deep Shopping Intelligence</p>
          </div>
        </div>

        {onCloseMobile && (
          <button
            type="button"
            onClick={onCloseMobile}
            className="md:hidden p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800"
          >
            <X className="h-4 w-4" />
          </button>
        )}
      </div>

      {/* New Research Button */}
      <div className="p-3">
        <button
          type="button"
          onClick={onNewConversation}
          className="w-full py-2.5 px-3.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold flex items-center justify-center space-x-2 shadow-xs transition-colors cursor-pointer"
        >
          <Plus className="h-4 w-4" />
          <span>New Shopping Research</span>
        </button>
      </div>

      {/* Research Depth Mode Selector - Section 24 */}
      <div className="px-3 py-2 border-b border-slate-800/80">
        <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1.5 px-1">
          Search Depth Mode
        </div>
        <div className="grid grid-cols-3 gap-1 bg-slate-800/90 p-1 rounded-xl text-[11px] font-semibold">
          <button
            type="button"
            onClick={() => onSelectSearchMode('quick')}
            className={`py-1.5 rounded-lg transition-colors flex items-center justify-center space-x-1 cursor-pointer ${
              searchMode === 'quick' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
            }`}
            title="Fast multi-merchant scan"
          >
            <Zap className="h-3 w-3" />
            <span>Quick</span>
          </button>
          <button
            type="button"
            onClick={() => onSelectSearchMode('deep')}
            className={`py-1.5 rounded-lg transition-colors flex items-center justify-center space-x-1 cursor-pointer ${
              searchMode === 'deep' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
            }`}
            title="Multi-source search with full spec & review analysis"
          >
            <Search className="h-3 w-3" />
            <span>Deep</span>
          </button>
          <button
            type="button"
            onClick={() => onSelectSearchMode('maximum')}
            className={`py-1.5 rounded-lg transition-colors flex items-center justify-center space-x-1 cursor-pointer ${
              searchMode === 'maximum' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
            }`}
            title="Exhaustive research with cross-seller pricing audit"
          >
            <BrainCircuit className="h-3 w-3" />
            <span>Max</span>
          </button>
        </div>
      </div>

      {/* Conversation Thread History */}
      <div className="flex-1 overflow-y-auto px-3 py-2 space-y-1">
        <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider px-2 py-1">
          Recent Research
        </div>

        {conversations.length === 0 ? (
          <div className="p-4 text-center text-xs text-slate-500">
            No research history yet. Start a search to see threads here!
          </div>
        ) : (
          conversations.map((c) => {
            const isActive = c.id === activeConversationId;

            return (
              <div
                key={c.id}
                onClick={() => onSelectConversation(c.id)}
                className={`group relative flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-medium cursor-pointer transition-colors ${
                  isActive
                    ? 'bg-slate-800 text-white border border-slate-700'
                    : 'text-slate-300 hover:bg-slate-800/60 hover:text-white'
                }`}
              >
                <div className="flex items-center space-x-2.5 min-w-0 pr-6">
                  <MessageSquare className={`h-3.5 w-3.5 shrink-0 ${isActive ? 'text-indigo-400' : 'text-slate-500'}`} />
                  <span className="truncate">{c.title || 'Shopping Search'}</span>
                </div>

                <button
                  type="button"
                  onClick={(e) => onDeleteConversation(c.id, e)}
                  className="opacity-0 group-hover:opacity-100 p-1 text-slate-400 hover:text-rose-400 transition-opacity absolute right-2"
                  title="Delete thread"
                >
                  <Trash2 className="h-3.5 w-3.5" />
                </button>
              </div>
            );
          })
        )}
      </div>

      {/* Bottom Shortcuts */}
      <div className="p-3 border-t border-slate-800 space-y-1">
        {onOpenPreferences && (
          <button
            type="button"
            onClick={onOpenPreferences}
            className="w-full flex items-center space-x-2.5 px-3 py-2 rounded-lg text-xs font-medium text-slate-300 hover:bg-slate-800 hover:text-white transition-colors cursor-pointer"
          >
            <SlidersHorizontal className="h-4 w-4 text-slate-400" />
            <span>Shopping Memory & Rules</span>
          </button>
        )}
        <div className="pt-2 border-t border-slate-800/60 flex items-center justify-between px-2 text-[11px] text-slate-500">
          <span>Zero-autonomous purchase</span>
          <span className="text-emerald-400">● Live Agents</span>
        </div>
      </div>
    </aside>
  );
}
