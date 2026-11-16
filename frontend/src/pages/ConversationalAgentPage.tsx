import React, { useState, useEffect, useRef } from 'react';
import { 
  Sparkles, 
  Menu, 
  Zap, 
  Search, 
  BrainCircuit, 
  Scale, 
  Laptop, 
  HardDrive, 
  Smartphone, 
  Headphones, 
  Shirt, 
  RotateCcw,
  ShieldCheck,
  AlertCircle
} from 'lucide-react';
import { api } from '../services/api';
import { 
  ConversationSummary, 
  ConversationDetail, 
  ChatMessage, 
  AgentStep, 
  ChatProductItem, 
  ProductSellerOption,
  CheckoutManifest
} from '../types';
import { ChatSidebar } from '../components/chat/ChatSidebar';
import { ChatMessageItem } from '../components/chat/ChatMessageItem';
import { ChatInputBox } from '../components/chat/ChatInputBox';
import { HumanApprovalModal } from '../components/checkout/HumanApprovalModal';

const SAMPLE_STARTER_PROMPTS = [
  { icon: Laptop, title: "AI Laptop Under ₹80k", query: "Find me the best laptop under ₹80,000 with 32GB RAM, 1TB SSD, and suitable for AI development." },
  { icon: Smartphone, title: "Flagship Phone Comparison", query: "Compare the best smartphones under ₹50,000 with flagship cameras and battery life." },
  { icon: HardDrive, title: "Cheapest 1TB NVMe SSD", query: "Find the cheapest 1TB M.2 NVMe SSD across all authorized stores with warranty." },
  { icon: Headphones, title: "Noise Cancelling Headphones", query: "Best wireless noise cancelling headphones under ₹15,000 for work and travel." },
  { icon: Shirt, title: "Running Shoes Under ₹5k", query: "Find running shoes under ₹5,000 with good cushioning and durability." },
  { icon: Sparkles, title: "RTX 5070 / 4060 Laptops", query: "Find all available RTX 4060 laptops with verified seller prices." }
];

