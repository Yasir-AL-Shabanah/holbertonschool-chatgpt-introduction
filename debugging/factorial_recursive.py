#!/usr/bin/python3
def factorial(n):
    """
    Function description:
      Compute the factorial of n using recursion.

    Parameters:
      n (int): non-negative integer.

    Returns:
      int: n! (product of integers from 1 to n). Returns 1 if n is 0.

    Raises:
      ValueError: if n is negative.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    import sys
    print(factorial(int(sys.argv[1])) if len(sys.argv) > 1 else factorial(5))
