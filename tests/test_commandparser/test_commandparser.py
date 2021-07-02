import pytest

import paramrunner.commandparser as cp
import paramrunner.logger as logger
import paramrunner.metrics as metrics

logger_test = logger.Logger(False)
config = {'command': 'echo "{string} {value}" | rev > {file}',
          'string': ['something1', 'something1', 'something2', 'something2'],
          'value': ['0', '1', '0', '1'],
          'file': ['out1.txt', 'out2.txt', 'out3.txt', 'out4.txt'],
          'params': ('string', 'value', 'file')}

def test_command_output():
    mt = metrics.Metrics(0, None)
    commands = cp.Command(config, mt, logger_test)
    assert (['echo "{string} {value}" | rev > out1.txt',
             'echo "{string} {value}" | rev > out2.txt',
             'echo "{string} {value}" | rev > out3.txt',
             'echo "{string} {value}" | rev > out4.txt'] == commands.get_commands())

def test_metric_command_output():
    mt = metrics.Metrics(2, "1970_01_01-00_00_00")
    commands = cp.Command(config, mt, logger_test)
    assert (['command time -a -o ParamRunner_Metrics_1970_01_01-00_00_00.csv -f 1,something1,0,out1.txt,%E,%P,%K,%M,%x echo "{string} {value}" | rev > out1.txt',
             'command time -a -o ParamRunner_Metrics_1970_01_01-00_00_00.csv -f 1,something1,0,out1.txt,%E,%P,%K,%M,%x echo "{string} {value}" | rev > out1.txt',
             'command time -a -o ParamRunner_Metrics_1970_01_01-00_00_00.csv -f 1,something1,1,out2.txt,%E,%P,%K,%M,%x echo "{string} {value}" | rev > out2.txt',
             'command time -a -o ParamRunner_Metrics_1970_01_01-00_00_00.csv -f 1,something1,1,out2.txt,%E,%P,%K,%M,%x echo "{string} {value}" | rev > out2.txt',
             'command time -a -o ParamRunner_Metrics_1970_01_01-00_00_00.csv -f 1,something2,0,out3.txt,%E,%P,%K,%M,%x echo "{string} {value}" | rev > out3.txt',
             'command time -a -o ParamRunner_Metrics_1970_01_01-00_00_00.csv -f 1,something2,0,out3.txt,%E,%P,%K,%M,%x echo "{string} {value}" | rev > out3.txt',
             'command time -a -o ParamRunner_Metrics_1970_01_01-00_00_00.csv -f 1,something2,1,out4.txt,%E,%P,%K,%M,%x echo "{string} {value}" | rev > out4.txt',
             'command time -a -o ParamRunner_Metrics_1970_01_01-00_00_00.csv -f 1,something2,1,out4.txt,%E,%P,%K,%M,%x echo "{string} {value}" | rev > out4.txt'] == commands.get_commands())