

def count_duplicate(test_ids: list)-> list:
    id_count = {}
    for test_id in test_ids:
        id_count[test_id] = id_count.get(test_id, 0) +1

    duplicates = [
        test_id
        for test_id, count in id_count.items()
    if count > 1
      ]

    return duplicates

def run_dsa_test():
    print("=" *55)
    print(" dsa problem 1 find duplicates ")
    print("=" *55)

    test_cases =[

        {
            "input": ["TC001", "TC002",
                      "TC001", "TC003", "TC002"],
            "expected": ["TC001", "TC002"],
            "desc": "Multiple duplicates"
        },
        {
            "input": ["TC001", "TC002", "TC003"],
            "expected": [],
            "desc": "No duplicates"
        },
        {
            "input": [],
            "expected": [],
            "desc": "Empty list"
        },
        {
            "input": ["TC001"],
            "expected": [],
            "desc": "Single item"
        },
        {
            "input": ["TC001", "TC001", "TC001"],
            "expected": ["TC001"],
            "desc": "Same ID three times"
        },
    ]
    passed =0
    failed =0
    for i , tc in enumerate(test_cases, start =1):
        result= count_duplicate(tc["input"])

        assertion = sorted == sorted (tc["expected"])
        icon = "✅ PASS" if assertion else "❌ FAIL"
        print(f"\n{icon} Test {i}: {tc['desc']}")
        print(f"       Input    : {tc['input']}")
        print(f"       Expected : {tc['expected']}")
        print(f"       Got      : {result}")

        if assertion:
            passed += 1
        else:
            failed += 1

    print(f"\n{'=' * 55}")
    print(f"  Results: {passed} passed | {failed} failed")
    print(f"{'=' * 55}")


if __name__ == "__main__":
    run_dsa_test()

