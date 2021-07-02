import pytest

import paramrunner.configparser as config
import paramrunner.logger as logger

logger_test = logger.Logger(False)

def test_csv_output():
    test_config = config.Config("docs/example_config.csv", "csv", logger_test)
    assert ({'command': 'echo "{string} {value}" | rev > {file}',
            'string': ['something1', 'something1', 'something2', 'something2'],
            'value': ['0', '1', '0', '1'],
            'file': ['out1.txt', 'out2.txt', 'out3.txt', 'out4.txt'],
            'params': ('string', 'value', 'file')} == test_config.get_config())

def test_tsv_output():
    test_config = config.Config("docs/example_config.tsv", "tsv", logger_test)
    assert ({'command': 'echo "{string} {value}" | rev > {file}',
            'string': ['something1', 'something1', 'something2', 'something2'],
            'value': ['0', '1', '0', '1'],
            'file': ['out1.txt', 'out2.txt', 'out3.txt', 'out4.txt'],
            'params': ('string', 'value', 'file')} == test_config.get_config())

def test_json_output():
    test_config = config.Config("docs/example_config.json", "json", logger_test)
    assert ({'command': 'echo "{string} {value}" | rev > {file}',
             'string': ['something1', 'something1', 'something2', 'something2'],
             'value': [0, 1, 0, 1],
             'file': ['out1.txt', 'out2.txt', 'out3.txt', 'out4.txt'],
             'params': ('string', 'value', 'file')} == test_config.get_config())

def test_yaml_output():
    test_config = config.Config("docs/example_config.yaml", "yaml", logger_test)
    assert ({'command': 'echo "{string} {value}" | rev > {file}',
             'string': ['something1', 'something1', 'something2', 'something2'],
             'value': [0, 1, 0, 1],
             'file': ['out1.txt', 'out2.txt', 'out3.txt', 'out4.txt'],
             'params': ('string', 'value', 'file')} == test_config.get_config())