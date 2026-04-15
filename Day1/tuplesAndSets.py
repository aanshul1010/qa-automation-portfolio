
# --- TUPLES ---
# Like a list BUT cannot be changed after creation
# Use () instead of []
# WHY: For data that should NEVER change
#      Browser options, fixed config values
#      Returning multiple values from a function

supported_browsers = ("chrome","firefox", "edge")
print(f"Supported Browsers :{supported_browsers}")
print(f"first browser {supported_browsers[0]}")

# returning mutiple value from function =tuple
def get_test_info():
    return "Tc001", "Valid_login", "Hight"
tes_id, tes_name, priority =get_test_info()
print(f"\n Id: {tes_id}, Name : {tes_name}, priority : {priority}")

# SETS
# it is an unorderd collection of unique items
# why it is used : to find unique values, removing duplicates,
# without sets
tag_list = ["smoke", "login", "smoke", "regression","login"]
print(f"List with duplicates : {tag_list}")
#with sets
tag_sets = set(tag_list)
print(f" list without duplicates: {tag_sets}")

#real use case
all_failures = ["Tc001","Tc004","Tc007","Tc001","Tc004","Tc001","Tc005"]
unique_failures =set(all_failures)
print(f"uniquw faild test cases {unique_failures}")
print(f"number of unqiue failed test cases {len(unique_failures)}")

