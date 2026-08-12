def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"


def add(a, b):
    """Add two numbers and return the result."""
    return a + b


def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    print(greet("World"))
    print(f"5 + 3 = {add(5, 3)}")
    print(f"First 10 Fibonacci numbers: {fibonacci(10)}")
