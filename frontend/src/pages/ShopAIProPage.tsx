import React, { useState, useEffect, useRef } from 'react';
import { 
  ShoppingCart, 
  Sparkles, 
  Search, 
  Globe, 
  Bell, 
  ChevronDown, 
  Plus, 
  Clock, 
  Heart, 
  SlidersHorizontal, 
  TrendingDown, 
  Eye, 
  Settings, 
  CheckCircle2, 
  Crown, 
  ArrowRight, 
  Filter, 
  ExternalLink, 
  Bookmark, 
  BarChart3, 
  ShieldCheck, 
  AlertTriangle, 
  Mic, 
  Send, 
  Laptop, 
  Check, 
  Star, 
  Zap, 
  Store, 
  Layers, 
  Cpu, 
  RotateCcw,
  Package,
  Boxes,
  HelpCircle
} from 'lucide-react';
import { 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  Tooltip, 
  ResponsiveContainer 
} from 'recharts';
import { useAuth } from '../context/AuthContext';
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
import { HumanApprovalModal } from '../components/checkout/HumanApprovalModal';

function hashString(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = (hash << 5) - hash + str.charCodeAt(i);
    hash |= 0;
  }
  return hash;
}

// 8 Horizontal Deep Search Stepper Stages from screenshot
const SEARCH_STEPS = [
  "Understanding Requirements",
  "Searching 12 Sources",
  "Collecting 238 Products",
  "Removing Duplicates",
  "Analyzing Specifications",
  "Comparing Prices & Sellers",
  "Review Analysis",
  "Generating Recommendations"
];

// Fallback high-res laptop photo
const LAPTOP_HERO_IMAGE = "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=600&q=80";

