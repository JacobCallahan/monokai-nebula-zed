"""Sample Python module with nonsense code."""
import os
from collections import defaultdict
# ruff: noqa: F401, F841, I001, T201, PTH123, PLR2004
DEBUG, PI = True, 3.14159
config = {"name": 'app', "items": [1, 2.5, None, True, False]}

def some_decorator(func):
    return func

class DataProcessor:
    """Docstrings are subdued, like normal comments."""
    def __init__(self, name="default"):
        self.name, self._value = name, 42

    @some_decorator
    def process(self, items=None, **kwargs):
        try:  # try to do something
            result = [f"#{i}: {item!r}" if isinstance(item, (str | int))
                     else x**2 for i, item in enumerate(items or [])
                     for x in range(2) if item is None]
            return result
        except ValueError as e:  # we failed to do it
            print(f"Error: {e}")

def analyze():
    square = lambda x: x * x
    data = {i: square(i) for i in range(3)}
    with open(__file__) as f:
        content = f.read()
    return any(len(line) > 80 for line in content.split('\n'))

if __name__ == "__main__":
    processor = DataProcessor("test")
    output = processor.process([1, "hello", 3.14])
    mask = 0xFF & 0x0F | 0x10
    valid = mask >= 10 and not False
    assert analyze() or valid, "Test failed"
