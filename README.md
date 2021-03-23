# ParamRunner
Automatic execution of user-specified parameters for commandline software tools

# Requirements
 * UNIX (Linux, Mac, Windows Subsystem for Linux (WSL))
 * Python >= 3.8

# How to Use
Run ParamRunner with the following command:  
`python3 ParamRunner.py -f {config file}`

The `config file` is a csv formatted file.  
The csv file consist of minimally 4 lines.

The first line contains the command to be run.  
The second line is empty.  
The third line contains the parameter names, these should match with the given command.  
From the fourth line on, values for the parameters are given.  
See [Example Config](docs/example_config.csv) for an easy viewable config file.

# License
MIT License
