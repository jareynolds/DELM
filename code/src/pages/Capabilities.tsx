import React, { useState } from 'react';
import { Search, Filter, Plus } from 'lucide-react';
import { Card, StatusBadge } from '../components';
import { useApp } from '../context/AppContext';
import type { Capability } from '../types';

export const Capabilities: React.FC = () => {
  const { capabilities } = useApp();
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCapability, setSelectedCapability] = useState<Capability | null>(null);

  const filteredCapabilities = capabilities.filter(
    (cap) =>
      cap.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      cap.id.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="space-y-6">
      {/* Search and Actions */}
      <div className="flex items-center gap-4">
        <div className="flex-1 relative">
          <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" size={18} />
          <input
            type="text"
            placeholder="Search capabilities..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full pl-10 pr-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800"
          />
        </div>
        <button className="btn-secondary flex items-center gap-2">
          <Filter size={18} />
          Filter
        </button>
        <button className="btn-primary flex items-center gap-2">
          <Plus size={18} />
          Add Capability
        </button>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Capabilities List */}
        <div className="lg:col-span-2 space-y-4">
          {filteredCapabilities.map((cap) => (
            <Card
              key={cap.id}
              className={`cursor-pointer transition-all ${
                selectedCapability?.id === cap.id ? 'ring-2 ring-primary-500' : ''
              }`}
            >
              <div onClick={() => setSelectedCapability(cap)}>
                <div className="flex items-start justify-between mb-2">
                  <div>
                    <h4 className="font-semibold">{cap.name}</h4>
                    <p className="text-sm text-gray-500 dark:text-gray-400">{cap.id}</p>
                  </div>
                  <StatusBadge status={cap.metadata.status} />
                </div>
                <p className="text-sm text-gray-600 dark:text-gray-300 mb-3">
                  {cap.description}
                </p>
                {cap.enablers.length > 0 && (
                  <div className="flex flex-wrap gap-2">
                    {cap.enablers.slice(0, 3).map((enabler) => (
                      <span
                        key={enabler}
                        className="px-2 py-1 bg-gray-100 dark:bg-gray-700 rounded text-xs"
                      >
                        {enabler}
                      </span>
                    ))}
                    {cap.enablers.length > 3 && (
                      <span className="px-2 py-1 text-xs text-gray-500">
                        +{cap.enablers.length - 3} more
                      </span>
                    )}
                  </div>
                )}
              </div>
            </Card>
          ))}
        </div>

        {/* Detail Panel */}
        <div className="lg:col-span-1">
          {selectedCapability ? (
            <Card title="Capability Details" className="sticky top-6">
              <div className="space-y-4">
                <div>
                  <label className="text-sm font-medium text-gray-500">Name</label>
                  <p className="font-semibold">{selectedCapability.name}</p>
                </div>
                <div>
                  <label className="text-sm font-medium text-gray-500">ID</label>
                  <p className="font-mono text-sm">{selectedCapability.id}</p>
                </div>
                <div>
                  <label className="text-sm font-medium text-gray-500">Status</label>
                  <div className="mt-1">
                    <StatusBadge status={selectedCapability.metadata.status} />
                  </div>
                </div>
                <div>
                  <label className="text-sm font-medium text-gray-500">Enablers</label>
                  <ul className="mt-1 space-y-1">
                    {selectedCapability.enablers.map((enabler) => (
                      <li key={enabler} className="text-sm">
                        {enabler}
                      </li>
                    ))}
                  </ul>
                </div>
                {selectedCapability.upstreamDependencies.length > 0 && (
                  <div>
                    <label className="text-sm font-medium text-gray-500">
                      Upstream Dependencies
                    </label>
                    <ul className="mt-1 space-y-1">
                      {selectedCapability.upstreamDependencies.map((dep) => (
                        <li key={dep} className="text-sm">
                          {dep}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
                {selectedCapability.downstreamImpacts.length > 0 && (
                  <div>
                    <label className="text-sm font-medium text-gray-500">
                      Downstream Impacts
                    </label>
                    <ul className="mt-1 space-y-1">
                      {selectedCapability.downstreamImpacts.map((impact) => (
                        <li key={impact} className="text-sm">
                          {impact}
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
                <div>
                  <label className="text-sm font-medium text-gray-500">
                    Implementation Notes
                  </label>
                  <p className="text-sm mt-1">{selectedCapability.implementationNotes}</p>
                </div>
              </div>
            </Card>
          ) : (
            <Card className="text-center text-gray-500">
              <p>Select a capability to view details</p>
            </Card>
          )}
        </div>
      </div>
    </div>
  );
};

export default Capabilities;
