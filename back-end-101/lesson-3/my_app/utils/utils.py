#cleaning room

def start_cleaning():
	steps = [
	collect_trash(),
	put_items_back(),
	wipe_dust(),
	vacuum_floor(),
	air_room(),
	make_bed(),
	fold_things()
	]

	return "\n".join(steps)

def collect_trash():
	return "Collect the trash in the bin."

def put_items_back():
	return "Put the scattered items back in their places."

def wipe_dust():
	return "Wipe the dust off the surfaces."

def vacuum_floor():
	return "Vacuum or sweep the floor."

def air_room():
	return "Air the room."

def make_bed():
	return "Straighten the bed."

def fold_things():
	return "Carefully fold the blankets and pillows."