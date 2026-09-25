class LoginPage:
    def __init__(self, url:str):
        self._username =""
        self._password = ""
        self._timeout = 10
        self._url = url

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,users:str):
        if not users :
            raise ValueError("Username cannot be empty")
        if len(users)<=3:
            raise ValueError("username must be more than 3 characters")

        self._username = users
        print(f"username is {users}")

    @property
    def password(self)->None:
        return "*" *len(self._password)


    @password.setter
    def password(self, Pass:str):
        if not Pass:
            raise ValueError("password cannot be empty")
        if len(Pass)<6:
            raise ValueError("password length must be more than 6 characters")
        self._password= Pass
        print(f"password is {'*'*len(Pass)}")

    @property
    def timeout(self)->int:
        return self._timeout

    @timeout.setter
    def timeout(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Timeout must be integer")
        if seconds < 1:
            raise ValueError("Minimum 1 second")
        if seconds > 30:
            raise ValueError("Maximum 30 seconds")
        self._timeout = seconds  # ✅ store in _timeout
        print(f"Timeout set to {seconds}s")

    @timeout.deleter
    def timeout(self):
        print("setting timeout to defualt value")
        self.timeout =10

    @property
    def url(self):
        return self._url

if __name__ == "__main__":

    page = LoginPage("https://saucedemo.com")

    print("=== USERNAME ===")
    page.username = "mycircle"
    print(f"Username: {page.username}")

    try:
        page.username = ""
    except ValueError as e:
        print(f"❌ {e}")

    try:
        page.username = "ab"
    except ValueError as e:
        print(f"❌ {e}")

    print("\n=== PASSWORD ===")
    page.password = "secret_sauce"
    print(f"Password: {page.password}")

    try:
        page.password = "abc"
    except ValueError as e:
        print(f"❌ {e}")

    print("\n=== TIMEOUT ===")
    page.timeout = 20
    print(f"Timeout: {page.timeout}")

    try:
        page.timeout = 0
    except ValueError as e:
        print(f"❌ {e}")

    try:
        page.timeout = 90
    except ValueError as e:
        print(f"❌ {e}")

    try:
        page.timeout = "fast"
    except TypeError as e:
        print(f"❌ {e}")

    del page.timeout
    print(f"After delete: {page.timeout}")

    print("\n=== URL READ-ONLY ===")
    print(f"URL: {page.url}")

    try:
        page.url = "https://evil.com"
    except AttributeError as e:
        print(f"❌ {e}")








