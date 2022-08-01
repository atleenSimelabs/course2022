#fibonacci series

def fib(n):
    if n == 1 or n == 2:
        print("Found fib(", n, "): returning 1!", sep = "")
        return 1

    else:
        print("Finding fib(", n, "): fib(", n - 1, ") + fib(", n-2, ")", sep = "")
        result =  fib(n - 1) + fib(n - 2)
        print("Found fib(", n, "): ", result, sep = "")
        return result

print("fib(5) is", fib(5))

