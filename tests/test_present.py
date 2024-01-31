import pytest
from lib.present import Present

"""
Initialises .contents to None
"""

def test_init_as_none():
    pres = Present()
    assert pres.contents == None

"""
.wrap() raises an exception if .contents != None
"""

def test_wrap_when_contents_not_none_exception():
    pres = Present()
    pres.contents = "not nothing"
    with pytest.raises(Exception) as e:
        pres.wrap("something")
    error_msg = str(e.value)
    assert error_msg == "A contents has already been wrapped."

"""
.wrap succesfully wraps if .contents == None
.unwrap succefully unwraps if .copntents != None
"""

def test_wrap_when_contents_none():
    pres = Present()
    pres.wrap("something")
    assert "something" == pres.unwrap()

"""
.unwrap raises exception if .contents == None
"""

def test_unwrap_when_contents_none():
    pres = Present()
    with pytest.raises(Exception) as e:
        pres.unwrap()
    error_msg = str(e.value)
    assert error_msg == "No contents have been wrapped."