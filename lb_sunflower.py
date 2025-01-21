grid_size = get_world_size()
entities_soil = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
sf_map = { 15: [], 14: [], 13: [], 12: [], 11: [], 10: [], 9: [], 8: [], 7: [] }
sf_arr = []
num_sunflower_threshold = 10

clear()
sf_arr = leaderboard_sunflower_setup(sf_arr)

while True:
  sf_arr = leaderboard_sunflower_loop(sf_arr)
  if (num_items(Items.Power) >= 100000):
    break

def leaderboard_sunflower_setup (arr = sf_arr):
	for x in range(grid_size):
		for y in range(grid_size):
			move_to(x, y)
			manage_plot_sunflower(x, y)
			arr.append((x, y))
	return arr

def leaderboard_sunflower_loop (arr = sf_arr):
	for i in range(len(arr)):
		x, y = arr[i].pop()
		move_to(x, y)
		size = manage_plot_sunflower(x, y)
		arr.append((x, y))
	return arr

def manage_plot_sunflower (x, y, force = False):
	if (can_harvest()):
		harvest()
	if (get_ground_type() == Grounds.Grassland):
		till()
	plant(Entities.Sunflower)
	size = measure()
	while (size < 10):
		harvest()
		plant(Entities.Sunflower)
		size = measure()
	if (size > 12):
		use_item(Items.Water)
	if (size > 14):
		use_item(Items.Fertilizer)
	return size