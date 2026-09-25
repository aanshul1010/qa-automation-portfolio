class Browserconfig:
    def __init__(self, browser: str, timeout :int =10):
        self.browser = browser
        self._timeout = timeout
        self._base_url = ''

    @property
    def timeout(self)->int:
        return self._timeout


    @timeout.setter
    def timeout(self, seconds:int)->None:
        if not isinstance(seconds, int):
            raise TypeError("timeout must be integer")
        if seconds< 1:
            raise ValueError("timeout miniumum is 1s")
        if seconds > 60:
            raise ValueError("timeout maximum is 60s")
        self._timeout = seconds
        print(f"timeout set to {seconds}")

    @timeout.deleter
    def timeout(self)->None:
        print("resetting timeout to default (10s)")
        self._timeout = 10

    @property
    def base_url(self)->str:
        return self._base_url

    @property
    def is_configured(self)->bool:
        return bool(self.browser and self._base_url)


if __name__ == "__main__":
    config = Browserconfig("chrome", 10)

    print(config.timeout)

    config.timeout= 20
    config.timeout = -39
    config.timeout = "fast"

    print(config.is_configured)

    del config.timeout
    print(config.timeout)
