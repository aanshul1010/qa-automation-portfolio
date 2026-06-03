class Product_page:
    def __init__(self, url, browser, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.products = ["apple", "banana", "orange"]
        self.is_loaded = False
        self.sortby = "price"

    def loads(self):
        self.is_loaded= True
        print(f"product page loaded on {self.browser}")

    def get_products(self)-> list:
        return self.products

    def get_cart_count(self)-> int:
        return len(self.products)

    def sort_products(self,
                      sort_by: str = "price") -> None:
        print(f"Sorting products by {sort_by}")

    def add_product_to_cart(self,
                            product_name: str) -> None:
        self.products.append(product_name)
        print(f"Adding '{product_name}' to cart")



if __name__ == "__main__":

    # Object 1 — Chrome:
    chrome = Product_page(
        "https://saucedemo.com", "chrome"
    )
    print(f"Loaded: {chrome.is_loaded}")  # False
    chrome.loads()
    print(f"Loaded: {chrome.is_loaded}")  # True
    chrome.add_product_to_cart("Backpack")
    chrome.add_product_to_cart("T-Shirt")
    print(f"Products: {chrome.get_products()}")
    print(f"Cart count: {chrome.get_cart_count()}")
    chrome.sort_products("az")

    print("\n" + "="*40 + "\n")

    # Object 2 — Firefox:
    firefox = Product_page(
        "https://saucedemo.com", "firefox",
        timeout=20
    )
    firefox.loads()
    firefox.add_product_to_cart("Onesie")
    print(f"Cart count: {firefox.get_cart_count()}")
    firefox.sort_products("price")

class TestSuite:
    def __init__(self, name, total_tests):
        self.name = name
        self.total = total_tests
        self.passed = 0
        self.failed = 0

suite = TestSuite("Login Tests", 10)
print(suite.name)
print(suite.total)
print(suite.passed)

