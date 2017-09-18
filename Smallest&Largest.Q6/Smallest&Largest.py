import random

lst = []

for x in range(6):
    numbers = int(input("Enter Number: "))
    lst.append(numbers)

    print("Largest number is: ", max(lst), "\n while the smallest number is: ", min(lst))