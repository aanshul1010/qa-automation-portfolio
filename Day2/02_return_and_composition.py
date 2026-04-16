#Return types
# 1. Returns nothing
def click_button(button_id:str)->None:
    print(f"clicking {button_id}")

#2 Return single value
def get_page_title()->str:
    return "products"    #real driver.title

def get_cart_count()->int:
    return 2

def is_logged_in()->bool:
    return True

#retrun multiple values
def run_suite()->tuple:
    passed, failed =8,1
    rate=round(passed/(passed+failed)*100,1)
    return passed, failed, rate

def verify_login(username:str, password:str)->dict:
    if not username:
        return {"success" :False, "message":"username is required","page":"login", "user":None }
    if not password:
        return {"success" :False, "message":"password is required","page":"login", "user":None }
    if username == "standard_user" and \
            password =="secret_sauce":
        return {"success" :True, "message":"login succesful ","page":"login", "user":username }
    return {"success" :False, "message":"doesnt match","page":"login", "user":None }

# Using return values;
titile = get_page_title()
count =get_cart_count()
logged =is_logged_in()
print(f"title {titile} cart {count} loggedin {logged}")

p, f, rate =run_suite()
print(f"passed {p}, failed :{f}, Rate :{rate}%")

result =verify_login("standard_user", "secret_sauce")
if result["success"]:
    print(f" logged in : {result['user']}, {result['page']}")
else:
    print(f"failed {result['message']}")

# Functions calling functions
# this is how automatioin frameworks are built
#small funcion - called by medium functions, called by large functions

# Small functions , each does one thing

def open_browser(browser:str = 'chrome')->str:
    print(f"opening {browser}")
    return f"{browser}_driver"

def go_to_url(driver :str, url: str)->None:
    print(f"{driver} {url}")

def type_in_field(driver:str, feild:str, text:str)->None:
    print(f"[{driver}] typing {text} in {feild}")

def click(driver :str, element: str)->None:
    print(f"{driver} Clicking {element}")

def get_page(driver: str) -> str:
    return "Products"    # simulated

def close(driver: str) -> None:
    print(f"[{driver}] Browser closed.")

# Medium calls smaller functions
def perform_login (username:str, password:str)->dict:
    """complete login flow using small functions"""
    driver =open_browser()
    go_to_url(driver, "https://www.saucedemo.com")
    type_in_field(driver, "username",  username)
    type_in_field(driver, "password", password)
    click(driver,"login_button")
    page =get_page(driver)
    return {"success" :page =="products", "page": page, "driver":driver}

# larger function calling medium functions
def run_all_login_test()->None:
    """run all login tests """
    tests=[("standard_user",  "secret_sauce",  True),
        ("locked_out_user","secret_sauce",  False),
        ("",               "secret_sauce",  False),]
    print("=============login suite===============")
    for username, password, expected in tests:
        result =perform_login(username, password)
        passed =result["success"] ==expected
        print(print(f"{'✅' if passed else '❌'} "
              f"user='{username}' → {result['page']}"))

run_all_login_test()