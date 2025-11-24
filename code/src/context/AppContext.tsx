import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import type {
  Capability,
  Enabler,
  Story,
  ServiceHealth,
  DashboardStats,
  AIGovernance
} from '../types';

interface AppContextType {
  capabilities: Capability[];
  enablers: Enabler[];
  stories: Story[];
  serviceHealth: ServiceHealth[];
  dashboardStats: DashboardStats | null;
  aiGovernance: AIGovernance;
  isLoading: boolean;
  error: string | null;
  setCapabilities: (capabilities: Capability[]) => void;
  setEnablers: (enablers: Enabler[]) => void;
  setStories: (stories: Story[]) => void;
  setServiceHealth: (health: ServiceHealth[]) => void;
  setDashboardStats: (stats: DashboardStats) => void;
  setAIGovernance: (governance: AIGovernance) => void;
  setError: (error: string | null) => void;
  setLoading: (loading: boolean) => void;
}

const defaultGovernance: AIGovernance = {
  presetLevel: 2,
  workflowCompliance: true,
  qualityGatesEnabled: true,
  documentationStandards: true,
  securityCompliance: true,
};

const AppContext = createContext<AppContextType | undefined>(undefined);

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [capabilities, setCapabilities] = useState<Capability[]>([]);
  const [enablers, setEnablers] = useState<Enabler[]>([]);
  const [stories, setStories] = useState<Story[]>([]);
  const [serviceHealth, setServiceHealth] = useState<ServiceHealth[]>([]);
  const [dashboardStats, setDashboardStats] = useState<DashboardStats | null>(null);
  const [aiGovernance, setAIGovernance] = useState<AIGovernance>(defaultGovernance);
  const [isLoading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  // Load mock data for development
  useEffect(() => {
    const mockCapabilities: Capability[] = [
      {
        id: 'CAP-008',
        name: 'Small Language Model for UI Design',
        metadata: {
          id: 'CAP-008',
          type: 'Capability',
          status: 'Planned',
          generated: '11/22/2025, 10:03:26 AM',
        },
        description: 'Core SLM capability for generating UI design solutions',
        enablers: [
          'Environment Setup Service',
          'TAD Service',
          'TDC Service',
          'Transformer Service',
          'Data Collection Services',
          'SLM Trainer',
          'Design Experience Small Language Model Engine',
          'DELM Fine Tuning Service',
        ],
        upstreamDependencies: [],
        downstreamImpacts: [
          'Dependency Management',
          'Output Delivery System',
          'Flow Visualization',
          'User Prompt Service',
        ],
        implementationNotes: 'Requires transformer architecture with specialized tokenizer for UI design patterns',
        acceptanceCriteria: ['Model generates valid UI components', 'Response time under 2 seconds'],
      },
      {
        id: 'CAP-318652',
        name: 'Capability Tracking',
        metadata: {
          id: 'CAP-318652',
          type: 'Capability',
          status: 'Implemented',
          generated: '11/22/2025, 10:24:01 AM',
        },
        description: 'Track and manage all system capabilities and their dependencies',
        enablers: ['Capability Service Endpoint', 'Health Monitoring'],
        upstreamDependencies: ['Design Artifact Management', 'Figma Integration Management'],
        downstreamImpacts: [],
        implementationNotes: 'Uses graph-based dependency tracking',
        acceptanceCriteria: ['All capabilities tracked', 'Dependencies visualized'],
      },
      {
        id: 'CAP-011',
        name: 'Output Delivery System',
        metadata: {
          id: 'CAP-011',
          type: 'Capability',
          status: 'In Progress',
          generated: '11/22/2025, 10:03:26 AM',
        },
        description: 'Delivers generated UI designs to users',
        enablers: [],
        upstreamDependencies: ['Small Language Model for UI Design'],
        downstreamImpacts: [],
        implementationNotes: 'Supports multiple output formats',
        acceptanceCriteria: ['Delivers all output types', 'Maintains formatting'],
      },
      {
        id: 'CAP-015',
        name: 'User Prompt Service',
        metadata: {
          id: 'CAP-015',
          type: 'Capability',
          status: 'In Progress',
          generated: '11/22/2025, 10:03:26 AM',
        },
        description: 'Handles user prompts for UI design generation',
        enablers: [],
        upstreamDependencies: ['Small Language Model for UI Design'],
        downstreamImpacts: [],
        implementationNotes: 'Natural language processing for design intent',
        acceptanceCriteria: ['Processes natural language', 'Extracts design intent'],
      },
      {
        id: 'CAP-004',
        name: 'System Health Monitoring',
        metadata: {
          id: 'CAP-004',
          type: 'Capability',
          status: 'Planned',
          generated: '11/22/2025, 10:03:26 AM',
        },
        description: 'Monitor system health and service status',
        enablers: ['Microservices Health Monitoring Enabler'],
        upstreamDependencies: [],
        downstreamImpacts: [],
        implementationNotes: 'Real-time health checks with alerting',
        acceptanceCriteria: ['All services monitored', 'Alerts functional'],
      },
    ];

    const mockServiceHealth: ServiceHealth[] = [
      { id: '1', name: 'SLM Engine', status: 'healthy', lastCheck: new Date().toISOString(), responseTime: 45, uptime: 99.9 },
      { id: '2', name: 'Transformer Service', status: 'healthy', lastCheck: new Date().toISOString(), responseTime: 120, uptime: 99.5 },
      { id: '3', name: 'Output Delivery', status: 'degraded', lastCheck: new Date().toISOString(), responseTime: 350, uptime: 98.2 },
      { id: '4', name: 'User Prompt Service', status: 'healthy', lastCheck: new Date().toISOString(), responseTime: 80, uptime: 99.8 },
    ];

    const mockStats: DashboardStats = {
      totalCapabilities: 5,
      implementedCapabilities: 1,
      totalEnablers: 8,
      implementedEnablers: 3,
      totalStories: 10,
      completedStories: 4,
      serviceHealth: 85,
    };

    setCapabilities(mockCapabilities);
    setServiceHealth(mockServiceHealth);
    setDashboardStats(mockStats);
  }, []);

  return (
    <AppContext.Provider
      value={{
        capabilities,
        enablers,
        stories,
        serviceHealth,
        dashboardStats,
        aiGovernance,
        isLoading,
        error,
        setCapabilities,
        setEnablers,
        setStories,
        setServiceHealth,
        setDashboardStats,
        setAIGovernance,
        setError,
        setLoading,
      }}
    >
      {children}
    </AppContext.Provider>
  );
};

export const useApp = () => {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error('useApp must be used within an AppProvider');
  }
  return context;
};
