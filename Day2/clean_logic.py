# BAD VERSION - messy nested loop
def validate_login_bad(username, password, is_active, role):
    if username:
        if password:
            if is_active:
                if role == "admin" or role == "tester":
                    return "access granted "
                else:
                    return "invalid role "
            else:
                return "account inactive"
        else:
            return "password required"
    else:
        return "username requireed"


# this is caleed arrow code

# Good version - Early returns flat structure ,
# handle failures first return early, happy path at bottom

def validate_login(username: str, password: str, is_active: bool, role: dict) -> str:
    print("=============================write failures first =======================================")
    if not username:
        return "username required"
    if not password:
        return "password required"
    if not is_active:
        return "account inactive"
    print("===================valid roles=============================================")
    valid_roles = ["admin", "tester", "manager"]
    if role not in valid_roles:
        return f"invalid role : {role}"

    return f"access granted for {role}: {username}"


# test it
print(validate_login("", "pass", True, "admin"))
print(validate_login("user", "", True, "admin"))
print(validate_login("user", "pass", False, "admin"))
print(validate_login("user", "pass", True, "hr"))
print(validate_login("user", "pass", True, "admin"))


# ----------------------------------------------------------------------------------------------
# real automation example - asserting test results cleanly
# ----------------------------------------------------------------------------------------------

def assert_page_loaded(page_title: str, expected_title: str, test_id: str) -> bool:
    titles_match = page_title.strip().lower() == \
                   expected_title.strip().lower()
    if titles_match:
        print(f" [{test_id}] page assertion passed")
        f"{page_title}"
        return True
    print(f" {test_id} page assertion failed")
    print(f" expecetd : {expected_title}")
    print(f" Actual : {page_title}")
    return False


print()
assert_page_loaded("Products", "products", "TC001")
assert_page_loaded("products", "Products", "TC002")
assert_page_loaded("login_page", "Products", "TC003")

# Ternary operator one line if else
#why cleaner for simple true or false

#withour ternay
passed =9
failed =0

if failed ==0:
    build_status="Green"
else:
    build_status="Red"
# with ternary
build_status = "Green" if failed ==0 else "Red"
print(f"\n build status {build_status}")

total = passed+failed
result_label = "Pass" if passed == total else "fail"
priority_flag = " High" if failed>3 else "Medium "\
    if failed>0 else "low "

print(f"Result {result_label}")
print(f"priority {priority_flag}")

