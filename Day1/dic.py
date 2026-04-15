# ============================================================
# File: day01/03_dictionaries.py
# ============================================================

# --- WHAT A DICTIONARY LOOKS LIKE ---
# Curly braces {}
# key: value pairs
# key is always a string (usually)
# value can be ANYTHING

# A single test case:
test_case = {
    "id": "TC001",
    "name": "Valid login test",
    "username": "standard_user",
    "password": "secret_sauce",
    "expected": "Prodcuts",
    "priority": "high",
    "status": "not_run"
}
# accesing values from dictionary
print(f"Test Id : {test_case['id']}")
print(f"Username : {test_case['username']}")
print(f"Expected : {test_case['expected']}")

# accesing with get
print(f"Browser : {test_case.get('browser', 'chrome')}")
# why are we using get method
# test_case['browser'] crahses if key is missing
# test_case.get('browser) returns none
# test_case.get('browser' , 'chrome') returns default

# modifying values in dic
test_case['status'] = 'running'
print(f"status updated to {test_case['status']}")
test_case['status'] = 'Passed'
print(f"status updated to {test_case['status']}")

# dictionary configuration/ operations
config = {
    "base_url": "https://www.saucedemo.com",
    "browser": "chrome",
    "headless": False,
    "timeout": 10,
    "retry_count": 2,
    "Screenshot_dir": "./screenshots",
    "reports": "./reports",
    "environment": "staging"
}
print(f"Running On {config['browser'].upper()}")
print(f"url : {config['base_url']}")
print(f"Environment : {config['environment'].upper()}")
print(f" timeouts {config['timeout']}s")

# List of dictionaries
login_tests = [
    {
        "id": "Tc001",
        'username': 'standard_user',
        'password': 'secret_sauce',
        'expected': 'products',
        'should_pass': True
    },
    {
        "id": "Tc002",
        'username': 'lockedout_user',
        'password': 'secret_sauce',
        'expected': 'locked_out',
        'should_pass': False
    },
    {
        "id": "Tc003",
        'username': '',
        'password': 'secret_sauce',
        'expected': 'username is required',
        'should_pass': False
    }
]

print("Test suit data")
for test in login_tests:
    print(f"\n [{test['id']}]")
    print(f"user : {test['username']}")
    print(f"Expected : {test['expected']}")
    print(f"should : { 'Pass' if test['should_pass'] else 'Fail'}")

# dic methods
print(f"Keys : {list(test_case.keys())}")
print(f"Values : {list(test_case.values())}")
