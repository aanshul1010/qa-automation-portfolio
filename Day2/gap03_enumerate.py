test_steps =["open browser", "enter url", "enter username", "enter password", "login successful"]
i=0
for step in test_steps:
    i = i+1
    print(f"{i} : {step}")

for step_num , step in enumerate(test_steps, start=1):
    print(f"steps {step_num} :---> {step} ")

test_results = [
    {"id": "TC001", "status": "pass"},
    {"id": "TC002", "status": "fail"},
    {"id": "TC003", "status": "pass"},
]

print("\nTest Execution Report:")
for num, result in enumerate(test_results, start=1):
    icon = "✅" if result["status"] == "pass" else "❌"
    print(f"  {num}. {icon} {result['id']} — {result['status']}")
# -------------------------------------------------------------------------------------------------


#TASK 1:
#You have this list of browsers:
browsers = ["chrome", "firefox", "edge", "safari"]
for steps, browser in enumerate(browsers, start=1):
    print(f"Browser {steps} : {browser}")

#You have test results:
resultsing = [
    {"id": "TC001", "status": "pass", "duration": 2.3},
    {"id": "TC002", "status": "fail", "duration": 1.1},
    {"id": "TC003", "status": "pass", "duration": 3.7},
    {"id": "TC004", "status": "fail", "duration": 0.9},
]

for nums, resul in enumerate(resultsing, start=1):
    icon = "✅" if resul["status"] == "pass" else "❌"
    print(f"{nums} {icon} {resul['id']} -{resul['status']} ({resul['duration']})")



#TASK 3:
#You have test steps as a list.
##ONLY the step number and name
#where the word "click" appears.

steps = [
    "Open browser",
    "Navigate to login page",
    "Enter username",
    "Enter password",
    "Click login button",
    "Verify page title",
    "Click add to cart",
    "Verify cart count"
]
for num, stp in enumerate(steps, start=1):
    if "Click" in stp :
        print(f"Step {num} contains click : {stp}")

steps = ["Login", "Search", "Add to cart"]

for num, step in enumerate(steps, start=1):
    print(f"Step {num}:{step}")

#Write code using enumerate that:
#→ Prints each test case with its number
#→ If the number is even → print "EVEN TEST"
#→ If the number is odd → print "ODD TEST"

cases = ["TC001", "TC002", "TC003",
         "TC004", "TC005"]
for num , case in enumerate(cases, start=1):
    if (num%2 ==0) :
        print(f" {num}. {case}- 'Even test' ")
    else:
        print(f" {num}. {case}- 'Odd test' ")