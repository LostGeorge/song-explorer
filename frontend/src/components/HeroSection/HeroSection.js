import React from 'react';
import '../../App.css';
import { Button } from '../Button/Button';
import './HeroSection.css';
import heroImg from '../../images/studio.jpg'

function HeroSection() {
  return (
    <div className='hero-container'>
      {/* <video src='/videos/video-1.mp4' autoPlay loop muted /> */}
      <img src={heroImg} className='hero-img'/>
      <h1>EAR BLEEDR</h1>
      <p>Find Your Spotify Recs Today</p>
      <div className='hero-btns'>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
        >
          GET STARTED
        </Button>
      </div>
    </div>
  );
}

export default HeroSection;