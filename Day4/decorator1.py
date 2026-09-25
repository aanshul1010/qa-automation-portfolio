# ============================================================
# File: day03/09_decorators.py
# ============================================================
import functools
import time


# ─── BASIC DECORATOR ────────────────────────────────────────
# A decorator is just a function that:
# 1. Takes a function as input
# 2. Defines a wrapper function
# 3. Returns the wrapper

def log_test(func):
    """Logs test start and end."""

    @functools.wraps(func)    # preserves metadata
    def wrapper(*args, **kwargs):
        print(f"\n▶️  Starting: {func.__name__}")
        result = func(*args, **kwargs)  # run original
        print(f"✅ Completed: {func.__name__}")
        return result

    return wrapper


# ─── USING THE DECORATOR ────────────────────────────────────
@log_test
def test_login():
    """Tests login functionality."""
    print("  → Entering credentials")
    print("  → Clicking login")
    return True

@log_test
def test_cart():
    """Tests cart functionality."""
    print("  → Adding item to cart")
    return True

# Calling decorated function:
test_login()
test_cart()

# What happens behind the scenes:
# @log_test = test_login = log_test(test_login)
# Calling test_login() actually calls wrapper()


# ─── DECORATOR WITH ARGUMENTS ───────────────────────────────
def retry(times: int = 3):
    """
    Decorator factory — takes argument.
    Returns actual decorator.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"  Attempt {attempt}/{times} "
                          f"failed: {e}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator


@retry(times=3)
def flaky_test():
    """Simulates a flaky test."""
    import random
    if random.random() < 0.7:
        raise Exception("Element not found")
    return True


# ─── TIMING DECORATOR ───────────────────────────────────────
def measure_time(func):
    """Measures test execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start  = time.time()
        result = func(*args, **kwargs)
        end    = time.time()
        print(f"⏱️  {func.__name__} took "
              f"{end - start:.2f}s")
        return result
    return wrapper


@measure_time
def test_checkout():
    time.sleep(0.1)   # simulate test work
    print("Checkout test passed")
    return True


# ─── STACKING DECORATORS ────────────────────────────────────
@log_test
@measure_time
def test_search():
    time.sleep(0.05)
    print("  → Search test running")
    return True

# Applied bottom up:
# test_search = log_test(measure_time(test_search))


if __name__ == "__main__":
    test_login()
    test_cart()
    test_checkout()
    test_search()