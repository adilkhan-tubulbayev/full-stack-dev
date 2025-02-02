from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins = ["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

class UserData(BaseModel):
	name: str
	email: str
	message: str

file_path = "contactForm.json"

def fetch_json_file():
	if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
		with open(file_path, 'r') as file:
			try:
				return json.load(file)
			except json.JSONDecodeError:
				return list()
	return list()
contactForm = list(fetch_json_file())

if contactForm == []:
	with open(file_path, 'w') as file:
		json.dump(contactForm, file)

@app.post("/form")
async def create_tasks(user: UserData):
	user_dict = user.model_dump()
	contactForm.append(user_dict)
	with open(file_path, 'w') as file:
		json.dump(contactForm, file)
	return contactForm