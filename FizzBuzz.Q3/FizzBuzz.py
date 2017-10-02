# Create a range from 1 to 100
for x in range(1, 101):
    result = ""
    result1 = ""
    result2 = ""
    print(x)
    # if number is divisible by 3
    if not x % 3:
        result += "Fizz"
        # if number is divisible by 5
    if not x % 5:
        result1 += "Buzz"
        # if number is divisible by 3 and 5
    if not x % 3 and 5:
        result2 += "FizzBuzz"
        print(result, result1, result2)