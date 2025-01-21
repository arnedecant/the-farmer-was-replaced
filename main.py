entities_water_allowed = [Entities.Carrot, Entities.Tree, Entities.Pumpkin, Entities.Sunflower]
entities_fertilizer_allowed = [Entities.Sunflower]
entities_soil = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
num_item_threshold = 1000000
num_weird_sub_threshold = 25000
water_threshold = 0.25
global_force_fertilizer = False
grid_size = get_world_size()
unlocks_auto_unlock = [Unlocks.Cactus, Unlocks.Dinosaurs, Unlocks.Mazes, Unlocks.Polyculture, Unlocks.Fertilizer]
leaderboard_speedup = 10000

# default_game_loop(Entities.Pumpkin)

while True:
	# leaderboard_run(Leaderboards.Maze, 'lb_maze', leaderboard_speedup)
	# leaderboard_run(Leaderboards.Dinosaur, 'lb_dino', leaderboard_speedup)
	# leaderboard_run(Leaderboards.Pumpkins, 'lb_pumpkin', leaderboard_speedup)
	leaderboard_run(Leaderboards.Sunflowers, 'lb_sunflower', leaderboard_speedup)