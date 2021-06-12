import csv
import json
import os
import re

import yaml

from .LogMessages import log_error, log_message
from .MeasureMetrics import create_command_info


########### Load config csv file
def get_config(filepath:str, format:str) -> dict:
    check_path_exist(filepath)
    check_file_exist(filepath)
    if format == "":
        format = determine_format(filepath)
    check_format(format)
    log_message(f"File {filepath} can be opened")
    config = get_function_dict().get(format)(filepath) # equivalent to 'config = parse_<format>(filename)'
    config = check_and_parse_config(config)
    create_command_info(config["params"])
    return config

def parse_csv(filename:str) -> dict:
    log_message("Parsing file {filename} in csv format.")
    data = dict()
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            data[row[0]] = row[1:]
    return data

def parse_tsv(filename:str) -> dict:
    log_message("Parsing file {filename} in tsv format.")
    data = dict()
    with open(filename) as file:
        reader = csv.reader(file, delimiter="\t")
        for row in reader:
            data[row[0]] = row[1:]
    return data

def parse_json(filename:str) -> dict:
    log_message("Parsing file {filename} in json format.")
    with open(filename) as file:
        data = json.load(file)
    return data

def parse_yaml(filename:str) -> dict:
    log_message("Parsing file {filename} in yaml format.")
    with open(filename) as file:
        data = yaml.full_load(file)
    return data

def check_and_parse_config(config:dict):
    check_presence_command(config) 
    config = parse_params_from_command(config)
    check_presence_params(config)
    check_length_params(config)
    check_uniqueness_params(config)
    config = parse_values_from_params(config)
    return config

def check_path_exist(input_arg:str):
    if not os.path.exists(input_arg):
        log_error("Invalid path to configfile.")
        raise FileNotFoundError("Invalid path to configfile.")

def check_file_exist(input_arg:str):
    if not os.path.isfile(input_arg):
        log_error("Configfile does not exist.")
        raise FileNotFoundError("Configfile does not exist.")

def check_format(format:str):
    if format not in get_function_dict().keys():
        log_error(f"The file format {format} is not supported.")
        raise ValueError(f"The file format {format} is not supported.")

def check_presence_command(config:dict):
    if "command" not in config.keys():
        log_error("The required field 'command' is not present in the configfile.")
        raise KeyError("The required field 'command' is not present in the configfile.")

def check_presence_params(config:dict):
    for param in config["params"]:
        if param not in config["command"]:
            log_error("The field for parameter '{param}' is not present in the configfile.")
            raise ValueError("The field for parameter '{param}' is not present in the configfile.")

def check_length_params(config:dict):
    params_subset = get_param_values(config)
    if len(set(map(len, params_subset.values()))) != 1: # Ensure all params lists are of the same length
        log_error("Not all parameters have an equal number of values.")
        raise ValueError("Not all parameters have an equal number of values.")

def check_uniqueness_params(config:dict):
    params_subset = get_param_values(config)
    values_subset = get_values_combinations(params_subset)
    if len(set(values_subset)) != len(values_subset):
        log_error("Not all combinations of parameter values are unique.")
        raise ValueError("Not all combinations of parameter values are unique.")

def determine_format(filename:str) -> str:
    return os.path.splitext(filename)[1][1:] # Use [1:] to get everything but the first character . so .csv becomes csv

def parse_params_from_command(config:dict) -> dict:
    config["command"] = str(config["command"][0])
    config["params"] = tuple(dict.fromkeys(re.findall("\{(.*?)\}", config["command"])))
    return config

def parse_values_from_params(config:dict) -> dict:
    values = []
    for item in range(len(config[config["params"][0]])):
        values.append({key: config[key][item] for key in config["params"]})
    config["values"] = values
    return config

def get_function_dict() -> dict:
    return {"csv":parse_csv, "tsv":parse_tsv, "json":parse_json,
            "yml":parse_yaml, "yaml":parse_yaml}

def get_param_values(config:dict) -> list:
    return {key: config[key] for key in config["params"]}

def get_values_combinations(subconfig:dict) -> list:
    return [x for x in zip(*subconfig.values())]
