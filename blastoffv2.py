import time


count = 5
tmin = "T-{}"
while count > 0:
        time.sleep(1)
        print(tmin.format(count))
        count -= 1
else:
        print("Blast Off!")