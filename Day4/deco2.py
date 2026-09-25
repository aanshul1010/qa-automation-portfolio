'''import time


def test_login():
    print("Testing login ")
    start= time.time()
    print("testing login")
    end = time.time()
    print(f"test_login took {end - start}s'")
    print("Pass")



test = test_login()

test'''
import functools


def run_twice(func):
    func()
    func()

def sayhi():
    print("hlw")

run_twice(sayhi)
print(f"{'='*100}")

#function returning a function
print("✅✅✅✅function returning a function")
def greet_people(name):
    def greet():
        print(f"hello {name}")

    return greet

hi = greet_people("namsate")
hi()
print(f"{'='*100}")


def my_decorator(func):

    def wrapper():
        print("\nbefore function runs")

        func()

        print("\nafter function runs")

    return wrapper
@my_decorator
def test_login():
    print("\ntesting login function ")
print(f"{'='*100}")

#print(what if function returns something)
print("✅✅✅✅what if function returns something")

def mera_decorator(func):
    def wrapper():
        print("\nBefore")
        result = func()
        print("After")
        return result
    return wrapper

@mera_decorator
def test_login():
    print("testing something in the login function")
    return True

result = test_login()
print(result)
print(f"{'='*100}")

#handling function argrument  problem is that what if decorated function has parameters
print("✅✅✅✅handling function argrument  problem is that what if decorated function has parameters")


def simple_decorator(func):
    def wrapper(*args, **kwargs):  #catch positional and keyword argumensts
        print("Before test ")
        result = func(*args, **kwargs) # unpack and pass arguements
        print("After test")
        return result
    return wrapper

@simple_decorator
def loginTest(username, password):
    print(f"logining with {username}")
    return True

@simple_decorator
def carttest():
    print("testing Cart")
    return True

loginTest("adming", "546465")
carttest()
print(f"{'='*100}")
'''# Check function name:
print(test_login.__name__)    # "wrapper" ← WRONG
print(test_login.__doc__)     # None ← LOST

# WHY WRONG:
# test_login now points to wrapper
# so its name IS wrapper
# original name "test_login" is lost
# docstring is lost too

# This breaks:
# → Pytest test discovery
# → Logging and error messages
# → Debugging tools
# → help() function'''
#TO fix above problem use @functiontools

def my_decorator(func):
    @functools.wraps(func) #add this function 
    def wrapper(*args, **kwargs):  # catch positional and keyword argumensts
        print("Before test ")
        result = func(*args, **kwargs)  # unpack and pass arguements
        print("After test")
        return result

    return wrapper

@my_decorator
def test_login():
    """Tests the login functionality."""
    return True

print(test_login.__name__)
print(test_login.__doc__)