export function ConversationalAgentPage() {
  const [conversations, setConversations] = useState<ConversationSummary[]>([]);
  const [activeConversation, setActiveConversation] = useState<ConversationDetail | null>(null);
  const [searchMode, setSearchMode] = useState<string>('deep');
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [isStreaming, setIsStreaming] = useState<boolean>(false);
  const [liveSteps, setLiveSteps] = useState<AgentStep[]>([]);
  const [mobileSidebarOpen, setMobileSidebarOpen] = useState<boolean>(false);

  // Human-in-the-Loop Checkout Gate Modal
  const [checkoutManifest, setCheckoutManifest] = useState<CheckoutManifest | null>(null);
  const [isCheckoutModalOpen, setIsCheckoutModalOpen] = useState<boolean>(false);
  const [checkoutNotice, setCheckoutNotice] = useState<string | null>(null);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  // Scroll to bottom
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [activeConversation?.messages, liveSteps, isStreaming]);

  // Initial load
  useEffect(() => {
    loadConversations();
  }, []);

  const loadConversations = async () => {
    try {
      const list = await api.listConversations();
      setConversations(list);
      if (list.length > 0 && !activeConversation) {
        // Load most recent thread
        const detail = await api.getConversation(list[0].id);
        setActiveConversation(detail);
        setSearchMode(detail.search_mode || 'deep');
      }
    } catch (err) {
      console.error('Failed to load conversations:', err);
    }
  };

  const handleSelectConversation = async (id: string) => {
    setIsLoading(true);
    setMobileSidebarOpen(false);
    try {
      const detail = await api.getConversation(id);
      setActiveConversation(detail);
      setSearchMode(detail.search_mode || 'deep');
    } catch (err) {
      console.error('Failed to fetch conversation:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleNewConversation = async () => {
    setIsLoading(true);
    setMobileSidebarOpen(false);
    try {
      const newConv = await api.createConversation("New Shopping Research", searchMode);
      setActiveConversation(newConv);
      setConversations(prev => [
        {
          id: newConv.id,
          title: newConv.title,
          search_mode: newConv.search_mode,
          created_at: newConv.created_at,
          updated_at: newConv.updated_at,
          message_count: 0
        },
        ...prev
      ]);
    } catch (err) {
      console.error('Failed to create conversation:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDeleteConversation = async (id: string, e: React.MouseEvent) => {
    e.stopPropagation();
    try {
      await api.deleteConversation(id);
      setConversations(prev => prev.filter(c => c.id !== id));
      if (activeConversation?.id === id) {
        const remaining = conversations.filter(c => c.id !== id);
        if (remaining.length > 0) {
          handleSelectConversation(remaining[0].id);
        } else {
          setActiveConversation(null);
        }
      }
    } catch (err) {
      console.error('Failed to delete conversation:', err);
    }
  };

  const handleSendMessage = async (queryText: string) => {
    if (!queryText.trim() || isLoading) return;

    let convId = activeConversation?.id;

    // If no active thread exists, create one first
    if (!convId) {
      try {
        const newConv = await api.createConversation(queryText.slice(0, 40), searchMode);
        convId = newConv.id;
        setActiveConversation(newConv);
      } catch (err) {
        console.error('Failed to create thread:', err);
        return;
      }
    }

    // 1. Optimistic User Message
    const userMsg: ChatMessage = {
      id: `temp-${Date.now()}`,
      conversation_id: convId,
      role: 'user',
      content: queryText,
      created_at: new Date().toISOString()
    };

    setActiveConversation(prev => prev ? {
      ...prev,
      messages: [...prev.messages, userMsg]
    } : null);

    setIsLoading(true);
    setIsStreaming(true);
    setLiveSteps([]);

    // 2. Connect to SSE stream for live agent thought steps
    let eventSource: EventSource | null = null;
    try {
      eventSource = new EventSource(`/api/v1/conversations/${convId}/stream`);
      eventSource.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (data && data.agent) {
            setLiveSteps(prev => [...prev, data]);
          }
        } catch {
          // ignore keepalive pings
        }
      };
    } catch {
      // SSE connection error fallback
    }

    // 3. Dispatch API Call
    try {
      const assistantMsg = await api.sendChatMessage(convId, queryText, searchMode);
      
      setActiveConversation(prev => prev ? {
        ...prev,
        messages: [...prev.messages, assistantMsg]
      } : null);

      // Refresh conversations list to update title and timestamps
      const list = await api.listConversations();
      setConversations(list);
    } catch (err: any) {
      console.error('Error executing conversational shopping research:', err);
      // Append error message
      const errorMsg: ChatMessage = {
        id: `err-${Date.now()}`,
        conversation_id: convId,
        role: 'assistant',
        content: `⚠️ Sorry, an error occurred while searching: ${err.message || 'Please check your connection and try again.'}`,
        created_at: new Date().toISOString()
      };
      setActiveConversation(prev => prev ? {
        ...prev,
        messages: [...prev.messages, errorMsg]
      } : null);
    } finally {
      if (eventSource) {
        eventSource.close();
      }
      setIsLoading(false);
      setIsStreaming(false);
      setLiveSteps([]);
    }
  };

  // Human-In-The-Loop Checkout Gate Handler
  const handleCheckoutAssist = async (product: ChatProductItem, seller: ProductSellerOption) => {
    try {
      const manifest = await api.requestCheckoutIntent({
        product_id: product.id,
        product_name: product.name,
        seller_name: seller.source || product.seller || 'Authorized Retailer',
        price: seller.price || product.lowest_price || product.price,
        shipping_cost: 0.0,
        product_url: seller.product_url || product.lowest_price_url || product.product_url || '#'
      });
      setCheckoutManifest(manifest);
      setIsCheckoutModalOpen(true);
    } catch (err: any) {
      alert(`Could not initiate checkout assistance: ${err.message}`);
    }
  };

  const handleConfirmCheckout = () => {
    if (checkoutManifest?.checkout_url && checkoutManifest.checkout_url !== '#') {
      window.open(checkoutManifest.checkout_url, '_blank', 'noopener,noreferrer');
      setCheckoutNotice(`✓ Securely redirected to ${checkoutManifest.seller_name} official checkout.`);
    }
    setIsCheckoutModalOpen(false);
    setTimeout(() => setCheckoutNotice(null), 6000);
  };

  return (
    <div className="flex h-screen bg-slate-50 overflow-hidden">
      {/* ChatGPT-Style Sidebar */}
      <ChatSidebar
        conversations={conversations}
        activeConversationId={activeConversation?.id}
        searchMode={searchMode}
        onSelectConversation={handleSelectConversation}
        onNewConversation={handleNewConversation}
        onDeleteConversation={handleDeleteConversation}
        onSelectSearchMode={setSearchMode}
        isOpenMobile={mobileSidebarOpen}
        onCloseMobile={() => setMobileSidebarOpen(false)}
      />

      {/* Main Conversational Workspace */}
      <div className="flex-1 flex flex-col h-full min-w-0 bg-slate-50 overflow-hidden relative">
        {/* Top Header Bar */}
        <header className="px-4 py-3 bg-white border-b border-slate-200 flex items-center justify-between z-10">
          <div className="flex items-center space-x-3">
            <button
              type="button"
              onClick={() => setMobileSidebarOpen(true)}
              className="md:hidden p-2 rounded-lg text-slate-600 hover:bg-slate-100"
            >
              <Menu className="h-5 w-5" />
            </button>
            <div>
              <h2 className="text-sm font-bold text-slate-900 truncate max-w-xs sm:max-w-md">
                {activeConversation?.title || 'Conversational Shopping Intelligence'}
              </h2>
              <div className="flex items-center space-x-2 text-[11px] text-slate-500">
                <span className="flex items-center text-indigo-600 font-semibold">
                  {searchMode === 'quick' && <Zap className="h-3 w-3 mr-0.5" />}
                  {searchMode === 'deep' && <Search className="h-3 w-3 mr-0.5" />}
                  {searchMode === 'maximum' && <BrainCircuit className="h-3 w-3 mr-0.5" />}
                  {searchMode.toUpperCase()} RESEARCH
                </span>
                <span>•</span>
                <span>Multi-Source Search & Verified Pricing</span>
              </div>
            </div>
          </div>

          <div className="flex items-center space-x-2">
            <button
              type="button"
              onClick={handleNewConversation}
              className="hidden sm:inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-slate-200 hover:bg-slate-50 text-xs font-semibold text-slate-700 transition-colors cursor-pointer"
            >
              <RotateCcw className="h-3.5 w-3.5 text-slate-500" />
              <span>Reset Chat</span>
            </button>
          </div>
        </header>

        {/* Global Alert Notice if Checkout Redirected */}
        {checkoutNotice && (
          <div className="bg-emerald-50 border-b border-emerald-200 px-4 py-2 text-xs font-semibold text-emerald-800 flex items-center justify-center space-x-2">
            <ShieldCheck className="h-4 w-4 text-emerald-600" />
            <span>{checkoutNotice}</span>
          </div>
        )}

        {/* Conversation Message Thread Canvas */}
        <div className="flex-1 overflow-y-auto px-4 py-6 md:px-8">
          <div className="max-w-4xl mx-auto">
            {(!activeConversation || activeConversation.messages.length === 0) ? (
              /* Welcome Screen / Empty State */
              <div className="py-8 sm:py-16 text-center">
                <div className="w-16 h-16 rounded-2xl bg-indigo-600 text-white flex items-center justify-center mx-auto mb-4 shadow-md">
                  <Sparkles className="h-8 w-8" />
                </div>
                <h2 className="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
                  What are you looking for today?
                </h2>
                <p className="mt-2 text-sm text-slate-600 max-w-xl mx-auto leading-relaxed">
                  Ask any shopping question in natural language. Our autonomous agents will search multiple authorized retailers, extract real specifications, compare cross-merchant prices, audit reviews, and recommend the strongest verified options.
                </p>

                {/* Prompt Suggestion Cards */}
                <div className="mt-8 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3 text-left">
                  {SAMPLE_STARTER_PROMPTS.map((prompt, idx) => {
                    const Icon = prompt.icon;
                    return (
                      <button
                        key={idx}
                        type="button"
                        onClick={() => handleSendMessage(prompt.query)}
                        className="p-3.5 rounded-2xl border border-slate-200 bg-white hover:border-indigo-300 hover:bg-indigo-50/40 text-left transition-all shadow-2xs hover:shadow-sm cursor-pointer group"
                      >
                        <div className="p-2 w-fit rounded-lg bg-indigo-50 text-indigo-600 mb-2 group-hover:bg-indigo-600 group-hover:text-white transition-colors">
                          <Icon className="h-4 w-4" />
                        </div>
                        <h3 className="text-xs font-bold text-slate-900 mb-1">{prompt.title}</h3>
                        <p className="text-[11px] text-slate-500 line-clamp-2 leading-relaxed">
                          "{prompt.query}"
                        </p>
                      </button>
                    );
                  })}
                </div>
              </div>
            ) : (
              /* Chat Message Stream */
              <div>
                {activeConversation.messages.map((msg) => (
                  <ChatMessageItem
                    key={msg.id}
                    message={msg}
                    onSuggestionClick={handleSendMessage}
                    onCheckoutAssist={handleCheckoutAssist}
                  />
                ))}

                {/* Live Streaming Indicator when research is active */}
                {isStreaming && (
                  <div className="flex justify-start mb-8">
                    <div className="flex items-start space-x-3 w-full max-w-4xl">
                      <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-indigo-600 to-violet-600 text-white flex items-center justify-center shrink-0 shadow-sm mt-0.5 animate-pulse">
                        <Sparkles className="h-4 w-4" />
                      </div>
                      <div className="flex-1 bg-white rounded-2xl border border-slate-200 p-4 shadow-xs">
                        <div className="flex items-center space-x-2 text-xs font-bold text-indigo-700 mb-2">
                          <span className="w-2 h-2 rounded-full bg-indigo-600 animate-ping" />
                          <span>AI Agents Deep Researching across Amazon, Flipkart, Croma...</span>
                        </div>
                        {liveSteps.length > 0 && (
                          <div className="space-y-1.5 border-t border-slate-100 pt-2">
                            {liveSteps.slice(-3).map((st, i) => (
                              <div key={i} className="text-xs text-slate-600 flex items-center space-x-2">
                                <span className="text-emerald-500 font-bold">✓</span>
                                <span className="font-semibold text-slate-800">{st.agent}:</span>
                                <span>{st.message}</span>
                              </div>
                            ))}
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                )}
                <div ref={messagesEndRef} />
              </div>
            )}
          </div>
        </div>

        {/* Sticky Bottom ChatGPT Input Bar */}
        <ChatInputBox
          onSendMessage={handleSendMessage}
          isLoading={isLoading}
          searchMode={searchMode}
          onSelectSearchMode={setSearchMode}
        />
      </div>

      {/* Human-In-The-Loop Confirmation Modal - Section 11 & 31 */}
      {isCheckoutModalOpen && checkoutManifest && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-xs p-4">
          <div className="bg-white rounded-2xl border border-slate-200 max-w-lg w-full p-6 shadow-2xl animate-in fade-in zoom-in-95 duration-150">
            <div className="flex items-center space-x-2.5 text-amber-600 font-bold text-sm mb-3">
              <AlertCircle className="h-5 w-5 shrink-0" />
              <span>{checkoutManifest.notice}</span>
            </div>

            <p className="text-xs text-slate-600 leading-relaxed mb-4">
              Our AI never purchases products autonomously or deducts funds without your explicit authorization. Please verify the itemized purchase details below before opening the merchant checkout page.
            </p>

            <div className="rounded-xl border border-slate-200 bg-slate-50 p-4 space-y-2 text-xs text-slate-800 mb-5">
              <div className="flex justify-between">
                <span className="text-slate-500">Product:</span>
                <span className="font-bold text-slate-900 text-right max-w-xs truncate">{checkoutManifest.product_name}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Selected Retailer:</span>
                <span className="font-bold text-slate-900">{checkoutManifest.seller_name}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Product Price:</span>
                <span className="font-bold text-slate-900">₹{checkoutManifest.price.toLocaleString()}</span>
              </div>
              <div className="flex justify-between">
                <span className="text-slate-500">Delivery / Shipping:</span>
                <span className="font-bold text-emerald-700">{checkoutManifest.shipping_cost === 0 ? 'FREE Standard Delivery' : `₹${checkoutManifest.shipping_cost}`}</span>
              </div>
              <div className="pt-2 border-t border-slate-200 flex justify-between text-sm font-extrabold text-slate-900">
                <span>Total Cost:</span>
                <span className="text-indigo-600">₹{checkoutManifest.total_cost.toLocaleString()}</span>
              </div>
            </div>

            <p className="text-[11px] text-slate-500 italic mb-5">
              🛡️ {checkoutManifest.security_guarantee}
            </p>

            <div className="flex items-center justify-end space-x-3">
              <button
                type="button"
                onClick={() => setIsCheckoutModalOpen(false)}
                className="px-4 py-2 rounded-xl border border-slate-200 text-xs font-semibold text-slate-700 hover:bg-slate-100 transition-colors cursor-pointer"
              >
                [Cancel]
              </button>
              <button
                type="button"
                onClick={handleConfirmCheckout}
                className="px-4 py-2 rounded-xl bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-bold shadow-xs transition-colors cursor-pointer flex items-center space-x-1"
              >
                <span>[Confirm & Proceed to {checkoutManifest.seller_name}]</span>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
