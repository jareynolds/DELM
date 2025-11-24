import React from 'react';
import { clsx } from 'clsx';
import type { Status } from '../types';

interface StatusBadgeProps {
  status: Status | string;
}

export const StatusBadge: React.FC<StatusBadgeProps> = ({ status }) => {
  const statusClass = {
    'Planned': 'status-planned',
    'In Progress': 'status-in-progress',
    'Implemented': 'status-implemented',
    'Pending': 'status-pending',
    'Completed': 'status-implemented',
    'healthy': 'status-implemented',
    'degraded': 'status-planned',
    'unhealthy': 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-200',
  }[status] || 'status-pending';

  return (
    <span className={clsx('status-badge', statusClass)}>
      {status}
    </span>
  );
};

export default StatusBadge;
