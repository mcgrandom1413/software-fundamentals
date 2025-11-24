#game 2 
import os
from random import randint 
lives = 3
status = True
def roll_dice(): 
    dice1 = randint (1,6)
    dice2 = randint (1,6)
    return dice1, dice2
while True : 
    key = input("press any key roll dices :")
    dices = roll_dice()
    print (f"dice1 : {dices[0]}")
    print (f"dice2 : {dices[1]}")
    if (dices[0] + dices [1]  ) % 2 == 0 : 
        lives += 1
    else : 
        lives -= 1
    if dices [0] == 6 and dices [1] == 6 : 
          print ("YOU WIN  ")
          os.system ("pause")
          break
    if lives == 0 :
          print ("GAME OVER ")
          break
    
    
    