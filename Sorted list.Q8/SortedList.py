# Adapted from - https://stackoverflow.com/questions/29615274/user-input-integer-list

# Ask user to enter a list of numbers
list1 = input("Please enter a list of numbers separated by a single space only: ")
list1 = list1.split(' ')

# Ask user to enter a list of numbers
list2 = input("Please enter a list of numbers separated by a single space only: ")
list2 = list2.split(' ')

# .extend allows for the two lists to join together
list1.extend(list2)
# sorted sorts the list
print(sorted(list1))