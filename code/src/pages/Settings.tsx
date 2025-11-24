import React from 'react';
import { Settings as SettingsIcon, Database, Cpu, Globe } from 'lucide-react';
import { Card } from '../components';

export const Settings: React.FC = () => {
  return (
    <div className="space-y-6">
      {/* SLM Configuration */}
      <Card title="SLM Configuration">
        <div className="space-y-4">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium mb-2">Model Name</label>
              <input
                type="text"
                defaultValue="DELM-UI-v1.0"
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Version</label>
              <input
                type="text"
                defaultValue="1.0.0"
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Temperature</label>
              <input
                type="number"
                defaultValue={0.7}
                step={0.1}
                min={0}
                max={2}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800"
              />
            </div>
            <div>
              <label className="block text-sm font-medium mb-2">Max Tokens</label>
              <input
                type="number"
                defaultValue={2048}
                className="w-full p-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800"
              />
            </div>
          </div>
          <div className="flex justify-end">
            <button className="btn-primary">Save Configuration</button>
          </div>
        </div>
      </Card>

      {/* System Settings */}
      <Card title="System Settings">
        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
            <div className="flex items-center gap-3">
              <Database className="text-blue-500" size={20} />
              <div>
                <p className="font-medium">Data Collection</p>
                <p className="text-sm text-gray-500">Enable training data collection</p>
              </div>
            </div>
            <label className="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" defaultChecked className="sr-only peer" />
              <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600"></div>
            </label>
          </div>

          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
            <div className="flex items-center gap-3">
              <Cpu className="text-purple-500" size={20} />
              <div>
                <p className="font-medium">Auto Fine-tuning</p>
                <p className="text-sm text-gray-500">Automatically fine-tune model on new data</p>
              </div>
            </div>
            <label className="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" className="sr-only peer" />
              <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600"></div>
            </label>
          </div>

          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
            <div className="flex items-center gap-3">
              <Globe className="text-green-500" size={20} />
              <div>
                <p className="font-medium">API Access</p>
                <p className="text-sm text-gray-500">Enable external API access</p>
              </div>
            </div>
            <label className="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" defaultChecked className="sr-only peer" />
              <div className="w-11 h-6 bg-gray-200 peer-focus:outline-none peer-focus:ring-4 peer-focus:ring-primary-300 dark:peer-focus:ring-primary-800 rounded-full peer dark:bg-gray-600 peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all dark:border-gray-600 peer-checked:bg-primary-600"></div>
            </label>
          </div>
        </div>
      </Card>

      {/* Workspace Info */}
      <Card title="Workspace Information">
        <div className="space-y-2 text-sm">
          <p><span className="font-medium">Workspace:</span> BALUT</p>
          <p><span className="font-medium">Project:</span> ESLM - UI Design Small Language Model</p>
          <p><span className="font-medium">Governance:</span> Preset 2 - Guided Recommendations</p>
          <p><span className="font-medium">Version:</span> 1.0.0</p>
        </div>
      </Card>
    </div>
  );
};

export default Settings;
