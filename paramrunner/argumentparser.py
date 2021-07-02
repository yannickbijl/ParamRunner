import argparse


def parse_arguments() -> tuple:
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest="configfile", type=str, required=True, help=_help_input_option())
    parser.add_argument('-f', '--format', dest='format', type=str, default="", choices=_get_allowed_formats(), required=False, help=_help_format_option())
    parser.add_argument('-l', '--logging', dest='logging', action='store_true', required=False, help=_help_logging_option())
    parser.add_argument('-m', '--measure', dest='measure', type=_check_positive, required=False, default=0, help=_help_measure_option())
    args = parser.parse_args()
    return args.configfile, args.format, args.logging, args.measure

def _check_positive(value:str) -> int:
    try:
        int_value = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is an invalid int value")
    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid int value")
    return int_value

def _get_allowed_formats() -> tuple:
    return ("csv", "tsv", "json", "yml", "yaml")

def _help_input_option() -> str:
    return "Formatted file with user settings."

def _help_format_option() -> str:
    return "Format of input file, use to overwrite the file extension."

def _help_logging_option() -> str:
    return "Logging of ParamRunner."

def _help_measure_option() -> str:
    return "Number of times command with same parameter settings must be run to measure performance."
