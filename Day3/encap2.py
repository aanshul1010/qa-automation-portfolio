class WebDriverConfig:
    def __init__(self, browser: str, environment: str):
        self.browser = browser
        self.environment = environment

        self._timeout = 10
        self._baseurl = "www.g.com"

        self.__credentials = {"username": "", "password": ""}

    def set_timeout(self, seconds: int) -> None:
        if seconds < 1:
            print("time out must be atleast 1")
            return

        if  seconds > 30:
            print("timeout cannot exceed 30 ")
            return

        self._timeout = seconds
        print(f"time out is set to {seconds}s")

    def get_timeout(self) -> int:
        return self._timeout

    def set_credentials(self, username: str, password: str) -> None:
        if not username:
            print("❌ Username cannot be empty")
            return
        if not password:
            print("❌ Password cannot be empty")
            return
        if len(password) < 6:
            print("❌ Password min 6 characters")
            return
        self.__credentials =\
            {
                "username": username,
                "password": password
            }

    def get_username(self):
        return self.__credentials["username"]

    def connect(self) -> None:
        print(f"Connecting {self.browser} "
              f"to {self._baseurl}")
        print(f"Environment: {self.environment}")
        print(f"Timeout: {self._timeout}s")
        print("✅ Connection established")


if __name__ == "__main__":
    webdriver = WebDriverConfig("chrome", "production")
    webdriver.set_timeout(12)
    webdriver.set_timeout(0)
    webdriver.set_credentials("standarduser", "122345")
    print(f"username: {webdriver.get_username()}")
    webdriver.connect()
    print(webdriver._WebDriverConfig__credentials)
