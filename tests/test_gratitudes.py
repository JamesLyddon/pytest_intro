from lib.gratitudes import Gratitudes

"""
Graduates initialises .gratitudes as an empty list
"""

def test_initialise_as_empty_list():
    grats = Gratitudes()
    assert grats.gratitudes == []

"""
.add() appeneds a new item to .gratitudes
"""

def test_add_single_item():
    grats = Gratitudes()
    grats.add("puppies")
    assert grats.gratitudes == ["puppies"]

def test_add_multiple_items():
    grats = Gratitudes()
    grats.add("puppies")
    grats.add("kittens")
    grats.add("sunshine")
    assert grats.gratitudes == ["puppies", "kittens", "sunshine"]

"""
.format returns the items in .gratitudes as a formatted string
e.g. "Be grateful for: puppies, kittens, sunshine"
"""

def test_no_items_formatted():
    grats = Gratitudes()
    result = grats.format()
    assert result == "Be grateful for: "

def test_add_multiple_items_formatted():
    grats = Gratitudes()
    grats.add("puppies")
    grats.add("kittens")
    grats.add("sunshine")
    result = grats.format()
    assert result == "Be grateful for: puppies, kittens, sunshine"
