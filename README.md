# Impossible Guesser (Or Random Guesser) MinusPlus Version
It's a simple game-script at python that generated a random number from -999 Billion until 999 Billion and "AI" Guess it. If "AI" guessed it wrong you should to guess it but you have infinity chances until you write "exit" or "Exit" :)

# Known Bugs
When you write "Exit" or "exit" it writes "Try Again" and then exits the game.

# How the "AI" works
When the game is generating the number with variable X to guess also with the game there is a same command to the variable Y. They generate two different numbers and if they equal (Chance One To Trillion) the game exits. If it not guessed it right so its users turn to guess. Here's an example to code of two variables that generate number from -1000 until 1000 and equal check.

import random

x = random.randint(-1000, 1000) #Number that "AI" and user need to guess.
y = random.randint(-1000, 1000) #Number that "AI" guessed.

if x==y: #Checks if its equal
  print("Yes") #If its right, it prints "Yes"
  else:
  print("No") #If its incorrect, it prints "No"


# Want a harder challenge?

Check another "Hell" and "VeryHotHell" branch that contains modified version of game that guesses from 1 and -999 Billion to 999 Billion, But now its with decimal number. Good Luck!
