class Basepage:
   def __init__(self, browser: str, url: str, timeout: int =10):
       self.browser = browser
       self.url =url
       self.timeout = timeout
       self.title =""
       print(f" base page inititaliexzed at {browser}")

   def open(self)-> None:
       print(f" opening {self.browser}")
       print(f"Navigating to {self.url}")

   def get_title(self):
       return self.title

   def take_screenshot(self, name: str)->None:
       print(f"Screenshot {name}.png saved")

   def close(self):
       print(f"closing {self.browser}")

   def wait_for_element(self, locator: str)-> None:
       print(f" waiting for {self.timeout}s"
          f" for {locator}")

class LoginPage(Basepage):
    def __init__(self, browser: str, url: str, timeout: int =10):
        super().__init__(browser, url, timeout)
        self.title ="Login page "
        print(f"lLogin page ready")

    def enter_username(self, username:str)-> None:
        print(f" Entering username : {username}")

    def enter_password(self, password:str)-> None:
        print(f"Entering password {'*'*len(password)}")

    def click_login(self)->None:
        print("clicking login button")

    def login(self, username:str, password: str)->None:
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

class ProductsPage(Basepage):
    def __init__(self, browser: str,url: str, timeout=10):
        super().__init__(browser, url, timeout)
        self.title = "Products"
        self.products = []
        print(f" Products page is ready")

    def add_to_cart(self, product:str)->None:
        self.products.append(product)
        print(f" added {product} to cart")

    def get_cart_count(self)-> int:
        return  len(self.products)

    def sortby(self, option: str)-> None:
        print(f"Sorting by: {option}")


if __name__ == "__main__":
        url = "www.scauedemo.com"

        login = LoginPage("chrome", url)
        login.open()
        login.login("standard_user", "bkjbk")
        login.take_screenshot("login")
        login.close()
        print("\n" +"=" * 40 + "\n")
        products = ProductsPage("Firefox", url)
        products.open()
        products.add_to_cart("Bakpack")
        products.take_screenshot("cart")
        print(products.get_title())
        products.close()











