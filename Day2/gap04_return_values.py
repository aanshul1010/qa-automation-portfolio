# understanding concept of return types and void functiona and value function
# void functions are
def click_login_button() -> None:
    print("login cutton is clicked")


def naviagte_to(url: str) -> str:
    print(f"user has navigated to the {url} ")


def take_screenshot(name: str) -> str:
    print(f"the screenshot file is {name}.png")


# value functions

def get_page_titile() -> str:
    return "products"


def is_logged_in() -> bool:
    return True


def get_cart_count() -> int:
    return 9


def get_test_result(test_id: str) -> dict:
    return {"id": {test_id}, "status": {"pass"}}


click_login_button()
naviagte_to("https:someting.com")
take_screenshot("login_test")

title = get_page_titile()
loggedin = is_logged_in()
count = get_cart_count()
test_result = get_test_result("tcoo1")

print(f"tile is {title}")
print(f" logged in  {loggedin}")
print(f" count {count}")
print(f"test result {test_result}")

#------------------------------------------------------------------------------------------------------------------------
# TASK 1:
# Write these 6 functions with correct
# return types and type hints:

def open_browser(browser: str):
    print(f"Opening {browser}")

def naviagte_to(url: str) -> str:
    return url

def get_current_url(url: str) -> str:
    current_url = url
    return url


def enter_text(field: str, text: str) -> str:
    print(f"Typing {text} in {field}")


def is_element_visible(element_id: str) -> bool:
    if element_id == "login-button":
        return True
    else:
        return False


def get_all_products(products: list) -> list:
    return products


def calculate_pass_rate(passed: int, total: int) -> float:
    result = round(passed / total * 100)
    return result


open_browser("chrome")
urls = get_current_url("www.something.com")
print(f"url is {urls}")
enter_text("username", "abcdef")
element = is_element_visible("login-button")
print(f"element present {element}")
products = get_all_products(["a", "b", "c"])
print(f"products are {products}")
passed = calculate_pass_rate(100, 200)
print(f"passed rate: {passed}")
print("----------------------------------------------------------------------------------------")

# task 3
url = "www.foxtrot.com"
browser = "firefox"
element_id = "login-button"
def run_login_test():
    open_browser("chrome")
    naviagte_to(url)
    get_current_url(url)
    is_element_visible(element_id)
    calculate_pass_rate(100,200)
    # Print test report
    print(f"url is {urls}")
    print(f"element present {element}")
    print(f"passed rate: {passed}")

run_login_test()

def is_logged_in() -> bool:
    return True

def run_test():
    is_logged_in()    # line A
    status = print("hello")  # line B
    return status

result = run_test()
print(result)

# What is wrong with line A?
# What does line B actually store?