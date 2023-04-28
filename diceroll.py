
import random

print("How many dice?")
num = int(input())
print()
print("How many sides?")
randomRange = int(input())

print()
while num > 0:
    rannum = random.randrange(1, randomRange)
    print(rannum)
    num -= 1
