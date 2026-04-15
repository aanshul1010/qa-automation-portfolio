
# --- CREATING LISTS ---
# A list is an ordered collection. Order matters.
# Use square brackets []

usernames = ["standard_user", "locked_out_user",
             "problem_user", "performance_glitch_user"]

prices = [29.99, 9.99, 15.99, 49.99, 7.99]

test_steps = [
    "Open browser",
    "Go to login page",
    "Enter username",
    "Enter password",
    "Click login",
    "Verify products page"
]

# --- ACCESSING ITEMS ---
# Lists are ZERO-indexed (first item = position 0)
# WHY: This is how computers count — from 0, not 1

print(usernames[0])    # standard_user  (first)
print(usernames[1])    # locked_out_user (second)
print(usernames[-1])   # performance_glitch_user (last)
print(usernames[-2])   # problem_user (second from last)

# --- LENGTH ---
print(f"\nTotal users to test: {len(usernames)}")
print(f"Total test steps: {len(test_steps)}")

# --- LOOPING (Data-Driven Testing Pattern) ---
print("\n--- Running tests for all users ---")
for username in usernames:
    print(f"Testing login with: {username}")

# Loop with step number:
print("\n--- Test Execution Steps ---")
for step_number, step in enumerate(test_steps, start=1):
    print(f"  Step {step_number}: {step}")

# --- ADDING AND REMOVING ---
test_results = []   # empty list — fill as tests run

# Add results as tests complete:
test_results.append("TC001: PASS")
test_results.append("TC002: PASS")
test_results.append("TC003: FAIL")
test_results.append("TC004: PASS")

print(f"\nTest results collected: {test_results}")
print(f"Total results: {len(test_results)}")

# --- CHECKING IF ITEM EXISTS ---
failed_tests = ["TC003", "TC007", "TC012"]

if "TC003" in failed_tests:
    print("\nTC003 is in failed list — needs investigation")

if "TC001" not in failed_tests:
    print("TC001 passed — no action needed")

# --- SLICING (Getting a portion of a list) ---
all_products = ["Backpack", "Bike Light", "T-Shirt",
                "Fleece Jacket", "Onesie", "Red T-Shirt"]

first_three = all_products[:3]    # items 0, 1, 2
last_two = all_products[-2:]      # last 2 items
middle = all_products[2:4]        # items 2, 3

print(f"\nFirst three products: {first_three}")
print(f"Last two products: {last_two}")
print(f"Middle products: {middle}")

# --- SORTING ---
# WHY: Verifying products are sorted correctly on page
unsorted_prices = [49.99, 9.99, 29.99, 7.99, 15.99]
sorted_low_high = sorted(unsorted_prices)
sorted_high_low = sorted(unsorted_prices, reverse=True)

print(f"\nLow to high: {sorted_low_high}")
print(f"High to low: {sorted_high_low}")
