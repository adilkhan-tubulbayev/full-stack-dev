import { Button } from './components/ui/button';
import { Link } from 'react-router';

export default function HomePage() {
  return (
    <div className="p-12 gap-4 flex flex-col">
      <h1 className="text-4xl">Main App</h1>
      <Link to="/projects">
        <h2>Go to Projects</h2>
      </Link>
      <Button className="w-48">Click me</Button>
    </div>
  );
}
