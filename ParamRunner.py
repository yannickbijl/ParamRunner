import argparse
from datetime import datetime
import logging

from libs.LoadConfig import load_config
from libs.ParseSettings import parse_settings
from libs.ExecuteSoftware import execute_software


def check_positive(value:str) -> int:
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid int value")
    return int_value

def check_measure_argument(value:int, params:tuple) -> tuple:
    if value == 0:
        return None
    info_header = generate_info_header(params)
    outfile = create_measurefile(info_header)
    return (outfile, value)

def generate_info_header(params:tuple) -> str:
    command_info = "Run," + ",".join(params)
    performance_info = "Elapsed Time,CPU Usage,Average Memory,Max Memory,Exit Status"
    return f"{command_info},{performance_info}\n"

def create_measurefile(header) -> str:
    outfile = f"ParamRunner_{timestamp}.csv"
    with open(outfile, "w") as file:
        file.write(header)
    return outfile


############ MAIN
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='configfile', type=str, required=True, help="CSV formatted file with user settings.")
    parser.add_argument('-m', '--measure', dest='measure', type=check_positive, required=False, default=0, help="")
    args = parser.parse_args()

    logger.info("Loading Configfile")
    config = load_config(args.configfile)
    logger.info("Parsing Settings")
    settings = parse_settings(config)
    measure = check_measure_argument(args.measure, settings["params"])
    logger.info("Execute Software")
    execute_software(settings, measure)

if __name__ == "__main__":
    timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    logfilename = f"ParamRunner_{timestamp}.log"
    logging.basicConfig(filename=logfilename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                        datefmt='%Y_%m_%d-%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger()
    main()
