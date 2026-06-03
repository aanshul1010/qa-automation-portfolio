class BasePage:
    def __init__(self, browser: str, url: str, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.title = ""

    def open(self):
        print(f"opening the {self.browser}")
        print(f"navigating to {self.url}")

    def close(self):
        print(f"Closing the browser")

    def get_title(self):
        return self.title

    def verify_page(self) -> bool:
        print(f"verifying page -: {self.title}")
        return True


class LoginPage(BasePage):
    def __init__(self, browser: str, url: str, timeout=10):
        super().__init__(browser, url, timeout)
        self.title = "Login page"

    def open(self) -> None:
        super().open()
        print(f" login form loaded ")

    def verify_page(self) -> bool:
        super().verify_page()
        print(f"checking login form")
        print(f"checking username field")
        print(f"checking password field")
        return True

    def login(self, username: str, password: str):
        self.username = username
        print(f"entering username : {username} ")
        self.password = password
        print(f"entering password : {'*' * len(password)} ")


class CartPage(BasePage):
    def __init__(self, browser: str, url: str, timeout=10):
        super().__init__(browser, url, timeout)
        self.title = "your cart"
        self.items = []

    def verify_page(self) -> bool:
        if len(self.items) > 0:
            print(f"{len(self.items)} found")
            return True
        print(f" no items found in cart")
        return False

    def add_item(self, item) -> None:
        self.items.append(item)

    def get_count(self) -> int:
        n = len(self.items)
        print(f"the number of items in cart are : {n}")


if __name__ == "__main__":
    url = "www.google.com"
    login = LoginPage("chrome", url)
    login.open()
    login.login("standard user", "asdfgh")
    login.verify_page()

    Cart = CartPage("firefox", url)
    Cart.add_item("blackbox")
    Cart.verify_page()

    print(f" login title :{login.get_title()}")
    print(f" cart title: {Cart.get_title()}")

print("\n" + "*" *30 +"\n")

class Vehicle:
    def start(self):
        print("Vehicle starting...")

    def describe(self):
        print("I am a vehicle")

class Car(Vehicle):
    def start(self):
        super().start()
        print("Car engine running 🚗")

class Truck(Vehicle):
    def start(self):
        print("Truck starting LOUD 🚛")

v = Vehicle()
c = Car()
t = Truck()

v.start()
print("---")
c.start()
print("---")
t.start()
print("---")
c.describe()
t.describe()

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def get_info(self):
        return f"Browser: {self.browser}"

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.title = "Login"

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Page: {self.title}"

page = LoginPage("chrome")
print(page.get_info())


class BasePage:
    def verify(self) -> bool:
        print("Base verification")
        return True

class CheckoutPage(BasePage):
    def verify(self) -> bool:
        # Run parent verification first:
        super().verify()
        # Add checkout specific check:
        print("Verifying payment form...")
        print("Verifying total amount...")
        return True

page = CheckoutPage()
result = page.verify()
print(result)