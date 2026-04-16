def login(username: str, password: str) -> bool:
    ''' Performoning login '''
    """ arguments are username and password return true if login is succesfull else false      """
    if username == "standard_user" and password == "secret_sauce":
        return True
    return False


result1 = login("standard_user", "secret_sauce")
result2 = login("wrong_user", "wrong_pass")
print(f"login 1 result is {result1}")
print(f"login 2 result is {result2}")


# why hint matters : it doesnt enforcce it communicates , whitout it , its unclear what to pass
def waiting(t):
    print(f"waiting {t}")


def waitfor(seconds: int) -> None:
    print(f"waiting for {seconds}")


waiting(12)
waitfor(255)


# Return types can be 1. str, 2. bool, 3.int, 4.list, 5. dic 6. none

# There are 5 types of parameters
# 1 MUT provied
def NavigateTo(url: str) -> None:
    print(f"navigating to {url}")


NavigateTo("www.something.com")


# 2  Default — optional, has fallback
def takeScreenshot(filename: str, folder: str = './screenshots') -> str:
    path = f"{folder}/{filename}.png"
    print(f"screenshot {path}")
    return path


screenshot1 = takeScreenshot("login_page")  # user default
screenshot2 = takeScreenshot("login_page", "./customs")  # use custom value


# 3  Keyword arguments — named when calling
def create_report(total: int, passed: int, failed: int, env: str = "staging") -> dict:
    rate = passed / total * 100 if total > 0 else 0
    return {"total": total, "passed": passed, rate: round(rate, 1), "env": env}


report = create_report(total=50, passed=25, failed=20, env="production")
print(f" Reports is {report}")


# 4 *args — any number of arguments
def log_steps(*steps: str) -> None:
    """ logs multpiple test steps in *args = tuple inside """
    print(" the test steps are ")
    for i, step in enumerate(steps, start=1):
        print(f" {i}. {step}")


log_steps("open browser", "navigagte to login", "add username and pasword", "verify producsts")


# 5 **kwargs — any number of named arguments

def configure(**settings) -> dict:
    """**kwargs becomes dictionary inside function"""
    defaults = {"browser": "chrome", "headless": False, "timeout": 10}
    defaults.update(settings)
    return defaults


cfg1 = configure(headless=True, timeout=20)
cfg2 = configure(browser="firefox")
print(f"\nConfig 1: {cfg1}")
print(f"Config 2: {cfg2}")
