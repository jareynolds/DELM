import React from 'react';
import { RefreshCw, AlertTriangle, CheckCircle, XCircle } from 'lucide-react';
import { Card, StatusBadge } from '../components';
import { useApp } from '../context/AppContext';

export const Health: React.FC = () => {
  const { serviceHealth } = useApp();

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'healthy':
        return <CheckCircle className="text-green-500" size={20} />;
      case 'degraded':
        return <AlertTriangle className="text-yellow-500" size={20} />;
      case 'unhealthy':
        return <XCircle className="text-red-500" size={20} />;
      default:
        return null;
    }
  };

  const overallHealth = serviceHealth.length > 0
    ? Math.round(
        serviceHealth.filter((s) => s.status === 'healthy').length /
          serviceHealth.length *
          100
      )
    : 0;

  return (
    <div className="space-y-6">
      {/* Overall Health */}
      <Card>
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-lg font-semibold">Overall System Health</h3>
            <p className="text-3xl font-bold mt-2">{overallHealth}%</p>
          </div>
          <button className="btn-secondary flex items-center gap-2">
            <RefreshCw size={18} />
            Refresh
          </button>
        </div>
        <div className="mt-4 h-2 bg-gray-200 dark:bg-gray-700 rounded-full overflow-hidden">
          <div
            className={`h-full transition-all ${
              overallHealth >= 80
                ? 'bg-green-500'
                : overallHealth >= 50
                ? 'bg-yellow-500'
                : 'bg-red-500'
            }`}
            style={{ width: `${overallHealth}%` }}
          />
        </div>
      </Card>

      {/* Service Status */}
      <Card title="Service Status">
        <div className="space-y-4">
          {serviceHealth.map((service) => (
            <div
              key={service.id}
              className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg"
            >
              <div className="flex items-center gap-3">
                {getStatusIcon(service.status)}
                <div>
                  <p className="font-medium">{service.name}</p>
                  <p className="text-sm text-gray-500">
                    Last check: {new Date(service.lastCheck).toLocaleTimeString()}
                  </p>
                </div>
              </div>
              <div className="text-right">
                <StatusBadge status={service.status} />
                <p className="text-sm text-gray-500 mt-1">
                  {service.responseTime}ms | {service.uptime}% uptime
                </p>
              </div>
            </div>
          ))}
        </div>
      </Card>

      {/* Enabler Services */}
      <Card title="SLM Enabler Services">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            'Environment Setup Service',
            'TAD Service',
            'TDC Service',
            'Transformer Service',
            'Data Collection Services',
            'SLM Trainer',
            'DELM Engine',
            'Fine Tuning Service',
          ].map((service) => (
            <div
              key={service}
              className="flex items-center justify-between p-3 bg-gray-50 dark:bg-gray-700 rounded-lg"
            >
              <span>{service}</span>
              <StatusBadge status="healthy" />
            </div>
          ))}
        </div>
      </Card>
    </div>
  );
};

export default Health;
