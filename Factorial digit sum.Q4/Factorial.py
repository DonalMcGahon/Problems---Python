# Adapted from - https://discuss.codechef.com/questions/56854/computing-sum-of-digits-of-large-factorial

from math import factorial

# Create a variable by asking the user to enter a number
user = int(input("Please enter a number: "))

# Store factorial of the users number
x = factorial(user)

# Typecast variable to string
x = str(x)

# Initialize num as 0
num = 0

# Iterate through the string x
for i in x:
    #Add each value after typecasting character into integer
    num += int(i)

# Print sum of the numbers when added together
print (num)