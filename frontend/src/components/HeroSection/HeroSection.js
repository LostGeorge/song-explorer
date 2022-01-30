import React from 'react';
import '../../App.css';
import { Button } from '../Button/Button';
import './HeroSection.css';
import rickRoll from '../../images/rickroll.mp4'

function HeroSection() {
  return (
    <div className='hero-container'>
      <video src={rickRoll} autoPlay loop controls className='hero-vid'/>
      {/* <img src={rickROll} className='hero-img'/> */}
      <h1>EAR BLEEDR</h1>
      <p>Find Your Spotify Recs Today</p>
      <div className='hero-btns'>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          redirect='/sign-up'
        >
          GET STARTED
        </Button>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          redirect='https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        >
          SEE EXAMPLES
        </Button>
      </div>
    </div>
  );
}

export default HeroSection;