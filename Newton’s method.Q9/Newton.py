"""z = int(input('Enter a number to find square root: '))
x = 0

z_next = z - ((z*z - x) / (2 * z))

print(z_next)"""

# Ask user to enter number
z = int(input('Enter a number to find square root: '))

# Muliply user number by 0.5
squareroot = 0.5 * z
x = 0.5 * (squareroot + z/squareroot)
# While squareroot is not equal to x, repeat x
while x != squareroot:
    squareroot = x
    x = 0.5 * (squareroot + z/squareroot)
    
    # print square root
print(squareroot)