# Simple Test Case Example

def subtract(a, b):
    return a - b


def test_subtract():
    expected = 15
    result = subtract(20, 5)

    if result == expected:
        print("Test Successful")
    else:
        print("Test Failed")


test_subtract()