import pytest
from billing import calculate_total

def test_1():
    assert calculate_total(200) == 210.00

def test_2():
    assert calculate_total(300) == 315.00

def test_3():
    assert calculate_total(400) == 369.00

def test_zero():
    assert calculate_total(0) == 0
    