# Create an empty list
lst = []
# Ask user how many numbers they would like in the list
num = int(input('How many numbers: '))

# For the amount of numbers the user wants in the list, ask them to enter a number for each digit in the list
for n in range(num):
    numbers = int(input('Enter number '))
    # .append adds the numbers to the list
    lst.append(numbers)
    # Print out the Lagest and Smallest numbers
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))