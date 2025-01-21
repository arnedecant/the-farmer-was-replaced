entities_water_allowed = [Entities.Carrot, Entities.Tree, Entities.Pumpkin, Entities.Sunflower]
entities_fertilizer_allowed = [Entities.Sunflower]
entities_soil = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
num_item_threshold = 1000000
num_weird_sub_threshold = 25000
water_threshold = 0.25
global_force_fertilizer = False
grid_size = get_world_size()
unlocks_auto_unlock = [Unlocks.Cactus, Unlocks.Dinosaurs, Unlocks.Mazes, Unlocks.Polyculture, Unlocks.Fertilizer]

while True:
  leaderboard_pumpkin_loop()
  if (num_items(Items.Pumpkin) >= 100000):
    break

def leaderboard_pumpkin_loop ():
	for x in range(grid_size):
		for y in range(grid_size):
			move_to_smart(x, y)
			replant_pumpkin()
	coords_replant_pumpkin = []
	coords_last_pumpkin = None
	has_replanted = False
	for x in range(grid_size):
		for y in range(grid_size):
			move_to_smart(x, y)
			if not can_harvest():
				coords_replant_pumpkin.append([x, y])
				replant_pumpkin(True)
				has_replanted = True
	while has_replanted:
		has_replanted = False
		for i in range(len(coords_replant_pumpkin)):
			coords = coords_replant_pumpkin[i]
			move_to_smart(coords[0], coords[1])
			if (get_entity_type() != Entities.Pumpkin):
				has_replanted = True
				replant_pumpkin(True)
				coords_last_pumpkin = coords
	if coords_last_pumpkin != None:
		move_to_smart(coords_last_pumpkin[0], coords_last_pumpkin[1])
		while not can_harvest():
			if (get_entity_type() != Entities.Pumpkin):
				replant_pumpkin(True)
	harvest()

def replant_pumpkin (use_water_fertilizer = False):
  manage_soil(Entities.Pumpkin)
  plant(Entities.Pumpkin)
  if (not use_water_fertilizer):
    return None
  use_item(Items.Water)
  use_item(Items.Fertilizer)