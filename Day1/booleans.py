# ============================================================
# File: day01/01_booleans.py
# ============================================================

# --- WHAT BOOLEANS LOOK LIKE ---
# Note: True and False ALWAYS start with capital letter
is_logged_in = False
is_element_visible = True
test_passed = True
cart_is_empty = False

# --- WHY BOOLEANS MATTER IN AUTOMATION ---

# Controlling test flow:
if is_logged_in:
    print("User is logged in — proceed to test")
else:
    print("User not logged in — login first")

# Assertions (the heart of testing):
expected = "Products"
actual = "Products"
assertion_result = (actual == expected)  # This IS a boolean
print(f"\nAssertion passed: {assertion_result}")


# WHY THIS MATTERS in automation:
username = ""   # empty string = falsy

if username:    # same as: if username != ""
    print("Username entered")
else:
    print("Username is empty — show error")
    # This is how you validate form fields!

# Another real example:
test_results = []   # empty list = falsycd

if test_results:
    print(f"Found {len(test_results)} results")
else:
    print("No test results yet — suite hasn't run")