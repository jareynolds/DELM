// Core types for ESLM UI Design application

export type Status = 'Planned' | 'In Progress' | 'Implemented' | 'Pending' | 'Completed';

export interface Metadata {
  id: string;
  type: 'Capability' | 'Enabler' | 'Story' | 'Requirement';
  status: Status;
  generated: string;
  lastModified?: string;
}

export interface Capability {
  id: string;
  name: string;
  metadata: Metadata;
  description: string;
  enablers: string[];
  upstreamDependencies: string[];
  downstreamImpacts: string[];
  implementationNotes: string;
  acceptanceCriteria: string[];
}

export interface Enabler {
  id: string;
  name: string;
  metadata: Metadata;
  description: string;
  parentCapability: string;
  implementationNotes: string;
  acceptanceCriteria: string[];
}

export interface Story {
  id: string;
  name: string;
  metadata: Metadata;
  overview: string;
  description: string;
  dependencies: string[];
  implementationNotes: string;
  flowVisualization: string;
  successCriteria: string[];
  statistics: StoryStatistics;
}

export interface StoryStatistics {
  totalTasks: number;
  completedTasks: number;
  progress: number;
}

export interface ServiceHealth {
  id: string;
  name: string;
  status: 'healthy' | 'degraded' | 'unhealthy';
  lastCheck: string;
  responseTime: number;
  uptime: number;
}

export interface UserPrompt {
  id: string;
  prompt: string;
  timestamp: string;
  status: 'pending' | 'processing' | 'completed' | 'failed';
  response?: string;
}

export interface OutputDelivery {
  id: string;
  type: 'component' | 'style' | 'layout' | 'code';
  content: string;
  timestamp: string;
  promptId: string;
}

export interface FlowNode {
  id: string;
  type: 'capability' | 'enabler' | 'service';
  name: string;
  status: Status;
}

export interface FlowEdge {
  source: string;
  target: string;
  type: 'dependency' | 'impact';
}

export interface FlowVisualization {
  nodes: FlowNode[];
  edges: FlowEdge[];
}

export interface SLMConfig {
  modelName: string;
  version: string;
  temperature: number;
  maxTokens: number;
  enabled: boolean;
}

export interface AIGovernance {
  presetLevel: 1 | 2 | 3;
  workflowCompliance: boolean;
  qualityGatesEnabled: boolean;
  documentationStandards: boolean;
  securityCompliance: boolean;
}

export interface DashboardStats {
  totalCapabilities: number;
  implementedCapabilities: number;
  totalEnablers: number;
  implementedEnablers: number;
  totalStories: number;
  completedStories: number;
  serviceHealth: number;
}
