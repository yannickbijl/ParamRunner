import argparse
import csv
from datetime import datetime
import logging
import os
import re


############ Load config csv file
def load_config(filepath:str) -> list:
    assert_exist(filepath)
    assert_file(filepath)
    assert_ends(filepath)
    logger.info(f"File {filepath} can be opened")
    config = read_config(filepath)
    logger.info(f"File {filepath} read into memory")
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
    logger.info(f"Parsed command '{settings['command']}'")
    settings["params"] = parse_command_into_params(settings["command"])
    logger.info(f"Parsed parameter names {settings['params']}")
    assert_command_params(settings["params"])
    logger.info("Parsed parameter names match names in command")
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

def parse_command_into_params(command:str) -> set:
    return set(re.findall("\{(.*?)\}", command))

def parse_values(lines:list) -> set:
    values = []
    for line in lines:
        if len(line) == len(lines[0]):
            values.append(tuple(line))
            logger.info(f"Parsed parameter values {tuple(line)}")
    return set(values)


############ Execute commands
def execute_software(settings:dict):
    for paramvalue in settings["values"]:
        run_command = create_command(settings["command"], settings["params"], paramvalue)
        logger.info(f"Running command with following values {paramvalue}")
        execute_command(run_command)

def create_command(command:str, params:set, values:tuple) -> str:
    for param, value in zip(params, values):
        command = command.replace(f"{'{' + param + '}'}", str(value))
    return command

def execute_command(run_command:str):
    os.system(run_command)


############ MAIN
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='configfile', type=str, required=True, help="CSV formatted file with user settings.")
    args = parser.parse_args()

    logger.info("Loading Configfile")
    config = load_config(args.configfile)
    logger.info("Parsing Settings")
    settings = parse_settings(config)
    logger.info("Execute Software")
    execute_software(settings)

if __name__ == "__main__":
    logfilename = 'ParamRunner_{:%Y_%m_%d-%H_%M_%S}.log'.format(datetime.now())
    logging.basicConfig(filename=logfilename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                        datefmt=':%Y_%m_%d-%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger()
    main()
