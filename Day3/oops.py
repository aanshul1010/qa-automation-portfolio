class login_page:
    pass


page1 = login_page
page2 = login_page
page3 = login_page

print(type(page1))
print(page1)
print(page2)
print(page1 == page2)


class Login:
    def __init__(self, url, browser):
        self.url = url
        self.browser = browser
        self.is_open = False

    def __str__(self):
        return f" {self.browser}, {self.is_open} , {self.url}"

    def get_info (self)-> dict:
        return {
            "url":self.url,
            "browser": self.browser,
            "is_open": self.is_open
        }




chrome_page = Login("www.pppp.com", "chrome",)
fire = Login("www.xfn.com", "firefox")
print(chrome_page)
print(chrome_page.get_info())