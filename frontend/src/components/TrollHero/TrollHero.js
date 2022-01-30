import React from 'react';
import '../../App.css';
import './TrollHero.css';
import skyrim from '../../images/skyrim.mp4'

function TrollHero() {
    
    let handleVideoMounted = element => {
        if (element !== null) {
          element.currentTime = 2;
        }
      };    
  return (
    <div className='hero-container'>
        {/* <video autoPlay loop controls className='troll-hero-vid'>
            <source src="../../images/skyrim.mp4#t=10,20" type="video/mp4" />
        </video> */}
      <video src={skyrim} autoPlay loop controls className='troll-hero-vid' ref={handleVideoMounted}/>
     
    </div>
  );
}

export default TrollHero;