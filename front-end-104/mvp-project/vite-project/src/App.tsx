import { BrowserRouter, Routes, Route } from 'react-router';
import HomePage from './HomePage';
import Projects from './Projects';

function App() {
  return (
    <>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/projects" element={<Projects />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
