#fibonacci series

# Fibonacci(n)
#     if n>2:
#         return Fibonacci(n-1) +Fibonacci(n-2)
#     else"
#         return 1

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print("fib(5) is", fib(5))
print("fib(10) is", fib(10))

