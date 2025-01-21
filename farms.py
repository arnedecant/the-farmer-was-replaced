grid_size = get_world_size()

def default_game_loop (requested_entity = None):
	clear()
	while True:
		change_hat(Hats.Straw_Hat)
		move_to(0, 0)
		check_unlocks()
		if (requested_entity == None):
			requested_entity = find_entity()
		current_entity = get_entity_type()
		if (requested_entity == Entities.Treasure):
			clear()
			maze_loop()
		elif (requested_entity == Entities.Dinosaur):
			clear_grid_for_dino()
			change_hat(Hats.Dinosaur_Hat)
			dino_loop()
		elif (requested_entity == Entities.Pumpkin):
			pumpkin_loop()
		elif (requested_entity == Entities.Sunflower):
			sunflower_loop()
		elif (current_entity == Entities.Cactus):
			cacti_loop()
		else:
			farm_loop(requested_entity)

def farm_loop (entity):
	for x in range(grid_size):
		for y in range(grid_size):
			move_to(x, y)
			manage_single_plot(entity)
			
def maze_loop ():
	n_substance = get_world_size() * num_unlocked(Unlocks.Mazes)
	all_dirs = [North, East, South, West]
	index = 0
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, n_substance)
	entity = get_entity_type()
	while entity != Entities.Treasure:
		has_moved = move(all_dirs[index])
		if (has_moved):
			index = (index + 1) % 4
		else:
			index = (index - 1) % 4
		entity = get_entity_type()
	harvest()
			
def sunflower_loop ():
	max_petals = 15
	map = []
	for i in range(max_petals):
		map.append([])
	for x in range(grid_size):
		for y in range(grid_size):
			move_to(x, y)
			manage_single_plot(Entities.Sunflower)
			size = measure()
			if (size == None):
				return None # ?
			map[max_petals - size].append([x, y])
	for i in range(len(map)):
		for pos in map[i]:
			move_to(pos[0], pos[1])
			harvest()
			
def pumpkin_loop ():
	for x in range(grid_size):
		for y in range(grid_size):
			move_to(x, y)
			manage_single_plot(Entities.Pumpkin)
	coords_replant_pumpkin = []
	has_replanted = False
	for x in range(grid_size):
		for y in range(grid_size):
			move_to(x, y)
			if not can_harvest():
				coords_replant_pumpkin.append([x, y])
				plant(Entities.Pumpkin)
				has_replanted = True
	while has_replanted:
		has_replanted = False
		for i in range(len(coords_replant_pumpkin)):
			coords = coords_replant_pumpkin[i]
			move_to(coords[0], coords[1])
			if (get_entity_type() != Entities.Pumpkin):
				has_replanted = True
				plant(Entities.Pumpkin)
				coords_last_pumpkin = coords
	if coords_last_pumpkin != None:
		move_to(coords_last_pumpkin[0], coords_last_pumpkin[1])
		while not can_harvest():
			if (get_entity_type() != Entities.Pumpkin):
				plant(Entities.Pumpkin)
	harvest()
	
def cacti_loop ():
	col_done = []
	for i in range(grid_size):
		col_done.append(False)
    sorted = False
    while not sorted:
        sorted = True
        for x in range(grid_size):
            if (col_done[x]):
                continue
            is_col_sorted = True
            for y in range(grid_size):
                move_to(x, y)
                current_size = measure()
                if (x < grid_size - 1):
                    east_size = measure(East)
                    if (east_size != None and current_size > east_size):
                        swap(East)
                        sorted = False
                        is_col_sorted = False
                if (y < grid_size - 1):
                    north_size = measure(North)
                    if (north_size != None and current_size > north_size):
                        swap(North)
                        sorted = False
                        is_col_sorted = False
			if is_col_sorted:
				col_done[x] = True
			elif x < grid_size - 1:
				col_done[x + 1] = False
	if (sorted):
		harvest()

def dino_loop ():
	dino_s_pattern()
	
			
