# ============================================================
# File: day01/01_none.py
# ============================================================

# --- WHAT NONE LOOKS LIKE ---
driver = None          # browser not launched yet
test_result = None     # test hasn't run yet
error_message = None   # no error yet

# --- WHY WE CHECK FOR NONE ---
# If you try to USE something that is None,
# your script CRASHES with AttributeError

# WRONG — will crash:
# driver.get("https://saucedemo.com")  # ERROR: None has no .get()

# RIGHT — check first:
if driver is None:
    print("Driver not ready — run setup() first")
else:
    print("Driver ready — proceeding with test")

# --- REAL AUTOMATION PATTERN ---
def get_error_message(login_failed: bool) -> str:
    """Returns error message if login failed, None if success."""
    if login_failed:
        return "Epic sadface: Username is required"
    return None   # No error = return None

# Using it:
result = get_error_message(False)

if result is None:
    print("✅ Login successful — no error message")
else:
    print(f"❌ Login failed: {result}")

# Always use 'is None' — not '== None'
# WHY: 'is' checks identity, '==' checks value
#      'is None' is the professional Python standard