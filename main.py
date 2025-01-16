entities_water_allowed = [Entities.Carrot, Entities.Tree, Entities.Pumpkin, Entities.Sunflower]
entities_fertilizer_allowed = [Entities.Sunflower]
entities_soil = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
num_item_threshold = 100000
num_weird_sub_threshold = 25000
water_threshold = 0.25
grid_size = get_world_size()
unlocks_auto_unlock = [Unlocks.Cactus, Unlocks.Dinosaurs, Unlocks.Mazes, Unlocks.Polyculture, Unlocks.Fertilizer]

clear()
			
while True:
	change_hat(Hats.Straw_Hat)
	move_to(0, 0)
	check_unlocks()
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
		