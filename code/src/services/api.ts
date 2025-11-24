import axios from 'axios';
import type {
  Capability,
  Enabler,
  Story,
  ServiceHealth,
  UserPrompt,
  OutputDelivery,
  DashboardStats,
  SLMConfig
} from '../types';

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Dashboard
export const getDashboardStats = async (): Promise<DashboardStats> => {
  const response = await api.get('/dashboard/stats');
  return response.data;
};

// Capabilities
export const getCapabilities = async (): Promise<Capability[]> => {
  const response = await api.get('/capabilities');
  return response.data;
};

export const getCapability = async (id: string): Promise<Capability> => {
  const response = await api.get(`/capabilities/${id}`);
  return response.data;
};

export const createCapability = async (capability: Partial<Capability>): Promise<Capability> => {
  const response = await api.post('/capabilities', capability);
  return response.data;
};

export const updateCapability = async (id: string, capability: Partial<Capability>): Promise<Capability> => {
  const response = await api.put(`/capabilities/${id}`, capability);
  return response.data;
};

// Enablers
export const getEnablers = async (): Promise<Enabler[]> => {
  const response = await api.get('/enablers');
  return response.data;
};

export const getEnabler = async (id: string): Promise<Enabler> => {
  const response = await api.get(`/enablers/${id}`);
  return response.data;
};

// Stories
export const getStories = async (): Promise<Story[]> => {
  const response = await api.get('/stories');
  return response.data;
};

export const getStory = async (id: string): Promise<Story> => {
  const response = await api.get(`/stories/${id}`);
  return response.data;
};

// Service Health
export const getServiceHealth = async (): Promise<ServiceHealth[]> => {
  const response = await api.get('/health/services');
  return response.data;
};

// User Prompts
export const submitPrompt = async (prompt: string): Promise<UserPrompt> => {
  const response = await api.post('/prompts', { prompt });
  return response.data;
};

export const getPromptHistory = async (): Promise<UserPrompt[]> => {
  const response = await api.get('/prompts');
  return response.data;
};

// Output Delivery
export const getOutputs = async (promptId?: string): Promise<OutputDelivery[]> => {
  const params = promptId ? { promptId } : {};
  const response = await api.get('/outputs', { params });
  return response.data;
};

// SLM Configuration
export const getSLMConfig = async (): Promise<SLMConfig> => {
  const response = await api.get('/slm/config');
  return response.data;
};

export const updateSLMConfig = async (config: Partial<SLMConfig>): Promise<SLMConfig> => {
  const response = await api.put('/slm/config', config);
  return response.data;
};

export default api;
