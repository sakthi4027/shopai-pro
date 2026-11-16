import React from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { Navbar } from './components/common/Navbar';
import { Footer } from './components/common/Footer';

// Conversational AI Primary Experience (ChatGPT / Perplexity-style) - ShopAI Pro Design
import { ShopAIProPage } from './pages/ShopAIProPage';
import { ConversationalAgentPage } from './pages/ConversationalAgentPage';

// Additional Deep-Dive Pages
import { LandingPage } from './pages/LandingPage';
import { LoginPage } from './pages/LoginPage';
import { RegisterPage } from './pages/RegisterPage';
import { AISearchPage } from './pages/AISearchPage';
import { SearchResultsPage } from './pages/SearchResultsPage';
import { ProductDetailPage } from './pages/ProductDetailPage';
import { ProductComparisonPage } from './pages/ProductComparisonPage';
import { AIRecommendationPage } from './pages/AIRecommendationPage';
import { PriceIntelligencePage } from './pages/PriceIntelligencePage';
import { ReviewIntelligencePage } from './pages/ReviewIntelligencePage';
import { SavedProductsPage } from './pages/SavedProductsPage';
import { PriceAlertsPage } from './pages/PriceAlertsPage';
import { ShoppingHistoryPage } from './pages/ShoppingHistoryPage';
import { AIAgentActivityPage } from './pages/AIAgentActivityPage';
import { SettingsPage } from './pages/SettingsPage';

function AppContent() {
  const location = useLocation();
  const isChatRoute = location.pathname === '/' || location.pathname === '/chat';

  if (isChatRoute) {
    return (
      <main className="h-screen w-screen overflow-hidden">
        <Routes>
          <Route path="/" element={<ShopAIProPage />} />
          <Route path="/chat" element={<ShopAIProPage />} />
        </Routes>
      </main>
    );
  }

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900 selection:bg-indigo-500 selection:text-white">
      <Navbar />
      <main className="flex-1">
        <Routes>
          <Route path="/portal" element={<LandingPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/search" element={<AISearchPage />} />
          <Route path="/search/results" element={<SearchResultsPage />} />
          <Route path="/products/:id" element={<ProductDetailPage />} />
          <Route path="/compare" element={<ProductComparisonPage />} />
          <Route path="/recommendations" element={<AIRecommendationPage />} />
          <Route path="/prices" element={<PriceIntelligencePage />} />
          <Route path="/reviews" element={<ReviewIntelligencePage />} />
          <Route path="/saved" element={<SavedProductsPage />} />
          <Route path="/alerts" element={<PriceAlertsPage />} />
          <Route path="/history" element={<ShoppingHistoryPage />} />
          <Route path="/agents" element={<AIAgentActivityPage />} />
          <Route path="/settings" element={<SettingsPage />} />
        </Routes>
      </main>
      <Footer />
    </div>
  );
}

export function App() {
  return (
    <AuthProvider>
      <Router>
        <AppContent />
      </Router>
    </AuthProvider>
  );
}

export default App;
