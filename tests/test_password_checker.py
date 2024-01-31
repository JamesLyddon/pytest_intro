import pytest
from lib.password_checker import PasswordChecker

"""
returns True if string >= 8
"""

def test_password_of_length_8():
    pass_checker = PasswordChecker()
    assert pass_checker.check("12345678") == True

def test_password_of_length_9():
    pass_checker = PasswordChecker()
    assert pass_checker.check("123456789") == True

"""
if password < 8
raises exception
"Invalid password, must be 8+ characters."
"""

def test_password_of_length_7():
    pass_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        pass_checker.check("1234567")
    err_msg = str(e.value)
    assert err_msg == "Invalid password, must be 8+ characters."

def test_password_of_length_0():
    pass_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        pass_checker.check("")
    err_msg = str(e.value)
    assert err_msg == "Invalid password, must be 8+ characters."

"""
Passing in anything with a length works...
Funciton should check for type == str
"""

def test_list_with_7_elements():
    pass_checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        pass_checker.check([1, 2, 3, 4, 5, 6, 7])
    err_msg = str(e.value)
    assert err_msg == "Invalid password, must be 8+ characters."

def test_list_with_8_elements():
    pass_checker = PasswordChecker()
    assert pass_checker.check([1,2,3,4,5,6,7,8]) == True