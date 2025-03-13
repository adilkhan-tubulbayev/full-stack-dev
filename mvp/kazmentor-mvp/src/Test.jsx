import React from "react";
import { useState } from "react";
import { SignedIn, SignInButton } from "@clerk/clerk-react";


export default function Test(){
	const [counter, setCounter] = useState(0)
	function handleClick(){
		console.log(counter)
		setCounter(counter => counter + 1)
		setCounter(counter => counter + 1)
		console.log(counter)
		// setCounter(counter + 1)
	}
	return(
		<>
		{/* <SignedIn> */}
			<h1>Test</h1>
			<button className="" onClick={handleClick}>Click Me</button>
			<h2>{counter}</h2>
			{/* <SignInButton/> */}
			{/* </SignedIn> */}
		</>
	);
}