#file manager
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f
    finally:
        f.close()

#timer context context

@contextmanager
def timer_cm(name="Block"):
    import time
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print(f"{name} took {end-start:.4f}s")

