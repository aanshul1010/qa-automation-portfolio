x = "25"
y = 25
print(x == y)
print(type(x) == type(y))
name = "  Standard_User  "
print(name.strip().lower())

url = "https://saucedemo.com/inventory.html"
parts = url.split("/")
print(parts[-1])
print(len(parts))


price = 29.9999
print(f"${price:.2f}")


a = None
b = None
print(a == b)
print(a is b)

text = "Epic sadface: Username is required"
print("username" in text)
print("Username" in text)
print("username" in text.lower())


products = ["Backpack", "Bike Light",
            "T-Shirt", "Jacket", "Onesie"]
print(products[2])
print(products[-2])
print(products[1:3])

test_case = {
    "id"      : "TC001",
    "status"  : "pass",
    "browser" : "chrome"
}
print(test_case.get("priority", "High"))
print(test_case.get("status"))
print(test_case.get("missing"))


tags = {"smoke", "login", "regression"}
tags.add("smoke")
tags.add("e2e")
print(len(tags))
print("login" in tags)




results = []
for i in range(1, 4):
    results.append(f"TC00{i}")
print(results)
config = {
    "url"    : "https://saucedemo.com",
    "timeout": 10
}
config["browser"] = "chrome"
config["timeout"] = 20
print(config)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
unique = set(numbers)
print(len(unique))
print(sorted(unique))


test = {
    "id"  : "TC001",
    "data": {
        "username": "admin",
        "expected": "Products"
    }
}
print(test["data"]["username"])
print(test["data"]["expected"])

score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Average")
else:
    print("Fail")

failed = 0
build = "GREEN" if failed == 0 else "RED"
priority = ("CRITICAL" if failed > 5
            else "HIGH" if failed > 2
            else "LOW")
print(build)
print(priority)



tests = ["TC001", "TC002",
         "TC003", "TC004", "TC005"]
for i, test in enumerate(tests, start=1):
    if i % 2 == 0:
        print(f"{test} - EVEN")
    else:
        print(f"{test} - ODD")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [n for n in numbers if n % 2 == 0]
print(result)

items = ["a", "b", "c", "d", "e"]
for item in items:
    if item == "c":
        break
    print(item)






def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("John"))
print(greet("John", "Hi"))
print(greet(greeting="Hey", name="John"))

def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b
    return None

x = calculate(5, 3)
y = calculate(5, 3, "multiply")
z = calculate(5, 3, operation="multiply")
print(x, y, z)

def process(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(process(1, 2, 3))
print(process(10, 20))
print(process(5))

def configure(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

configure(browser="chrome",
          timeout=10,
          headless=False)

def get_title():
    title = "Products"

result = get_title()
print(result)


def is_valid_user(username, password):
    if not username:
        return False
    if not password:
        return False
    if len(password) < 6:
        return False
    return True

print(is_valid_user("admin", "secret"))
print(is_valid_user("", "secret"))
print(is_valid_user("admin", "abc"))
print(is_valid_user("admin", ""))

double = lambda x: x * 2
add = lambda x, y: x + y

print(double(5))
print(add(3, 4))



def screenshot(name, folder="./screenshots"):
    print(f"{folder}/{name}.png")

screenshot("login", "./custom")
screenshot("login", folder="./custom")

def outer():
    message = "Hello"
    def inner():
        print(message)
    inner()

outer()

results = [
    {"status": "pass", "duration": 2.1},
    {"status": "fail", "duration": 1.3},
    {"status": "pass", "duration": 3.5},
    {"status": "fail", "duration": 0.8},
]

total = 0
for r in results:
    total += r["duration"]

print(round(total, 1))
print(round(total / len(results), 2))

names = ["Alice", "Bob", "Charlie",
         "David", "Eve"]

result = [n for n in names if len(n) > 4]
print(result)

expected = ["Products", "Cart", "Checkout"]
actual   = ["Products", "Cart", "Checkoutt"]

for exp, act in zip(expected, actual):
    status = "✅" if exp == act else "❌"
    print(f"{status} {exp}")

tests = [
    {"id": "TC001", "priority": "high"},
    {"id": "TC002", "priority": "low"},
    {"id": "TC003", "priority": "high"},
    {"id": "TC004", "priority": "medium"},
]

grouped = {}
for test in tests:
    p = test["priority"]
    if p not in grouped:
        grouped[p] = []
    grouped[p].append(test["id"])

print(grouped)



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [num for num in numbers if num %3==0]
print(result)

words = ["apple", "banana", "cherry",
         "date", "elderberry"]

for i, word in enumerate(words):
    if i == 2:
        break
    print(word)



total = 0
count = 0
for n in [10, 20, 30, 40, 50]:
    if n > 25:
        total += n
        count += 1

print(total)
print(count)

data = [5, 3, 8, 1, 9, 2, 7, 4, 6]
minimum = data[0]
maximum = data[0]

for n in data:
    if n < minimum:
        minimum = n
    if n > maximum:
        maximum = n

print(minimum, maximum)