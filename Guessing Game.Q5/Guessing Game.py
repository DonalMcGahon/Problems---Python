import random

# Create a number bewteen 1 and 100
number = random.randint(1, 100)

# The amount of trys the user can have
tries = 6

# Create a for loop in range of the number of trys the user can have
for userguess in range(tries):
    # Ask user to enter number between 1 and 100
    guess = int(input('Take a guess of a number between 1 and 100, You have 6 attempts to get the corrrect answer: '))

    if guess < number:
        print('Too small')
    elif guess > number:
        print('Too large')
        
    # If the user gets the correct number
    else:
        print('Well done! The number was ', number)
        print('It took you', tries, 'attempts')

        # A break to incase user gets number wrong
        break

# If user does not get the correct answer
if guess != number:
    print('Sorry you reached the maximum number of tries')
    print('The secret number was', number)