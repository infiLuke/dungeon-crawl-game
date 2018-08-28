import os
import random
import sys

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)]

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# generate random locations for player, door and monster
def get_location(CELLS):
  '''returns a tuple with three random elements from an iterable argument'''
  return random.sample(CELLS, 3)

# move the player
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

# get possible moves for the player
def get_moves(player):
  moves = ['left', 'right', 'up', 'down']
  x, y = player
  if y == 0:
    moves.remove('up')
  if y == 4:
    moves.remove('down')
  if x == 0:
    moves.remove('left')
  if x == 4:
    moves.remove('right')
  return moves

# print a map to the screen using 'underscore' and 'pipe'
def draw_map(player):
  print(' _' * 5)
  tile = '|{}'
  for cell in CELLS:
    x, y = cell
    if x < 4:
      line_end = ''
      if cell == player:
        output = tile.format('X')
      else:
        output = tile.format('_')
    else:
      line_end = '\n'
      if cell == player:
        output = tile.format('X|')
      else:
        output = tile.format('_|')
    print(output, end=line_end)
  print()

# start new game
def game_loop():
  # generate new map locations
  monster, player, door = get_location(CELLS)

  # player turns
  while True:
    clear_screen()
    draw_map(player)
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
      input('Can not move to {}. Press enter to continue'.format(move))
      continue
    else:
      player = move_player(player, move)

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
