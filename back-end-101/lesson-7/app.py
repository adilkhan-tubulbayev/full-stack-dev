import argparse
parser = argparse.ArgumentParser()

lst = [
			"Check email, Slack messages, and task tracker", 
			"Develop a new API endpoint or update existing functionality on the server", 
			"Implement a new React component and connect it to the API",
			"Check and update Docker containers, push updates to the cloud",
			"Review and evaluate Pull Requests, add comments, and improve code"
			]

parser.add_argument("-a", "--add", action="append", help="Add an item to the list")
parser.add_argument("-l", "--list", action="store_true", help="Show items from the list")
parser.add_argument("-u", "--update", nargs=2, help="Update an item from the list")
parser.add_argument("-d", "--delete", help="Delete an item from the list")

def existing_list():
	for i in range(len(lst)):
		print(f"[{i}] : {lst[i]}")

args = parser.parse_args()
if args.add:
	value = args.add
	lst.extend(value)
	existing_list()

elif args.list:
	existing_list()

elif args.update:
	index, value = args.update
	lst[int(index)] = value
	existing_list()

elif args.delete:
	index = args.delete
	lst.pop(int(index))
	existing_list()