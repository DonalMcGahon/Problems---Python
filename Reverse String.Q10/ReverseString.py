#user_string = str(input('Enter a string: '))

#user_string_rev = reversed(user_string)

#user_string_rev.join(reverse(my_string))

#print(user_string_rev)

# Create a function
def string_reverse(str1):

# Create an empty String
    reverseString = ''
    # Return the lenght of the string
    x = len(str1)
    # While lenght of the string is greater than 0
    while x > 0:
        # Create a new string by syarting backways on the user entered string
        reverseString += str1[ x - 1 ]
        x = x - 1
    return reverseString
# Ask user to enter a  word
user_string = str(input('Enter a string: '))
# Print out word backways
print(string_reverse(user_string))