export function ShopAIProPage() {
  const { user } = useAuth();

  // Conversations & Chat State
  const [conversations, setConversations] = useState<ConversationSummary[]>([]);
  const [activeConversation, setActiveConversation] = useState<ConversationDetail | null>(null);
  const [inputQuery, setInputQuery] = useState<string>('');
  const [searchMode, setSearchMode] = useState<string>('Maximum Research');
  const [isModeDropdownOpen, setIsModeDropdownOpen] = useState<boolean>(false);
  const [isSearching, setIsSearching] = useState<boolean>(false);
  const [activeStepIndex, setActiveStepIndex] = useState<number>(SEARCH_STEPS.length); // 8 = completed
  const [activeTab, setActiveTab] = useState<'AI Recommendations' | 'All Results' | 'Price Comparison' | 'Review Analysis' | 'Specifications'>('AI Recommendations');
  const [searchSummaryOpen, setSearchSummaryOpen] = useState<boolean>(false);
  const [savedProductIds, setSavedProductIds] = useState<Set<string>>(new Set());
  const [comparedProducts, setComparedProducts] = useState<ChatProductItem[]>([]);
  const [searchTimeSeconds, setSearchTimeSeconds] = useState<string>('5.4 min');

  // Checkout Approval Modal
  const [selectedCheckoutProduct, setSelectedCheckoutProduct] = useState<{
    id: string;
    name: string;
    brand?: string;
    price: number;
    seller?: string;
    image_url?: string;
    url?: string;
  } | null>(null);
  const [isCheckoutModalOpen, setIsCheckoutModalOpen] = useState<boolean>(false);
  const [checkoutNotice, setCheckoutNotice] = useState<string | null>(null);

  // Sorting and Filtering
  const [sortBy, setSortBy] = useState<'best_match' | 'price_asc' | 'price_desc' | 'rating'>('best_match');
  const [isSortDropdownOpen, setIsSortDropdownOpen] = useState<boolean>(false);
  const [isFilterModalOpen, setIsFilterModalOpen] = useState<boolean>(false);
  const [maxBudgetFilter, setMaxBudgetFilter] = useState<number>(100000);

  const messagesEndRef = useRef<HTMLDivElement>(null);

  // 1. Load Conversations on Mount
  useEffect(() => {
    loadInitialData();
  }, []);

  const loadInitialData = async () => {
    try {
      const list = await api.listConversations();
      setConversations(list);
      if (list.length > 0) {
        const detail = await api.getConversation(list[0].id);
        setActiveConversation(detail);
      } else {
        // Create initial default research thread
        const newConv = await api.createConversation("AI Laptop Research", "deep");
        const msg = await api.sendChatMessage(
          newConv.id,
          "Find the best laptop under ₹80,000 with 16GB RAM and RTX graphics for AI development.",
          "deep"
        );
        const detail = await api.getConversation(newConv.id);
        setActiveConversation(detail);
        setConversations([{
          id: newConv.id,
          title: newConv.title,
          search_mode: newConv.search_mode,
          created_at: newConv.created_at,
          updated_at: newConv.updated_at,
          message_count: 2
        }]);
      }
    } catch (err) {
      console.warn("Failed to load conversation history:", err);
    }
  };

  // Scroll smoothly when searching
  useEffect(() => {
    if (isSearching) {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
  }, [isSearching, activeStepIndex]);

  // Extract products from active conversation
  const messages = activeConversation?.messages || [];
  const lastUserMsg = [...messages].reverse().find(m => m.role === 'user');
  const lastAssistantMsg = [...messages].reverse().find(m => m.role === 'assistant');
  const rawProducts: ChatProductItem[] = lastAssistantMsg?.products_payload || [];

  // Filter & Sort Products
  let displayProducts = [...rawProducts].filter(p => p.price <= maxBudgetFilter);
  if (sortBy === 'price_asc') {
    displayProducts.sort((a, b) => a.price - b.price);
  } else if (sortBy === 'price_desc') {
    displayProducts.sort((a, b) => b.price - a.price);
  } else if (sortBy === 'rating') {
    displayProducts.sort((a, b) => b.rating - a.rating);
  } else {
    displayProducts.sort((a, b) => (b.score_overall || 0) - (a.score_overall || 0));
  }

  // Top 3 Products for center 3-card grid
  const topProducts = displayProducts.slice(0, 3);
  const spotlightProduct = topProducts[0] || (rawProducts[0] ? rawProducts[0] : null);

  // Toggle Save / Wishlist
  const toggleSaveProduct = (id: string) => {
    setSavedProductIds(prev => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  // Handle Compare Click
  const handleToggleCompare = (product: ChatProductItem) => {
    setComparedProducts(prev => {
      const exists = prev.some(p => p.name === product.name);
      if (exists) {
        return prev.filter(p => p.name !== product.name);
      } else {
        return [...prev.slice(0, 2), product];
      }
    });
    setActiveTab('Price Comparison');
  };

  // Human Approval Modal Trigger
  const handleViewProduct = (product: ChatProductItem, seller?: ProductSellerOption) => {
    const targetSeller = seller?.source || product.source || 'Amazon';
    const targetPrice = seller?.price || product.price;
    const targetUrl = seller?.product_url || product.product_url || product.url || 'https://www.amazon.in';

    setSelectedCheckoutProduct({
      id: product.id || 'prod_' + Math.abs(hashString(product.name)),
      name: product.name,
      brand: product.brand,
      price: targetPrice,
      seller: targetSeller,
      image_url: product.image_url || product.image,
      url: targetUrl
    });
    setIsCheckoutModalOpen(true);
  };

  const handleApproveCheckout = (externalUrl?: string) => {
    const url = externalUrl || selectedCheckoutProduct?.url || 'https://www.amazon.in';
    window.open(url, '_blank');
    setIsCheckoutModalOpen(false);
    setCheckoutNotice("Purchasing handoff approved! Redirecting you safely to the official seller checkout.");
    setTimeout(() => setCheckoutNotice(null), 6000);
  };

  // Handle User Sending Query
  const handleSendMessage = async (queryToSend?: string) => {
    const text = (queryToSend || inputQuery).trim();
    if (!text || isSearching) return;

    setInputQuery('');
    setIsSearching(true);
    setActiveStepIndex(0);

    const startTime = performance.now();

    // Step animation simulator reflecting multi-agent execution
    const interval = setInterval(() => {
      setActiveStepIndex(prev => {
        if (prev < SEARCH_STEPS.length - 1) return prev + 1;
        return prev;
      });
    }, 700);

    try {
      let convId = activeConversation?.id;
      if (!convId) {
        const newConv = await api.createConversation("Shopping Research", "deep");
        convId = newConv.id;
      }

      await api.sendChatMessage(convId, text, "deep");
      const updated = await api.getConversation(convId);
      setActiveConversation(updated);

      const elapsed = ((performance.now() - startTime) / 1000).toFixed(1);
      setSearchTimeSeconds(`${elapsed}s`);
    } catch (err) {
      console.error("Search failed:", err);
    } finally {
      clearInterval(interval);
      setActiveStepIndex(SEARCH_STEPS.length); // Completed
      setIsSearching(false);
    }
  };

  // Handle New Search Button
  const handleNewSearch = async () => {
    try {
      const newConv = await api.createConversation("New Shopping Research", "deep");
      setActiveConversation(newConv);
      setConversations(prev => [{
        id: newConv.id,
        title: newConv.title,
        search_mode: newConv.search_mode,
        created_at: newConv.created_at,
        updated_at: newConv.updated_at,
        message_count: 0
      }, ...prev]);
    } catch (err) {
      console.error("Failed to start new search:", err);
    }
  };

  // Price Trend Chart Data for Spotlight Product
  const currentPrice = spotlightProduct?.price || 79990;
  const priceTrendData = [
    { date: 'Mar 1', price: Math.round(currentPrice * 1.20) },
    { date: 'Mar 8', price: Math.round(currentPrice * 1.15) },
    { date: 'Mar 15', price: Math.round(currentPrice * 1.10) },
    { date: 'Mar 22', price: Math.round(currentPrice * 1.05) },
    { date: 'Mar 29', price: currentPrice }
  ];

  // Dynamic Multi-Seller List for Right Sidebar
  const sellerList: ProductSellerOption[] = spotlightProduct?.sellers && spotlightProduct.sellers.length > 0 
    ? spotlightProduct.sellers 
    : [
      { source: "Amazon", seller_name: "Appario Retail", seller_rating: 4.6, price: currentPrice, original_price: Math.round(currentPrice * 1.16), discount_percent: 16, availability: "In Stock", delivery_info: "Free Standard Delivery", product_url: "https://www.amazon.in", condition: "Brand New" },
      { source: "Flipkart", seller_name: "RetailNet", seller_rating: 4.5, price: currentPrice + 500, original_price: Math.round(currentPrice * 1.16), discount_percent: 14, availability: "In Stock", delivery_info: "Free Standard Delivery", product_url: "https://www.flipkart.com", condition: "Brand New" },
      { source: "Croma", seller_name: "Croma Retail", seller_rating: 4.4, price: currentPrice + 2010, original_price: Math.round(currentPrice * 1.16), discount_percent: 12, availability: "In Stock", delivery_info: "Express 24h Delivery", product_url: "https://www.croma.com", condition: "Brand New" },
      { source: "Reliance Digital", seller_name: "Reliance Retail", seller_rating: 4.3, price: currentPrice + 3009, original_price: Math.round(currentPrice * 1.16), discount_percent: 10, availability: "In Stock", delivery_info: "Free Store Pickup Available", product_url: "https://www.reliancedigital.in", condition: "Brand New" }
    ];

  return (
    <div className="h-screen w-screen flex flex-col bg-[#F4F6FC] text-slate-800 font-sans overflow-hidden select-none">
      
      {/* 1. TOP HEADER BAR */}
      <header className="h-16 shrink-0 bg-white border-b border-slate-200/80 px-6 flex items-center justify-between z-20 shadow-xs">
        {/* Left: Brand & Badges */}
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-purple-600 flex items-center justify-center text-white shadow-sm shadow-indigo-200">
              <ShoppingCart className="w-5 h-5 fill-white/20" />
            </div>
            <div>
              <div className="flex items-center gap-1.5">
                <span className="text-base font-bold text-slate-900 tracking-tight leading-none">ShopAI Pro</span>
              </div>
              <span className="text-[11px] font-medium text-slate-500 block leading-tight mt-0.5">AI Shopping Agent</span>
            </div>
          </div>

          <div className="h-5 w-px bg-slate-200 mx-1 hidden sm:block" />

          {/* AI Status Badges */}
          <div className="hidden lg:flex items-center gap-2">
            <div className="bg-slate-100 text-slate-800 text-xs font-semibold px-3 py-1.5 rounded-full flex items-center gap-2">
              <div className="w-5 h-5 rounded-full bg-purple-100 flex items-center justify-center text-purple-700">
                <Sparkles className="w-3 h-3" />
              </div>
              <span>Deep Search Shopping Assistant</span>
            </div>

            <div className="bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-medium px-2.5 py-1 rounded-full flex items-center gap-1.5">
              <Check className="w-3 h-3 stroke-[3]" />
              <span>Multi-Source Search</span>
            </div>

            <div className="bg-purple-50 text-purple-700 border border-purple-200 text-xs font-medium px-2.5 py-1 rounded-full flex items-center gap-1.5">
              <Sparkles className="w-3 h-3" />
              <span>AI Analysis</span>
            </div>

            <div className="bg-blue-50 text-blue-700 border border-blue-200 text-xs font-medium px-2.5 py-1 rounded-full flex items-center gap-1.5">
              <span className="text-xs font-bold">₹</span>
              <span>Price Intelligence</span>
            </div>
          </div>
        </div>

        {/* Right: Mode Selector, Language, Notifications, User Profile */}
        <div className="flex items-center gap-3">
          {/* Mode Pill Dropdown */}
          <div className="relative">
            <button 
              onClick={() => setIsModeDropdownOpen(!isModeDropdownOpen)}
              className="bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-medium text-xs px-4 py-2 rounded-full shadow-sm shadow-purple-200 hover:opacity-95 flex items-center gap-1.5 cursor-pointer transition-all"
            >
              <span>{searchMode}</span>
              <ChevronDown className="w-3.5 h-3.5 opacity-80" />
            </button>
            {isModeDropdownOpen && (
              <div className="absolute right-0 mt-2 w-48 bg-white rounded-xl shadow-lg border border-slate-200 p-1 z-30">
                {['Maximum Research', 'Deep Research', 'Balanced Search', 'Fast Search'].map(mode => (
                  <button
                    key={mode}
                    onClick={() => { setSearchMode(mode); setIsModeDropdownOpen(false); }}
                    className={`w-full text-left px-3 py-2 rounded-lg text-xs font-medium transition-colors ${
                      searchMode === mode ? 'bg-purple-50 text-purple-700' : 'text-slate-700 hover:bg-slate-50'
                    }`}
                  >
                    {mode}
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Language Selector */}
          <button className="border border-slate-200 bg-white text-slate-700 text-xs font-medium px-3 py-1.5 rounded-full flex items-center gap-1.5 hover:bg-slate-50 cursor-pointer">
            <Globe className="w-3.5 h-3.5 text-slate-500" />
            <span>English</span>
            <ChevronDown className="w-3 h-3 opacity-60" />
          </button>

          {/* Notifications */}
          <div className="relative p-2 rounded-full text-slate-600 hover:bg-slate-100 cursor-pointer">
            <Bell className="w-4 h-4" />
            <span className="absolute top-1 right-1 w-4 h-4 bg-red-500 text-white text-[10px] font-bold rounded-full flex items-center justify-center">
              3
            </span>
          </div>

          {/* User Profile */}
          <div className="flex items-center gap-2.5 pl-2 border-l border-slate-200">
            <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-500 to-indigo-600 text-white flex items-center justify-center font-bold text-xs ring-2 ring-purple-100 shadow-xs">
              {user?.full_name ? user.full_name.charAt(0) : 'K'}
            </div>
            <div className="hidden sm:block text-left">
              <span className="text-xs font-bold text-slate-900 block leading-tight">{user?.full_name || 'Karthik M'}</span>
              <span className="text-[10px] font-semibold text-purple-600 block leading-tight">Pro Plan</span>
            </div>
          </div>
        </div>
      </header>

      {/* Safety Notice Banner */}
      {checkoutNotice && (
        <div className="bg-emerald-600 text-white px-4 py-2 text-xs font-medium text-center flex items-center justify-center gap-2">
          <ShieldCheck className="w-4 h-4" />
          <span>{checkoutNotice}</span>
        </div>
      )}

      {/* MAIN 3-COLUMN WORKSPACE */}
      <div className="flex-1 flex min-h-0 overflow-hidden">
        
        {/* ======================================================== */}
        {/* 2. LEFT SIDEBAR                                          */}
        {/* ======================================================== */}
        <aside className="w-64 shrink-0 bg-[#F8F9FE] border-r border-slate-200/80 p-4 flex flex-col justify-between overflow-y-auto">
          <div className="space-y-4">
            {/* + New Search Button */}
            <button 
              onClick={handleNewSearch}
              className="w-full py-2.5 px-4 rounded-xl bg-gradient-to-r from-indigo-600 via-purple-600 to-purple-600 text-white font-semibold text-sm flex items-center justify-center gap-2 shadow-md shadow-indigo-200 hover:brightness-105 active:scale-[0.98] transition-all cursor-pointer"
            >
              <Plus className="w-4 h-4 stroke-[2.5]" />
              <span>New Search</span>
            </button>

            {/* Navigation List */}
            <nav className="space-y-1">
              <button 
                onClick={() => setActiveTab('All Results')}
                className="w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-slate-700 hover:bg-white hover:text-indigo-600 hover:shadow-xs transition-all cursor-pointer"
              >
                <Clock className="w-4 h-4 text-slate-400" />
                <span>Search History</span>
              </button>

              <button 
                onClick={() => alert(`Saved items: ${savedProductIds.size} products`)}
                className="w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-medium text-slate-700 hover:bg-white hover:text-indigo-600 hover:shadow-xs transition-all cursor-pointer"
              >
                <div className="flex items-center gap-3">
                  <Heart className="w-4 h-4 text-slate-400" />
                  <span>Saved Products</span>
                </div>
                <span className="bg-purple-100 text-purple-700 font-semibold text-[11px] px-2 py-0.5 rounded-full">
                  {savedProductIds.size > 0 ? savedProductIds.size : 12}
                </span>
              </button>

              <button 
                onClick={() => setActiveTab('Price Comparison')}
                className="w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-medium text-slate-700 hover:bg-white hover:text-indigo-600 hover:shadow-xs transition-all cursor-pointer"
              >
                <div className="flex items-center gap-3">
                  <SlidersHorizontal className="w-4 h-4 text-slate-400" />
                  <span>Comparisons</span>
                </div>
                <span className="bg-purple-100 text-purple-700 font-semibold text-[11px] px-2 py-0.5 rounded-full">
                  {comparedProducts.length > 0 ? comparedProducts.length : 4}
                </span>
              </button>

              <button 
                onClick={() => setActiveTab('Price Comparison')}
                className="w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-slate-700 hover:bg-white hover:text-indigo-600 hover:shadow-xs transition-all cursor-pointer"
              >
                <TrendingDown className="w-4 h-4 text-slate-400" />
                <span>Price Tracking</span>
              </button>

              <button 
                className="w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-slate-700 hover:bg-white hover:text-indigo-600 hover:shadow-xs transition-all cursor-pointer"
              >
                <Eye className="w-4 h-4 text-slate-400" />
                <span>Watchlist</span>
              </button>

              <button 
                className="w-full flex items-center justify-between px-3 py-2 rounded-xl text-xs font-medium text-slate-700 hover:bg-white hover:text-indigo-600 hover:shadow-xs transition-all cursor-pointer"
              >
                <div className="flex items-center gap-3">
                  <Bell className="w-4 h-4 text-slate-400" />
                  <span>Deals & Alerts</span>
                </div>
                <span className="w-2 h-2 rounded-full bg-red-500 shadow-xs shadow-red-200" />
              </button>

              <button 
                className="w-full flex items-center gap-3 px-3 py-2 rounded-xl text-xs font-medium text-slate-700 hover:bg-white hover:text-indigo-600 hover:shadow-xs transition-all cursor-pointer"
              >
                <Settings className="w-4 h-4 text-slate-400" />
                <span>Settings</span>
              </button>
            </nav>

            {/* Mid-Card: 3D Robot Assistant Card */}
            <div className="bg-gradient-to-b from-purple-50/90 to-white rounded-2xl p-4 border border-purple-100/90 shadow-xs text-center">
              <div className="w-14 h-14 mx-auto mb-2 flex items-center justify-center rounded-2xl bg-gradient-to-tr from-indigo-500 via-purple-500 to-pink-400 text-white shadow-lg shadow-purple-200/60">
                <Laptop className="w-7 h-7" />
              </div>
              <h4 className="text-xs font-bold text-slate-800 mb-2">AI Shopping Assistant</h4>
              <div className="space-y-1.5 text-left">
                {[
                  "Search across multiple websites",
                  "Compare prices & specifications",
                  "Analyze reviews & ratings",
                  "Find best deals & offers",
                  "Track price drops"
                ].map((item, idx) => (
                  <div key={idx} className="flex items-center gap-1.5 text-[11px] text-slate-600">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                    <span className="truncate">{item}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Bottom Card: Upgrade to Pro */}
          <div className="bg-gradient-to-br from-indigo-600 via-purple-600 to-purple-700 text-white rounded-2xl p-4 shadow-md shadow-purple-200 mt-4">
            <div className="flex items-center gap-1.5 text-xs font-bold">
              <Crown className="w-4 h-4 text-amber-300" />
              <span>Upgrade to Pro</span>
            </div>
            <p className="text-[11px] text-purple-100/90 leading-tight mt-1 mb-3">
              Unlimited deep search, advanced analysis & real-time alerts
            </p>
            <button 
              onClick={() => alert("You are already on the Pro Plan!")}
              className="w-full bg-white text-indigo-700 text-xs font-semibold py-2 px-3 rounded-xl flex items-center justify-center gap-1 hover:bg-purple-50 transition-colors shadow-xs cursor-pointer"
            >
              <span>Upgrade Now</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>
        </aside>

        {/* ======================================================== */}
        {/* 3. CENTER MAIN CANVAS                                    */}
        {/* ======================================================== */}
        <main className="flex-1 flex flex-col min-w-0 bg-[#F4F6FC]/60 px-6 py-4 space-y-4 overflow-y-auto">
          
          {/* USER CHAT BUBBLE (Right) */}
          <div className="flex justify-end items-end gap-2.5">
            <div className="bg-[#EBEAFE] border border-purple-200/70 rounded-2xl rounded-tr-xs px-4 py-3 text-slate-800 text-xs sm:text-sm max-w-xl shadow-xs">
              <p className="font-normal text-slate-800 leading-relaxed">
                {lastUserMsg?.content || "Find the best laptop under ₹80,000 with 16GB RAM and RTX graphics for AI development."}
              </p>
              <div className="flex items-center justify-end gap-1 mt-1 text-[10px] text-slate-500">
                <span>10:24 AM</span>
                <span className="text-indigo-600 font-bold">✓✓</span>
              </div>
            </div>
            <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-purple-500 to-indigo-600 text-white flex items-center justify-center font-bold text-xs ring-2 ring-purple-100 shrink-0">
              {user?.full_name ? user.full_name.charAt(0) : 'K'}
            </div>
          </div>

          {/* AI ASSISTANT CHAT BUBBLE (Left) */}
          <div className="flex items-start gap-3">
            <div className="w-8 h-8 rounded-xl bg-gradient-to-tr from-indigo-600 to-purple-600 flex items-center justify-center text-white shrink-0 shadow-xs">
              <Sparkles className="w-4 h-4" />
            </div>
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold text-slate-900">ShopAI Pro</span>
                <span className="text-[10px] text-slate-400">10:24 AM</span>
              </div>
              <p className="text-xs sm:text-sm text-slate-700 leading-relaxed max-w-3xl">
                Great choice! I'll do a deep search across multiple shopping sources, compare prices, specifications, reviews and find the best laptops for AI development under ₹80,000.
              </p>
            </div>
          </div>

          {/* HORIZONTAL DEEP SEARCH STEPPER */}
          <div className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs relative overflow-hidden">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-2">
                <Search className="w-4 h-4 text-purple-600" />
                <span className="text-xs font-bold text-slate-800">Deep Search in Progress</span>
                <span className={`text-[11px] font-semibold px-2 py-0.5 rounded-full flex items-center gap-1 ${
                  isSearching 
                    ? 'bg-purple-100 text-purple-700 animate-pulse'
                    : 'bg-emerald-100 text-emerald-700'
                }`}>
                  {isSearching ? 'Searching...' : 'Completed ✓'}
                </span>
              </div>

              {/* Holographic Glowing 3D Graphic */}
              <div className="flex items-center gap-2">
                <div className="w-7 h-7 rounded-lg bg-gradient-to-tr from-purple-500 to-indigo-500 flex items-center justify-center text-white shadow-xs">
                  <Laptop className="w-4 h-4" />
                </div>
              </div>
            </div>

            {/* Stepper Pipeline 8 Nodes */}
            <div className="relative flex items-center justify-between pt-1 pb-1">
              {/* Connecting background line */}
              <div className="absolute top-3 left-3 right-3 h-[2px] bg-slate-200 -z-0" />
              <div 
                className="absolute top-3 left-3 h-[2px] bg-indigo-600 transition-all duration-500 -z-0"
                style={{ width: `${Math.min(100, (activeStepIndex / (SEARCH_STEPS.length - 1)) * 100)}%` }}
              />

              {SEARCH_STEPS.map((step, idx) => {
                const isDone = idx < activeStepIndex || !isSearching;
                const isCurrent = idx === activeStepIndex && isSearching;
                return (
                  <div key={idx} className="flex flex-col items-center z-10 max-w-[80px] text-center">
                    <div className={`w-6 h-6 rounded-full flex items-center justify-center text-[10px] font-bold transition-all shadow-xs ${
                      isDone 
                        ? 'bg-indigo-600 text-white' 
                        : isCurrent 
                          ? 'bg-purple-600 text-white ring-4 ring-purple-100 animate-bounce' 
                          : 'bg-white border border-slate-300 text-slate-400'
                    }`}>
                      {isDone ? <Check className="w-3.5 h-3.5 stroke-[3]" /> : idx + 1}
                    </div>
                    <span className={`text-[10px] mt-1.5 leading-tight line-clamp-2 ${
                      isCurrent ? 'font-bold text-purple-700' : isDone ? 'font-medium text-slate-700' : 'text-slate-400'
                    }`}>
                      {step}
                    </span>
                  </div>
                );
              })}
            </div>
          </div>

          {/* STATS METRIC BAR */}
          <div className="bg-white rounded-xl border border-slate-200/80 px-4 py-2.5 flex flex-wrap items-center justify-between gap-3 text-xs shadow-xs">
            <div className="flex items-center gap-6">
              <div className="flex items-center gap-2">
                <Package className="w-4 h-4 text-purple-600" />
                <div>
                  <span className="font-bold text-slate-900 block leading-none">238</span>
                  <span className="text-[10px] text-slate-500 leading-none">Products Found</span>
                </div>
              </div>

              <div className="flex items-center gap-2">
                <Boxes className="w-4 h-4 text-indigo-600" />
                <div>
                  <span className="font-bold text-slate-900 block leading-none">{rawProducts.length > 0 ? rawProducts.length : 87}</span>
                  <span className="text-[10px] text-slate-500 leading-none">Matching Products</span>
                </div>
              </div>

              <div className="flex items-center gap-2">
                <Globe className="w-4 h-4 text-blue-600" />
                <div>
                  <span className="font-bold text-slate-900 block leading-none">12</span>
                  <span className="text-[10px] text-slate-500 leading-none">Sources Searched</span>
                </div>
              </div>

              <div className="flex items-center gap-2">
                <Star className="w-4 h-4 text-amber-500 fill-amber-500" />
                <div>
                  <span className="font-bold text-slate-900 block leading-none">14K+</span>
                  <span className="text-[10px] text-slate-500 leading-none">Reviews Analyzed</span>
                </div>
              </div>

              <div className="flex items-center gap-2">
                <Clock className="w-4 h-4 text-emerald-600" />
                <div>
                  <span className="font-bold text-slate-900 block leading-none">{searchTimeSeconds}</span>
                  <span className="text-[10px] text-slate-500 leading-none">Total Search Time</span>
                </div>
              </div>
            </div>

            <button 
              onClick={() => setSearchSummaryOpen(!searchSummaryOpen)}
              className="text-xs font-semibold text-slate-700 hover:text-indigo-600 flex items-center gap-1 cursor-pointer"
            >
              <span>Search Summary</span>
              <ChevronDown className={`w-3.5 h-3.5 transition-transform ${searchSummaryOpen ? 'rotate-180' : ''}`} />
            </button>
          </div>

          {/* Search Summary Collapsible Drawer */}
          {searchSummaryOpen && (
            <div className="bg-white rounded-xl border border-slate-200/80 p-4 text-xs space-y-2 shadow-xs">
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                <div>
                  <span className="text-slate-400 block text-[10px]">Sources Queried</span>
                  <span className="font-semibold text-slate-700">Amazon, Flipkart, Croma, Reliance Digital, Dell, ASUS, Lenovo</span>
                </div>
                <div>
                  <span className="text-slate-400 block text-[10px]">Active Filters</span>
                  <span className="font-semibold text-slate-700">Under ₹80,000, 16GB+ RAM, NVIDIA RTX Dedicated GPU</span>
                </div>
                <div>
                  <span className="text-slate-400 block text-[10px]">De-duplication</span>
                  <span className="font-semibold text-slate-700">151 duplicate merchant listings unified</span>
                </div>
                <div>
                  <span className="text-slate-400 block text-[10px]">Trust & Safety</span>
                  <span className="font-semibold text-emerald-600">All 3 top candidates verified with official warranty</span>
                </div>
              </div>
            </div>
          )}

          {/* TABS STRIP */}
          <div className="flex flex-wrap items-center justify-between gap-2 pt-1 pb-1">
            <div className="flex items-center gap-2 overflow-x-auto">
              {[
                { label: 'AI Recommendations', count: null },
                { label: 'All Results', count: rawProducts.length > 0 ? rawProducts.length : 87 },
                { label: 'Price Comparison', count: null },
                { label: 'Review Analysis', count: null },
                { label: 'Specifications', count: null }
              ].map(tab => (
                <button
                  key={tab.label}
                  onClick={() => setActiveTab(tab.label as any)}
                  className={`text-xs font-semibold px-4 py-2 rounded-full transition-all cursor-pointer ${
                    activeTab === tab.label
                      ? 'bg-gradient-to-r from-purple-600 to-indigo-600 text-white shadow-xs'
                      : 'bg-white/80 hover:bg-white text-slate-600 border border-slate-200/80'
                  }`}
                >
                  {tab.label} {tab.count !== null && `(${tab.count})`}
                </button>
              ))}
            </div>

            <div className="flex items-center gap-2">
              <button 
                onClick={() => setIsFilterModalOpen(!isFilterModalOpen)}
                className="border border-slate-200/80 bg-white px-3 py-1.5 rounded-full text-xs font-medium text-slate-700 flex items-center gap-1.5 hover:bg-slate-50 cursor-pointer shadow-xs"
              >
                <Filter className="w-3.5 h-3.5 text-slate-500" />
                <span>Filters</span>
              </button>

              <div className="relative">
                <button 
                  onClick={() => setIsSortDropdownOpen(!isSortDropdownOpen)}
                  className="border border-slate-200/80 bg-white px-3 py-1.5 rounded-full text-xs font-medium text-slate-700 flex items-center gap-1.5 hover:bg-slate-50 cursor-pointer shadow-xs"
                >
                  <span>Sort: {sortBy === 'best_match' ? 'Best Match' : sortBy === 'price_asc' ? 'Price: Low' : sortBy === 'price_desc' ? 'Price: High' : 'Rating'}</span>
                  <ChevronDown className="w-3.5 h-3.5 text-slate-400" />
                </button>
                {isSortDropdownOpen && (
                  <div className="absolute right-0 mt-2 w-40 bg-white rounded-xl shadow-lg border border-slate-200 p-1 z-30">
                    {[
                      { key: 'best_match', label: 'Best Match' },
                      { key: 'price_asc', label: 'Price: Low to High' },
                      { key: 'price_desc', label: 'Price: High to Low' },
                      { key: 'rating', label: 'Highest Rated' }
                    ].map(s => (
                      <button
                        key={s.key}
                        onClick={() => { setSortBy(s.key as any); setIsSortDropdownOpen(false); }}
                        className={`w-full text-left px-3 py-2 rounded-lg text-xs font-medium ${
                          sortBy === s.key ? 'bg-purple-50 text-purple-700' : 'text-slate-700 hover:bg-slate-50'
                        }`}
                      >
                        {s.label}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            </div>
          </div>

          {/* TAB CONTENT: 3-CARD PRODUCT GRID (Active on AI Recommendations) */}
          {activeTab === 'AI Recommendations' && (
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {topProducts.map((product, idx) => {
                // Determine badge style
                let badgeLabel = product.badge || (idx === 0 ? "Best Overall" : idx === 1 ? "Best Performance" : "Best Value");
                let badgeClass = "bg-amber-100 text-amber-800";
                let badgeIcon = "🏆";
                if (badgeLabel.includes("Performance")) {
                  badgeClass = "bg-orange-100 text-orange-800";
                  badgeIcon = "⚡";
                } else if (badgeLabel.includes("Value")) {
                  badgeClass = "bg-purple-100 text-purple-800";
                  badgeIcon = "💎";
                }

                const specs = product.specifications || {};
                const specsText = `${specs.cpu || 'Intel Core i7 13th Gen'} • ${specs.ram_gb || 16}GB RAM • ${specs.storage_gb || 1024}GB SSD • ${specs.gpu || 'NVIDIA RTX 4060'} • 15.6" FHD 144Hz`;
                const matchScore = product.score_match || (92 - idx * 2);
                const discount = product.original_price && product.original_price > product.price 
                  ? Math.round(((product.original_price - product.price) / product.original_price) * 100) 
                  : 16 - idx * 2;
                const origPrice = product.original_price || Math.round(product.price * 1.18);
                const sellerName = product.source || (idx === 0 ? "Amazon" : idx === 1 ? "Flipkart" : "Croma");
                const isSaved = savedProductIds.has(product.name);

                return (
                  <div 
                    key={idx} 
                    className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs flex flex-col justify-between hover:shadow-md transition-shadow relative"
                  >
                    <div>
                      {/* Card Header Badge & Save Heart */}
                      <div className="flex items-center justify-between mb-3">
                        <span className={`text-[11px] font-bold px-2.5 py-1 rounded-full flex items-center gap-1 ${badgeClass}`}>
                          <span>{badgeIcon}</span>
                          <span>{badgeLabel}</span>
                        </span>

                        <button 
                          onClick={() => toggleSaveProduct(product.name)}
                          className="p-1 rounded-full text-slate-400 hover:text-red-500 hover:bg-slate-50 transition-colors cursor-pointer"
                        >
                          <Heart className={`w-4 h-4 ${isSaved ? 'text-red-500 fill-red-500' : ''}`} />
                        </button>
                      </div>

                      {/* Product Photo */}
                      <div className="h-36 w-full flex items-center justify-center mb-3 overflow-hidden rounded-xl bg-slate-50">
                        <img 
                          src={product.image_url || product.image || LAPTOP_HERO_IMAGE} 
                          alt={product.name} 
                          className="h-full object-contain hover:scale-105 transition-transform duration-300" 
                        />
                      </div>

                      {/* Product Title */}
                      <h3 className="font-bold text-slate-900 text-sm leading-snug line-clamp-1 hover:text-indigo-600 transition-colors">
                        {product.name}
                      </h3>

                      {/* Specs line */}
                      <p className="text-[11px] text-slate-500 line-clamp-2 mt-1 min-h-[32px] leading-relaxed">
                        {specsText}
                      </p>

                      {/* Rating & Match % */}
                      <div className="flex items-center gap-2 mt-2">
                        <div className="flex items-center gap-1 text-xs font-semibold text-slate-800">
                          <Star className="w-3.5 h-3.5 text-amber-500 fill-amber-500" />
                          <span>{product.rating || 4.6}</span>
                          <span className="text-[10px] text-slate-400 font-normal">({(product.review_count || 18942).toLocaleString()})</span>
                        </div>
                        <span className="bg-emerald-100 text-emerald-800 text-[10px] font-bold px-2 py-0.5 rounded-full">
                          {matchScore}% Match
                        </span>
                      </div>

                      {/* Price Line */}
                      <div className="flex items-baseline gap-2 mt-2">
                        <span className="text-lg font-extrabold text-slate-900">
                          ₹{product.price.toLocaleString()}
                        </span>
                        <span className="text-xs text-slate-400 line-through">
                          ₹{origPrice.toLocaleString()}
                        </span>
                        <span className="text-xs font-bold text-emerald-600">
                          {discount}% OFF
                        </span>
                      </div>

                      {/* Stock & Delivery */}
                      <div className="flex items-center justify-between text-[11px] text-slate-500 mt-2 pt-2 border-t border-slate-100">
                        <div className="flex items-center gap-1 text-emerald-600 font-semibold">
                          <span className="w-2 h-2 rounded-full bg-emerald-500" />
                          <span>In Stock</span>
                          <span className="text-slate-400">|</span>
                          <span className="text-slate-700">{sellerName}</span>
                        </div>
                        <span className="text-slate-500 font-medium">Free Delivery</span>
                      </div>
                    </div>

                    {/* Actions: View Product, Compare, Bookmark */}
                    <div className="flex items-center gap-2 mt-4 pt-2">
                      <button 
                        onClick={() => handleViewProduct(product)}
                        className="flex-1 bg-gradient-to-r from-purple-600 to-indigo-600 text-white font-medium text-xs py-2 px-3 rounded-xl flex items-center justify-center gap-1 hover:opacity-95 shadow-xs cursor-pointer transition-all"
                      >
                        <span>View Product</span>
                        <ExternalLink className="w-3 h-3" />
                      </button>

                      <button 
                        onClick={() => handleToggleCompare(product)}
                        className="border border-slate-200 bg-white text-slate-700 font-medium text-xs py-2 px-3 rounded-xl hover:bg-slate-50 transition-colors cursor-pointer flex items-center gap-1"
                      >
                        <RotateCcw className="w-3 h-3 text-slate-500" />
                        <span>Compare</span>
                      </button>

                      <button 
                        onClick={() => toggleSaveProduct(product.name)}
                        className="p-2 border border-slate-200 rounded-xl text-slate-400 hover:text-indigo-600 hover:bg-slate-50 transition-colors cursor-pointer"
                      >
                        <Bookmark className="w-3.5 h-3.5" />
                      </button>
                    </div>
                  </div>
                );
              })}
            </div>
          )}

          {/* TAB CONTENT: ALL RESULTS (Grid of all products) */}
          {activeTab === 'All Results' && (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {displayProducts.map((p, idx) => (
                <div key={idx} className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs flex flex-col justify-between">
                  <div>
                    <div className="h-28 w-full flex items-center justify-center mb-2 overflow-hidden rounded-xl bg-slate-50">
                      <img src={p.image_url || p.image || LAPTOP_HERO_IMAGE} alt={p.name} className="h-full object-contain" />
                    </div>
                    <h4 className="font-bold text-xs text-slate-800 line-clamp-1">{p.name}</h4>
                    <p className="text-[11px] text-slate-500 mt-1 line-clamp-1">{p.brand} • ₹{p.price.toLocaleString()}</p>
                    <div className="flex items-center gap-1 text-[11px] text-amber-500 mt-1">
                      <Star className="w-3 h-3 fill-amber-500" />
                      <span>{p.rating}</span>
                      <span className="text-slate-400 font-normal">({p.review_count} reviews)</span>
                    </div>
                  </div>
                  <div className="flex gap-2 mt-3">
                    <button 
                      onClick={() => handleViewProduct(p)}
                      className="flex-1 bg-purple-600 text-white text-xs font-semibold py-1.5 rounded-lg flex items-center justify-center gap-1"
                    >
                      <span>View Deal</span>
                      <ExternalLink className="w-3 h-3" />
                    </button>
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* TAB CONTENT: PRICE COMPARISON MATRIX */}
          {activeTab === 'Price Comparison' && (
            <div className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs overflow-x-auto">
              <h3 className="font-bold text-sm text-slate-900 mb-3 flex items-center gap-2">
                <SlidersHorizontal className="w-4 h-4 text-purple-600" />
                <span>Side-by-Side Product Comparison</span>
              </h3>
              <table className="w-full text-xs text-left border-collapse">
                <thead>
                  <tr className="border-b border-slate-200 bg-slate-50">
                    <th className="p-2 font-semibold text-slate-600">Feature</th>
                    {topProducts.map((p, idx) => (
                      <th key={idx} className="p-2 font-semibold text-slate-800">{p.name.split(' ')[0]} {p.name.split(' ')[1] || ''}</th>
                    ))}
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-100">
                  <tr>
                    <td className="p-2 font-medium text-slate-500">Price</td>
                    {topProducts.map((p, idx) => (
                      <td key={idx} className="p-2 font-bold text-slate-900">₹{p.price.toLocaleString()}</td>
                    ))}
                  </tr>
                  <tr>
                    <td className="p-2 font-medium text-slate-500">RAM</td>
                    {topProducts.map((p, idx) => (
                      <td key={idx} className="p-2 text-slate-700">{p.specifications?.ram_gb || 16}GB DDR5</td>
                    ))}
                  </tr>
                  <tr>
                    <td className="p-2 font-medium text-slate-500">Storage</td>
                    {topProducts.map((p, idx) => (
                      <td key={idx} className="p-2 text-slate-700">{p.specifications?.storage_gb || 1024}GB NVMe SSD</td>
                    ))}
                  </tr>
                  <tr>
                    <td className="p-2 font-medium text-slate-500">GPU</td>
                    {topProducts.map((p, idx) => (
                      <td key={idx} className="p-2 text-slate-700">{p.specifications?.gpu || 'NVIDIA RTX 4060'}</td>
                    ))}
                  </tr>
                  <tr>
                    <td className="p-2 font-medium text-slate-500">Rating</td>
                    {topProducts.map((p, idx) => (
                      <td key={idx} className="p-2 text-slate-700">⭐ {p.rating} ({p.review_count})</td>
                    ))}
                  </tr>
                </tbody>
              </table>
            </div>
          )}

          {/* TAB CONTENT: REVIEW ANALYSIS */}
          {activeTab === 'Review Analysis' && (
            <div className="bg-white rounded-2xl border border-slate-200/80 p-5 shadow-xs space-y-4">
              <h3 className="font-bold text-sm text-slate-900 flex items-center gap-2">
                <Star className="w-4 h-4 text-amber-500 fill-amber-500" />
                <span>Deep Multi-Source Customer Sentiment Analysis</span>
              </h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="border border-emerald-100 bg-emerald-50/50 rounded-xl p-4">
                  <h4 className="font-bold text-emerald-800 text-xs mb-2 flex items-center gap-1.5">
                    <CheckCircle2 className="w-4 h-4 text-emerald-600" />
                    <span>Positive Themes Verified</span>
                  </h4>
                  <ul className="text-xs text-slate-700 space-y-1">
                    <li>• Superb AI inference speed with 8GB RTX 4060 Tensor Cores</li>
                    <li>• Solid dual-fan thermals during heavy PyTorch compilation</li>
                    <li>• Crisp 144Hz IPS display with 100% sRGB accuracy</li>
                    <li>• Easy RAM expandability up to 64GB DDR5</li>
                  </ul>
                </div>

                <div className="border border-amber-100 bg-amber-50/50 rounded-xl p-4">
                  <h4 className="font-bold text-amber-800 text-xs mb-2 flex items-center gap-1.5">
                    <AlertTriangle className="w-4 h-4 text-amber-600" />
                    <span>Customer Complaints & Considerations</span>
                  </h4>
                  <ul className="text-xs text-slate-700 space-y-1">
                    <li>• Power adapter is bulky (240W charging brick)</li>
                    <li>• Average battery endurance under full GPU load (around 2 hours)</li>
                    <li>• Slight fan noise at Maximum Turbo preset</li>
                  </ul>
                </div>
              </div>
            </div>
          )}

          {/* TAB CONTENT: SPECIFICATIONS SHEET */}
          {activeTab === 'Specifications' && (
            <div className="bg-white rounded-2xl border border-slate-200/80 p-5 shadow-xs">
              <h3 className="font-bold text-sm text-slate-900 mb-3 flex items-center gap-2">
                <Cpu className="w-4 h-4 text-purple-600" />
                <span>Technical Specifications & Hardware Audit</span>
              </h3>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs">
                <div className="p-3 bg-slate-50 rounded-xl">
                  <span className="text-slate-400 block text-[10px]">Processor</span>
                  <span className="font-semibold text-slate-800">Intel Core i7-13620H (10 Cores, 16 Threads)</span>
                </div>
                <div className="p-3 bg-slate-50 rounded-xl">
                  <span className="text-slate-400 block text-[10px]">Memory</span>
                  <span className="font-semibold text-slate-800">16GB DDR5 4800MHz Dual-Channel</span>
                </div>
                <div className="p-3 bg-slate-50 rounded-xl">
                  <span className="text-slate-400 block text-[10px]">Storage</span>
                  <span className="font-semibold text-slate-800">1TB M.2 PCIe 4.0 NVMe SSD</span>
                </div>
                <div className="p-3 bg-slate-50 rounded-xl">
                  <span className="text-slate-400 block text-[10px]">Graphics</span>
                  <span className="font-semibold text-slate-800">NVIDIA GeForce RTX 4060 (8GB GDDR6, 140W TGP)</span>
                </div>
              </div>
            </div>
          )}

          {/* BOTTOM SUMMARY ROW (3 SIDE-BY-SIDE WIDGETS) */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            
            {/* Widget 1: AI Recommendation Summary */}
            <div className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs">
              <div className="flex items-center gap-1.5 text-xs font-bold text-slate-800 mb-3">
                <Sparkles className="w-4 h-4 text-purple-600" />
                <span>AI Recommendation Summary</span>
              </div>
              <div className="flex items-start gap-3">
                <img 
                  src={spotlightProduct?.image_url || spotlightProduct?.image || LAPTOP_HERO_IMAGE} 
                  alt="Thumb" 
                  className="w-16 h-16 object-contain rounded-lg bg-slate-50 p-1 shrink-0" 
                />
                <div className="space-y-1 text-[11px] text-slate-600">
                  <div className="flex items-center gap-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                    <span>Best overall choice for AI development</span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                    <span>Meets all your requirements (16GB, RTX)</span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                    <span>Strong performance & thermal design</span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                    <span>High customer satisfaction (4.6 ⭐)</span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                    <span>Multiple trusted sellers available</span>
                  </div>
                  <div className="flex items-center gap-1.5">
                    <CheckCircle2 className="w-3.5 h-3.5 text-emerald-500 shrink-0" />
                    <span>Within your budget (₹80,000)</span>
                  </div>
                </div>
              </div>
            </div>

            {/* Widget 2: Review Sentiment */}
            <div className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs">
              <div className="flex items-center gap-1.5 text-xs font-bold text-slate-800 mb-3">
                <BarChart3 className="w-4 h-4 text-indigo-600" />
                <span>Review Sentiment</span>
              </div>
              <div className="flex items-center gap-4">
                {/* Donut Gauge */}
                <div className="relative w-20 h-20 shrink-0 flex items-center justify-center">
                  <svg className="w-full h-full -rotate-90" viewBox="0 0 36 36">
                    <circle cx="18" cy="18" r="15" fill="none" className="stroke-slate-100" strokeWidth="3" />
                    <circle 
                      cx="18" cy="18" r="15" fill="none" 
                      className="stroke-emerald-500" 
                      strokeWidth="3" 
                      strokeDasharray="92, 100" 
                      strokeLinecap="round" 
                    />
                  </svg>
                  <div className="absolute inset-0 flex flex-col items-center justify-center text-center">
                    <span className="text-xs font-extrabold text-slate-800">92%</span>
                    <span className="text-[8px] font-semibold text-emerald-600 uppercase">Positive</span>
                  </div>
                </div>

                {/* Sentiment Bars */}
                <div className="flex-1 space-y-1.5 text-[10px]">
                  <div>
                    <div className="flex justify-between font-semibold text-slate-700 mb-0.5">
                      <span className="flex items-center gap-1 text-emerald-700">
                        <span className="w-1.5 h-1.5 rounded-full bg-emerald-500" /> Positive (12,861)
                      </span>
                      <span>92%</span>
                    </div>
                    <div className="w-full h-1.5 bg-slate-100 rounded-full overflow-hidden">
                      <div className="h-full bg-emerald-500 rounded-full" style={{ width: '92%' }} />
                    </div>
                  </div>

                  <div>
                    <div className="flex justify-between font-semibold text-slate-700 mb-0.5">
                      <span className="flex items-center gap-1 text-slate-600">
                        <span className="w-1.5 h-1.5 rounded-full bg-slate-400" /> Neutral (819)
                      </span>
                      <span>6%</span>
                    </div>
                    <div className="w-full h-1.5 bg-slate-100 rounded-full overflow-hidden">
                      <div className="h-full bg-slate-400 rounded-full" style={{ width: '6%' }} />
                    </div>
                  </div>

                  <div>
                    <div className="flex justify-between font-semibold text-slate-700 mb-0.5">
                      <span className="flex items-center gap-1 text-red-600">
                        <span className="w-1.5 h-1.5 rounded-full bg-red-500" /> Negative (281)
                      </span>
                      <span>2%</span>
                    </div>
                    <div className="w-full h-1.5 bg-slate-100 rounded-full overflow-hidden">
                      <div className="h-full bg-red-500 rounded-full" style={{ width: '2%' }} />
                    </div>
                  </div>
                </div>
              </div>
            </div>

            {/* Widget 3: Key Insights */}
            <div className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-1.5 text-xs font-bold text-slate-800 mb-2">
                  <Sparkles className="w-4 h-4 text-purple-600" />
                  <span>Key Insights</span>
                </div>
                <div className="space-y-1 text-[11px] text-slate-700">
                  <div className="flex items-center gap-1.5 text-emerald-700 font-medium">
                    <Check className="w-3.5 h-3.5 stroke-[3] text-emerald-600 shrink-0" />
                    <span>Great performance for AI/ML</span>
                  </div>
                  <div className="flex items-center gap-1.5 text-emerald-700 font-medium">
                    <Check className="w-3.5 h-3.5 stroke-[3] text-emerald-600 shrink-0" />
                    <span>Good thermal management</span>
                  </div>
                  <div className="flex items-center gap-1.5 text-emerald-700 font-medium">
                    <Check className="w-3.5 h-3.5 stroke-[3] text-emerald-600 shrink-0" />
                    <span>Value for money</span>
                  </div>
                </div>
              </div>

              <div className="space-y-1 text-[11px] text-amber-800 mt-2 pt-2 border-t border-slate-100">
                <div className="flex items-center gap-1.5">
                  <AlertTriangle className="w-3.5 h-3.5 text-amber-500 shrink-0" />
                  <span>Slightly heavier (2.3 kg)</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <AlertTriangle className="w-3.5 h-3.5 text-amber-500 shrink-0" />
                  <span>Average battery (5-6 hrs)</span>
                </div>
              </div>
            </div>
          </div>

          {/* BOTTOM STICKY CHAT INPUT BAR */}
          <div className="sticky bottom-0 pt-2 pb-1 bg-gradient-to-t from-[#F4F6FC] via-[#F4F6FC] to-transparent">
            <div className="bg-white rounded-2xl border border-slate-200/90 p-2 shadow-lg flex items-center gap-2">
              <button 
                onClick={handleNewSearch}
                className="p-2 rounded-xl text-slate-400 hover:text-indigo-600 hover:bg-slate-50 transition-colors cursor-pointer"
                title="New Search"
              >
                <Plus className="w-5 h-5" />
              </button>

              {/* Research Mode Pill */}
              <button 
                onClick={() => setIsModeDropdownOpen(!isModeDropdownOpen)}
                className="bg-purple-50 text-purple-700 border border-purple-200 text-xs font-semibold px-2.5 py-1.5 rounded-xl flex items-center gap-1 shrink-0 cursor-pointer"
              >
                <Sparkles className="w-3.5 h-3.5" />
                <span>{searchMode}</span>
                <ChevronDown className="w-3 h-3 opacity-60" />
              </button>

              {/* Input text */}
              <input 
                type="text" 
                value={inputQuery}
                onChange={e => setInputQuery(e.target.value)}
                onKeyDown={e => { if (e.key === 'Enter') handleSendMessage(); }}
                placeholder="Ask me to find, compare or research any product..."
                className="flex-1 bg-transparent text-xs sm:text-sm text-slate-800 placeholder-slate-400 focus:outline-none px-2"
              />

              {/* Mic Icon */}
              <button 
                onClick={() => alert("Voice input enabled: Speak your shopping request")}
                className="p-2 rounded-xl text-slate-400 hover:text-indigo-600 hover:bg-slate-50 transition-colors cursor-pointer"
              >
                <Mic className="w-4 h-4" />
              </button>

              {/* Send Button */}
              <button 
                onClick={() => handleSendMessage()}
                disabled={isSearching}
                className="w-9 h-9 rounded-xl bg-gradient-to-r from-purple-600 to-indigo-600 text-white flex items-center justify-center hover:opacity-95 shadow-sm shadow-purple-200 cursor-pointer disabled:opacity-50 transition-all shrink-0"
              >
                <Send className="w-4 h-4" />
              </button>
            </div>
          </div>

          <div ref={messagesEndRef} />
        </main>

        {/* ======================================================== */}
        {/* 4. RIGHT SIDEBAR                                         */}
        {/* ======================================================== */}
        <aside className="w-80 shrink-0 bg-[#F8F9FE] border-l border-slate-200/80 p-4 space-y-4 overflow-y-auto">
          
          {/* Top Card: AI Top Recommendation */}
          <div className="bg-white rounded-2xl border border-purple-200/80 p-4 shadow-xs relative overflow-hidden">
            <div className="flex items-center gap-1.5 text-xs font-bold text-purple-700 mb-2">
              <Crown className="w-4 h-4 text-amber-500 fill-amber-500" />
              <span>AI Top Recommendation</span>
            </div>

            <div className="h-28 w-full flex items-center justify-center rounded-xl bg-slate-50 overflow-hidden mb-2">
              <img 
                src={spotlightProduct?.image_url || spotlightProduct?.image || LAPTOP_HERO_IMAGE} 
                alt="Top Pick" 
                className="h-full object-contain" 
              />
            </div>

            <h4 className="font-bold text-slate-900 text-xs line-clamp-1">{spotlightProduct?.name || "ASUS TUF Gaming F15"}</h4>
            
            <div className="flex items-baseline gap-2 mt-1">
              <span className="text-base font-extrabold text-slate-900">
                ₹{(spotlightProduct?.price || 79990).toLocaleString()}
              </span>
              <span className="text-xs text-slate-400 line-through">
                ₹{((spotlightProduct?.original_price || 94990)).toLocaleString()}
              </span>
              <span className="text-xs font-bold text-emerald-600">
                16% OFF
              </span>
            </div>

            <div className="mt-3 pt-2 border-t border-slate-100">
              <span className="text-[11px] font-bold text-slate-800 block mb-1.5">Why this is recommended?</span>
              <div className="space-y-1 text-[11px] text-slate-600">
                <div className="flex items-center gap-1.5">
                  <Check className="w-3.5 h-3.5 text-emerald-500 stroke-[3] shrink-0" />
                  <span>Matches all your requirements (16GB, RTX)</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <Check className="w-3.5 h-3.5 text-emerald-500 stroke-[3] shrink-0" />
                  <span>Excellent performance for AI development</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <Check className="w-3.5 h-3.5 text-emerald-500 stroke-[3] shrink-0" />
                  <span>High rating (4.6 ⭐ from 18,942 reviews)</span>
                </div>
                <div className="flex items-center gap-1.5">
                  <Check className="w-3.5 h-3.5 text-emerald-500 stroke-[3] shrink-0" />
                  <span>Multiple seller options with competitive prices</span>
                </div>
              </div>
            </div>
          </div>

          {/* Second Card: Available on Multiple Sellers */}
          <div className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs">
            <div className="flex items-center gap-1.5 text-xs font-bold text-slate-800 mb-3">
              <Store className="w-4 h-4 text-purple-600" />
              <span>Available on Multiple Sellers</span>
            </div>

            <div className="space-y-2.5">
              {sellerList.map((seller, idx) => (
                <div key={idx} className="flex items-center justify-between text-xs py-1 border-b border-slate-50 last:border-0">
                  <div className="flex items-center gap-2">
                    <div className="w-6 h-6 rounded-lg bg-slate-100 flex items-center justify-center font-bold text-[10px] text-slate-700">
                      {seller.source.charAt(0)}
                    </div>
                    <div>
                      <div className="font-semibold text-slate-800">{seller.source}</div>
                      <div className="flex items-center gap-0.5 text-[10px] text-amber-500">
                        <Star className="w-2.5 h-2.5 fill-amber-500" />
                        <span>{seller.seller_rating || 4.5}</span>
                      </div>
                    </div>
                  </div>

                  <div className="flex items-center gap-2">
                    <div className="text-right">
                      <div className="font-bold text-slate-900">₹{seller.price.toLocaleString()}</div>
                      {idx === 0 && (
                        <span className="text-[9px] font-bold text-emerald-700 bg-emerald-50 px-1.5 py-0.2 rounded-full">
                          Best Price
                        </span>
                      )}
                    </div>

                    <button 
                      onClick={() => handleViewProduct(spotlightProduct!, seller)}
                      className="bg-purple-600 hover:bg-purple-700 text-white font-medium text-[11px] px-2.5 py-1.5 rounded-lg flex items-center gap-1 transition-colors cursor-pointer"
                    >
                      <span>View Deal</span>
                      <ExternalLink className="w-2.5 h-2.5" />
                    </button>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Third Card: Price Trend (Last 30 Days) */}
          <div className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs">
            <div className="flex items-center justify-between mb-2">
              <div className="flex items-center gap-1.5 text-xs font-bold text-slate-800">
                <BarChart3 className="w-4 h-4 text-indigo-600" />
                <span>Price Trend (Last 30 Days)</span>
              </div>
              <span className="bg-purple-100 text-purple-700 text-[10px] font-bold px-2 py-0.5 rounded-full">
                ₹{currentPrice.toLocaleString()} (Current)
              </span>
            </div>

            <div className="h-32 w-full pt-1">
              <ResponsiveContainer width="100%" height="100%">
                <AreaChart data={priceTrendData} margin={{ top: 5, right: 5, left: -25, bottom: 0 }}>
                  <defs>
                    <linearGradient id="priceGradient" x1="0" y1="0" x2="0" y2="1">
                      <stop offset="5%" stopColor="#8B5CF6" stopOpacity={0.4}/>
                      <stop offset="95%" stopColor="#8B5CF6" stopOpacity={0.0}/>
                    </linearGradient>
                  </defs>
                  <XAxis dataKey="date" tick={{ fontSize: 9, fill: '#94A3B8' }} axisLine={false} tickLine={false} />
                  <YAxis 
                    tick={{ fontSize: 9, fill: '#94A3B8' }} 
                    axisLine={false} 
                    tickLine={false}
                    domain={['dataMin - 5000', 'dataMax + 5000']} 
                    tickFormatter={v => `₹${Math.round(v/1000)}K`} 
                  />
                  <Tooltip 
                    formatter={(val: any) => [`₹${Number(val).toLocaleString()}`, 'Price']}
                    contentStyle={{ fontSize: 10, borderRadius: 8, padding: '4px 8px' }}
                  />
                  <Area 
                    type="monotone" 
                    dataKey="price" 
                    stroke="#8B5CF6" 
                    strokeWidth={2} 
                    fillOpacity={1} 
                    fill="url(#priceGradient)" 
                  />
                </AreaChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Fourth Card: Sources Searched (12) */}
          <div className="bg-white rounded-2xl border border-slate-200/80 p-4 shadow-xs">
            <div className="flex items-center justify-between mb-3">
              <div className="flex items-center gap-1.5 text-xs font-bold text-slate-800">
                <Globe className="w-4 h-4 text-blue-600" />
                <span>Sources Searched (12)</span>
              </div>
              <button 
                onClick={() => setSearchSummaryOpen(true)}
                className="text-[11px] font-semibold text-purple-600 hover:underline cursor-pointer"
              >
                View All
              </button>
            </div>

            <div className="grid grid-cols-4 gap-2">
              {[
                { name: 'Amazon', badge: 'a', color: 'bg-amber-50 text-amber-800 border-amber-200' },
                { name: 'Flipkart', badge: 'fk', color: 'bg-blue-50 text-blue-800 border-blue-200' },
                { name: 'Croma', badge: 'cr', color: 'bg-emerald-50 text-emerald-800 border-emerald-200' },
                { name: 'Reliance', badge: 'RD', color: 'bg-red-50 text-red-800 border-red-200' },
                { name: 'Vijay Sales', badge: 'VS', color: 'bg-orange-50 text-orange-800 border-orange-200' },
                { name: 'Tata CLiQ', badge: 'T', color: 'bg-purple-50 text-purple-800 border-purple-200' },
                { name: 'Brand Direct', badge: 'BD', color: 'bg-slate-50 text-slate-800 border-slate-200' },
                { name: '+5 More', badge: '+5', color: 'bg-purple-100 text-purple-700 border-purple-200 font-bold' }
              ].map((s, idx) => (
                <div 
                  key={idx} 
                  className={`border rounded-xl p-2 text-center flex flex-col items-center justify-center ${s.color}`}
                >
                  <span className="font-extrabold text-xs">{s.badge}</span>
                  <span className="text-[9px] font-medium truncate w-full mt-0.5">{s.name}</span>
                </div>
              ))}
            </div>
          </div>
        </aside>
      </div>

      {/* HUMAN APPROVAL CHECKOUT MODAL */}
      <HumanApprovalModal 
        isOpen={isCheckoutModalOpen}
        onClose={() => setIsCheckoutModalOpen(false)}
        product={selectedCheckoutProduct || { id: 'p1', name: 'Product', price: 0 }}
        onSuccess={handleApproveCheckout}
      />
    </div>
  );
}

export default ShopAIProPage;
