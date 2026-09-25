#without encapsulation  no security anyone can change it
class Login:
    def __init__(self, url, title, ):
        self.url =url
        self.title= title
        self.username =""
        self.password =""

login = Login('wwwjpjfpjpf', "amase")
login.username ="ashdohas"
login.password ="aosdsh"
print(login.title)
print(login.username)
print(login.password)

# protected

class powder:
    def __init__(self, cloth, shoes, belt,):
        self.cloth = cloth
        self._shoes = shoes
        self.belt = belt
        self._ring = 50

power= powder("shirt", "bata", "gucci")
print(power._shoes)
print(power._ring)
power._ring = 855
print(power._ring)


# PROTECTED in inheritance — real example:

class BasePage:
    def __init__(self, browser: str):
        self.browser  = browser      # public
        self._driver  = None         # protected
        self._timeout = 10           # protected

    def _find_element(self,
                      locator: str):
        """
        Protected method.
        Child classes use this internally.
        Tests should never call this directly.
        """
        print(f"Finding: {locator}")
        return f"element_{locator}"


class LoginPage(BasePage):
    def __init__(self, browser: str):
        super().__init__(browser)

    def enter_username(self,
                       username: str) -> None:
        # Child class USES protected method:
        element = self._find_element(username)
        print(f"Typing {username} in {element}")

    def enter_password(self,
                       password: str) -> None:
        # Child class USES protected timeout:
        print(f"Waiting {self._timeout}s")
        element = self._find_element(password)
        print(f"Typing in {element}")


# LoginPage CAN use _find_element ✅
# LoginPage CAN use _timeout ✅
# Tests SHOULD NOT call _find_element directly
login = LoginPage("chrome")
login.enter_username("abc")
login.enter_password("dkadblasbld")
login._timeout =789
print(login._timeout)

# private double underscore
class browsersession:
    def __init__(self):
        self.__apikey= "secretkey"
        self.__password = "scecretpassword"

session = browsersession()
print(session._browsersession__apikey) #user underscore +classname+attributename

class BrowserSession:
    def __init__(self):
        self.__api_key = "sk-secret-123"

    def get_session_info(self) -> dict:
        """Public method — controlled access."""
        return {
            "connected": True,
            # Does NOT expose api_key
        }

    def authenticate(self) -> bool:
        """Uses private key internally."""
        if self.__api_key.startswith("sk-"):
            return True
        return False

sess= BrowserSession()
print(sess.get_session_info())
print(sess.authenticate())


class BasePage:
    """
    Real Page Object base class.
    Shows exactly how access levels
    are used in professional frameworks.
    """

    def __init__(self, browser: str,
                 url: str):

        # PUBLIC — tests can read these:
        self.browser     = browser
        self.page_title  = ""
        self.is_loaded   = False

        # PROTECTED — child pages use these:
        self._driver     = None    # WebDriver
        self._timeout    = 10      # wait time
        self._base_url   = url

        # PRIVATE — this class only:
        self.__session_token = ""
        self.__auth_header   = {}

    # PUBLIC — tests call this:
    def open(self) -> None:
        self._initialize()    # uses protected
        self.is_loaded = True
        print(f"Page opened: {self.browser}")

    # PUBLIC — tests call this:
    def get_title(self) -> str:
        return self.page_title

    # PROTECTED — child pages call this:
    def _find_element(self, locator: str):
        print(f"Finding: {locator}")
        return locator

    def _wait_for(self, locator: str) -> None:
        print(f"Waiting {self._timeout}s "
              f"for {locator}")

    # PRIVATE — this class only:
    def __initialize(self) -> None:
        self._driver = f"{self.browser}_driver"
        self.__session_token = "abc123"

    def _initialize(self) -> None:
        self.__initialize()    # calls private


class LoginPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)
        self.page_title = "Login Page"

    def enter_username(self,
                       username: str) -> None:
        # Uses PROTECTED method from BasePage:
        self._wait_for("#username")
        element = self._find_element("#username")
        print(f"Typing: {username}")

    def login(self, username: str,
              password: str) -> None:
        self.enter_username(username)
        self._find_element("#password")
        self._find_element("#login-btn")
        print("Login complete")


# ── IN YOUR TEST FILE ───────────────────────
if __name__ == "__main__":
    page = LoginPage(
        "chrome", "https://saucedemo.com"
    )

    # Tests use PUBLIC interface only:
    page.open()                           # ✅
    page.login("standard_user", "pass")  # ✅
    print(page.get_title())              # ✅
    print(page.is_loaded)                # ✅
    print(page.browser)                  # ✅

    # Tests NEVER do:
    # page._driver          ← bad practice
    # page.__session_token  ← blocked
    # page._find_element()  ← internal method