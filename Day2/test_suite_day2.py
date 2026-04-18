# DAY 2 — PROJECT FILE
# File: day02/test_suite_day2.py
# Applying Day 1 + Day 2 concepts together
# Website: SauceDemo — https://www.saucedemo.com

from typing import Optional

# confguration
config = {
    "base_url": "https://www.saucedemo.com",
    "browser": "chrome",
    "environment": "staging",
    "timeout": 10,
    "retry_count": 2,
    "headless": False,
    "report_dir": "./reports"
}

# test data
users = {
    "valid": {"username": "standard_user", "password": "secret_sauce"},
    "locked": {"username": "locked_out_user", "password": "secret_sauce"},
    "invalid": {"username": "wrong_user", "password": "wrong_pass"},
    "empty_user": {"username": "", "password": "secret_sauce"},
    "empty_pass": {"username": "standard_user", "password": ""},
}

products = [
    {"id": "P001", "name": "Sauce Labs Backpack",
     "price": 29.99, "in_stock": True},
    {"id": "P002", "name": "Sauce Labs Bike Light",
     "price": 9.99, "in_stock": True},
    {"id": "P003", "name": "Sauce Labs Bolt T-Shirt",
     "price": 15.99, "in_stock": True},
    {"id": "P004", "name": "Sauce Labs Fleece Jacket",
     "price": 49.99, "in_stock": True},
    {"id": "P005", "name": "Sauce Labs Onesie",
     "price": 7.99, "in_stock": True},
]


# CORE FUNCTIONS (Simulated — Real browser calls in Week 2)
def simulate_login(username: str, password: str) -> dict:
    """simulate login return result dic """
    if not username:
        return {"success": False, "message": "username is required", "page": "login "}
    if not password:
        return {"success": False, "message": "password is required", "page": "login "}
    if username == "locked_out_user":
        return {"success": False, "message": "sorry this user is locked", "page": "login "}

    valid = {"standard_user": "secret_sauce", "problem_user": "secret_sauce", "performance_glitch_user": "secret_sauce"}

    if username in valid and valid[username] == password:
        return {"success": True, "message": "login succesful", "page": "products"}

    return {"success": False, "message": "username  and password don not match", "page": "login "}


def simultate_add_to_cart(product_id: str, prodcut_list: list) -> dict:
    """simulate adding product to cart """
    product_ids = [p["id"] for p in prodcut_list]

    if product_id:
        return {"success": False, "message": "product id cannot be empty"}
    if product_id not in product_ids:
        return {"success": False, "message": "product id cannot be empty"}
    product = next(p for p in prodcut_list if p["id"] == product_id)

    return {"success": True, "message": f"{product['name']} added to cart", "product": product}


def calculate_order_total(cart_items: list, tax_rate: float = 0.08) -> dict:
    """calculates order toal with tacx """
    if not cart_items:
        return {"success": False,
                "message": "Cart is empty",
                "subtotal": 0,
                "tax": 0,
                "total": 0}

    subtotal = sum(item["price"] for item in cart_items)
    tax = round(subtotal * tax_rate, 2)
    total = round(subtotal + tax, 2)

    return {
        "success": True,
        "subtotal": round(subtotal, 2),
        "tax": tax,
        "total": total,
        "items": len(cart_items)
    }

# helper functions
def print_header(title:str, subtitle: str = "") ->None:
    "prints formatted section header"
    print(f"\n {'='*60}")
    print(f"{title}")
    if subtitle:
        print(f"{subtitle}")
    print(f"{'='*60}")


def print_test_result(test_id: str, description: str, passed:  bool, detail : str='')->bool:
    "prit test result and resturns pass or fail bool"
    icon = "✅ PASS" if passed else "❌ FAIL"
    print(f"\n{icon} | {test_id}  | {description}")
    if detail:
        print(f" {detail}")
    return passed

def print_suite_summary(suite_name: str, passed: int, failed:int)->None:
    "prints suite level summary "
    total = passed +failed
    rate = (passed / total * 100) if total > 0 else 0
    status = "All Passed " if failed ==0 else " FAILED"
    print(f" \n {suite_name} : " 
          f"{passed}/{total} passed ({rate: .0f}%) - {status}")

