import time

def client_request():
	print("Клиент отправляет запрос на сервер.")

def server_response():
	time.sleep(1)
	print("Сервер обрабатывает запрос ...")
	time.sleep(1)
	print("Сервер отправляет ответ: Добро пожаловать в интернет!")

req = input("Отправить запрос на сервер? 1 - да ---> ")

if req == "1":
	client_request()
	server_response()
else:
	print("Ну нет так нет")