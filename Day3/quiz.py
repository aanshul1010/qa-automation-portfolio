from abc import ABC, abstractmethod

class BasePage(ABC):
    @abstractmethod
    def verify_page(self):
        pass

    @abstractmethod
    def get_title(self):
        pass

class LoginPage(BasePage):
    def verify_page(self):
        return True

page = LoginPage("chrome")
print(page.verify_page())