"""Simple calculator module used to demonstrate CI/CD and code review."""


class Calculator:
    """Performs basic arithmetic operations."""

    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return a minus b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return a divided by b; raise ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def is_even(n):
        """Return True if n is even."""
        return n % 2 == 0

    @staticmethod
    def factorial(n):
        """Return n! for non-negative n; raise ValueError if n is negative."""
        if n < 0:
            raise ValueError("Negative numbers not allowed")
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result