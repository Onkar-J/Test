import pytest


def test_func1():
    a = 5
    b = 10
    assert a == b, "test failed"


def test_func2():
    name = "Onkar Jadhav"
    assert name.lower() == "onkar jadhav"