from datetime import datetime
import logging


class Logger:
    def __init__(self, log_setting:bool) -> None:
        self.log_setting = log_setting
        
        self.logger = None
        self.timestamp = None

        if self.log_setting == True:
            self._create_timestamp()
            self._create_logger()

    def _create_timestamp(self) -> None:
        self.timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

    def _create_logger(self) -> None:
        logfilename = f"ParamRunner_{self.timestamp}.log"
        logging.basicConfig(filename=logfilename,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(levelname)s %(message)s',
                            datefmt='%Y_%m_%d-%H:%M:%S',
                            level=logging.DEBUG)
        self.logger = logging.getLogger()

    def log_message(self, message:str) -> None:
        if self.logger != None:
            self.logger.info(message)

    def log_error(self, error:str) -> None:
        if self.logger != None:
            self.logger.error(error)