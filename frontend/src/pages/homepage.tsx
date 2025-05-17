// src/pages/HomePage.tsx
import React from 'react';
import Navigation from '../components/navigation';

const HomePage = () => {
  return (
    <div>
      <Navigation />
      {/* Other homepage content */}
      <main className="p-8">
        <h1 className="text-3xl font-bold">Welcome to AuxiVault!</h1>
        <p className="mt-4 text-gray-700">Your secure and easy content vault.</p>
      </main>
    </div>
  );
};

export default HomePage;
