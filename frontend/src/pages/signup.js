import React from 'react';
import LoginHeroSection from '../components/LoginHero/LoginHeroSection';

const SignUp = () => {
  return (
    <div
      style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '90vh'
      }}
    >
      <LoginHeroSection />
    </div>
  );
};

export default SignUp;