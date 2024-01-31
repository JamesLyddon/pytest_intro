from lib.greet import *

def test_greet_returns_thom_for_thom():
    result = greet('Thom')
    assert result == f'Hello, Thom!'