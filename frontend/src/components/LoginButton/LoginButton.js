// import React from 'react';
// import './Button.css';
// import { Link } from 'react-router-dom';

// export function Button() {
//   return (
//     <Link to='sign-up'>
//       <button className='btn'>Sign Up</button>
//     </Link>
//   );
// }

import { React } from 'react';
import './LoginButton.css';
import { useNavigate } from "react-router-dom";
import axios from "axios";


const STYLES = ['btn--primary', 'btn--outline', 'btn--test'];

const SIZES = ['btn--medium', 'btn--large'];

export const LoginButton = ({
  children,
  type,
  buttonStyle,
  buttonSize, 
}) => {
  const checkButtonStyle = STYLES.includes(buttonStyle)
    ? buttonStyle
    : STYLES[0];

  const checkButtonSize = SIZES.includes(buttonSize) ? buttonSize : SIZES[0];

  let navigate = useNavigate(); 

  const routeChange = async () =>{ 
    try {
      console.log('here')
      const response = await axios.get('http://localhost:5000/get-auth-url')
      console.log(response)
      //window.location.replace(response.data.url);
      navigate('/skyrim')
    } catch (error) {
      console.log(error);
      navigate('/')
    }
  }

  return (
      <button
        className={`btn ${checkButtonStyle} ${checkButtonSize}`}
        onClick={routeChange}
        type={type}
      >
        {children}
      </button>
  );
};