from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Annotated
import json
import os

file_path = "tasks.json"

class Task(BaseModel):
	task_id : int
	task_description: str

app = FastAPI()

def fetch_json_file():
	if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
		with open(file_path, 'r') as file:
			try:
				return json.load(file)
			except json.JSONDecodeError:
				return list()
	return list()

task_list = list(fetch_json_file())

if task_list == []:
	with open(file_path, 'w') as file:
		json.dump(task_list, file)

@app.get("/tasks", summary="Just Get List of Existing Tasks")
async def get_tasks():
	return task_list

@app.get("/tasks/{task_id},", summary="Get Tasks By ID", description="write integer for id checking")
async def get_tasks(task_id: int):
	return task_list[task_id]

@app.post("/tasks", summary="Create New Own Tasks")
async def create_tasks(item: Task):
	item_dict = item.model_dump()
	task_list.append(item_dict)
	with open(file_path, 'w') as file:
		json.dump(task_list, file)
	return task_list

@app.put("/tasks/{task_id}", summary="Update Existing List of Tasks")
async def update_tasks(task_id: int, task_description: str):
	task_list[task_id] = {"task_id" : task_id, "task_description" : task_description}
	with open(file_path, 'w') as file:
		json.dump(task_list, file)
	return task_list


@app.delete("/tasks/{task_id}", summary="Delete Tasks By ID")
async def delete_tasks(task_id: int):
	task_list.pop(task_id)
	with open(file_path, 'w') as file:
		json.dump(task_list, file)
	return task_list