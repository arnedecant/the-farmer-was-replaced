# Tried asking ChatGPT... But this thing doesn't work.

next_x = None
next_y = None
tail_positions = []
apples_eaten = 0

clear()
move_dino_to(0, 0)
change_hat(Hats.Dinosaur_Hat)

while True:
	# If no target apple position is given, determine it
    if next_x == None and next_y == None:
        m = measure()
        if m == None:
            break  # No apple found
        next_x, next_y = m[0], m[1]

    # Get current position of the dino
    curr_x, curr_y = get_pos()

    # Determine the hugging direction (we assume the dino hugs the right wall)
    if curr_x == 0 or curr_x == get_world_size() - 1:  # If on left or right wall
        # Move vertically (North/South) along the wall until y aligns with the apple
        if curr_y < next_y:
            has_moved = move_dino_to(curr_x, get_world_size() - 1)  # Move South along the right wall
        else:
            has_moved = move_dino_to(curr_x, 0)  # Move North along the left wall
    else:
        # If not on the wall, move horizontally (East/West) to align with the apple
        has_moved = move_dino_to(next_x, curr_y)

    # After moving, check if the apple is eaten
    if has_moved:
        # Update tail with the new position
        tail_positions = update_tail(tail_positions)
        
        m = measure()
        if m == None:
            break  # No apple found
        if (m[0] != next_x or m[1] != next_y):
            next_x, next_y = measure()
            apples_eaten = apples_eaten + 1

def move_dino_to(target_x, target_y):
    # Move towards the target x,y position
    while get_pos_x() != target_x:
        if get_pos_x() < target_x:
            if not move(East):
                return False  # Failed to move East
        else:
            if not move(West):
                return False  # Failed to move West

    while get_pos_y() != target_y:
        if get_pos_y() < target_y:
            if not move(North):
                return False  # Failed to move North
        else:
            if not move(South):
                return False  # Failed to move South

    return True  # Successfully moved to the target position

def update_tail(tail):
    # Add the new position to the tail
    tail.append((curr_x, curr_y))  # Add the new head position

    # Ensure tail doesn't grow too long
    while len(tail) > apples_eaten:
        tail.pop(0)  # Remove the oldest tail segment

    return tail  # Return the updated tail

def check_for_apple(x, y):
    # Check if the dino is on an apple (i.e., if it has eaten an apple)
    if get_pos() == (x, y):
        return 1  # Apple eaten
    return 0  # No apple eaten
    