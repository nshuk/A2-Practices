print("The fibonacci sequence starts with digit 1 as the first term")
nth = int(input("Please enter the nth term of a Fibonacci sequence: "))

def fibonacci (nth):
    if nth <= 1:
        return nth
    else:
        answer = fibonacci(nth - 1) + fibonacci(nth - 2)
        return answer

result = fibonacci(nth)
print("The ", nth, "th term of the Fibonacci sequence is: ")
print(result)