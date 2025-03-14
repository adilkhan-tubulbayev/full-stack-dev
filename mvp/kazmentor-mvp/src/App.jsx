import React from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Landing from './Landing';
import Login from './Login';
import Register from './Register';
import Game from './Game';
import Home from './Home';
import Learn from './Learn';

export default function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Landing />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/game" element={<Game />} />
          <Route path="/home" element={<Home />} />
          <Route path="/learn" element={<Learn />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}
