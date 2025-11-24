import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import {
  LayoutDashboard,
  Layers,
  Cpu,
  MessageSquare,
  Activity,
  BookOpen,
  Settings,
  Shield
} from 'lucide-react';
import { clsx } from 'clsx';

interface LayoutProps {
  children: React.ReactNode;
}

const navItems = [
  { path: '/', label: 'Dashboard', icon: LayoutDashboard },
  { path: '/capabilities', label: 'Capabilities', icon: Layers },
  { path: '/slm', label: 'SLM Engine', icon: Cpu },
  { path: '/prompts', label: 'Prompts', icon: MessageSquare },
  { path: '/health', label: 'Health', icon: Activity },
  { path: '/stories', label: 'Stories', icon: BookOpen },
  { path: '/governance', label: 'AI Governance', icon: Shield },
  { path: '/settings', label: 'Settings', icon: Settings },
];

export const Layout: React.FC<LayoutProps> = ({ children }) => {
  const location = useLocation();

  return (
    <div className="min-h-screen flex">
      {/* Sidebar */}
      <aside className="w-64 bg-gray-900 text-white flex flex-col">
        <div className="p-4 border-b border-gray-800">
          <h1 className="text-xl font-bold">ESLM</h1>
          <p className="text-xs text-gray-400">UI Design Language Model</p>
        </div>
        <nav className="flex-1 p-4">
          <ul className="space-y-2">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path;
              return (
                <li key={item.path}>
                  <Link
                    to={item.path}
                    className={clsx(
                      'flex items-center gap-3 px-3 py-2 rounded-lg transition-colors',
                      isActive
                        ? 'bg-primary-600 text-white'
                        : 'text-gray-300 hover:bg-gray-800 hover:text-white'
                    )}
                  >
                    <Icon size={18} />
                    <span>{item.label}</span>
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>
        <div className="p-4 border-t border-gray-800">
          <div className="text-xs text-gray-500">
            <p>Governance: Preset 2</p>
            <p>Guided Recommendations</p>
          </div>
        </div>
      </aside>

      {/* Main content */}
      <main className="flex-1 overflow-auto">
        <header className="bg-white dark:bg-gray-800 shadow-sm border-b border-gray-200 dark:border-gray-700 px-6 py-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-semibold">
              {navItems.find(item => item.path === location.pathname)?.label || 'ESLM'}
            </h2>
            <div className="flex items-center gap-4">
              <span className="text-sm text-gray-500">BALUT Workspace</span>
            </div>
          </div>
        </header>
        <div className="p-6">
          {children}
        </div>
      </main>
    </div>
  );
};

export default Layout;
