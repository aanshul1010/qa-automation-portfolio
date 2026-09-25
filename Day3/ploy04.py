class TestResult:
    def __init__(self, test_id, status, duration):
        self.test_id = test_id
        self.status = status
        self.duration = duration

    def __str__(self) -> str:
        return f"{self.test_id} , {self.status}, {self.duration}"

    def __repr__(self) -> str:
        return (f"TestResult ( "
                f"{self.test_id} , {self.status}, {self.duration} )")

    def __eq__(self, other):
        if not isinstance(other, TestResult):
            return False
        return (self.test_id == other.test_id and self.status == other.status)

    def __lt__(self, other) -> bool:
        return self.duration < other.duration


class TestSuite:
    def __init__(self, name: str):
        self.name = name
        self.cases = []

    def add(self, other):
        self.cases.append(other)

    def __len__(self) -> int:
        return len(self.cases)

    def __contains__(self, test_id: str) -> bool:
        return any(t.test_id == test_id for t in self.cases)

    def __getitem__(self, index:int):
        return self.cases[index]


r1 = TestResult("tc001", "pass", 2.60)
r2 = TestResult("tc001", "fail", 1.2)
suite = TestSuite("login test")
suite.add(r1)
suite.add(r2)


print(r2)
print(r1 == r2)
print(repr(r2))
print(r2 == "tc001 , pass, 2.60")
print(sorted([r1, r2]))
print(len(suite))
if suite:
    print("suite has tests")

if not suite:
    print("suite is empty")

print("tc001" in suite)
print(suite[0])