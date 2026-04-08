# ============================================================
# File: day01/01_numbers.py
# ============================================================

# --- INTEGER (whole numbers) ---
timeout = 10          # seconds to wait
max_retries = 3       # how many times to retry
cart_count = 2        # items in cart
total_tests = 14      # number of test cases

# --- FLOAT (decimal numbers) ---
product_price = 29.99
tax_rate = 0.08       # 8% tax
pass_rate = 95.5      # percentage

# --- MATH IN AUTOMATION ---
# Calculating order total:
price = 29.99
quantity = 2
tax = 0.08

subtotal = price * quantity
tax_amount = subtotal * tax
total = subtotal + tax_amount

print(f"Price per item : ${price}")
print(f"Quantity       : {quantity}")
print(f"Subtotal       : ${subtotal:.2f}")
print(f"Tax (8%)       : ${tax_amount:.2f}")
print(f"Total          : ${total:.2f}")

# :.2f means "show 2 decimal places"
# WHY: $29.990000001 looks wrong in a test report
#      $29.99 looks right

# --- USEFUL FOR TEST REPORTS ---
passed = 12
failed = 2
total = passed + failed
pass_percentage = (passed / total) * 100

print(f"\nTest Results:")
print(f"Passed  : {passed}")
print(f"Failed  : {failed}")
print(f"Total   : {total}")
print(f"Pass %  : {pass_percentage:.1f}%")

# --- COMPARISON (used in assertions) ---
expected_price = 29.99
actual_price = 29.99

print(f"\nPrice assertion: {actual_price == expected_price}")
print(f"Cart not empty : {cart_count > 0}")
print(f"Tests all pass : {failed == 0}")