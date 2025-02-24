import { Link } from 'react-router-dom';

export default function Projects() {
  return (
    <>
      <div className="p-12 gap-4 flex flex-col">
        <h1 className="text-4xl">Projects</h1>
        <Link to="/">
          <h2>Go to Home Page</h2>
        </Link>
      </div>
    </>
  );
}
