import React from 'react';
import { SignIn } from '@clerk/clerk-react';

export default function Login() {
  return (
    <>
      <div className="flex">
        <div className="mt-30 ml-85">
          <SignIn
            signUpUrl="/register"
            fallbackRedirectUrl="/game"
          />
        </div>
        <div className="ml-30">
          <img src="/tesla.gif" alt="Tesla Gif" className="" />
        </div>
      </div>
    </>
  );
}
