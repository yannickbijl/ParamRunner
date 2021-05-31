import argparse
from typing import Union

def parse_options(args: argparse.ArgumentParser, settings:dict, timestamp:str) -> dict:
    options = {}
    options['measure'] = check_measure_option(args.measure, settings["params"], timestamp)
    return options

# Measure Option
def check_measure_option(value:int, params:tuple, timestamp:str) -> Union[None, tuple]:
    if value == 0:
        return None
    info_header = generate_info_header(params)
    outfile = create_measurefile_with_header(info_header, timestamp)
    return (outfile, value)

def generate_info_header(params:tuple) -> str:
    command_info = "Run," + ",".join(params)
    performance_info = "Elapsed Time,CPU Usage,Average Memory,Max Memory,Exit Status"
    return f"{command_info},{performance_info}\n"

def create_measurefile_with_header(header:str, timestamp:str) -> str:
    outfile = f"ParamRunner_{timestamp}.csv"
    with open(outfile, "w") as file:
        file.write(header)
    return outfile
