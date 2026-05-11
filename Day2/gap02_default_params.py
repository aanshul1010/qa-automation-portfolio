# TASK 1: navigate_to() function
def navigate_to(url, browser="chrome", headless=False, timeout=10):
    """Navigate to a URL with specified browser and options."""
    print(f"url: {url}")
    print(f"browser: {browser}")
    print(f"headless: {headless}")
    print(f"timeout: {timeout}")




# Task 1 - Call 1: Only url
print("\n--- Task 1, Call 1: Only url ---")
navigate_to("https://example.com")


# Task 1 - Call 2: url + browser="firefox"
print("\n--- Task 1, Call 2: url + browser='firefox' ---")
navigate_to("https://example.com", browser="firefox")


# Task 1 - Call 3: url + headless=True + timeout=30
print("\n--- Task 1, Call 3: url + headless=True + timeout=30 ---")
navigate_to("https://example.com", headless=True, timeout=30)




# TASK 2: create_test_report() function
def create_test_report(total, passed, failed, environment="staging", send_email=False):
    """Create a test report with pass rate calculation."""
    pass_rate = (passed / total) * 100
    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "pass_rate": pass_rate,
        "environment": environment,
        "send_email": send_email
    }




# Task 2 - Call 1: create_test_report(10, 9, 1)
print("\n--- Task 2, Call 1: create_test_report(10, 9, 1) ---")
result1 = create_test_report(10, 9, 1)
print(result1)


# Task 2 - Call 2: create_test_report(10, 10, 0, environment="production")
print("\n--- Task 2, Call 2: create_test_report(10, 10, 0, environment='production') ---")
result2 = create_test_report(10, 10, 0, environment="production")
print(result2)


# Task 2 - Call 3: create_test_report(5, 3, 2, send_email=True)
print("\n--- Task 2, Call 3: create_test_report(5, 3, 2, send_email=True) ---")
result3 = create_test_report(5, 3, 2, send_email=True)
print(result3)




# TASK 3: take_screenshot() function
def take_screenshot(test_id, folder=None):
    """Take a screenshot and save it to the specified folder."""
    if folder is None:
        folder = "./screenshots"
    print(f"Screenshot saved: {folder}/{test_id}.png")




# Task 3 - Call 1: take_screenshot("TC001")
print("\n--- Task 3, Call 1: take_screenshot('TC001') ---")
take_screenshot("TC001")


# Task 3 - Call 2: take_screenshot("TC002", "./custom_folder")
print("\n--- Task 3, Call 2: take_screenshot('TC002', './custom_folder') ---")
take_screenshot("TC002", "./custom_folder")


