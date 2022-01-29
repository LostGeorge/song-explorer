import React from 'react';
import HeroSection from '../components/HeroSection';

const Home = () => {
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '90vh'
      }}
    >
      <HeroSection />
    </div>
  );
};

export default Home;