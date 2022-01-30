import React from 'react';
import TrollHero from '../components/TrollHero/TrollHero';

const Troll = () => {
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '90vh'
      }}
    >
      <TrollHero />
    </div>
  );
};

export default Troll;