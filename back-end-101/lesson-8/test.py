import json

dict = {
	"task1" : "to-do-1",
	"task2" : "to-do-2",
	"task3" : "to-do-3"
}

dumped = json.dumps(dict)
print(dumped)

with open('data/tasks.json', 'w') as file:
	json.dump(dict, file)