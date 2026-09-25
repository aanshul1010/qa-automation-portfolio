class TestCase:
    def __init__(self, test_id: str, name: str, priority: str, status: str):
        self.test_id = test_id
        self.name = name
        self.priority = priority
        self.status = "pending"

    def __str__(self) -> str:
        return (f"TestSuite: {self.test_id} | "
                f"{self.name} | "
                f"{self.priority} | "
                f"{self.status}")

    def __repr__(self) -> str:
        return (f"TestCase(test_id ={self.test_id}"
                f"name = {self.name} "
                f"status= {self.status} "
                f"priority ='{self.priority}')")

    def __eq__(self, other) -> bool:
        if not isinstance(other, TestCase):
            return False
        return (self.test_id == other.test_id and
                self.status == other.status)

    def __lt__(self, other) -> bool:
        order = {"high": 1, "medium": 2, "low": 3}
        return order[self.priority] < order[other.priority]


class TestSuite:

    def __init__(self, name: str):
        self._cases = []
        self.name = name

    def __len__(self) -> int:
        return len(self._cases)

    def __str__(self) -> str:
        high_no = sum(1 for c in self._cases
                      if c.priority == "high")
        return (f"Suite:{self.name} |"
                f" {len(self._cases)} tests |"
                f" {high_no} high priority")

    def __contains__(self, test_id) -> bool:
        return any(t.test_id == test_id
                   for t in self._cases)

    def __getitem__(self, index: int) -> TestCase:
        return self._cases[index]

    def add(self, result: TestCase) -> None:
        self._cases.append(result)


if __name__ == "__main__":
    T1 = TestCase("TC001", "login", "high", "pending")
    T2 = TestCase("TC002", "product", "low", "pending")
    T3 = TestCase("TC003", "cart", "high", "pending")
    T4 = TestCase("TC004", "landing", "low", "pending")

print("\n=== SORTED BY PRIORITY ===")
sorted_cases = sorted([T1, T2, T3, T4])
for c in sorted_cases:
    print(c)


    print(T1)
    print(T2)
    print(T3)
    print(T4)

    print(repr(T1))

    print(T1 == T2)
    print(T3 == T4)

    suite = TestSuite("Login Tests")
    suite.add(T1)
    suite.add(T2)
    suite.add(T3)

    print(f"\nTotal tests: {len(suite)}")

    print("TC061" in suite)

    print(suite[0])
    print(suite)

class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Fish(Animal):
    pass

animals = [Dog(), Cat(), Fish()]
for a in animals:
    a.sound()

class Product:
    def __init__(self, name, price):
        self.name  = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price}"

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

p1 = Product("Backpack", 29.99)
p2 = Product("T-Shirt",  15.99)
p3 = Product("Onesie",   29.99)

print(p1)              # what prints?
print(p1 == p3)        # what prints?
print(p1 == p2)        # what prints?
print(sorted([p1, p2, p3])[0])  # what prints?