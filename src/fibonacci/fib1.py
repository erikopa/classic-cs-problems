def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)


if __name__ == '__main__':
    '''
    That solution should create an error:
    RecursionError: maximum recursion depth exceeded
    '''
    print(fib1(5))
