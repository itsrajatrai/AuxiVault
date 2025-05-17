// src/App.tsx
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/homepage';

const App = () => {
  return (
    <Router>
      <Routes>
        {/* Route for HomePage */}
        <Route path="/" element={<HomePage />} />
        {/* You can add more routes here later */}
      </Routes>
    </Router>
  );
};

export default App;
