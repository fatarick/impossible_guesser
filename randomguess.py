import random
import time

print("Picking a random number...")
time.sleep(2)

x = random.randint(1, 999999999999)
y = random.randint(1, 999999999999)

if x==y:
    print("Yes, i guessed it!")
    print("It was", x)
else:
    print("Oh no... I gueesed", y, ",Now you guess it!")
    while True:
     user_guess = input("Now you guess! ")
     if user_guess==x:
         print("You guessed it!")
         print("It was: ", x)
     else:
         print("Try Again!")
         
     if user_guess=="exit":
        break
        
     if user_guess=="Exit":
        break
         
