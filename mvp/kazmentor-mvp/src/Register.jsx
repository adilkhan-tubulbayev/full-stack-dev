import React from 'react';
import { SignUp } from '@clerk/clerk-react';

export default function Register() {
  return (
    <>
      <div className="flex">
        <div className="mt-20 ml-85">
          <SignUp signInUrl="/login" fallbackRedirectUrl="/login" />
        </div>
        <div className="">
          <img
            src="/enstein_gif.gif"
            alt="Enstein Gif"
            className="mt-30 ml-30"
          />
        </div>
      </div>
    </>
  );
}