# test suite
def test_login_suite()-> tuple:
    "TC-1 -5 login test "
    print_header("login test suite ", f"URL : {config['base_url']}")
    test_cases = [
        {
            "id": "TC001",
            "desc": "Valid login — standard user",
            "user": users["valid"],
            "expect": "Products",
            "field": "page"
        },
        {
            "id": "TC002",
            "desc": "Locked out user",
            "user": users["locked"],
            "expect": "locked out",
            "field": "message"
        },
        {
            "id": "TC003",
            "desc": "Empty username field",
            "user": users["empty_user"],
            "expect": "Username is required",
            "field": "message"
        },
        {
            "id": "TC004",
            "desc": "Empty password field",
            "user": users["empty_pass"],
            "expect": "Password is required",
            "field": "message"
        },
        {
            "id": "TC005",
            "desc": "Invalid credentials",
            "user": users["invalid"],
            "expect": "do not match",
            "field": "message"
        },

    ]
    passed = failed = 0
    for tc in test_cases:
        result = simulate_login(
            tc['user']['username'],
            tc["user"]["password"]
        )
        assertion = tc["expect"].lower() in \
                    result[tc["field"]].lower()
        detail = (f"expected '{tc['expect']}' in "
                  f"{tc['field']}='{result[tc['field']]}'")
        if print_test_result(tc["id"], tc["desc"], assertion,detail):
            passed +=1
        else:
            failed +=1
    print_suite_summary("login suite", passed, failed)
    return passed, failed

def test_cart_suite() -> tuple:
    " tc 06 - 09 cart tests"
    print_header("Cart test suite ")

    test_cases = \
        [
         {
             "id": "TC006",
             "desc": "Add valid product to cart",
             "product_id": "P001",
             "should_pass": True
         },
         {
             "id": "TC007",
             "desc": "Add another valid product",
             "product_id": "P003",
             "should_pass": True
         },
         {
             "id": "TC008",
             "desc": "Add non-existent product",
             "product_id": "P999",
             "should_pass": False
         },
         {
             "id": "TC009",
             "desc": "Add with empty product ID",
             "product_id": "",
             "should_pass": False
         },
     ]
    passed = failed =0
    for tc in test_cases:
        result = simultate_add_to_cart(
            tc["product_id"], products
        )
        assertion = result["success"] == tc["should_pass"]
        detail = result["message"]

        if print_test_result(tc["id"], tc["desc"],
                             assertion, detail):
            passed += 1
        else:
            failed += 1

    print_suite_summary("Cart Suite", passed, failed)
    return passed, failed


    passed = failed = 0




def test_order_total_suite() -> tuple:
    """TC010–TC013: Order calculation tests."""
    print_header("ORDER TOTAL TEST SUITE")

    cart_with_items = [products[0], products[2]]
    # Backpack (29.99) + T-Shirt (15.99) = 45.98

    test_cases = [
        {
            "id": "TC010",
            "desc": "Calculate total for 2 items",
            "cart": cart_with_items,
            "expected_total": 49.66,
            "should_pass": True
        },
        {
            "id": "TC011",
            "desc": "Empty cart returns zero total",
            "cart": [],
            "expected_total": 0,
            "should_pass": False
        },
        {
            "id": "TC012",
            "desc": "Single item total calculation",
            "cart": [products[0]],
            "expected_total": 32.39,
            "should_pass": True
        },
        {
            "id": "TC013",
            "desc": "All products total calculation",
            "cart": products,
            "expected_total": 123.64,
            "should_pass": True
        },
    ]

    passed = failed = 0

    for tc in test_cases:
        result = calculate_order_total(tc["cart"])
        assertion = result["success"] == tc["should_pass"]

        detail = (f"total=${result['total']} | "
                  f"expected=${tc['expected_total']} | "
                  f"success={result['success']}")

        if print_test_result(tc["id"], tc["desc"],
                             assertion, detail):
            passed += 1
        else:
            failed += 1

    print_suite_summary("Order Suite", passed, failed)
    return passed, failed

# MASTER RUNNER

def run_all_tests() -> None:
    """Runs all test suites. Prints full report."""
    print("\n" + "🔥 " * 15)
    print("  DAY 2 — QA AUTOMATION PORTFOLIO")
    print(f"  Site        : {config['base_url']}")
    print(f"  Environment : {config['environment'].upper()}")
    print("🔥 " * 15)

    all_passed = 0
    all_failed = 0

    for suite in [test_login_suite,
                  test_cart_suite,
                  test_order_total_suite]:
        p, f = suite()
        all_passed += p
        all_failed += f

    total = all_passed + all_failed
    rate = (all_passed / total * 100) if total > 0 else 0

    print("\n" + "=" * 60)
    print("  📊 FINAL REPORT — DAY 2")
    print("=" * 60)
    print(f"  Total  : {total}")
    print(f"  ✅ Pass : {all_passed}")
    print(f"  ❌ Fail : {all_failed}")
    print(f"  Rate   : {rate:.1f}%")
    print("=" * 60)
    status = ("🎉 GREEN — All passed!"
              if all_failed == 0
              else "🚨 RED — Failures found!")
    print(f"  Build  : {status}")
    print("=" * 60)


if __name__ == "__main__":
    run_all_tests()


