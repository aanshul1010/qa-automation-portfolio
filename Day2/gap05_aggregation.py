test_results = [
    {"id": "TC001", "status": "pass", "duration": 2.3},
    {"id": "TC002", "status": "fail", "duration": 1.1},
    {"id": "TC003", "status": "pass", "duration": 3.7},
    {"id": "TC004", "status": "fail", "duration": 0.9},
    {"id": "TC005", "status": "pass", "duration": 4.2},
]

# pattern 1 counting
passed = 0
failed = 0
for result in test_results:
    if result["status"] == "pass":
        passed += 1
    else:
        failed += 1

print(f"passed : {passed} | failed : {failed}")

# pattern 2 Summing
total_duration = 0
for duration in test_results:
    total_duration += duration["duration"]

print(f" total duration is {total_duration}")

#pattern 3 collecting

failed_ids =[]
for result in test_results:
    if result["status"] == "fail":
        failed_ids.append(result["id"])
print(f" The failed ids are {failed_ids}")

#pattern 4 grouping
grouped = {"pass":[], "fail": []}
for result in test_results:
    grouped[result["status"]].append(result["id"])
print(f" total passed an failed {grouped}")


results = [
    {"id": "TC001", "status": "pass", "duration": 1.2},
    {"id": "TC002", "status": "fail", "duration": 2.4},
    {"id": "TC003", "status": "pass", "duration": 0.8},
    {"id": "TC004", "status": "pass", "duration": 3.1},
    {"id": "TC005", "status": "fail", "duration": 1.5},
    {"id": "TC006", "status": "pass", "duration": 2.2},
]
def generate_report(results:list)->dict:
    passed = 0
    failed = 0
    total_duration = 0
    failed_ids = []
    passed_ids=[]
    slowest_test = results[0]
    fastest_test = results[0]

    for result in results:
        total_duration += result["duration"]
        if result["status"] == "pass":
            passed += 1
        else:
            failed += 1
            failed_ids.append(result["id"])

    total = passed + failed
    pass_rate = round((passed / total) * 100, 2)

    for test in results:
        if test["status"] == "fail":
            failed_ids.append(test["id"])
        else:
            passed_ids.append(test["id"])


    for test in results:
        if test["duration"] > slowest_test["duration"]:
            slowest_test = test

        if test["duration"] < fastest_test["duration"]:
            fastest_test = test

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": pass_rate,
        "total_duration": round(total_duration, 1),
        "failed_id": failed_ids,
        "passed_ids": passed_ids,
        "Slowest_test": slowest_test,
        "Fastest_test": fastest_test
    }


report = generate_report(results)
print(f"\n=== TEST REPORT ===")
for key, value in report.items():
    print(f"  {key}: {value}")

print("----------------------------------------------------------------------------------------------------------------")

products = [
    {"name": "Backpack",  "price": 29.99, "category": "bags"},
    {"name": "Bike Light","price": 9.99,  "category": "accessories"},
    {"name": "T-Shirt",   "price": 15.99, "category": "clothing"},
    {"name": "Jacket",    "price": 49.99, "category": "clothing"},
    {"name": "Onesie",    "price": 7.99,  "category": "clothing"},
]

grouped_products = {}

for product in products:
    category = product["category"]
    name = product["name"]

    # Create category if not present
    if category not in grouped_products:
        grouped_products[category] = []

    # Add product name to category list
    grouped_products[category].append(name)

print(grouped_products)





tests = [
    {"id": "TC001", "status": "pass", "priority": "high"},
    {"id": "TC002", "status": "fail", "priority": "high"},
    {"id": "TC003", "status": "fail", "priority": "low"},
    {"id": "TC004", "status": "pass", "priority": "medium"},
    {"id": "TC005", "status": "fail", "priority": "high"},
    {"id": "TC006", "status": "pass", "priority": "high"},
    {"id": "TC007", "status": "fail", "priority": "medium"},
    {"id": "TC008", "status": "pass", "priority": "low"},
]

high_failed_count = 0
high_failed_ids = []

for test in tests:
    if test["status"] == "fail" and test["priority"] == "high":
        high_failed_count += 1
        high_failed_ids.append(test["id"])

print("High Priority Failed Count:", high_failed_count)
print("High Priority Failed IDs:", high_failed_ids)