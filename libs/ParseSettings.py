import logging
import re

logger = logging.getLogger(__name__)

############ Parse settings from config
def parse_settings(config:list) -> dict:
    assert_min_length(config)
    assert_command(list(filter(None, config[0])))
    assert_empty(list(filter(None, config[1])))
    settings = {}
    settings["command"] = list(filter(None, config[0]))[0] # First line, first item
    logger.info(f"Parsed command '{settings['command']}'")
    params = parse_command_into_params(settings["command"])
    logger.info(f"Parsed parameter names {params}")
    assert_command_params(params)
    logger.info("Parsed parameter names match names in command")
    assert_items_presence(config[2], params) # Ensure number of params are defined
    assert_params_presence(config[2], params)
    settings["params"] = config[2]
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

def assert_command_params(params:tuple):
    # Ensure there are params
    assert len(params) >= 1

def assert_params_presence(line:list, params:tuple):
    # Ensure that each item in line is also in params
    for item in line:
        assert item in params

def assert_items_presence(line:list, params:tuple):
    # Ensure that the csv line has an equal number of items as params
    assert len(line) == len(params)

def parse_command_into_params(command:str) -> tuple:
    return tuple(dict.fromkeys(re.findall("\{(.*?)\}", command)))

def parse_values(lines:list) -> set:
    values = []
    for line in lines:
        if len(line) == len(lines[0]):
            values.append(tuple(line))
            logger.info(f"Parsed parameter values {tuple(line)}")
    return set(values)