# Zion Amsalem Advent Of Code 2025 Day 2 Part One & Two
from collections.abc import Callable

PATH = "../input.txt"

def is_valid(num: str) -> bool:
    """ for part two """
    chunk = ""
    if num is None:
        return False
    
    if len(num) > 1:
        for value in num:
            chunk += str(value)
            spaces = int(len(num) / len(chunk))

            if spaces >= 2:
                if chunk * spaces == num:
                    return True
    return False

def invalid(num: str) -> bool:
    """ for part one """
    if num is None or num == "":
        return False
    if len(num) % 2 != 0:
        return False
    half = len(num) // 2
    return num[:half] == num[half:]

def read_line(chunks: list[str], validator: Callable) -> int:
    result = 0
    for chunk in chunks:
        start, end = chunk.split("-")
        result += iterator(int(start), int(end) + 1, validator)
    return result

def iterator(start: int, end: int, validator: Callable) -> int:
    sum_for_range = 0
    for num in range(start, end):
        # TODO: remove the comments to run the first part!
        if validator(str(num)):
            sum_for_range += num
    return sum_for_range

def load_file(path: str) -> list[str]:
    with open(path, "r", encoding="utf8") as file:
        return file.read().strip().split(",")  # more "cleaner" handler

def test_invalid() -> None:
    assert invalid("1010") == True
    assert invalid("2222") == True
    assert invalid("22") == True
    assert invalid("300") == False
    assert invalid("313478") == False
    assert invalid("11001100") == True
    assert invalid("250250") == True
    assert invalid("AB") == False
    assert invalid("") == False
    assert invalid(None) == False

def test_is_valid() -> None:
    assert is_valid("123123") == True
    assert is_valid("11") == True
    assert is_valid("22") == True
    assert is_valid("1") == False
    assert is_valid("323") == False
    assert is_valid("123411123411") == True
    assert is_valid("123321123321") == True
    assert is_valid("ABCD") == False
    assert is_valid("") == False
    assert is_valid(None) == False

if __name__ == "__main__":
    test_invalid()
    test_is_valid()
    chunks: list[str] = load_file(PATH)
    
    result: int = read_line(chunks, invalid)
    print(f"The solution for the first part is: {result}")

    result: int = read_line(chunks, is_valid)
    print(f"The solution for the second part is: {result}")
