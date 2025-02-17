import React, { useState } from "react";
import { Unity, useUnityContext } from "react-unity-webgl";

export default function Game() {
  // Флаг для отображения Unity после нажатия кнопки
  const [isGameStarted, setIsGameStarted] = useState(false);

  // Unity-контекст (загружается, когда нажата кнопка)
  const { unityProvider, sendMessage, isLoaded } = useUnityContext({
    loaderUrl: "/KazMentor_WebGL/Build/KazMentor_WebGL.loader.js",
    dataUrl: "/KazMentor_WebGL/Build/KazMentor_WebGL.data",
    frameworkUrl: "/KazMentor_WebGL/Build/KazMentor_WebGL.framework.js",
    codeUrl: "/KazMentor_WebGL/Build/KazMentor_WebGL.wasm",
  });

  // Функция для запуска Unity WebGL
  const startGame = () => {
    setIsGameStarted(true); // Показываем Unity
  };

  return (
    <div className="w-screen h-screen flex justify-center items-center bg-gray-900">
      {/* UI-контейнер */}
      {!isGameStarted ? (
        <div className="bg-black/60 text-white p-6 rounded-lg shadow-lg text-center">
          <h1 className="text-2xl font-bold">KazMentor Game</h1>
          <p className="mb-4">Нажмите, чтобы запустить игру!</p>
          <button 
            className="px-6 py-3 bg-blue-500 text-white text-lg rounded-md hover:bg-blue-700"
            onClick={startGame}
          >
            🚀 Запустить игру
          </button>
        </div>
      ) : (
        // Unity WebGL отображается только после нажатия кнопки
        <Unity unityProvider={unityProvider} className="w-screen h-screen object-fill" />
      )}
    </div>
  );
}
