import random


rolling = "y"
while rolling == "y":
    print()
    print("How many dice?")
    num = int(input())
    print()
    print("How many sides?")
    randomRange = int(input())
    print()

    while num > 0:
        ranNum = random.randrange(1, randomRange)
        print("nat"+str(ranNum))
        num -= 1

    rolling = input("Roll again??")
else:
    print("Come again!")