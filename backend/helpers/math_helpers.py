# helpers/math_helpers.py
"""
Math helper functions
"""
import math
import random
from typing import List

def square(n):
    """Return square of n"""
    return n ** 2

def cube(n):
    """Return cube of n"""
    return n ** 3

def average(numbers: List[float]):
    """Return average of a list; returns 0 for empty list"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def factorial(n: int):
    """Return factorial (iterative to avoid recursion limit)"""
    if n < 0:
        raise ValueError("factorial() not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_prime(n: int):
    """Return True if n is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def square_root(n):
    """Return square root"""
    return math.sqrt(n)

def power(n, m):
    """Return n**m"""
    return n ** m

def absolute(n):
    """Return absolute value"""
    return abs(n)

def sine(angle_deg):
    """Sine of angle in degrees"""
    return math.sin(math.radians(angle_deg))

def cosine(angle_deg):
    """Cosine of angle in degrees"""
    return math.cos(math.radians(angle_deg))

def tangent(angle_deg):
    """Tangent of angle in degrees"""
    return math.tan(math.radians(angle_deg))

def random_int(start: int, end: int):
    """Random integer between start and end inclusive"""
    return random.randint(start, end)
