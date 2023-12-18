from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 10, "default") == "default"
    assert arrs.get([], 0) is None

def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]
    assert arrs.my_slice([1, 2, 3, 4, 5], end=-2) == [1, 2, 3]
    assert arrs.my_slice([], 0, 2) == []
