import React from "react";
import { BrowserRouter, Route, Link, Routes } from "react-router-dom";
import HomePage from "./HomePage";
import LoginPage from "./app/entry/LoginPage";
import RegistrationPage from "./app/entry/RegistrationPage";
import Login from "./Login";
import Register from "./Register";
import Game from "./Game";

export default function App() {
	return(
		<>
			<BrowserRouter>
				<Routes>
					<Route path="/" element={<HomePage/>}/>
					<Route path="/login" element={<Login/>}/>
					<Route path="/register" element={<Register/>}/>
					<Route path="/game" element={<Game/>}/>
				</Routes>
			</BrowserRouter>
		</>
);
}