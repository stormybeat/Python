import random

passLength = int(input("How long would you like your password?\n"))
characters = ("qwertyuiopasdfghjklzxcvbnm[]!@#$%^&*()-=+QWERTYUIOPASDFGHJKLZXCVBNM1234567890")
password = "".join(random.sample(characters,passLength))
print(password)