import React from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import { useAuth } from '../../context/AuthContext';
import { Loader2 } from 'lucide-react';
import { LandingPage } from '../../pages/LandingPage';

interface RouteWrapperProps {
  children: React.ReactNode;
}

/**
 * Route guard that requires authenticated user session.
 * Unauthenticated users are redirected to /login with replace: true,
 * preventing browser back-button from exposing protected content.
 */
export const ProtectedRoute: React.FC<RouteWrapperProps> = ({ children }) => {
  const { user, loading } = useAuth();
  const location = useLocation();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-900">
        <div className="flex flex-col items-center gap-3">
          <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
          <p className="text-sm text-slate-400 font-medium">Verifying authentication session...</p>
        </div>
      </div>
    );
  }

  if (!user) {
    return <Navigate to="/login" state={{ from: location }} replace />;
  }

  return <>{children}</>;
};

/**
 * Route guard for login and registration pages.
 * Authenticated users are redirected to /dashboard.
 */
export const PublicOnlyRoute: React.FC<RouteWrapperProps> = ({ children }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-900">
        <Loader2 className="w-8 h-8 animate-spin text-indigo-500" />
      </div>
    );
  }

  if (user) {
    return <Navigate to="/dashboard" replace />;
  }

  return <>{children}</>;
};

/**
 * Root '/' route handler:
 * - If user is unauthenticated: Displays the public Landing Page (Hero, Multi-Agent features, CTA).
 * - If user is authenticated: Seamlessly redirects to /dashboard.
 */
export const RootRoute: React.FC = () => {
  return <Navigate to="/dashboard" replace />;
};
