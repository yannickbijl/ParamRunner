import logging
import os

logger = logging.getLogger(__name__)

############ Execute commands
def execute_software(settings:dict):
    for paramvalue in settings["values"]:
        run_command = create_command(settings["command"], settings["params"], paramvalue)
        logger.info(f"Running command with following values {paramvalue}")
        execute_command(run_command)

def create_command(command:str, params:set, values:tuple) -> str:
    for param, value in zip(params, values):
        command = command.replace(f"{'{' + param + '}'}", str(value))
    return command

def execute_command(run_command:str):
    os.system(run_command)
