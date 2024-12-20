import Calculate
import pytest


def test_calculate():
    result = Calculate.calculate(100, "USD")
    assert result == 100
