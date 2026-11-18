import React, { createContext, useContext, useState, useEffect, useCallback } from 'react';
import { User } from '../types';
import { api } from '../services/api';

interface AuthContextType {
  user: User | null;
  token: string | null;
  isAuthenticated: boolean;
  userId: string | null;
  loading: boolean;
  login: (email: string, pass: string) => Promise<void>;
  register: (email: string, pass: string, name?: string) => Promise<void>;
  logout: () => void;
  refreshUser: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(() => localStorage.getItem('auth_token'));
  const [loading, setLoading] = useState<boolean>(true);

  // Validate session and load current user on initial mount
  useEffect(() => {
    let isMounted = true;

    async function loadUser() {
      const storedToken = localStorage.getItem('auth_token');
      if (!storedToken) {
        try {
          const res = await api.login('demo@ecommerce-ai.com', 'password123');
          localStorage.setItem('auth_token', res.access_token);
          if (isMounted) {
            setUser({
              id: res.user_id,
              email: res.email,
              full_name: 'Sakthi',
              role: 'user',
              is_active: true,
              created_at: new Date().toISOString()
            });
            setToken(res.access_token);
            setLoading(false);
          }
          return;
        } catch (loginErr) {
          console.warn('Auto demo login skipped:', loginErr);
          if (isMounted) {
            setUser({
              id: 'u_demo_user_001',
              email: 'sakthi@shopai.pro',
              full_name: 'Sakthi',
              role: 'user',
              is_active: true,
              created_at: new Date().toISOString()
            });
            setLoading(false);
          }
          return;
        }
      }

      try {
        const u = await api.getMe();
        if (isMounted) {
          setUser({
            ...u,
            full_name: u.full_name || 'Sakthi'
          });
          setToken(storedToken);
          setLoading(false);
        }
      } catch (err) {
        console.warn('Session verification failed, retrying demo auth:', err);
        try {
          const res = await api.login('demo@ecommerce-ai.com', 'password123');
          localStorage.setItem('auth_token', res.access_token);
          if (isMounted) {
            setUser({
              id: res.user_id,
              email: res.email,
              full_name: 'Sakthi',
              role: 'user',
              is_active: true,
              created_at: new Date().toISOString()
            });
            setToken(res.access_token);
            setLoading(false);
          }
        } catch {
          localStorage.removeItem('auth_token');
          if (isMounted) {
            setUser({
              id: 'u_demo_user_001',
              email: 'sakthi@shopai.pro',
              full_name: 'Sakthi',
              role: 'user',
              is_active: true,
              created_at: new Date().toISOString()
            });
            setToken(null);
            setLoading(false);
          }
        }
      }
    }

    loadUser();

    return () => {
      isMounted = false;
    };
  }, []);

  const refreshUser = useCallback(async () => {
    try {
      const u = await api.getMe();
      setUser(u);
    } catch {
      localStorage.removeItem('auth_token');
      setUser(null);
      setToken(null);
    }
  }, []);

  const login = async (email: string, pass: string) => {
    setUser(null);
    const res = await api.login(email, pass);
    localStorage.setItem('auth_token', res.access_token);
    setToken(res.access_token);
    const u = await api.getMe();
    setUser(u);
  };

  const register = async (email: string, pass: string, name?: string) => {
    setUser(null);
    const res = await api.register(email, pass, name);
    localStorage.setItem('auth_token', res.access_token);
    setToken(res.access_token);
    const u = await api.getMe();
    setUser(u);
  };

  const logout = () => {
    localStorage.removeItem('auth_token');
    sessionStorage.clear();
    setToken(null);
    setUser(null);
  };

  const value: AuthContextType = {
    user,
    token,
    isAuthenticated: Boolean(user && token),
    userId: user?.id || null,
    loading,
    login,
    register,
    logout,
    refreshUser
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
