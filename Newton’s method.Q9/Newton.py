z = int(input('Enter a number to find square root: '))
x = 0

z_next = z - ((z*z - x) / (2 * z))

print(z_next)