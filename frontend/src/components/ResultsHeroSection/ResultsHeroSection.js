import React from 'react';
import '../../App.css';
import { Button } from '../Button/Button';
import './HeroSection.css';
import heroImg from '../../images/studio.jpg'

function ResultsHeroSection() {
  return (
    <div className='hero-container'>
      <img src={heroImg} className='hero-img'/>
      <h1>EAR BLEEDR</h1>
      <p>Enjoy The Listening!</p>
      <div className='hero-btns'>
        <Button
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          redirect='/sign-up'
        >
          GET STARTED
        </Button>
      </div>
    </div>
  );
}

export default ResultsHeroSection;