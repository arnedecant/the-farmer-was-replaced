def clamp (val, min, max):
	return max(min, min(val, max))

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

def move_to_smart (x, y):
    x_dir = determine_x_dir(get_pos_x(), x)
    y_dir = determine_y_dir(get_pos_y(), y)
    while get_pos_x() != x:
        has_moved = move(x_dir)
        if (not has_moved):
            return False
    while get_pos_y() != y:
        has_moved = move(y_dir)
        if (not has_moved):
            return False
	return True

def determine_x_dir (x_from, x_to):
  right_moves = (x_to - x_from) % grid_size
  left_moves = (x_from - x_to) % grid_size
  if (right_moves < left_moves):
    return East
  else:
    return West

def determine_y_dir (y_from, y_to):
  up_moves = (y_to - y_from) % grid_size
  down_moves = (y_from - y_to) % grid_size
  if (up_moves < down_moves):
    return North
  else:
    return South
	
def try_dirs ():
	dirs = [North, West, East, South]
	for dir in dirs:
		if (move(dir)):
			return dir
	return None
				
def get_pos ():
	return [get_pos_x(), get_pos_y()]