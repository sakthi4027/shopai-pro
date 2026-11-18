import React from 'react';
import { BrowserRouter as Router, Routes, Route, useLocation } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import { ProtectedRoute, PublicOnlyRoute, RootRoute } from './components/common/ProtectedRoute';
import { Navbar } from './components/common/Navbar';
import { Footer } from './components/common/Footer';

// Conversational AI Flagship Experience - ShopAI Pro Canvas
import { ShopAIProPage } from './pages/ShopAIProPage';

// Public & Deep-Dive Pages
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

  // Fullscreen view for ShopAI Pro dashboard canvas
  const isDashboardFullscreen =
    location.pathname === '/dashboard' ||
    location.pathname === '/chat' ||
    location.pathname === '/app' ||
    location.pathname.startsWith('/app');

  if (isDashboardFullscreen) {
    return (
      <main className="h-screen w-screen overflow-hidden">
        <Routes>
          <Route
            path="/dashboard"
            element={
              <ProtectedRoute>
                <ShopAIProPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/chat"
            element={
              <ProtectedRoute>
                <ShopAIProPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/app/*"
            element={
              <ProtectedRoute>
                <ShopAIProPage />
              </ProtectedRoute>
            }
          />
        </Routes>
      </main>
    );
  }

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900 selection:bg-indigo-500 selection:text-white">
      <Navbar />
      <main className="flex-1">
        <Routes>
          {/* Public Routes */}
          <Route path="/" element={<RootRoute />} />
          <Route path="/about" element={<LandingPage />} />
          <Route path="/portal" element={<LandingPage />} />
          <Route
            path="/login"
            element={
              <PublicOnlyRoute>
                <LoginPage />
              </PublicOnlyRoute>
            }
          />
          <Route
            path="/register"
            element={
              <PublicOnlyRoute>
                <RegisterPage />
              </PublicOnlyRoute>
            }
          />

          {/* Protected Routes */}
          <Route
            path="/products"
            element={
              <ProtectedRoute>
                <SearchResultsPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/products/:id"
            element={
              <ProtectedRoute>
                <ProductDetailPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/search"
            element={
              <ProtectedRoute>
                <AISearchPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/search/results"
            element={
              <ProtectedRoute>
                <SearchResultsPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/compare"
            element={
              <ProtectedRoute>
                <ProductComparisonPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/recommendations"
            element={
              <ProtectedRoute>
                <AIRecommendationPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/prices"
            element={
              <ProtectedRoute>
                <PriceIntelligencePage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/reviews"
            element={
              <ProtectedRoute>
                <ReviewIntelligencePage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/watchlist"
            element={
              <ProtectedRoute>
                <SavedProductsPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/saved"
            element={
              <ProtectedRoute>
                <SavedProductsPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/alerts"
            element={
              <ProtectedRoute>
                <PriceAlertsPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/history"
            element={
              <ProtectedRoute>
                <ShoppingHistoryPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/profile"
            element={
              <ProtectedRoute>
                <SettingsPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/settings"
            element={
              <ProtectedRoute>
                <SettingsPage />
              </ProtectedRoute>
            }
          />
          <Route
            path="/agents"
            element={
              <ProtectedRoute>
                <AIAgentActivityPage />
              </ProtectedRoute>
            }
          />

          {/* Catch-all fallback */}
          <Route path="*" element={<RootRoute />} />
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
