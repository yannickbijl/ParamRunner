import argparse
import csv
import os
import re
import sys


############ Load config csv file
def load_config(filepath:str) -> list:
    assert_exist(filepath)
    assert_file(filepath)
    assert_ends(filepath)
    config = read_config(filepath)
    return config

def assert_exist(input_arg:str):
    # Ensure input_arg is a valid existence
    assert os.path.exists(input_arg)

def assert_file(input_arg:str):
    # Ensure input_arg is a file
    assert os.path.isfile(input_arg)

def assert_ends(input_arg:str):
    # Ensure input_arg file extensions ends with csv
    assert input_arg.endswith('csv')

def read_config(filepath:str) -> list:
    with open(filepath) as infile:
        configreader = csv.reader(infile, delimiter=",")
        config = [row for row in configreader]
    return config


############ Parse settings from config
def parse_settings(config:list) -> dict:
    assert_min_length(config)
    assert_command(config[0])
    assert_empty(config[1])
    settings = {}
    settings["command"] = config[0][0] # First line, first item
    settings["params"] = parse_command_into_params(settings["command"])
    assert_command_params(settings["params"])
    assert_items_presence(config[2], settings["params"]) # Ensure number of params are defined
    assert_params_presence(config[2], settings["params"])
    assert_items_presence(config[3], settings["params"]) # Ensure at least one line with values
    settings["values"] = parse_values(config[3:])
    return settings

def assert_min_length(lines:list):
    # Ensure that there at least 4 lines, which would be command, empty, param names, param values.
    assert len(lines) >= 4

def assert_command(line:list):
    # Ensure that line is only 1 item
    assert len(line) == 1
    # Ensure that the line is not empty text
    assert line[0].strip != ""

def assert_empty(line:list):
    # Ensure that line is empty
    assert len(line) == 0

def assert_command_params(params:list):
    # Ensure there are params
    assert len(params) >= 1

def assert_params_presence(line:list, params:list):
    # Ensure that each item in line is also in params
    for item in line:
        assert item in params

def assert_items_presence(line:list, params:list):
    # Ensure that the csv line has an equal number of items as params
    assert len(line) == len(params)

def parse_command_into_params(command:str) -> list:
    return re.findall("\{(.*?)\}", command)

def parse_values(lines:list) -> set:
    values = [tuple(line) for line in lines if len(line) == len(lines[0])]
    return set(values)


############ MAIN
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='configfile', type=str, required=True, help="CSV formatted file with user settings.")
    args = parser.parse_args()

    config = load_config(args.configfile)
    settings = parse_settings(config)
    print(settings)

if __name__ == "__main__":
    main()
