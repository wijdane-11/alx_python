#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

print("Last digit of {} is {} and is ".format(number, last_digit), end="")

if last_digit == 0 and number != 0:
    print("0")
elif number < 0:
    print("-{} and is less than 6 and not 0".format(last_digit))
else:
    print("greater than 5")