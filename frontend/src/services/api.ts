import {
  User,
  UserPreferences,
  Product,
  SearchWorkflowResult,
  ReviewAnalysis,
  SellerPrice,
  ConversationSummary,
  ConversationDetail,
  ChatMessage,
  CheckoutManifest
} from '../types';

const API_BASE = '/api/v1';

function getAuthHeader(): Record<string, string> {
  const token = localStorage.getItem('auth_token');
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function handleResponse<T>(res: Response): Promise<T> {
  if (!res.ok) {
    let errorDetail = 'API Request Failed';
    try {
      const data = await res.json();
      errorDetail = data.detail || errorDetail;
    } catch {
      // fallback
    }
    throw new Error(errorDetail);
  }
  return res.json();
}

export const api = {
  // Auth
  async login(email: string, password: string): Promise<{ access_token: string; user_id: string; email: string; full_name?: string }> {
    const res = await fetch(`${API_BASE}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    return handleResponse(res);
  },

  async register(email: string, password: string, full_name?: string): Promise<{ access_token: string; user_id: string; email: string }> {
    const res = await fetch(`${API_BASE}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password, full_name })
    });
    return handleResponse(res);
  },

  async getMe(): Promise<User> {
    const res = await fetch(`${API_BASE}/auth/me`, {
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  // Preferences
  async getPreferences(): Promise<UserPreferences> {
    const res = await fetch(`${API_BASE}/preferences`, {
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  async updatePreferences(pref: Partial<UserPreferences>): Promise<UserPreferences> {
    const res = await fetch(`${API_BASE}/preferences`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json', ...getAuthHeader() },
      body: JSON.stringify(pref)
    });
    return handleResponse(res);
  },

  async resetPreferences(): Promise<{ message: string }> {
    const res = await fetch(`${API_BASE}/preferences`, {
      method: 'DELETE',
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  // Search
  async search(query: string, custom_budget_max?: number): Promise<SearchWorkflowResult> {
    const res = await fetch(`${API_BASE}/search/query`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeader() },
      body: JSON.stringify({ query, custom_budget_max })
    });
    return handleResponse(res);
  },

  async getSearchHistory(): Promise<Array<{ id: string; title: string; status: string; created_at: string }>> {
    const res = await fetch(`${API_BASE}/search/history`, {
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  // Products
  async getProducts(params?: { category?: string; search?: string }): Promise<Product[]> {
    const q = new URLSearchParams();
    if (params?.category) q.append('category', params.category);
    if (params?.search) q.append('search', params.search);
    const res = await fetch(`${API_BASE}/products?${q.toString()}`);
    return handleResponse(res);
  },

  async getProductDetail(id: string): Promise<Product & { prices: SellerPrice[]; price_history: Array<{ date: string; price: number }> }> {
    const res = await fetch(`${API_BASE}/products/${id}`);
    return handleResponse(res);
  },

  // Compare
  async compareProducts(product_ids: string[]): Promise<any> {
    const res = await fetch(`${API_BASE}/compare`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ product_ids })
    });
    return handleResponse(res);
  },

  // Reviews
  async getReviews(product_id: string): Promise<any[]> {
    const res = await fetch(`${API_BASE}/reviews/${product_id}`);
    return handleResponse(res);
  },

  async getReviewAnalysis(product_id: string): Promise<ReviewAnalysis> {
    const res = await fetch(`${API_BASE}/reviews/${product_id}/analysis`);
    return handleResponse(res);
  },

  // Prices
  async getSellerPrices(product_id: string): Promise<SellerPrice[]> {
    const res = await fetch(`${API_BASE}/prices/${product_id}/sellers`);
    return handleResponse(res);
  },

  async getPriceHistory(product_id: string): Promise<{ product_id: string; history: Array<{ date: string; price: number }>; price_insight: string }> {
    const res = await fetch(`${API_BASE}/prices/${product_id}/history`);
    return handleResponse(res);
  },

  // Saved Products
  async getSavedProducts(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/saved`, {
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  async saveProduct(product_id: string, notes?: string): Promise<{ message: string }> {
    const res = await fetch(`${API_BASE}/saved/${product_id}`, {
      method: 'POST',
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  async removeSavedProduct(product_id: string): Promise<{ message: string }> {
    const res = await fetch(`${API_BASE}/saved/${product_id}`, {
      method: 'DELETE',
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  // Alerts
  async getAlerts(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/alerts`, {
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  async createAlert(product_id: string, target_price: number): Promise<{ message: string }> {
    const res = await fetch(`${API_BASE}/alerts`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeader() },
      body: JSON.stringify({ product_id, target_price })
    });
    return handleResponse(res);
  },

  async deleteAlert(alert_id: string): Promise<{ message: string }> {
    const res = await fetch(`${API_BASE}/alerts/${alert_id}`, {
      method: 'DELETE',
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  // Checkout (Human-in-the-Loop)
  async reviewCheckout(product_id: string, seller_id?: string): Promise<any> {
    const res = await fetch(`${API_BASE}/checkout/review`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeader() },
      body: JSON.stringify({ product_id, seller_id })
    });
    return handleResponse(res);
  },

  async confirmCheckout(product_id: string, seller_id: string, total_amount: number, user_confirmed: boolean): Promise<any> {
    const res = await fetch(`${API_BASE}/checkout/confirm`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeader() },
      body: JSON.stringify({ product_id, seller_id, total_amount, user_confirmed })
    });
    return handleResponse(res);
  },

  // Audit Logs
  async getAuditLogs(): Promise<any[]> {
    const res = await fetch(`${API_BASE}/audit`, {
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  // Agents
  async getAgentTasks(session_id: string): Promise<any> {
    const res = await fetch(`${API_BASE}/agents/tasks/${session_id}`);
    return handleResponse(res);
  },

  // Conversational AI Deep Search
  async listConversations(): Promise<ConversationSummary[]> {
    const res = await fetch(`${API_BASE}/conversations`, {
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  async createConversation(title?: string, search_mode: string = "deep"): Promise<ConversationDetail> {
    const res = await fetch(`${API_BASE}/conversations`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeader() },
      body: JSON.stringify({ title, search_mode })
    });
    return handleResponse(res);
  },

  async getConversation(id: string): Promise<ConversationDetail> {
    const res = await fetch(`${API_BASE}/conversations/${id}`, {
      headers: { ...getAuthHeader() }
    });
    return handleResponse(res);
  },

  async deleteConversation(id: string): Promise<void> {
    const res = await fetch(`${API_BASE}/conversations/${id}`, {
      method: 'DELETE',
      headers: { ...getAuthHeader() }
    });
    if (!res.ok) {
      throw new Error("Failed to delete conversation");
    }
  },

  async sendChatMessage(id: string, content: string, search_mode?: string): Promise<ChatMessage> {
    const res = await fetch(`${API_BASE}/conversations/${id}/messages`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeader() },
      body: JSON.stringify({ content, search_mode })
    });
    return handleResponse(res);
  },

  async requestCheckoutIntent(data: {
    product_id?: string;
    product_name: string;
    seller_name: string;
    price: number;
    shipping_cost?: number;
    product_url: string;
  }): Promise<CheckoutManifest> {
    const res = await fetch(`${API_BASE}/conversations/checkout-intent`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', ...getAuthHeader() },
      body: JSON.stringify(data)
    });
    return handleResponse(res);
  }
};
