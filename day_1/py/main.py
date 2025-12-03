# Zion Amsalem Advent Of Code 2025 - Day 1

PATH = "../input.txt"
LOCK = 50

def right(lock: int, steps: int) -> int:
    # move the lock n steps right
    lock = lock + steps
    if lock >= 100:
        lock = lock - 100
    return lock

def left(lock: int, steps: int) -> int:
    # move the lock n steps left
    lock = lock - steps
    if lock < 0:
        lock = 100 + lock
    return lock

def tests() -> None:
    # tests is all you need
    lock = LOCK
    assert left(lock, 0) == 50
    assert left(lock, 49) == 1
    assert left(lock, 100) == 50
    assert left(lock, 51) == 99
    assert right(lock, 50) == 0
    assert right(lock, 51) == 1
    assert right(lock, 52) == 2
    assert right(lock, 100) == 50
    assert right(lock, 1) == 51
    assert right(lock, (549 % 100)) == 99
    assert tour_test(lock) == 2

def tour_test(lock: int) -> int:
    # simplest e2e test
    result = 0
    _actions = ["R10", "L60", "R101", "L1"]
    for action in _actions:
        steps = int(action[1:]) % 100
        if action[0] == "R":
            lock = right(lock, steps)
        elif action[0] == "L":
            lock = left(lock, steps)
        if lock == 0:
            result += 1
    return result

def load_file(path: str) -> list[str]:
    # load the file
    with open(path, "r", encoding="utf8") as file:
        return file.readlines()

def pick(file: list[str], lock: int) -> int:
    # pick the lock
    result = 0
    for action in file:
        steps = int(action[1:]) % 100
        if action[0] == "R":
            lock = right(lock, steps)
        elif action[0] == "L":
            lock = left(lock, steps)
        if lock == 0:
            result += 1
    return result

if __name__ == "__main__":
    tests()
    actions_list = load_file(PATH)
    secret = pick(actions_list,LOCK)
    print(f"the code for the lock is: {secret}")
