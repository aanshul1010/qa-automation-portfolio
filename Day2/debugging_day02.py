# ============================================================
# DEBUGGING CHALLENGE — DAY 2
# 6 bugs hidden. Find them all.
# ============================================================

test_data = [
    {"id": "TC001", "username": "standard_user",
     "password": "secret_sauce", "expected": "Products"},
    {"id": "TC002", "username": "locked_out_user",
     "password": "secret_sauce", "expected": "locked out"},
    {"id": "TC003", "username": "",
     "password": "secret_sauce", "expected": "Username"},
]

def simulate_login(username, password):
    if not username:
        return "Username is required"
    if not password:
        return "Password is required"
    if username == "locked_out_user":
        return "Sorry, this user has been locked out"
    if username == "standard_user" and password == "secret_sauce": # missing :
        return "Products"
    return "Credentials do not match"


def run_tests(data):
    passed = 0
    failed = 0

    for test in data:
        result = simulate_login(
            test["username"],
            test["password"]
        )

        if test["expected"].lower() in result.lower(): # founf L but the method is in small letters lower()
            passed += 1
            print(f"✅ PASS: {test['id']}")
        else:
            failed = failed - 1
            print(f"❌ FAIL: {test['id']}")

    total = passed + failed  # found == but it should be = as is assignment operator but == is equality operator
    print(f"\nTotal: {passed} passed, {failed} failed")
    print(f"Pass rate: {passed/total*100}%")


run_tests(test_data)