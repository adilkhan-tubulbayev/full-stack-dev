import React from "react";
import RegistrationPage from "./app/entry/RegistrationPage";
import { SignIn, SignUp } from "@clerk/clerk-react";

export default function Register() {
	return (
		<>
			<div className="flex m-20 w-screen">
				{/* <RegistrationPage></RegistrationPage> */}
				<SignUp signInUrl="/login" fallbackRedirectUrl="/login" /> 
			</div>
		</>
	)
}