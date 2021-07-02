import os

from . import argumentparser
from . import commandparser
from . import configparser
from . import logger
from . import metrics

class ParamRunner:
    def __init__(self, configfile:str, format:str, log:bool, measure:int) -> None:
        self.configfile = configfile
        self.format = format
        self.log = log
        self.measure = measure

        self.logger = logger.Logger(self.log)
        self.metrics = metrics.Metrics(self.measure, self.logger.timestamp)
        
        self.parse_config = configparser.Config(self.configfile, self.format, self.logger)
        config = self.parse_config.get_config()
        self.parse_commands = commandparser.Command(config, self.metrics, self.logger)
        self.commands = self.parse_commands.get_commands()
        print(self.commands)
        
        self._run_commands()

    def _run_commands(self) -> None:
        for command in self.commands:
            self.logger.log_message(f"Executing following command: {command}")
            os.system(command)


def main():
    ParamRunner(*argumentparser.parse_arguments())


if __name__ == "__main__":
    main()
