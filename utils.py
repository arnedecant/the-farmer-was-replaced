def move_to (x, y):
    while get_pos_x() != x:
        if get_pos_x() < x:
            has_moved = move(East)
            if (not has_moved):
                return False
        else:
            has_moved = move(West)
            if (not has_moved):
                return False
    while get_pos_y() != y:
        if get_pos_y() < y:
            has_moved = move(North)
            if (not has_moved):
                return False
        else:
            has_moved = move(South)
            if (not has_moved):
                return False
	return True
	
def try_dirs ():
	dirs = [North, West, East, South]
	for dir in dirs:
		if (move(dir)):
			return dir
	return None
				
def get_pos ():
	return [get_pos_x(), get_pos_y()]
		
def clamp (val, min, max):
	return max(min, min(val, max))

def manage_single_plot (entity = Entities.Grass):
	allow_tree_even = get_pos_x() % 2 == 0 and get_pos_y() % 2 == 0
	allow_tree_odd = get_pos_x() % 2 == 1 and get_pos_y() % 2 == 1
	allow_tree = allow_tree_even or allow_tree_odd
	if (can_harvest()):
		harvest()
	manage_soil(entity)
	if (entity == None):
		return None
	# has_companion = get_entity_type() != None
	if (entity != Entities.Tree):
		plant(entity)
	elif (allow_tree):
		plant(entity)
		# plant_companion()
	# elif (not has_companion): 
	else:
		plant(Entities.Bush)
	manage_water(entity)
	
def plant_companion ():
	curr_x = get_pos_x()
	curr_y = get_pos_y()
	companion = get_companion()
	if (companion == None):
		return None
	companion_type, (x, y) = companion
	move_to(x, y)
	plant(companion_type)
	move_to(curr_x, curr_y)
		
def manage_water (entity = Entities.Grass, threshold = water_threshold):
	if (entity in entities_water_allowed and get_water() <= threshold):
		use_item(Items.Water)
	force_fertilizer = num_items(Items.Weird_Substance) < num_weird_sub_threshold
	force_fertilizer = force_fertilizer and num_items(Items.Fertilizer)
	if (get_entity_type() in entities_fertilizer_allowed or force_fertilizer):
		use_item(Items.Fertilizer)
		
def manage_soil (entity = Entities.Grass):
	if (entity == None):
		return None
	should_till_soil = get_ground_type() == Grounds.Grassland and entity in entities_soil
	should_till_grass = get_ground_type() == Grounds.Soil and entity not in entities_soil
	if (should_till_soil or should_till_grass):
		till()

def find_entity (use_random = False):
	has_enough_weird_sub = num_items(Items.Weird_Substance) > get_world_size() * num_unlocked(Unlocks.Mazes)
	if (num_items(Items.Power) < num_item_threshold / 20):
		return Entities.Sunflower
	elif (num_items(Items.Hay) < num_item_threshold):
		return Entities.Grass
	elif (num_items(Items.Wood) < num_item_threshold):
		return Entities.Tree
	elif (num_items(Items.Carrot) < num_item_threshold):
		return Entities.Carrot
	elif (num_items(Items.Pumpkin) < num_item_threshold):
		return Entities.Pumpkin
	elif (num_items(Items.Cactus) < num_item_threshold * 10):
		return Entities.Cactus
	elif (num_items(Items.Bone) < num_item_threshold * 10):
		return Entities.Dinosaur
	elif (num_items(Items.Gold) < num_item_threshold * 10 and has_enough_weird_sub):
		return Entities.Treasure
	# elif (use_random):
	# 	return get_random_entity()
	else:
		return Entities.Tree 
		
def check_unlocks ():
	for i in range(len(unlocks_auto_unlock)):
		u = unlocks_auto_unlock[i]
		cost_map = get_cost(u)
		can_unlock = True
		for item in cost_map:
			cost = cost_map[item]
			if (num_items(item) < cost):
				can_unlock = False
		if can_unlock:
			unlock(u)