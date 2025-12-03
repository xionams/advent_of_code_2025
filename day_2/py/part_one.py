# Zion Amsalem Advent Of Code 2025 Day 2 Part One

PATH = "../input.txt"


def invalid(num: str) -> bool:
    if len(num) % 2 != 0:
        return False
    half = len(num) // 2
    return num[:half] == num[half:]


def read_line(chunks: list[str]) -> int:
    result = 0
    for chunk in chunks:
        start, end = chunk.split("-")
        result += iterator(int(start), int(end) + 1)
    return result


def iterator(start: int, end: int) -> int:
    sum_for_range = 0
    for num in range(start, end):
        if invalid(str(num)):
            sum_for_range += num
    return sum_for_range


def load_file(path: str) -> list[str]:
    with open(path, "r", encoding="utf8") as file:
        return file.read().strip().split(",")  # more "cleaner" handler


if __name__ == "__main__":
    chunks: list[str] = load_file(PATH)
    result: int = read_line(chunks)
    print(f"The result is: {result}")
