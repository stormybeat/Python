
import random
rolling=True
while rolling == True:
    print()
    print("How many dice?")
    num = int(input())
    print()
    print("How many sides?")
    randomRange = int(input())
    print()

    while num > 0:
        ranNum = random.randrange(1, randomRange)
        print(ranNum)
        num -= 1
