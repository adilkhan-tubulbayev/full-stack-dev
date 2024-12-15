import argparse
import json
import os

file_path = "data/tasks.json"

parser = argparse.ArgumentParser()

# lst = [
# 			"Check email, Slack messages, and task tracker", 
# 			"Develop a new API endpoint or update existing functionality on the server", 
# 			"Implement a new React component and connect it to the API",
# 			"Check and update Docker containers, push updates to the cloud",
# 			"Review and evaluate Pull Requests, add comments, and improve code"
# 			]


parser.add_argument("-a", "--add", action="append", help="Add an item to the list")
parser.add_argument("-l", "--list", action="store_true", help="Show items from the list")
parser.add_argument("-u", "--update", nargs=2, help="Update an item from the list")
parser.add_argument("-d", "--delete", help="Delete an item from the list")


def load_list():
	if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
		with open(file_path, 'r') as file:
			try:
				return json.load(file)
			except json.JSONDecodeError:
				return list()
	return list()

lst = load_list()

def existing_list():
	for i in range(len(lst)):
		print(f"[{i}] : {lst[i]}")

def saving_list():
	with open(file_path, 'a') as file:
		json.dump(lst, file)

def update_list():
	with open(file_path, 'w') as file:
		json.dump(lst, file)

args = parser.parse_args()

if args.add:
	value = args.add
	lst.extend(value)
	update_list()
	existing_list()

elif args.list:
	existing_list()

elif args.update:
	index, value = args.update
	lst[int(index)] = value
	update_list()
	existing_list()

elif args.delete:
	index = args.delete
	lst.pop(int(index))
	update_list()
	existing_list()