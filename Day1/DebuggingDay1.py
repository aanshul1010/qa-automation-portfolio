# DEBUGGING CHALLENGE — DAY 1
# Find and fix all 5 bugs
# Write what each bug was as a comment above fix

products = [
    {"name": "Backpack", "price": 29.99},
    {"name": "Bike Light", "price": 9.99},
    {"name": "T-Shirt", "price": 15.99},
]
config = {
    "browser": "chrome",
    "timeout": 10,
    "environment": "staging"
}


def calculate_total(product_list):
    total = 0
    for product in product_list:
        total = total + product["price"]  # p was capital
    return total


def print_config(cfg):
    print("Browser: " + cfg["browser"])
    print( f"Timeout: {cfg['timeout']}")   # cannot concatenate integer and string
    print("Environment: " + cfg["environment"])  # it doesnt had ""


def run_summary():
    total = calculate_total(products)
    print(f"Total: ${total}")
    print(print_config(config))  # wrong funcion name


run_summary() # had wrong syntax