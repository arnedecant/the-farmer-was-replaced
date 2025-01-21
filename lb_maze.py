from farms import maze_loop

clear()
while True:
  maze_loop()
  if (num_items(Items.Gold) >= 300000):
    break