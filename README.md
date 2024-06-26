# Impossible Guesser (Or Random Guesser)
It's a simple game-script at python that generated an random number until 999 Billion and "AI" Guess it. If "AI" guessed it wrong you should to guess it but you have infinity chances until you write "exit" or "Exit" :)

# Known Bugs
When you write "Exit" or "exit" it writes "Try Again" and then exits the game.

# How the "AI" works
When the game is generating the number with variable X to guess also with the game there is a same command to the variable Y. They generate two different numbers and if they equal (Chance One To Trillion) the game exits (Maybe, i don't know). If it not guessed it right so its users turn to guess. Here's an example to code of two variables that generate number until 1000 and equal check.

import random

x = random.randint(1, 1000) #Number that "AI" and user need to guess.
y = random.randint(1, 1000) #Number that "AI" guessed.

if x==y: #Checks if its equal
  print("Yes") #If its right, it prints "Yes"
  else:
  print("No") #If its incorrect, it prints "No"

# How you can help
If you are a lucky boy and AI guessed it, write if it exits the game or not.

# Want a harder challenge?

Check another "MinusPlus" branch that contains modified version of game that guesses from -999 Billion to 999 Billion. Or check two harder versions: "Hell" and "VeryHotHell" with same numbers but also you will need to guess it using decimal numbers, not just numbers.
