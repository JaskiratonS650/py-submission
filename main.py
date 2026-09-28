import sys


def solve(data: str) -> str:
    # TODO: replace with the real bounty logic
    return data.strip()[::-1]


def main() -> None:
    data = sys.stdin.read() if not sys.stdin.isatty() else "hello bountied"
    print("=== Bountied solver output ===")
    print(f"input : {data!r}")
    print(f"result: {solve(data)!r}")
    print("status: OK")


if __name__ == "__main__":
    main()
