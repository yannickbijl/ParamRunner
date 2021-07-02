import pytest

import paramrunner.metrics as metrics

def test_metrics_off():
    mt = metrics.Metrics(0, None)
    assert mt.metrics == None

def test_metrics_timestamp():
    mt = metrics.Metrics(2, "1970_01_01-00_00_00")
    assert mt.metrics == "ParamRunner_Metrics_1970_01_01-00_00_00.csv"
    assert mt.timestamp == "1970_01_01-00_00_00"