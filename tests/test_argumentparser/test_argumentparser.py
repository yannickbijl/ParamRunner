import argparse
import pytest

import paramrunner.argumentparser as ap


def test_check_positive_str():
    with pytest.raises(argparse.ArgumentTypeError):
        ap._check_positive("a")

def test_check_positive_float():
    with pytest.raises(argparse.ArgumentTypeError):
        ap._check_positive("1.23")

def test_check_positive_negint():
    with pytest.raises(argparse.ArgumentTypeError):
        ap._check_positive("-2")

def test_check_positive_int():
    assert ap._check_positive("1") == 1
