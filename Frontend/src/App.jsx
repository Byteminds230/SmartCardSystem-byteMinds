import React, { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Lazy load your pages
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Settings = lazy(() => import('./pages/Settings'));
const NotFound = lazy(() => import('./pages/NotFound'));

function App() {
  return (
    <Suspense fallback={<p className="text-center text-[1.5vw] text-slate-900">Loading...</p>}>
      <Router>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />}>
            <Route path="settings" element={<Settings />} />
          </Route>
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Router>
    </Suspense>
  );
}

export default App;
