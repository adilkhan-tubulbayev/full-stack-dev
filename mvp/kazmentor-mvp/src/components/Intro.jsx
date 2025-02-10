import Logo from "../img/logo.png";
import '../css/main.css';

export default function Intro() {
	return (
		<>
			<div className="flex flex-col items-center justify-center p-8 gap-4 h-screen text-xs text-center">
				<h1 className="text-blue-400 text-2xl sm:text-3xl md:text-4xl lg:text-5xl">KazMentor - Скоро!</h1>
				<p className="text-white text-center leading-[1.5] sm:text-sm md:text-base lg:text-lg">Интерактивная платформа, где образование превращается в увлекательное приключение. Улучши свои знания в науке через игру!🚀</p>
				<img src={Logo} alt="KazMentor Logo" className="border-dashed border-2 border-white w-3xs h-3xs rounded-full sm:w-2xs sm:h-2xs md:w-xs md:h-xs lg:w-sm lg:h-sm" />
				<a className="border-2 p-4 rounded-xl bg-blue-400 hover:bg-blue-500 border-none sm:text-sm md:text-base lg:text-lg" href="https://www.instagram.com/kazmentor_game/" target="_blank">Следить за релизом</a>
				<a className="border-2 p-4 rounded-xl bg-red-400 hover:bg-red-500 border-none sm:text-sm md:text-base lg:text-lg" href="https://adilkhanix.itch.io/kazmentor" target="_blank">Тестовая версия (для ПК)</a>
			</div>
		</>
	)
}