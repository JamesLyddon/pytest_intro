from lib.check_codeword import *

def test_check_codeword_returns_correct_for_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_returns_close_for_hooorse():
    result = check_codeword("hooorse")
    assert result == "Close, but nope."

def test_check_codeword_returns_close_for_he():
    result = check_codeword("he")
    assert result == "Close, but nope."

def test_check_codeword_returns_wrong_for_hors():
    result = check_codeword("hors")
    assert result == "WRONG!"

def test_check_codeword_returns_wrong_for_HORSE():
    result = check_codeword("HORSE")
    assert result == "WRONG!"