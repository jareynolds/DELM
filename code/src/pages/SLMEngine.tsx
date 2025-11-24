import React, { useState } from 'react';
import { Send, Cpu, Zap, Clock } from 'lucide-react';
import { Card } from '../components';
import toast from 'react-hot-toast';

export const SLMEngine: React.FC = () => {
  const [prompt, setPrompt] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [outputs, setOutputs] = useState<Array<{ id: string; prompt: string; response: string; timestamp: string }>>([]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim()) return;

    setIsGenerating(true);

    // Simulate SLM generation
    setTimeout(() => {
      const newOutput = {
        id: Date.now().toString(),
        prompt: prompt,
        response: `Generated UI component for: "${prompt}"\n\n\`\`\`tsx\nimport React from 'react';\n\nexport const GeneratedComponent: React.FC = () => {\n  return (\n    <div className="p-4 bg-white rounded-lg shadow">\n      <h2 className="text-xl font-bold">Generated UI</h2>\n      <p>Based on your prompt: ${prompt}</p>\n    </div>\n  );\n};\n\`\`\``,
        timestamp: new Date().toISOString(),
      };
      setOutputs([newOutput, ...outputs]);
      setPrompt('');
      setIsGenerating(false);
      toast.success('UI component generated successfully');
    }, 2000);
  };

  return (
    <div className="space-y-6">
      {/* Model Info */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <div className="flex items-center gap-3">
            <Cpu className="text-primary-500" size={24} />
            <div>
              <p className="text-sm text-gray-500">Model</p>
              <p className="font-semibold">DELM v1.0</p>
            </div>
          </div>
        </Card>
        <Card>
          <div className="flex items-center gap-3">
            <Zap className="text-yellow-500" size={24} />
            <div>
              <p className="text-sm text-gray-500">Status</p>
              <p className="font-semibold text-green-600">Online</p>
            </div>
          </div>
        </Card>
        <Card>
          <div className="flex items-center gap-3">
            <Clock className="text-blue-500" size={24} />
            <div>
              <p className="text-sm text-gray-500">Avg Response</p>
              <p className="font-semibold">1.2s</p>
            </div>
          </div>
        </Card>
      </div>

      {/* Prompt Input */}
      <Card title="Generate UI Component">
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">
              Describe the UI component you want to generate
            </label>
            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="e.g., Create a responsive navigation bar with dropdown menus and a dark mode toggle..."
              className="w-full h-32 p-3 border border-gray-300 dark:border-gray-600 rounded-lg bg-white dark:bg-gray-800 resize-none"
              disabled={isGenerating}
            />
          </div>
          <div className="flex justify-end">
            <button
              type="submit"
              className="btn-primary flex items-center gap-2"
              disabled={isGenerating || !prompt.trim()}
            >
              {isGenerating ? (
                <>
                  <div className="animate-spin rounded-full h-4 w-4 border-2 border-white border-t-transparent" />
                  Generating...
                </>
              ) : (
                <>
                  <Send size={18} />
                  Generate
                </>
              )}
            </button>
          </div>
        </form>
      </Card>

      {/* Output History */}
      <Card title="Generated Outputs">
        {outputs.length === 0 ? (
          <p className="text-gray-500 text-center py-8">
            No outputs yet. Enter a prompt above to generate UI components.
          </p>
        ) : (
          <div className="space-y-4">
            {outputs.map((output) => (
              <div
                key={output.id}
                className="p-4 bg-gray-50 dark:bg-gray-700 rounded-lg"
              >
                <div className="flex items-center justify-between mb-2">
                  <p className="font-medium">Prompt: {output.prompt}</p>
                  <span className="text-xs text-gray-500">
                    {new Date(output.timestamp).toLocaleTimeString()}
                  </span>
                </div>
                <pre className="mt-2 p-3 bg-gray-900 text-gray-100 rounded text-sm overflow-x-auto">
                  {output.response}
                </pre>
              </div>
            ))}
          </div>
        )}
      </Card>
    </div>
  );
};

export default SLMEngine;
