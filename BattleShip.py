#First test of BattleShip

#!/user/bin/python
from random import randint

# create the sea board 5x5
board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

# random position of the ship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
# Debugging:
#print ship_row
#print ship_col

# Input player guess for 4 tries(turns)
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
# check answer
  # if correct
  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    
# Future development: bigger ocean and more than one ships
#                     more than one player   
    break
  # if not correct
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    if (turn == 3):
      print "Game Over"
    print_board(board)
