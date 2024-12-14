# To-Do List Script

This Python script allows you to manage a to-do list via command-line arguments using the `argparse` module. You can add, list, update, and delete tasks in your list.

## Features
- **Add items to the list**: `-a` or `--add` argument.
- **View the current list**: `-l` or `--list` argument.
- **Update an item**: `-u` or `--update` with an index and new value.
- **Delete an item**: `-d` or `--delete` with the index to remove an item.

### Usage Examples
- Add a task: `python app.py -a "New Task"`
- List tasks: `python app.py -l`
- Update a task: `python app.py -u <index> "Updated Task"`
- Delete a task: `python app.py -d <index>`

