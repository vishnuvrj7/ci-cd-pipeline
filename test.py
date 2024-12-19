# test.py
def test_addition():
    assert 1 + 1 == 2, "Test Failed"

def test_subtraction():
    assert 2 - 1 == 1, "Test Failed"

if __name__ == "__main__":
    test_addition()
    test_subtraction()
    print("All tests passed!")
