import argparse
import csv
import os
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
    assert_command(config[0])
    settings = {}
    return settings

def assert_command(line):
    # Ensure that line is only 1 item
    assert len(line) == 1
    # Ensure that the line is not empty text
    assert line[0].strip != ""


############ MAIN
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='configfile', type=str, required=True, help="CSV formatted file with user settings.")
    args = parser.parse_args()

    config = load_config(args.configfile)
    settings = parse_settings(config)

if __name__ == "__main__":
    main()
