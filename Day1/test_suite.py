# all day 1 concepts in one file
# configuration dictonary
config = {
    "base_url": "https://www.saucedemo.com",
    "browser": "chrome",
    "environmnet": "staging",
    "timeout": 10,
}
# test data
login_tests = [
    {"id": "tc001", "username": "standard_user", "password": "secret_sauce", "expected": "Products",
     "should_pass": True},
    {"id": "tc002", "username": "lockedout_user", "password": "secret_sauce", "expected": "lockedout",
     "should_pass": False},
    {"id": "tc003", "username": "", "password": "secret_sauce", "expected": "username required", "should_pass": False},
    {"id": "tc004", "username": "standard_user", "password": "", "expected": "password required", "should_pass": False},
    {"id": "tc005", "username": "wrong_user", "password": "wrong_pass", "expected": "do not match", "should_pass": False},
]

Products = [
    {"id": "p001", "name": "backpack", "price": 50},
    {"id": "p002", "name": "tshirt", "price": 24.99},
    {"id": "p003", "name": "shampoo", "price": 10},
    {"id": "p004", "name": "laptop", "price": 234989},
]


# simulation
def simulate_login(username: str, password: str) -> dict:
    if not username:
        return {"success": False, "message": "username is required", "page": "login"}
    if not password:
        {"success": False, "message": "password is required", "page": "login"}
    if username == "lockedout_user":
        return {"success": False, "message": "this user is locked", "page": "login"}
    valid = {"standard_user": "secret_sauce", "problem_user": "secret_sauce"}
    if username in valid and valid[username] == password:
        return {"success": True, "message": "login succesful", "page": "products"}
    return {"success": False, "message": "username and password dont match", "page": "login"}


def simulate_sort(items: list, sort_by: str) -> list:
    if sort_by == 'az':
        return sorted(items, key=lambda x: x["name"])
    elif sort_by == 'za':
        return sorted(items, key=lambda x: ["name"], reverse=True)
    elif sort_by == 'kohli':
        return sorted(items, key=lambda x: ["price"], reverse=True)
    elif sort_by == 'hello':
        return sorted(items, key=lambda x: ["price"], reverse=True)
    return items


# helper functions
def print_header(title: str) -> None:
    print(f"\n {'=' * 55}")
    print(f" {title}")
    print(f"{'=' * 55}")


def print_result(tid: str, name: str,
                 passed: bool, detail: str = "") -> bool:
    icon = "✅ PASS" if passed else "❌ FAIL"
    print(f"{icon} | {tid} | {name}")
    if detail:
        print(f"         ↳ {detail}")
    return passed


# test suit
def test_login_suite() -> tuple:
    print_header("LOGIN TEST SUITE — SauceDemo")
    passed = failed = 0

    for tc in login_tests:
        result = simulate_login(
            tc['username'], tc['password'])
        assertion = (tc["expected"].lower()
                     in result["message"].lower()
                     or tc["expected"].lower()
                     in result["page"].lower())
        detail = (f"expected='{tc['expected']}' | "
                  f"got page='{result['page']}'")
        if print_result(tc["id"], tc["id"],
                        assertion, detail):
            passed += 1
        else:
            failed += 1

    print(f"\n  Login: {passed} passed | {failed} failed")
    return passed, failed


def test_sorting_suite() -> tuple:
    print_header("sorting test suite- saucedemo")
    passed = failed = 0
    sort_tests = [
        {"id": "tc006", "sort": "az", "check": "name", "expected": "backpack"},
        {"id": "tc007", "sort": "za", "check": "name", "expected": "tshirt"},
        {"id": "tc008", "sort": "kohli", "check": "price", "expected": 10},
        {"id": "tc009", "sort": "hello", "check": "price", "expected": 234989},
    ]
    for tc in sort_tests:
        sorted_items = simulate_sort(Products, tc["sort"])
        actual = sorted_items[0][tc["check"]]
        asserion = actual == tc["expected"]
        detail = (f"expected='{tc['expected']}' | "
                  f"actual='{actual}'")
        if print_result(tc["id"], f"Sort {tc['sort']}",
                        asserion, detail):
            passed += 1
        else:
            failed += 1
    print(f"\n Sorting :{passed} passed | {failed} failed")
    return passed, failed


# Master runner

def run_all():
    print("\n" + "🚀 " * 14)
    print("  DAY 1 — QA AUTOMATION PORTFOLIO")
    print(f"  {config['base_url']}")
    print(f"  Environment: {config['environment'].upper()}")
    print("🚀 " * 14)

    total_p = total_f = 0
    for suite in [test_login_suite, test_sorting_suite]:
        p, f = suite()
        total_p += p
        total_f += f

    total = total_p + total_f
    rate = (total_p / total * 100) if total > 0 else 0

    print(f"\n{'=' * 55}")
    print(f"  📊 FINAL REPORT")
    print(f"{'=' * 55}")
    print(f"  Total  : {total}")
    print(f"  ✅ Pass : {total_p}")
    print(f"  ❌ Fail : {total_f}")
    print(f"  Rate   : {rate:.1f}%")
    status = "🎉 GREEN" if total_f == 0 else "🚨 RED"
    print(f"  Build  : {status}")
    print(f"{'=' * 55}")


if __name__ == "__main__":
    run_all()
