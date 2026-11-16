import React, { createContext, useContext, useState, useEffect } from 'react';
import { User } from '../types';
import { api } from '../services/api';

interface AuthContextType {
  user: User | null;
  token: string | null;
  loading: boolean;
  login: (email: string, pass: string) => Promise<void>;
  register: (email: string, pass: string, name?: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType>({} as AuthContextType);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [token, setToken] = useState<string | null>(localStorage.getItem('auth_token'));
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    async function loadUser() {
      let activeToken = token;
      if (!activeToken) {
        // Auto-authenticate default pro session for instant live access
        try {
          const res = await api.login('karthik@shopaipro.com', 'karthik123');
          localStorage.setItem('auth_token', res.access_token);
          setToken(res.access_token);
          activeToken = res.access_token;
        } catch (e1) {
          try {
            const res2 = await api.login('demo@ecommerce-ai.com', 'password123');
            localStorage.setItem('auth_token', res2.access_token);
            setToken(res2.access_token);
            activeToken = res2.access_token;
          } catch (e2) {
            console.warn('Auto-login fallback failed', e2);
          }
        }
      }

      if (activeToken) {
        try {
          const u = await api.getMe();
          setUser(u);
        } catch (err) {
          console.warn('Token validation failed, clearing session', err);
          localStorage.removeItem('auth_token');
          setToken(null);
          setUser(null);
        }
      }
      setLoading(false);
    }
    loadUser();
  }, [token]);

  const login = async (email: string, pass: string) => {
    const res = await api.login(email, pass);
    localStorage.setItem('auth_token', res.access_token);
    setToken(res.access_token);
    const u = await api.getMe();
    setUser(u);
  };

  const register = async (email: string, pass: string, name?: string) => {
    const res = await api.register(email, pass, name);
    localStorage.setItem('auth_token', res.access_token);
    setToken(res.access_token);
    const u = await api.getMe();
    setUser(u);
  };

  const logout = () => {
    localStorage.removeItem('auth_token');
    setToken(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, token, loading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
