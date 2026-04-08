url = "https://www.saucedemo.com"
username = "standard_user"
password = "secret_sauce"
locator = "login-button"
xpath = "//input[id ='user-name']"

print("basic stirngs")
print(url)
print(username)

# string and integer
age_string = "24"
age_number = 24

print(" string vs integer ")
print(type(age_string))
print(type(age_number))
print(age_number + 188)

# string operations
page_title = "product_page"
username_raw = "STANDARD_user"
test_url = "https://www.saucedemo.com/inventory.html"
error_msg = "Epic sadface: Username is required"

print(f"berfore strip :{page_title}")
print(f"after strip : {page_title.strip()}")

print(f"original username: {username_raw}")
print(f"lowerd case username : {username_raw.lower()}")

staging_url = test_url.replace("www", "staging")
print(f" original url :{test_url}")
print(f"stanging url : {staging_url}")

url_parts =  test_url.split("/")
print(f" spilts into parts:{url_parts}")

print(f"username error : {'username' in error_msg}")
print(f"password error : {'password' in error_msg}")

passw = "secret_sauce"
print(f"the length of password is {len(passw)}")
print(f" if password length is min 8 characters : {len(passw)>=8}")





