import pytest
from project import build_table, get_number_of_results, get_city


def test_build_table():
    assert build_table([{"name": "Muu Steakhouse",
                         "rating": 4.9,
                         "address": "Rua do Almada 149A, 4050-037 Porto, Portugal"}],
                       1) == [{"name": "Muu Steakhouse",
                               "rating": 4.9,
                               "address": "Rua do Almada 149A, 4050-037 Porto, Portugal"}]


def test_get_number_of_results():
    with pytest.raises(ValueError):
        get_number_of_results("cat")


def test_get_city():
    assert get_city("porto") == "porto"
