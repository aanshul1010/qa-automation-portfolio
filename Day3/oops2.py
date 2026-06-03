class Login_Page:
    def __init__(self, url, browser: str, timeout: int = 10):
        self.url = url
        self.browser = browser
        self.timeout = timeout
        self.username = ""
        self.password = ""

    def open(self) -> None:
        self.is_open = True
        print(f"opening {self.browser}")
        print(f"navigating to {self.url}")

    def enter_username(self, username: str) -> None:
        self.username = username
        print(f"the user name is {self.username}")

    def enter_password(self, password: str) -> None:
        self.password = password
        print(f"entering password {self.password}")

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)

    def get_current_url(self) -> str:
        return self.url

    def close(self) -> None:
        self.is_open = False
        print(f"closing {self.browser}")


page = Login_Page("https://saucedemo.com", "chrome")
page.open()
page.login("standard_user", "abcdef")
print(f" brwoser name {page.browser}")
print(f"current url {page.get_current_url()}")
page.close()
print("\n ")
page1= Login_Page("https://saucedemo.com", "edge")
page1.open()
page1.login("some_user", "ab654646546f")
print(f" brwoser name {page1.browser}")
print(f"current url {page1.get_current_url()}")
page1.close()