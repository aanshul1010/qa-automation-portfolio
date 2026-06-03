def calculate_pass_rate(passed, total) -> float:
    return round((passed / total) * 100, 2)


def get_failed_tests(results) -> list:
    failed_tests = []

    for result in results:
        if result["status"] == "fail":
            failed_tests.append(result["id"])

    return failed_tests


def print_report(report) -> None:
    print("\n=== TEST REPORT ===")

    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":

    results = [
        {"id": "TC001", "status": "pass"},
        {"id": "TC002", "status": "fail"},
        {"id": "TC003", "status": "pass"},
        {"id": "TC004", "status": "fail"},
        {"id": "TC005", "status": "pass"},
    ]

    passed = 0

    for result in results:
        if result["status"] == "pass":
            passed += 1

    total = len(results)

    pass_rate = calculate_pass_rate(passed, total)

    failed_tests = get_failed_tests(results)

    report = {
        "total_tests": total,
        "passed": passed,
        "failed": len(failed_tests),
        "pass_rate": pass_rate,
        "failed_tests": failed_tests
    }

    print_report(report)


# Q: What happens when you run test_suite.py directly?
# A: The code inside:
#    if __name__ == "__main__":
#    will execute.
#    So run_all() will run automatically.


# Q: What happens if another file imports test_suite?
# A: The functions and variables from test_suite.py
#    become available to use, but run_all()
#    will NOT execute automatically.


# Q: Why is this important for automation frameworks?
# A: It prevents test execution from starting automatically
#    when files are imported into other modules.
#    This helps keep automation frameworks modular,
#    reusable, and easier to control.


q1 # a) When a file is run directly:
__name__ == "__main__"


# b) When a file is imported by another file:
__name__ == "filename"
# Example:
# If the file name is test_suite.py
# then:
__name__ == "test_suite"
q2 Running utils.py directly → prints Total: 60
Importing utils.py from another file → only imports the function, no extra code runs automatically.

q3 def run_all_tests():
    print("Running all tests...")

def generate_report():
    print("Generating report...")

if __name__ == "__main__":
    run_all_tests()
    generate_report()
q4 # a) Functions defined in a file run
#    automatically when the file is imported.
# FALSE
# Functions only run when they are called.


# b) Code inside if __name__ == "__main__"
#    runs when the file is imported.
# FALSE
# That block only runs when the file is executed directly.


# c) __name__ equals "__main__" only when
#    the file is run directly.
# TRUE


# d) You can have multiple
#    if __name__ == "__main__" blocks.
# TRUE
# Python allows it, though usually one block is preferred.

q5 # page_objects.py

class LoginPage:

    def enter_username(self):
        pass

    def enter_password(self):
        pass

    def click_login(self):
        pass


# Test the page object only when this file
# is run directly
if __name__ == "__main__":

    print("Testing LoginPage...")

    login = LoginPage()

    login.enter_username()
    login.enter_password()
    login.click_login()

    print("LoginPage test complete.")