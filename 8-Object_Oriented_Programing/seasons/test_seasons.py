import pytest
from seasons import number_to_words

def test_get_birth_date():
    assert number_to_words(525600) == "five hundred twenty-five thousand, six hundred"
