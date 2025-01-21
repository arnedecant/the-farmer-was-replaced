from utils import get_pos


# possible next tactic could be wall hugging

def move_to_safe (target_x, target_y):
    curr_x, curr_y = get_pos()
    while curr_x != target_x:
        if curr_x < target_x:
            if not move(East):
                return False
        elif curr_x > target_x:
            if not move(West):
                return False
        curr_x, curr_y = get_pos()
    while curr_y != target_y:
        if curr_y < target_y:
            if not move(North):
                return False
        elif curr_y > target_y:
            if not move(South):
                return False
        curr_x, curr_y = get_pos()
    return True

def dino_s_pattern (row=0, current_x=0):
    world_size = get_world_size()
    current_y = get_pos_y()
    if row == world_size:
        move_to_safe(0, 0)
        dino_s_pattern()
    if row % 2 == 0:  # ltr
        for x in range(current_x, world_size):
            if x == 0:
                continue
            if not move_to_safe(x, row):
                return
        current_x = world_size - 1
    else:  # rtl
        for x in range(current_x, -1, -1):
            if x == 0:
                continue
            if not move_to_safe(x, row):
                return
        current_x = 0 
    dino_s_pattern(row + 1, current_x)

def dino_loop_simple (next_x = None, next_y = None, num_retries = 0):
	if (not next_x and not next_y):
		m = measure()
		if (m == None):
			return None
		next_x = m[0]
		next_y = m[1]
	curr_x, curr_y = get_pos()
	has_moved = move_to(next_x, next_y)
	if (has_moved):
		dino_loop_simple()
	else:
		possible_dir = try_dirs()
		while possible_dir != None and num_retries < 4:
			num_retries = num_retries + 1
			dino_loop_simple(next_x, next_y)