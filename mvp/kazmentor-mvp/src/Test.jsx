import React from "react";
import { Input } from "./components/ui/input";
import { Button } from "./components/ui/button";

export default function Test() {
	function handleForm(formData) {
		const data = Object.fromEntries(formData);
		console.log("Form data:", data);
	}

	return (
		<div className="text-center flex flex-col items-center p-12">
			<h1 className="text-2xl mb-8">Test</h1>
			<form action={handleForm} className="gap-4 flex flex-col">
				<Input name="email" type="email" placeholder="example@example.com" required />
				<Input name="password" type="password" placeholder="password" required />
				<Button type="submit">Submit</Button>
			</form>
		</div>
	);
}
