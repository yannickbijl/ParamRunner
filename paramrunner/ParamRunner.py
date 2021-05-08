import argparse
import logging

from datetime import datetime

from .libs.LoadConfig import load_config
from .libs.ParseOptions import parse_options
from .libs.ParseSettings import parse_settings
from .libs.ExecuteSoftware import execute_software


def check_positive(value:str) -> int:
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid int value")
    return int_value


############ MAIN
def main():
    # Argument Options
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='configfile', type=str, required=True, help="CSV formatted file with user settings.")
    parser.add_argument('-m', '--measure', dest='measure', type=check_positive, required=False, default=0, help="Number of times command with same parameter settings must be run to measure performance.")
    args = parser.parse_args()

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
    logger.info("Parsing Options")
    options = parse_options(args, settings, timestamp)
    logger.info("Execute Software")
    execute_software(settings, options)

if __name__ == "__main__":
    main()
