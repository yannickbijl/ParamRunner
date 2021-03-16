import argparse
import os
import sys

import yaml
from yaml.error import YAMLError


############ Load YAML file
def load_yaml(filepath:str) -> dict:
    assert_exist(filepath)
    assert_file(filepath)
    assert_ends(filepath)
    yamltext = open_text(filepath)
    yamldict = open_yaml(yamltext)
    return yamldict

def assert_exist(input_arg:str):
    # Ensure input_arg is a valid existence
    assert os.path.exists(input_arg)

def assert_file(input_arg:str):
    # Ensure input_arg is a file
    assert os.path.isfile(input_arg)

def assert_ends(input_arg:str):
    # Ensure input_arg ends with .yaml or .yml 
    assert not input_arg.endswith('.yaml') or not input_arg.endswith('.yml')

def open_text(filepath:str) -> str:
    with open(filepath) as file:
        text = file.read()
    return text

def open_yaml(yamltext:str) -> dict:
    try:
        return yaml.load(yamltext)
    except yaml.YAMLError as error:
        print(error)
        sys.exit()



############ MAIN
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='yamlfile', type=str, required=True, help="YAML formatted file with user settings.")
    args = parser.parse_args()

    settings = load_yaml(args.yamlfile)

if __name__ == "__main__":
    main()
