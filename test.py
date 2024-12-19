# test.py
import pytest

def test_addition():
    assert 1 + 1 == 2, "Addition test failed"

def test_subtraction():
    assert 2 - 1 == 1, "Subtraction test failed"

if __name__ == "__main__":
    pytest.main()
