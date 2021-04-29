import argparse
from datetime import datetime
import logging

from libs.LoadConfig import load_config
from libs.ParseSettings import parse_settings
from libs.ExecuteSoftware import execute_software

def check_positive(value):
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid int value")
    return int_value

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
    logger.info("Execute Software")
    execute_software(settings, args.measure)
    if args.measure > 0:
        #Further analysis.
        pass

if __name__ == "__main__":
    logfilename = 'ParamRunner_{:%Y_%m_%d-%H_%M_%S}.log'.format(datetime.now())
    logging.basicConfig(filename=logfilename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                        datefmt=':%Y_%m_%d-%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger()
    main()
