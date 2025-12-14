import time
from funtools import wraps


#timer decorator
def timer(func):
    @warps(func)
    def wrapper(*args,**kwargs)
        start=time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f}s")
        return result
    return wrapper



#retry decorator

def retry(times=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {i+1} failed: {e}")
            print("All attempts failed")
        return wrapper
    return decorator

