import pytest

import functions_pytest as fp

def test_division():
    assert fp.division(30, 6) == 5
    assert fp.division(2, 1) == 2
    assert fp.division(1000, 4) == 250

