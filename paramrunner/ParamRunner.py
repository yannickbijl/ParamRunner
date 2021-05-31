import argparse
import logging

from datetime import datetime
from typing import Union

from .libs.LoadConfig import load_config
from .libs.ParseArgs import parse_args
from .libs.ParseSettings import parse_settings
from .libs.ExecuteSoftware import execute_software

def check_measure_argument(value:int, params:tuple, timestamp:str) -> Union[None, tuple]:
    if value == 0:
        return None
    info_header = generate_info_header(params)
    outfile = create_measurefile(info_header, timestamp)
    return (outfile, value)

def generate_info_header(params:tuple) -> str:
    command_info = "Run," + ",".join(params)
    performance_info = "Elapsed Time,CPU Usage,Average Memory,Max Memory,Exit Status"
    return f"{command_info},{performance_info}\n"

def create_measurefile(header, timestamp) -> str:
    outfile = f"ParamRunner_{timestamp}.csv"
    with open(outfile, "w") as file:
        file.write(header)
    return outfile


############ MAIN
def main():
    # Argument Options
    args = parse_args()
    
    # Creating general variables

    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    logfilename = f"ParamRunner_{timestamp}.log"

    logging.basicConfig(filename=logfilename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                        datefmt='%Y_%m_%d-%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger()

    logger.info("Loading Configfile")
    config = load_config(args.configfile)
    logger.info("Parsing Settings")
    settings = parse_settings(config)
    measure = check_measure_argument(args.measure, settings["params"], timestamp)
    logger.info("Execute Software")
    execute_software(settings, measure)

if __name__ == "__main__":
    main()
