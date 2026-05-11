from numpy.ma import count

test_steps = ["open browser", " visit login page", "enter details", "click on login "]
print(test_steps)
print("------------------------------------------------------------------------------------------")
test_case = [
    {"test_id": "tc001", "username": "standad_user", "password": "abcde"},
    {"test_id": "tc002", "username": "wronng_user", "password": "abcde"},
    {"test_id": "tc003", "username": "", "password": "abcde"}
]
print(test_case[0])
print(test_case[-1])
print(count(test_case))
print("----------------------------------------------------------------------")

test_cases = {"test_id": "tc001", "username": "standad_user", "password": "abcde"}

print(test_cases["username"])
test_cases.update({"browser": "chrome"})
print(test_cases)
print("----------------------------------------------------------------------")

browsers = ("firefox", "edge", "chrome")
print("------------------------------------------------------------------------------------------")

environment = ("staging", "qa", "prod")
print(environment[0])
# environment[0]= "test"

print("------------------------------------------------------------------------------------------")

print(browsers)
tags = {"smoke", "snaity", "regression", "smoke", "smoke"}
print(tags)
tags.update({"e2e"})
print(tags)
print("------------------------------------------------------------------------------------------")
test_tags={"smoke", "login", "regresioion"}
test_tags.add("smoke")
print(len(test_tags))
print("login" in test_tags)

#########################################################################################################################

def wait_for_element(locator, timeout):
    print(f"Waiting {timeout}s for {locator}")

wait_for_element("#login-btn", 10)
wait_for_element("#login-btn")


# WITH default — timeout is optional:
def wait_for_element(locator, timeout=10):
    print(f"Waiting {timeout}s for {locator}")

wait_for_element("#login-btn")
wait_for_element("#login-btn", 30)
wait_for_element("#login-btn", timeout=20)



def login(username, password,
          remember_me=False,
          browser="chrome",
          timeout=10):

    print(f"Browser : {browser}")
    print(f"User: {username}")
    print(f"Remember: {remember_me}")
    print(f"Timeout : {timeout}s")


login("standard_user", "secret_sauce")


login("standard_user", "secret_sauce", browser="firefox")


login("standard_user", "secret_sauce",
      remember_me=True, timeout=30)


