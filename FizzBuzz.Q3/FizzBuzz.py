for x in range(1, 101):
    result = ""
    result1 = ""
    result2 = ""
    if not x % 3:
        result1 += "Fizz"
    if not x % 5:
        result += "Buzz"
        print(x, result, result1, result2)