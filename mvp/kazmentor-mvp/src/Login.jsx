import React from "react";
import LoginPage from "@/app/entry/LoginPage";
import { SignIn } from "@clerk/clerk-react";


export default function Login() {
	return (
		<>
			{/* <LoginPage></LoginPage> */}
			<div className="m-30">
				<SignIn 
					signUpUrl="/register" 
					fallbackRedirectUrl="/game" 
					appearance={{
						elements: {
							// cardBox: {margin: '0 auto'}
						},
					}}
				/>
			</div>
		</>
	)
}