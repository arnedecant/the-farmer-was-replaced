ENTITIES_WATER_ALLOWED = [Entities.Carrot, Entities.Tree, Entities.Pumpkin, Entities.Sunflower]
ENTITIES_FERTILIZER_ALLOWED = [Entities.Sunflower]
ENTITIES_SOIL = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
NUM_ITEM_THRESHOLD = 1000000
NUM_WEIRD_SUB_THRESHOLD = 25000
WATER_THRESHOLD = 0.25
FORCE_FERTILIZER = False
grid_size = get_world_size()
UNLOCKS = [Unlocks.Cactus, Unlocks.Dinosaurs, Unlocks.Mazes, Unlocks.Polyculture, Unlocks.Fertilizer]

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