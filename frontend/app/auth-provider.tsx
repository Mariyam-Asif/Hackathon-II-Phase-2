
'use client';

import {
  createContext,
  useContext,
  useEffect,
  useState,
  ReactNode,
} from 'react';
import { authService, AuthResponse } from '../lib/auth';
import { useRouter } from 'next/navigation';

interface AuthContextType {
  isAuthenticated: boolean;
  user: AuthResponse | null;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<AuthResponse | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const router = useRouter();

  useEffect(() => {
    const validateUser = async () => {
      setIsLoading(true);
      const token = authService.getToken();
      if (token) {
        const isValid = await authService.validateToken(token);
        if (isValid) {
          // In a real app, you'd fetch user data here
          // For now, we'll assume the token is enough
          // and decode it to get some user info.
          const decodedToken = JSON.parse(atob(token.split('.')[1]));
          setUser(decodedToken);
        } else {
          await authService.logout();
          setUser(null);
        }
      } else {
        setUser(null);
      }
      setIsLoading(false);
    };

    validateUser();
  }, []);

  const login = async (email: string, password: string) => {
    try {
      const userData = await authService.login({ email, password });
      setUser(userData);
      router.push('/dashboard');
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    }
  };

  const logout = async () => {
    await authService.logout();
    await fetch('/api/auth/logout', { method: 'POST' });
    setUser(null);
    router.push('/auth/login');
  };

  const value = {
    isAuthenticated: !!user,
    user,
    isLoading,
    login,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
}
