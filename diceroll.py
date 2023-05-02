import random

print("\n\n\n")
rolling = input("wanna roll? (y/n)\n")
while rolling == "y":
    print()
    num = int(input("How many dice?\n"))
    print()
    randomRange = int(input("How many sides?\n"))
    print()

    while num > 0:
        ranNum = random.randrange(1, randomRange)
        print("nat"+str(ranNum))
        num -= 1

    rolling = input("Roll again? (y/n) \n")
else:
    print("Come again!")