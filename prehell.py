import random

print("Pre-Hell is a practice to hell with decimal numbers.")
print("Choose your practice:")
print("1. From 1 to 100")
print("2. From 1 to 1000")
print("3. From -100 to 100")
print("4. From -1000 to 1000")

choose = input("Practice Number: ")

if choose == "1":
    x1 = random.uniform(1, 100)
    while True:
        uc1 = input("Number: ")
        if uc1 == str(x1):
            print("Congrats!")
            break
        else:
            print("Try Again!")

elif choose == "2":
    x2 = random.uniform(1, 1000)
    while True:
        uc2 = input("Number: ")
        if uc2 == str(x2):
            print("Congrats!")
            break
        else:
            print("Try Again!")

elif choose == "3":
    x3 = random.uniform(-100, 100)
    while True:
        uc3 = input("Number: ")
        if uc3 == str(x3):
            print("Congrats!")
            break
        else:
            print("Try Again!")

elif choose == "4":
    x4 = random.uniform(-1000, 1000)
    while True:
        uc4 = input("Number: ")
        if uc4 == str(x4):
            print("Congrats!")
            break
        else:
            print("Try Again!")

else:
    print("Invalid choice. Please enter a number between 1 and 4.")
