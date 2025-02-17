import React from "react";
import { Button } from "./components/ui/button";
import { Link } from "react-router-dom";


export default function HomePage() {
	return (
	<>
			<video 
				autoPlay 
				loop 
				muted 
				className="absolute w-screen h-screen object-fill"
			>
				<source src="/kazmentor_intro_web.mp4" type="video/mp4"/>
			</video>
			<div className="absolute w-full h-full bg-black opacity-65"></div>
			<div className="ml-8 absolute flex flex-col gap-4 justify-center items-start w-96 h-full">
					<p className="text-white uppercase text-2xl">An innovative educational platform with gamification and AI</p>
					<p className="text-white text-lg leading-[1.2]">
						Immerse yourself in the world of knowledge through interactive 
						quests with historical figures!
					</p>
					<Link to="/login">
							<Button className="px-28 py-6 bg-white hover:bg-gray-400 text-black cursor-pointer">Play</Button>
					</Link>
			</div>
	</>
	);
}