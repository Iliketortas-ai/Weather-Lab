import random

days = int(input("Enter number of days: "))

for day in range(1, days + 1):
    temp = random.randint(-10, 100)
    print("Day", day, "temperature:", temp, "°F")

