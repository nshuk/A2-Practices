number = int(input("Please enter an integer: "))

def factorial(number):
    if number == 0:
        answer = 1
    else:
        answer = number * factorial(number - 1)
    return answer

result = factorial(number)
print("The factorial of ", number, "is:")
print(result)