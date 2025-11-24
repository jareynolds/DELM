import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { AppProvider } from './context/AppContext';
import { Layout } from './components';
import {
  Dashboard,
  Capabilities,
  SLMEngine,
  Health,
  Governance,
  Stories,
  Settings,
  Prompts,
} from './pages';

const App: React.FC = () => {
  return (
    <AppProvider>
      <Layout>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/capabilities" element={<Capabilities />} />
          <Route path="/slm" element={<SLMEngine />} />
          <Route path="/prompts" element={<Prompts />} />
          <Route path="/health" element={<Health />} />
          <Route path="/stories" element={<Stories />} />
          <Route path="/governance" element={<Governance />} />
          <Route path="/settings" element={<Settings />} />
        </Routes>
      </Layout>
    </AppProvider>
  );
};

export default App;
