import React from 'react';
import { Layers, Cpu, BookOpen, Activity } from 'lucide-react';
import { Card, StatusBadge } from '../components';
import { useApp } from '../context/AppContext';

export const Dashboard: React.FC = () => {
  const { dashboardStats, capabilities, serviceHealth } = useApp();

  if (!dashboardStats) {
    return <div>Loading...</div>;
  }

  const statCards = [
    {
      label: 'Capabilities',
      value: `${dashboardStats.implementedCapabilities}/${dashboardStats.totalCapabilities}`,
      icon: Layers,
      color: 'bg-blue-500',
    },
    {
      label: 'Enablers',
      value: `${dashboardStats.implementedEnablers}/${dashboardStats.totalEnablers}`,
      icon: Cpu,
      color: 'bg-purple-500',
    },
    {
      label: 'Stories',
      value: `${dashboardStats.completedStories}/${dashboardStats.totalStories}`,
      icon: BookOpen,
      color: 'bg-green-500',
    },
    {
      label: 'Service Health',
      value: `${dashboardStats.serviceHealth}%`,
      icon: Activity,
      color: 'bg-yellow-500',
    },
  ];

  return (
    <div className="space-y-6">
      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {statCards.map((stat) => {
          const Icon = stat.icon;
          return (
            <Card key={stat.label}>
              <div className="flex items-center gap-4">
                <div className={`${stat.color} p-3 rounded-lg`}>
                  <Icon className="text-white" size={24} />
                </div>
                <div>
                  <p className="text-sm text-gray-500 dark:text-gray-400">{stat.label}</p>
                  <p className="text-2xl font-bold">{stat.value}</p>
                </div>
              </div>
            </Card>
          );
        })}
      </div>

      {/* Recent Capabilities */}
      <Card title="Recent Capabilities">
        <div className="space-y-3">
          {capabilities.slice(0, 5).map((cap) => (
            <div
              key={cap.id}
              className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg"
            >
              <div>
                <p className="font-medium">{cap.name}</p>
                <p className="text-sm text-gray-500 dark:text-gray-400">{cap.id}</p>
              </div>
              <StatusBadge status={cap.metadata.status} />
            </div>
          ))}
        </div>
      </Card>

      {/* Service Health */}
      <Card title="Service Health">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {serviceHealth.map((service) => (
            <div
              key={service.id}
              className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg"
            >
              <div>
                <p className="font-medium">{service.name}</p>
                <p className="text-sm text-gray-500 dark:text-gray-400">
                  {service.responseTime}ms | {service.uptime}% uptime
                </p>
              </div>
              <StatusBadge status={service.status} />
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
};

export default Dashboard;
