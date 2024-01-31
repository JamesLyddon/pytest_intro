from lib.report_length import *

def test_report_length_returns_5_for_hello():
    result = report_length('hello')
    assert result == "This string was 5 characters long."

def test_report_length_returns_11_for_hello_there():
    result = report_length('hello there')
    assert result == "This string was 11 characters long."

def test_report_length_returns_0_for_empty_string():
    result = report_length('')
    assert result == "This string was 0 characters long."