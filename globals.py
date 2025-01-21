ENTITIES_WATER_ALLOWED = [Entities.Carrot, Entities.Tree, Entities.Pumpkin, Entities.Sunflower]
ENTITIES_FERTILIZER_ALLOWED = [Entities.Sunflower]
ENTITIES_SOIL = [Entities.Carrot, Entities.Pumpkin, Entities.Sunflower, Entities.Cactus]
NUM_ITEM_THRESHOLD = 1000000
NUM_WEIRD_SUB_THRESHOLD = 25000
WATER_THRESHOLD = 0.25
FORCE_FERTILIZER = False

WORLD_SIZE = get_world_size()

UNLOCKS = [Unlocks.Cactus, Unlocks.Dinosaurs, Unlocks.Mazes, Unlocks.Polyculture, Unlocks.Fertilizer]

LEADERBOARD_SPEEDUP = 10000
LEADERBOARDS = {
	Leaderboards.Maze: 'lb_maze',
	Leaderboards.Dinosaur: 'lb_dino',
	Leaderboards.Pumpkins: 'lb_pumpkin',
	Leaderboards.Sunflowers: 'lb_sunflower'
}