import argparse
from datetime import datetime
import logging

from libs.LoadConfig import load_config
from libs.ParseSettings import parse_settings
from libs.ExecuteSoftware import execute_software

############ MAIN
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='configfile', type=str, required=True, help="CSV formatted file with user settings.")
    args = parser.parse_args()

    logger.info("Loading Configfile")
    config = load_config(args.configfile)
    logger.info("Parsing Settings")
    settings = parse_settings(config)
    logger.info("Execute Software")
    execute_software(settings)

if __name__ == "__main__":
    logfilename = 'ParamRunner_{:%Y_%m_%d-%H_%M_%S}.log'.format(datetime.now())
    logging.basicConfig(filename=logfilename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                        datefmt=':%Y_%m_%d-%H:%M:%S',
                        level=logging.DEBUG)
    logger = logging.getLogger()
    main()
