# Ask user to input a string
user_string = str(input('Enter a string to see if it is palindrome or not: '))
# This is used to reverse the string
string_rev = reversed(user_string)

# Check to see if the string is equal to itself in reverse
if list(user_string) == list(string_rev):
   print("It is palindrome")
else:
   print("It is not palindrome")