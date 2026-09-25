from abc import ABC, abstractmethod

class BasePage(ABC):
    def __init__(self, browser:str,url:str):
        self.browser = browser
        self.url =url
        self.is_loaded = False

    def open(self)->None:
        self.is_loaded =True
        print(f"Opening {self.browser}")
        print(f"Navigating to {self.url}")

    def close(self)->None:
        self.is_loaded=False
        print(f"Closing {self.browser}")

    def take_screenshot(self, name:str)->None:
        print(f"Screenshot : {name}.png saved")

    @abstractmethod
    def verify_page(self)->bool:
        """Every page MUST return its title."""
        pass

    @abstractmethod
    def get_url(self)->str:
        """Every page MUST return its URL."""
        pass

    @abstractmethod
    def get_page_title(self) -> str:
        """Every page MUST return its title."""
        pass

class LoginPage(BasePage):
    def __init__(self, browser:str, url:str):
        super().__init__(browser,url)
        self.title = "login page "

    def verify_page(self) ->bool:
        print("checking username ")
        print("checking password")
        print("checking login button")
        return True

    def get_page_title(self)->bool:
        return self.title

    def get_url(self) ->str:
        return self.url

    def login(self, username:str, password:str)->None:
        print(f"logining in as {username}")




class CartPage(BasePage):
    def __init__(self, browser:str, url:str):
        super().__init__(browser,url)
        self.title = "your CART Myloard"
        self.items =[]

    def verify_page(self) ->bool:
        if not self.items:
            print("cart is empty")
            return False
        print(f"{len(self.items)}items in cart")
        return True

    def get_page_title(self) -> str:
        return self.title

    def get_url(self) ->str:
        return self.url

    def add_items(self, item:str)->None:
        self.items.append(item)
        print(f"ADDED : {item}")

    def get_count(self):
        return len(self.items)


if __name__ =="__main__":
    url = "www.google.com"
    login = LoginPage("chrome", url)
    login.open()
    login.verify_page()
    print(login.get_page_title())
    login.take_screenshot("login")
    login.close()

    print("\n" + "=" * 40 + "\n")

    cart = CartPage("edge", url)
    cart.open()
    print(f"Verify emoty : {cart.verify_page()}")
    cart.add_items("phone")
    cart.add_items("belt")
    print(cart.get_count())
    print(f"Verifyiing items : {cart.verify_page()}")
    cart.close()
    base= BasePage("chrome","www.mouse.com")
    base.verify_page()







