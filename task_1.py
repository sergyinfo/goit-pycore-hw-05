"""
Task 1: Fibonacci numbers
"""
def caching_fibonacci() -> callable:
    """
    Return function that calculates the n-th Fibonacci number 
    using a cache to store intermediate results.

    :return: callable
    """

    cache = {}

    def fibonacci(n: int) -> int:
        """
        Return the n-th Fibonacci number using a cache to store intermediate results.

        :param n: int
        :return: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(10)) # 55
    print(fib(15)) # 610
    print(fib(50)) # 12586269025
    print(fib(100)) # 354224848179261915075
