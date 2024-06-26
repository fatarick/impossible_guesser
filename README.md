# Impossible Guesser (Or Random Guesser)
It's a simple game-script at python that generated a random decimal number from 1 until 999 Billion and "AI" Guess it. If "AI" guessed it wrong you should to guess it but you have infinity chances until you write "exit" or "Exit" :)

# Known Bugs
When you write "Exit" or "exit" it writes "Try Again" and then exits the game.

# How the "AI" works
When the game is generating the decimal number with variable X to guess also with the game there is a same command to the variable Y. They generate two different decimal numbers and if they equal (Chance One To Trillion) the game exits (Maybe, i don't know). If it not guessed it right so its users turn to guess. Here's an example to code of two variables that generate number until 1000 and equal check.

import random

x = random.uniform(1, 1000) #Number that "AI" and user need to guess.
y = random.uniform(1, 1000) #Number that "AI" guessed.

if x==y: #Checks if its equal
  print("Yes") #If its right, it prints "Yes"
  else:
  print("No") #If its incorrect, it prints "No"


# Want a harder challenge?

Check another "VeryHotHell". Same as this branch but its from -999 billion to 999 billion.

# Want to practice?

Check "PreHell" Branch with choose to random number. From 1 to 100 or 1000 and From -100 or -1000 and From 100 to 1000
