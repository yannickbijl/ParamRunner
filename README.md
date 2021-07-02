# ParamRunner
Automatic execution of user-specified parameters for UNIX commands

---
ParamRunner is a CLI tool for running the same command with different parameter settings.

ParamRunner is written in Python.
It runs UNIX commands with user-defined parameter values.
See the section [Configfiles](#configfiles) for more information about defining the command and parameters.

## Requirements
* UNIX (Linux, Mac, Windows Subsystem for Linux (WSL))
* Python >= 3.8 (tested, earlier versions could potentially work as well)


## Installation 
Install paramrunner as a package using the following command

```bash
git clone https://github.com/yannickbijl/ParamRunner.git
cd ParamRunner
python3 setup.py install
```


## Running Tests
To run tests, run the following command in the project folder

```bash
cd ParamRunner
pytest .
```


## Usage/Examples
For basic usage, use the following command
```bash
paramrunner -i configfile.csv
```

Measuring compute resources can be gathered using the -m option.  
A command will be repeated a given *n* times to see reproducibility.  
Use the following command as example
```bash
paramrunner -i configfile.csv -m 2
```

Use the following command for more information about available options
```bash
paramrunner -h
```

### Configfiles
The configfile is a csv, tsv, json, or yaml formatted file.  
The string `command` is a reserved keyword, coupled to a valid unix command.  
Parameters with different settings need to be place between `{}`.  
The following example will be used as `unix_command`
```bash 
bash doSomething.sh {param1} {param2} {param3} constant
```

#### CSV / TSV
The `command` and `parameter names` need to be in the first column (A).  
The `unix_command` needs to be in column B.  
The `parameter names` must match with the parameters between `{}` in `unix_command`.  
Values for the parameters are behind the `parameter names` and placed row-wise.

| Row\Col | A       | B            | C      |
|---------|---------|--------------|--------|
| 1       | command | unix_command |        |
| 3       | param1  | value1       | value2 |
| 4       | param2  | value3       | value4 |
| 5       | param3  | value5       | value6 |

#### JSON
The `parameter names` must match with the parameters between `{}` in `unix_command`.  
Values for the parameters have to be in a list structure.

```json
{
    "command": "unix_command",
    "param1": [value1, value2],
    "param2": [value3, value4],
    "param3": [value5, value6]
}
```

#### YAML
The `parameter names` must match with the parameters between `{}` in `unix_command`.  
Values for the parameters have to be in a list structure.

```yaml
command: unix_command
param1: [value1, value2]
param2: [value3, value4]
param3: [value5, value6]
```


## FAQ
#### Q. How does a config file look like?
A. See the examples in [docs](./docs/). Also see the section [Configfiles](#configfiles).

#### Q. Are there unix commands that do not work with paramrunner?
A. In theory all valid unix commands should work.  
However, permission restrictions to work with specific folders/files could hinder paramrunner.


## License
[MIT](https://choosealicense.com/licenses/mit/)
