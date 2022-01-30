import React from 'react';
import '../../App.css';
import { LoginButton } from '../LoginButton/LoginButton';
import './LoginHeroSection.css';
import loginImg from '../../images/login.jpg'

function LoginHeroSection() {
  return (
    <div className='hero-container'>
      {/* <video src='/videos/video-1.mp4' autoPlay loop muted /> */}
      <img src={loginImg} className='login-hero-img'/>
      <div className='hero-btns'>
        <LoginButton
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
        >
          Login
        </LoginButton>
      </div>
    </div>
  );
}

export default LoginHeroSection;