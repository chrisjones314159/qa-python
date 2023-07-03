
# def test_func(num):
#     return num * 2

# def test_ans():
#     assert test_func(4) == 8

def count(sequence, item):
    sum = 0
    for n in sequence:
        if n == item:
            sum += 1
    return sum


def test_count_int():
    assert count([2, 2, 4, 6], 2) == 2
    assert count([2, 2, 4, 6], 9) == 0

def test_count_str():
    assert count(["r", "t", "r"], "r") == 2
    assert count(["r", "t", "r"], "t") == 1
