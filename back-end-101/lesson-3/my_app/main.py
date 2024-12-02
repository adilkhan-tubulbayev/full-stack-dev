from utils.utils import *

if __name__ == "__main__":
	cleaning_steps = [
		collect_trash,
		put_items_back,
		wipe_dust,
		vacuum_floor,
		air_room,
		make_bed,
		fold_things
	]

	for step in cleaning_steps:
		print(step())