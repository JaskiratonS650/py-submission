import sys


def solve(data: str) -> str:
    # TODO: replace with the real bounty logic
    return data.strip()[::-1]


TEST_CASES = [
    ("hello", "olleh"),
    ("bountied", "deitnuob"),
    ("  spaces  ", "secaps"),
    ("", ""),
]


def main() -> int:
    print("=== Bountied solver output ===")
    passed = 0
    for i, (given, expected) in enumerate(TEST_CASES, 1):
        got = solve(given)
        ok = got == expected
        passed += ok
        print(f"test {i}: input={given!r} expected={expected!r} got={got!r} -> {'PASS' if ok else 'FAIL'}")
    print(f"summary: {passed}/{len(TEST_CASES)} passed")
    print("status:", "OK" if passed == len(TEST_CASES) else "FAILED")
    return 0 if passed == len(TEST_CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
