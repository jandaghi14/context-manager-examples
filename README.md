# Context Managers Practice

Day 63 project - Learning context managers.

## What I Learned
- Context managers guarantee cleanup code runs
- `__enter__` and `__exit__` methods
- `@contextmanager` decorator is easier than writing classes
- Code before `yield` = setup
- Code after `yield` = cleanup

## Examples
```python
@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Took: {time.time() - start:.2f}s")

with timer():
    # your code here
```

## Built 3 Context Managers
1. Timer - measures execution time
2. Database - manages SQLite connections
3. Temp File - handles file writing