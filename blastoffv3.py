import time
count = int(input("How many do you want to count from? "))
while count > 0:
    print("T - ", str(count))
    time.sleep(1)
    count -= 1
else:
    print("Blastoff!")
