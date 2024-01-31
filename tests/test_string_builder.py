from lib.string_builder import *

"""
Initialises str as an empty string
"""

def test_string_builder_init_as_empty():
    sb = StringBuilder()
    result = sb.str
    assert result == ""

"""
.add() takes a string and concaternates it onto .str
"""

def test_string_builder_add_hello():
    sb = StringBuilder()
    sb.add("hello")
    result = sb.str
    assert result == "hello"

def test_string_builder_add_multiple():
    sb = StringBuilder()
    sb.add("hello")
    sb.add(" ")
    sb.add("world")
    sb.add("!")
    result = sb.str
    assert result == "hello world!"

"""
.size returns the length of .str
"""

def test_string_builder_size_empty():
    sb = StringBuilder()
    result = sb.size()
    assert result == 0

def test_string_builder_size_hello():
    sb = StringBuilder()
    sb.add("hello")
    result = sb.size()
    assert result == 5

"""
.output returns .str
"""

def test_string_builder_returns_empty():
    sb = StringBuilder()
    result = sb.output()
    assert result == ""

def test_string_builder_returns_hello():
    sb = StringBuilder()
    sb.add("hello")
    result = sb.output()
    assert result == "hello"