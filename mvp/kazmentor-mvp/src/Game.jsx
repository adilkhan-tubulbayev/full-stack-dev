import { SignedIn, UserButton } from "@clerk/clerk-react";
import React, { useState } from "react";
import { Unity, useUnityContext } from "react-unity-webgl";
import { dark } from "@clerk/themes";

export default function Game() {
  const [isGameStarted, setIsGameStarted] = useState(false);

  // Инициализация Unity-контекста
  const {
    unityProvider,
    isLoaded,            // Флаг: загружен ли движок
    loadingProgression, // Прогресс загрузки [0..1]
    requestFullscreen,  // Метод для перехода в fullscreen
  } = useUnityContext({
    loaderUrl: "/KazMentor_WebGL/Build/KazMentor_WebGL.loader.js",
    dataUrl: "/KazMentor_WebGL/Build/KazMentor_WebGL.data",
    frameworkUrl: "/KazMentor_WebGL/Build/KazMentor_WebGL.framework.js",
    codeUrl: "/KazMentor_WebGL/Build/KazMentor_WebGL.wasm",
  });

  function startGame() {
    setIsGameStarted(true);
  }

  function handleFullscreen() {
    requestFullscreen(true);
  }

  return (
		<>
		<SignedIn>
		<UserButton/>
    <div className="w-screen h-screen flex flex-col items-center justify-center bg-gray-900 text-white">
      {/* Пока не нажали кнопку, показываем UI */}
      {!isGameStarted ? (
        <div className="bg-black/60 p-6 rounded-lg shadow-lg text-center">
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
        // После нажатия — секция с Unity
        <div className="relative w-full h-full">
          {/* Если Unity ещё грузится, покажем прогресс-бар */}
          {!isLoaded && (
            <div className="absolute inset-0 flex flex-col items-center justify-center bg-black/80 z-10">
              <div className="mb-4 text-lg">Загрузка...</div>
              <div className="w-64 h-4 bg-gray-700">
                <div
                  className="h-4 bg-blue-500"
                  style={{ width: `${100 * loadingProgression}%` }}
                />
              </div>
            </div>
          )}

          {/* Само окно Unity */}
          <Unity
            unityProvider={unityProvider}
            style={{
              width: "100%",
              height: "100%",
              background: "black", // фон на случай, если Canvas прозрачен
            }}
          />

          {/* Простейший футер, как в дефолтном index.html */}
          <div className="absolute bottom-0 left-0 w-full flex justify-between items-center bg-black bg-opacity-50 p-2">
            <div id="unity-build-title" className="px-2">
              KAZMENTOR
            </div>
            <button
              onClick={handleFullscreen}
              className="px-3 py-1 bg-blue-600 rounded hover:bg-blue-700"
            >
              Полный экран
            </button>
          </div>
        </div>
      )}
    </div>
		</SignedIn>
		</>
  );
}
