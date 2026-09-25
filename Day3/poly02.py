# ============================================================
# File: day03/07_magic_methods.py
# ============================================================

class TestResult:
    """
    Represents a single test result.
    Magic methods make it behave like
    a proper Python citizen.
    """

    def __init__(self, test_id: str,
                 status: str,
                 duration: float):
        self.test_id  = test_id
        self.status   = status
        self.duration = duration

    # ── __str__ ─────────────────────────────────────────────
    # Called when: print(result) or str(result)
    # Purpose: Human readable output
    def __str__(self) -> str:
        icon = "✅" if self.status == "pass" else "❌"
        return (f"{icon} [{self.test_id}] "
                f"{self.status.upper()} "
                f"({self.duration}s)")

    # ── __repr__ ────────────────────────────────────────────
    # Called when: repr(result) or in Python REPL
    # Purpose: Developer/debug output
    # Should show how to recreate the object
    def __repr__(self) -> str:
        return (f"TestResult(test_id='{self.test_id}', "
                f"status='{self.status}', "
                f"duration={self.duration})")

    # ── __eq__ ──────────────────────────────────────────────
    # Called when: result1 == result2
    # Purpose: Compare two TestResult objects
    def __eq__(self, other) -> bool:
        if not isinstance(other, TestResult):
            return False
        return (self.test_id == other.test_id and
                self.status  == other.status)

    # ── __lt__ ──────────────────────────────────────────────
    # Called when: result1 < result2
    # Purpose: Sort by duration
    def __lt__(self, other) -> bool:
        return self.duration < other.duration


class TestSuite:
    """
    Represents a collection of test results.
    """

    def __init__(self, name: str):
        self.name    = name
        self._tests  = []

    # ── __len__ ─────────────────────────────────────────────
    # Called when: len(suite)
    def __len__(self) -> int:
        return len(self._tests)

    # ── __contains__ ────────────────────────────────────────
    # Called when: "TC001" in suite
    def __contains__(self, test_id: str) -> bool:
        return any(t.test_id == test_id
                   for t in self._tests)

    # ── __getitem__ ─────────────────────────────────────────
    # Called when: suite[0] or suite["TC001"]
    def __getitem__(self, index: int) -> TestResult:
        return self._tests[index]

    # ── __str__ ─────────────────────────────────────────────
    def __str__(self) -> str:
        passed = sum(1 for t in self._tests
                     if t.status == "pass")
        return (f"TestSuite: {self.name} | "
                f"{len(self)} tests | "
                f"{passed} passed")

    def add(self, result: TestResult) -> None:
        self._tests.append(result)


# ─── USING MAGIC METHODS ────────────────────────────────────
if __name__ == "__main__":

    # Create test results:
    r1 = TestResult("TC001", "pass", 2.3)
    r2 = TestResult("TC002", "fail", 1.1)
    r3 = TestResult("TC003", "pass", 3.7)
    r4 = TestResult("TC001", "pass", 2.3)

    # __str__ called:
    print(r1)             # ✅ [TC001] PASS (2.3s)
    print(r2)             # ❌ [TC002] FAIL (1.1s)

    # __repr__ called:
    print(repr(r1))       # TestResult(test_id='TC001'...)

    # __eq__ called:
    print(r1 == r4)       # True (same id + status)
    print(r1 == r2)       # False

    # __lt__ called (sorting):
    results = [r3, r1, r2]
    sorted_results = sorted(results)   # uses __lt__
    for r in sorted_results:
        print(r)          # sorted by duration

    # TestSuite magic methods:
    suite = TestSuite("Login Tests")
    suite.add(r1)
    suite.add(r2)
    suite.add(r3)

    # __len__:
    print(f"\nTotal tests: {len(suite)}")   # 3

    # __contains__:
    print("TC001" in suite)    # True
    print("TC999" in suite)    # False

    # __getitem__:
    print(suite[0])            # first test

    # __str__:
    print(suite)