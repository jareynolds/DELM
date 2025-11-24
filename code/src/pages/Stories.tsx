import React from 'react';
import { BookOpen, ChevronRight } from 'lucide-react';
import { Card, StatusBadge } from '../components';

export const Stories: React.FC = () => {
  const mockStories = [
    {
      id: 'STORY-001',
      name: 'UI Component Generation',
      status: 'In Progress',
      progress: 65,
      description: 'Generate React components from natural language descriptions',
    },
    {
      id: 'STORY-002',
      name: 'Design System Integration',
      status: 'Planned',
      progress: 0,
      description: 'Integrate with existing design systems and style guides',
    },
    {
      id: 'STORY-003',
      name: 'Multi-format Export',
      status: 'Pending',
      progress: 20,
      description: 'Export generated components in multiple formats',
    },
    {
      id: 'STORY-004',
      name: 'Real-time Preview',
      status: 'Implemented',
      progress: 100,
      description: 'Preview generated components in real-time',
    },
  ];

  return (
    <div className="space-y-6">
      {/* Stories List */}
      <Card title="User Stories">
        <div className="space-y-4">
          {mockStories.map((story) => (
            <div
              key={story.id}
              className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-600 cursor-pointer transition-colors"
            >
              <div className="flex items-start justify-between mb-2">
                <div className="flex items-center gap-3">
                  <BookOpen className="text-primary-500" size={20} />
                  <div>
                    <h4 className="font-medium">{story.name}</h4>
                    <p className="text-sm text-gray-500">{story.id}</p>
                  </div>
                </div>
                <div className="flex items-center gap-2">
                  <StatusBadge status={story.status} />
                  <ChevronRight className="text-gray-400" size={20} />
                </div>
              </div>
              <p className="text-sm text-gray-600 dark:text-gray-300 mb-3">
                {story.description}
              </p>
              <div className="flex items-center gap-2">
                <div className="flex-1 h-2 bg-gray-200 dark:bg-gray-600 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-primary-500 transition-all"
                    style={{ width: `${story.progress}%` }}
                  />
                </div>
                <span className="text-sm text-gray-500">{story.progress}%</span>
              </div>
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
};

export default Stories;
