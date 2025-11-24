import React, { useState } from 'react';
import { Clock, CheckCircle, AlertCircle, Loader } from 'lucide-react';
import { Card, StatusBadge } from '../components';

export const Prompts: React.FC = () => {
  const [prompts] = useState([
    {
      id: '1',
      prompt: 'Create a responsive card component with image, title, and description',
      status: 'completed',
      timestamp: new Date(Date.now() - 3600000).toISOString(),
      response: 'Generated CardComponent.tsx with responsive design and Tailwind styling',
    },
    {
      id: '2',
      prompt: 'Design a navigation bar with dropdown menus',
      status: 'completed',
      timestamp: new Date(Date.now() - 7200000).toISOString(),
      response: 'Generated NavBar.tsx with dropdown functionality',
    },
    {
      id: '3',
      prompt: 'Build a form with validation for user registration',
      status: 'processing',
      timestamp: new Date().toISOString(),
      response: null,
    },
    {
      id: '4',
      prompt: 'Create a dashboard layout with sidebar',
      status: 'pending',
      timestamp: new Date().toISOString(),
      response: null,
    },
  ]);

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'completed':
        return <CheckCircle className="text-green-500" size={16} />;
      case 'processing':
        return <Loader className="text-blue-500 animate-spin" size={16} />;
      case 'pending':
        return <Clock className="text-yellow-500" size={16} />;
      case 'failed':
        return <AlertCircle className="text-red-500" size={16} />;
      default:
        return null;
    }
  };

  return (
    <div className="space-y-6">
      {/* Prompt Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <p className="text-sm text-gray-500">Total Prompts</p>
          <p className="text-2xl font-bold">{prompts.length}</p>
        </Card>
        <Card>
          <p className="text-sm text-gray-500">Completed</p>
          <p className="text-2xl font-bold text-green-600">
            {prompts.filter((p) => p.status === 'completed').length}
          </p>
        </Card>
        <Card>
          <p className="text-sm text-gray-500">Processing</p>
          <p className="text-2xl font-bold text-blue-600">
            {prompts.filter((p) => p.status === 'processing').length}
          </p>
        </Card>
        <Card>
          <p className="text-sm text-gray-500">Pending</p>
          <p className="text-2xl font-bold text-yellow-600">
            {prompts.filter((p) => p.status === 'pending').length}
          </p>
        </Card>
      </div>

      {/* Prompt History */}
      <Card title="Prompt History">
        <div className="space-y-4">
          {prompts.map((prompt) => (
            <div
              key={prompt.id}
              className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg"
            >
              <div className="flex items-start justify-between mb-2">
                <div className="flex items-center gap-2">
                  {getStatusIcon(prompt.status)}
                  <span className="font-medium">{prompt.prompt}</span>
                </div>
                <span className="text-xs text-gray-500">
                  {new Date(prompt.timestamp).toLocaleString()}
                </span>
              </div>
              {prompt.response && (
                <p className="text-sm text-gray-600 dark:text-gray-300 mt-2 pl-6">
                  {prompt.response}
                </p>
              )}
              {prompt.status === 'processing' && (
                <p className="text-sm text-blue-500 mt-2 pl-6">
                  Generating UI component...
                </p>
              )}
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
};

export default Prompts;
