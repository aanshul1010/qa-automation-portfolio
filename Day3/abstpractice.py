from abc import ABC, abstractmethod

class BasePage(ABC):
    @abstractmethod
    def verify_page(self) -> bool:
        print("Running base verification...")
        return True

class Loginpage(BasePage):
    def verify_page(self) -> bool:
        super().verify_page()
        print("login page is running")

login =Loginpage()
login.verify_page()