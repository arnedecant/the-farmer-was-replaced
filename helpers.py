from globals import UNLOCKS, WORLD_SIZE, NUM_ITEM_THRESHOLD, WATER_THRESHOLD, NUM_WEIRD_SUB_THRESHOLD, ENTITIES_SOIL, ENTITIES_WATER_ALLOWED, ENTITIES_FERTILIZER_ALLOWED

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
		
def manage_water (entity = Entities.Grass, threshold = WATER_THRESHOLD):
	if (entity in entities_water_allowed and get_water() <= threshold):
		use_item(Items.Water)
	force_fertilizer = num_items(Items.Weird_Substance) < NUM_WEIRD_SUB_THRESHOLD
	force_fertilizer = force_fertilizer and num_items(Items.Fertilizer)
	force_fertilizer = force_fertilizer and FORCE_FERTILIZER
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
	has_enough_weird_sub = num_items(Items.Weird_Substance) > WORLD_SIZE * num_unlocked(Unlocks.Mazes)
	if (num_items(Items.Power) < NUM_ITEM_THRESHOLD / 100):
		return Entities.Sunflower
	elif (num_items(Items.Hay) < NUM_ITEM_THRESHOLD):
		return Entities.Grass
	elif (num_items(Items.Wood) < NUM_ITEM_THRESHOLD):
		return Entities.Tree
	elif (num_items(Items.Carrot) < NUM_ITEM_THRESHOLD):
		return Entities.Carrot
	elif (num_items(Items.Pumpkin) < NUM_ITEM_THRESHOLD):
		return Entities.Pumpkin
	elif (num_items(Items.Cactus) < NUM_ITEM_THRESHOLD):
		return Entities.Cactus
	elif (num_items(Items.Bone) < NUM_ITEM_THRESHOLD):
		return Entities.Dinosaur
	elif (num_items(Items.Gold) < NUM_ITEM_THRESHOLD and has_enough_weird_sub):
		return Entities.Treasure
	# elif (use_random):
	# 	return get_random_entity()
	else:
		return Entities.Tree 
		
def check_unlocks ():
	for i in range(len(UNLOCKS)):
		u = UNLOCKS[i]
		cost_map = get_cost(u)
		can_unlock = True
		for item in cost_map:
			cost = cost_map[item]
			if (num_items(item) < cost):
				can_unlock = False
		if can_unlock:
			unlock(u)

def clear_grid_for_dino ():
	if (get_entity_type() == None):
		return None
	for x in range(WORLD_SIZE):
		for y in range(WORLD_SIZE):
			move_to(x, y)
			harvest()
			if (get_ground_type() == Grounds.Grassland):
				till()