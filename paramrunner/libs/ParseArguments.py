import argparse


def get_arguments() -> argparse.ArgumentParser:
    parser = create_parser()
    arguments = parser.parse_args()
    return arguments

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest="configfile", type=str, required=True, help=help_input_option())
    parser.add_argument('-f', '--format', dest='format', type=str, default="", choices=get_allowed_formats(), required=False, help=help_format_option())
    parser.add_argument('-l', '--logging', dest='logging', action='store_true', required=False, help=help_logging_option())
    parser.add_argument('-m', '--measure', dest='measure', type=check_positive, required=False, default=0, help=help_measure_option())
    return parser

def check_positive(value:str) -> int:
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid int value")
    return int_value

def get_allowed_formats() -> tuple:
    return ("csv", "tsv", "json", "yml", "yaml")

def help_input_option() -> str:
    return "Formatted file with user settings."

def help_format_option() -> str:
    return "Format of input file, use to overwrite the file extension."

def help_logging_option() -> str:
    return "Logging of ParamRunner."

def help_measure_option() -> str:
    return "Number of times command with same parameter settings must be run to measure performance."