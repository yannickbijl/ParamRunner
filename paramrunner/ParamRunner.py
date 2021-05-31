import argparse
import logging

from datetime import datetime

from .libs.LoadConfig import load_config
from .libs.ParseOptions import parse_options
from .libs.ParseSettings import parse_settings
from .libs.ExecuteSoftware import execute_software


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
    logger.info("Parsing Options")
    options = parse_options(args, settings, timestamp)
    logger.info("Execute Software")
    execute_software(settings, options)

if __name__ == "__main__":
    main()
