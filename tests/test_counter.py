from lib.counter import *

"""
Creates state with the number 0
.add() takes a number and adds it to the number in state
.report() returns the number is state as f"Counted to {self.count} so far."
"""

def test_counter_0():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counter_add_5():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_counter_add_10_add_50():
    counter = Counter()
    counter.add(10)
    counter.add(50)
    result = counter.report()
    assert result == "Counted to 60 so far."