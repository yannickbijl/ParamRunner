# ParamRunner
Automatic execution of user-specified parameters for UNIX commands

---
ParamRunner is a CLI tool for running the same command with different parameter settings.

ParamRunner is written in Python.
It runs UNIX commands with user-defined parameter values.
See the section [Configfile](#configfile) for more information about defining the command and parameters. In principle ParamRunner is able to execute any valid Unix command.


## Requirements
 * UNIX (Linux, Mac, Windows Subsystem for Linux (WSL))
 * Python >= 3.8 (tested, earlier versions could potentially work as well)

## Installation
Currently the only option to install ParamRunner is through manual installation.
```bash
git clone https://github.com/yannickbijl/ParamRunner.git
cd ParamRunner
python setup.py install
```

## Usage
### CLI
The basic usage of ParamRunner is the following command with a config file:
```bash
paramrunner -f [configfile]
```

### Configfile
The configfile is a csv formatted file.
In the first cell (A1) the `command` needs to be placed.
The rest of the first row is empty.

The `command` is a valid unix command. Parameters with different settings need to be place between `{}`.
```bash 
bash doSomething.sh {param1} {param2} {param3} constant
```

The second row is completely empty.
The third row commands the parameter names.
These must match with parameters in the command, though the order is irrelevant.
From the fourth row onwards are the values for the different parameters.

| Row\Col | A       | B      | C      |
|---------|---------|--------|--------|
| 1       | command |        |        |
| 2       |         |        |        |
| 3       | param1  | param2 | param3 |
| 4       | value   | value  | value  |

## License
MIT License
