from typing import Generator



#fibonacci generator
def fibonacci(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


#even numbers genrator
def evens(limit: int) -> Generator[int, None, None]:
    for i in range(limit):
        if i % 2 == 0:
            yield i

