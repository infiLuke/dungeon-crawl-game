import os
import random
import sys

# 2-D Map Coordinates Layout
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2), (9, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4),
         (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (9, 5),
         (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (9, 6),
         (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7), (9, 7),
         (0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8),
         (0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9),]

MAP_HEIGHT = 10
MAP_WIDTH = 10

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# generate random locations for player, door and monster_one
def get_location(CELLS):
  '''returns a tuple with five random elements from an iterable argument'''
  return random.sample(CELLS, 5)

# move the player object
def move_player(player, move):
  x, y = player
  if move == 'left':
    x -= 1
  elif move == 'right':
    x += 1
  elif move == 'up':
    y -= 1
  elif move == 'down':
    y += 1
  new_player = (x, y)
  return new_player

# get permitted move-actions for the player
def get_moves(player):
  moves = ['left', 'right', 'up', 'down']
  x, y = player
  if y == 0:
    moves.remove('up')
  if y == MAP_HEIGHT - 1:
    moves.remove('down')
  if x == 0:
    moves.remove('left')
  if x == MAP_WIDTH - 1:
    moves.remove('right')
  return moves

# AI moves:
def ai_move(monster):
  allowed_moves = get_moves(monster)
  ai_number = random.randint(-1, len(allowed_moves) - 1)
  if ai_number == -1:
    return monster
  ai_choice = allowed_moves[ai_number]
  new_monster = move_player(monster, ai_choice)
  return new_monster

# print a map to the screen using 'underscore' and 'pipe'
def draw_map(player, monster_one, monster_two, monster_three, door):
  print(' _' * MAP_WIDTH)
  tile = '|{}'
  for cell in CELLS:
    x, y = cell
    if x < MAP_WIDTH - 1:
      line_end = ''
      if cell == door:
        output = tile.format('O')
      elif cell == monster_one:
        output = tile.format('§')
      elif cell == monster_two:
        output = tile.format('§')
      elif cell == monster_three:
        output = tile.format('§')
      elif cell == player:
        output = tile.format('X')
      else:
        output = tile.format('_')
    else:
      line_end = '\n'
      if cell == door:
        output = tile.format('O|')
      elif cell == monster_one:
        output = tile.format('§|')
      elif cell == monster_two:
        output = tile.format('§|')
      elif cell == monster_three:
        output = tile.format('§|')
      elif cell == player:
        output = tile.format('X|')
      else:
        output = tile.format('_|')
    print(output, end=line_end)
  print()

# check for collision of player and monsters
def check_snake(player, monster_one, monster_two, monster_three, door):
    if player == monster_one or player == monster_two or player == monster_three:
      clear_screen()
      draw_map(player, monster_one, monster_two, monster_three, door)
      input('The snake got you.')
      main_menu()

# start new game
def game_loop():
  # generate new map locations for monster_ones, player and door
  monster_one, monster_two, monster_three, player, door = get_location(CELLS)

  # player turns
  while True:
    clear_screen()
    draw_map(player, monster_one, monster_two, monster_three, door)
    possible_moves = get_moves(player)
    moves_string = ', '.join(possible_moves)
    room_string = '{} - {}'.format(player[0] + 1, player[1] + 1)

    print('Welcome to the dungeon!')
    print('You are currently in room {}'.format(room_string))
    print('You can move {}'.format(moves_string))
    print('Enter QUIT to quit the game')

    move = input('>  ')
    move = move.lower()

    if move == 'quit':
      main_menu()
    elif move not in possible_moves:
      input('Can not move {}. Press enter to continue'.format(move))
      continue
    else:
      player = move_player(player, move)
      check_snake(player, monster_one, monster_two, monster_three, door)
      monster_one = ai_move(monster_one)
      monster_two = ai_move(monster_two)
      monster_three = ai_move(monster_three)
    if player == door:
      input('You made it to the entrace before the snakes found you.')
      main_menu()
    else:
      check_snake(player, monster_one, monster_two, monster_three, door)

# initialize main menu
def main_menu():
  clear_screen()
  print('Welcome to the dungeon!')
  print('Press Return to start a new game!')
  print('Enter QUIT to exit to desktop')
  select = input(' >  ').lower()
  if select == 'quit':
    sys.exit()
  game_loop()

# initialize the program
main_menu()
