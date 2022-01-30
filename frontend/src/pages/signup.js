import React from 'react';
import Login from "../components/Login/Login";

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
      <Login />
    </div>
  );
};

export default SignUp;