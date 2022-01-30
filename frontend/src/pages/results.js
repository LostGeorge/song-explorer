import React from 'react';
import ResultsHeroSection from '../components/Results/Results';

const Results = () => {
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '90vh'
      }}
    >
      <ResultsHeroSection />
    </div>
  );
};

export default Results;