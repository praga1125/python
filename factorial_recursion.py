def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)


number = 5
print("The factorial of ", number, "is : ", factorial(number))
