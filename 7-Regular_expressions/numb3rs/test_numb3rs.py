import pytest
from numb3rs import validate

def test_validate():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("100.1.12.23") == True
    assert validate("100.1.cat.200") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("100") == False
    assert validate("100.1") == False
    assert validate("1") == False
    assert validate("256.255.255.255") == False
    assert validate("64.128.256.512") == False
    assert validate("a") == False
    assert validate("cat") == False
