class loginPage:
    def verify_page(self)->bool:
        print(f'Verifying login page of astra')
        return True

    def get_title(self):
        print(f'lOGIN Page')

class ProductPage:
    def verify_page(self)->bool:
        print(f'Verifying product page of astr')
        return True

    def get_title(self)->bool:
        print(f'Product Page')

class CartPage:
    def verify_page(self):
        print(f'Verifying cart page of astra')
        return False

    def get_title(self):
        print(f'Cart Page')


def Alldetails(polys)->None:
    for n in polys:
        result =n.verify_page()
        n.get_title()
        print(f"Result : {result}")
        if result == True:
            print("Pass")
        else:
            print("Fail")

ploys=[loginPage(), ProductPage(), CartPage()]
Alldetails(ploys)

class WebTest:
    def run(self):
        print(f"this is webtes")

class APITest:
    def run(self):
        print(f"this is api test ")

class DatabaseTest:
    def run(self):
        print(f"this is database test")

def execute_all(tests:list):
    for r in tests:
        r.run()

tests=[WebTest(), DatabaseTest(), APITest()]
execute_all(tests)

