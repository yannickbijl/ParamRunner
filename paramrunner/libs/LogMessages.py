import logging
from datetime import datetime

logger = None
timestamp = None

def make_logger(log:bool):
    if log:
        global logger
        global timestamp
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
        logfilename = f"PRECC_{timestamp}.log"
        logging.basicConfig(filename=logfilename,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                            datefmt='%Y_%m_%d-%H:%M:%S',
                            level=logging.DEBUG)
        logger = logging.getLogger()

def log_message(message:str):
    if logger != None:
        logger.info(message)

def log_error(message:str):
    if logger != None:
        logger.error(message)

def get_log_timestamp() -> str:
    global timestamp
    return timestamp