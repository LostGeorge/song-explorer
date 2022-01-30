import React from 'react';
import '../../App.css';
import { Button } from '../Button/Button';
import './LoginHeroSection.css';
import loginImg from '../../images/login.jpg'

function LoginHeroSection() {
  return (
    <div className='hero-container'>
      {/* <video src='/videos/video-1.mp4' autoPlay loop muted /> */}
      <img src={loginImg} className='login-hero-img'/>
      <div className='hero-btns'>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          redirect='http://localhost:5000/get-auth-url'
        >
          Login
        </Button>
      </div>
    </div>
  );
}

export default LoginHeroSection;