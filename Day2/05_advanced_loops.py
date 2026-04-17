products = [
    {"name": "Backpack", "price": 29.99, "in_stock": True},
    {"name": "light", "price": 9.99, "in_stock": True},
    {"name": "tshirt", "price": 49.99, "in_stock": False},
    {"name": "jacket", "price": 50.99, "in_stock": True},
    {"name": "socks", "price": 2.99, "in_stock": False}
]

test_results = [
    {"id": "TC001", "status": "pass", "duration": 2.3},
    {"id": "TC002", "status": "fail", "duration": 1.1},
    {"id": "TC003", "status": "pass", "duration": 3.9},
    {"id": "TC004", "status": "fail", "duration": 2.8},
    {"id": "TC005", "status": "pass", "duration": 1.9}
]

# PATTERN 1: enumerate() — Loop with index
# WHY: Step numbers in test reports, tracking position

print("Test execution log ")
for step, product in enumerate(products, start=1):
    print(f"step {step} verifying [{product['name']}]")

# PATTERN 2: Filtering in loops
# WHY: Run only high-priority tests, only failed tests, etc.

print("============ failed tests only ================")
for result in test_results:
    if result["status"] == "fail":
        print(f" {result['id']}  Failed " 
              f"(duration: {result['duration']}s)")

print(" \n ========= In stock products only ===========")

for product in products:
    if product['in_stock']:
        print(f" {product['name']} - ${product['price']}")


# PATTERN 3: Aggregating in loops
# WHY: Counting pass/fail, summing totals, building reports

total_duration=0
pass_count=0
fail_count =0
failed_test_ids =[]

for result in test_results:
    total_duration+= result['duration']
    if result['status']== 'pass':
        pass_count+=1
    else:
        fail_count+=1
        failed_test_ids.append(result['id'])

print(f" \n ========== suite summary ===============")
print(f" paseed   : {pass_count}")
print(f" failed   : {fail_count}")
print(f" total duration    : {total_duration :.1f}s")
print(f" failedtest ids   : {failed_test_ids}")

# PATTERN 4: List Comprehension — Python's superpower
# WHY: Cleaner, faster, professional standard

# without list comprehension
failed_ids_old =[]
for result in test_results:
    if result['status'] == 'fail':
        failed_ids_old.append(result['id'])

# WITH list comprehension (professional way):
# Read as: "give me result['id'] FOR EACH result
#           IN test_results IF status is fail"


failed_ids_new =[r['id'] for r in test_results
                 if r['status'] == 'fail']

print(f"\n failed ids : {failed_ids_old}")
print(f"failed ids : {failed_ids_new}")

all_price = [p ["price"] for p in products]
expensive =[p['name'] for p in products if p['price']>20]
name_upper = [p['name'].upper() for p in products]

print(f"\nAll prices    : {all_price}")
print(f"Expensive (20+): {expensive}")
print(f"Names upper   : {name_upper}")


# PATTERN 5: zip() — Loop through TWO lists together
# WHY: Comparing expected vs actual values in assertions

expected_titles = ["products", 'your cart', "checkout", "order complete"]
actual_title =["products", "your cart", "checkout", "order complete"]

print("\n ==================== page title assertioins =================")

for expected, actual in zip (expected_titles, actual_title):
    match = expected == actual
    icon = "✅" if match else "❌"
    print(f" {icon} expecetd : {expected} | actual : {actual}")


# PATTERN 6: break and continue — Flow control in loops

# continue - skips iteration and keep looping
print("\n-------------------------- skipping disabled test --------------")
all_tests =[
    {"id": "Tc001", "enabled": True},
    {"id": "Tc002", "enabled": False},
    {"id": "Tc003", "enabled": True},
    {"id": "Tc004", "enabled": False},
    {"id": "Tc005", "enabled": True},
]

for test in all_tests:
    if not test["enabled"]:
        print(f"skiping disbaled test :{test['id']}")
        continue
    print(f" Running {test['id']}")

# break stop loop entrirely

print("\n ================= stop on first critical failure =============")
critical_tests=[
     {"id": "TC001", "critical": True,  "passed": True},
     {"id": "TC002", "critical": True,  "passed": True},
     {"id": "TC003", "critical": True,  "passed": False},
     {"id": "TC004", "critical": True,  "passed": True},
     {"id": "TC005", "critical": False,  "passed": True}
 ]

for test in critical_tests:
    if test['critical'] and not  test['passed']:
        print(f" critical test {test['id']} failed "
              f"stopping suite immediately")
        break
    print(f"{test['id']} passed ")

