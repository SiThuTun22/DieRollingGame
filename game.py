import random
# requesting the number of Time The Die is cast
def inputTheNumOfTimesDieCast():
    # if num is not even OR negative request again
    while(True):
      num = int(input("enter the number of Time The Die is cast(only even positive number): "))
      if num > 0 and num %2 == 0:
        return num

def play_game(n):
  player1_points = 0
  player2_points = 0

  for _ in range(int(n/2)):
     player1_roll = roll_die()
     player2_roll = roll_die()
     print(f"Player 1 rolled: {player1_roll},Player 2 rolled: {player2_roll}")
     player1_points += player1_roll
     player2_points += player2_roll
  print("_______________________________________")
  print(f"Player 1 total points: {player1_points}")
  print(f"player 2 total points: {player2_points}")

  if player1_points > player2_points:
     print("player 1 wins")
  elif player2_points > player1_points:
     print("Player 2 wins")
  else:
     print("It's a draw!")
# rolling dice
def roll_die():
   return random.randint(1,6)

n = inputTheNumOfTimesDieCast()
play_game(n)
        
   