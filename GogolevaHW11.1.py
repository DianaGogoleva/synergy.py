def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorial_list(n):
    fact = factorial(n)
    return [factorial(i) for i in range(fact, 0, -1)]