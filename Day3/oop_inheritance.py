class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.title = ""

    def open(self) -> None:
        self.is_open = True
        print(f"Opening browser {self.browser}")
        print(f"Navigating to {self.url}")

    def close(self) -> None:
        self.is_open = False
        print(f"closing browser {self.browser}")


    def get_title(self):
        return self.title

    def take_screenshot(self, name: str) -> None:
        print(f" the screenshot is stored in {name}.png")

    def wait_for(self) -> None:
        print(f"waiting for {self.timeout}s")


class LoginPage(BasePage):
    def __init__(self, browser, url: str, timeout=10):
        super().__init__(browser, url, timeout)
        self.title = "Login page"
        print(f" login page is ready")

    def enter_username(self, username: str) -> None:
        print(f"entering username : {username} ")

    def enter_password(self, password: str) -> None:
        print(f"entering password : {'*' * len(password)} ")

    def click_login(self) -> None:
        print(f"Clicking on the element")

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


class CartPage(BasePage):
    def __init__(self, browser: str, url: str, timeout=10):
        super().__init__(browser, url, timeout)
        self.title = "Cart page"
        self.items = []
        print(f"opening cart page")

    def add_items(self, item) -> None:
        self.items.append(item)
        print(f"{item} added to cart")

    def remove_item(self, item) -> None:
        self.items.remove(item)
        print(f"{item} removed from the cart")

    def get_item_count(self) -> int:
        return len(self.items)

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    url = "www.google.com"

    login = LoginPage("Chrome", url)
    login.open()
    login.login("standard_user", "password")
    login.close()
    print(login.is_open)
    print("**************************************************************************************")
    cart =CartPage("Firefox", url)
    cart.open()
    cart.add_items("silver")
    print(cart.get_item_count())
    print(cart.is_empty())
    print(cart.is_open)


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    pass

dog = Dog("Rex")
cat = Cat("Whiskers")

dog.speak()
cat.speak()
print(dog.name)
print(cat.name)



class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def close(self):
        print(f"Closing {self.browser}")

class CheckoutPage(BasePage):

    def __init__(self, browser, total):
        super().__init__( browser)
        self.total = total

    def confirm_order(self):
        print(f"Order confirmed: ${self.total}")


page = CheckoutPage("chrome", 49.99)
page.confirm_order()
page.close()
print(page.total)