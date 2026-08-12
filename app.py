from typing import List

def greet(name: str = "World") -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    """Add two numbers and return the result."""
    return a + b


def fibonacci(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []

    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    print(greet())
    print(f"5 + 3 = {add(5, 3)}")
    print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
