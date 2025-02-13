import { Checkbox } from "@/components/ui/checkbox"
import { Button } from "./components/ui/button";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { CheckboxWithText } from "./components/ui/CheckboxWithText";
import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel"
import { BrowserRouter as Router, Route, Link, Routes, BrowserRouter } from "react-router-dom";
import Logo from "/logo.png";
import {Page, RegPage} from "./app/login/page";
import { SidebarProvider, SidebarTrigger } from "@/components/ui/sidebar"
import { AppSidebar } from "@/components/app-sidebar"

function Home() {
	return (
	<>
		<SidebarProvider>
		<AppSidebar />
		<main>
		<SidebarTrigger />
			<div className="">
				<img src="/nis-school.png" alt="" className="w-full h-full absolute"/>
				<div className="absolute flex items-center gap-8 flex-col justify-center h-full w-full">
				<h1 className="text-9xl font-bold text-white text-center mt-4">KazMentor</h1>
				<h2 className="text-white text-3xl">Gaming and AI educational game</h2>
				<Link to="/authorization">
				<a className="border-2 p-8 pr-12 pl-12 rounded-xl bg-blue-400 hover:bg-blue-500 border-none sm:text-sm md:text-base lg:text-lg" href="https://adilkhanix.itch.io/kazmentor" target="_blank">Start learning</a>
				</Link>
				</div>
			</div>
			</main>
		</SidebarProvider>
	</>
)
}

function Authorization() {
	return (
	<>
		<h2 className="text-center text-4xl mt-12">Authorization</h2>
		<AppSidebar/>
		<Page/>
	</>
)}

function Registration(){
	return(
		<>
			<h2 className="text-center text-4xl mt-12">Registration</h2>
			<RegPage/>
		</>
	)
}

export default function App() {
	return (
	<>
		<BrowserRouter>
				<Routes>
					<Route path="/" element={<Home/>} />
					<Route path="/authorization" element={<Authorization/>} />
					<Route path="/registration" element={<Registration/>}/>
				</Routes>
		</BrowserRouter>
	</>
  )
}