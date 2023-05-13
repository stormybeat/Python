import random

def diceRoll(num):
    global total
    global randomRange
    ranNum = random.randrange(1, randomRange)
    print(f"nat {str(ranNum)}")
    total = ranNum + total

print("\n\n\n")
rolling = input("wanna roll? (y/n)\n")
while rolling == "y":
    num = int(input("\nHow many dice?\n"))
    randomRange = int(input("\nHow many sides?\n"))
    print()
    total = 0
    while num > 0:
        diceRoll(num)
        num -= 1
    print(f"Total:  {str(total)}")
    rolling = input("Roll again? (y/n) \n")
else:
    print("Come again!")

    # version 1.2