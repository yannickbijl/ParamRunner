import csv
import logging
import os

logger = logging.getLogger(__name__)

########### Load config csv file
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