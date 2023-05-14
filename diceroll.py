import random

print("\n\n\n")
rolling = input("wanna roll? (y/n)\n")
while rolling == "y":
    print()
    num = int(input("How many dice?\n"))
    print()
    randomRange = int(input("How many sides?\n"))
    print()
    total = int(0)

    while num > 0:
        ranNum = random.randrange(1, randomRange)
        print(f"nat {str(ranNum)}")
        num -= 1
        total = ranNum + total
    print(f"Total:  {str(total)}")
    rolling = input("Roll again? (y/n) \n")
else:
    print("Come again!")



# 1.1