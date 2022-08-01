# recusrsive function

# n=input("Enter the number: ")
def recur_factorial(n):
    if n == 1:
       return 1
    else:
        return n * recur_factorial(n - 1)

# print("Factorial of the number is "recur_factorial())
# recur_factorial(int(n))
print("5! is", recur_factorial(5))
print("10! is", recur_factorial(10))


