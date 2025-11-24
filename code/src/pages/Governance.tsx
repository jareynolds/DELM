import React from 'react';
import { Shield, CheckCircle, AlertTriangle } from 'lucide-react';
import { Card } from '../components';
import { useApp } from '../context/AppContext';

export const Governance: React.FC = () => {
  const { aiGovernance, setAIGovernance } = useApp();

  const presetDescriptions = {
    1: 'Awareness (Advisory) - Minimal guidance for early development',
    2: 'Guided Recommendations (Suggested) - Active guidance with flexibility',
    3: 'Strict Enforcement (Required) - Full compliance required',
  };

  const toggleSetting = (key: keyof typeof aiGovernance) => {
    if (key === 'presetLevel') return;
    setAIGovernance({
      ...aiGovernance,
      [key]: !aiGovernance[key],
    });
  };

  return (
    <div className="space-y-6">
      {/* Current Preset */}
      <Card>
        <div className="flex items-center gap-4">
          <Shield className="text-primary-500" size={40} />
          <div>
            <h3 className="text-lg font-semibold">AI Governance - Preset 2</h3>
            <p className="text-gray-500">{presetDescriptions[aiGovernance.presetLevel]}</p>
          </div>
        </div>
      </Card>

      {/* Governance Settings */}
      <Card title="Governance Controls">
        <div className="space-y-4">
          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
            <div className="flex items-center gap-3">
              {aiGovernance.workflowCompliance ? (
                <CheckCircle className="text-green-500" size={20} />
              ) : (
                <AlertTriangle className="text-yellow-500" size={20} />
              )}
              <div>
                <p className="font-medium">Workflow Compliance</p>
                <p className="text-sm text-gray-500">
                  Follow state machine compliance and provide warnings
                </p>
              </div>
            </div>
            <button
              onClick={() => toggleSetting('workflowCompliance')}
              className={`px-3 py-1 rounded ${
                aiGovernance.workflowCompliance
                  ? 'bg-green-100 text-green-800'
                  : 'bg-gray-200 text-gray-600'
              }`}
            >
              {aiGovernance.workflowCompliance ? 'Enabled' : 'Disabled'}
            </button>
          </div>

          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
            <div className="flex items-center gap-3">
              {aiGovernance.qualityGatesEnabled ? (
                <CheckCircle className="text-green-500" size={20} />
              ) : (
                <AlertTriangle className="text-yellow-500" size={20} />
              )}
              <div>
                <p className="font-medium">Quality Gates</p>
                <p className="text-sm text-gray-500">
                  Verify pre-conditions and recommend actions
                </p>
              </div>
            </div>
            <button
              onClick={() => toggleSetting('qualityGatesEnabled')}
              className={`px-3 py-1 rounded ${
                aiGovernance.qualityGatesEnabled
                  ? 'bg-green-100 text-green-800'
                  : 'bg-gray-200 text-gray-600'
              }`}
            >
              {aiGovernance.qualityGatesEnabled ? 'Enabled' : 'Disabled'}
            </button>
          </div>

          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
            <div className="flex items-center gap-3">
              {aiGovernance.documentationStandards ? (
                <CheckCircle className="text-green-500" size={20} />
              ) : (
                <AlertTriangle className="text-yellow-500" size={20} />
              )}
              <div>
                <p className="font-medium">Documentation Standards</p>
                <p className="text-sm text-gray-500">
                  Recommend template usage and highlight missing sections
                </p>
              </div>
            </div>
            <button
              onClick={() => toggleSetting('documentationStandards')}
              className={`px-3 py-1 rounded ${
                aiGovernance.documentationStandards
                  ? 'bg-green-100 text-green-800'
                  : 'bg-gray-200 text-gray-600'
              }`}
            >
              {aiGovernance.documentationStandards ? 'Enabled' : 'Disabled'}
            </button>
          </div>

          <div className="flex items-center justify-between p-4 bg-gray-50 dark:bg-gray-700 rounded-lg">
            <div className="flex items-center gap-3">
              {aiGovernance.securityCompliance ? (
                <CheckCircle className="text-green-500" size={20} />
              ) : (
                <AlertTriangle className="text-yellow-500" size={20} />
              )}
              <div>
                <p className="font-medium">Security Compliance</p>
                <p className="text-sm text-gray-500">
                  Check approval status before proceeding
                </p>
              </div>
            </div>
            <button
              onClick={() => toggleSetting('securityCompliance')}
              className={`px-3 py-1 rounded ${
                aiGovernance.securityCompliance
                  ? 'bg-green-100 text-green-800'
                  : 'bg-gray-200 text-gray-600'
              }`}
            >
              {aiGovernance.securityCompliance ? 'Enabled' : 'Disabled'}
            </button>
          </div>
        </div>
      </Card>

      {/* Policy Summary */}
      <Card title="Preset 2 Policy Summary">
        <div className="prose dark:prose-invert max-w-none">
          <p className="text-sm text-gray-600 dark:text-gray-300">
            Preset 2 (Guided Recommendations) provides active guidance while maintaining flexibility.
            AI agents will follow best practices by default, provide clear warnings for deviations,
            recommend corrective actions, and log all overrides. User overrides are allowed with
            explicit confirmation.
          </p>
          <ul className="text-sm mt-4 space-y-2">
            <li>Follow tasks in sequential order by default</li>
            <li>Warn when attempting to skip states</li>
            <li>Explain consequences of workflow deviations</li>
            <li>Suggest corrections when state mismatches detected</li>
            <li>Log all workflow deviations for review</li>
          </ul>
        </div>
      </Card>
    </div>
  );
};

export default Governance;
