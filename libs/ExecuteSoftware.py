from datetime import datetime
import logging
import os

logger = logging.getLogger(__name__)

############ Execute commands
def execute_software(settings:dict, measure:tuple=None):
    for paramvalue in settings["values"]:
        run_command = create_command(settings["command"], settings["params"], paramvalue)
        if measure == None:
           logger.info(f"Running command with following values {paramvalue}")
           execute_command(run_command)
        else:
            for run in range(measure[1]):                
                logger.info(f"Running command with following values {paramvalue}")
                logger.info(f"Performance metrics will be measured amd logged in {measure[0]}")
                info_line = generate_info_line(run+1,paramvalue)
                measure_command = adjust_command(run_command, measure[0], info_line)
                execute_command(measure_command)

def generate_info_line(run:int, values:tuple) -> str:
    command_info = f"{run}," + ",".join(values)
    performance_info = "%E,%P,%K,%M,%x"
    return f"{command_info},{performance_info}"

def create_command(command:str, params:tuple, values:tuple) -> str:
    for param, value in zip(params, values):
        command = command.replace(f"{'{' + param + '}'}", str(value))
    return command

def adjust_command(original_command:str, outfile:str, info:str) -> str:
    return f"command time -a -o {outfile} -f {info} {original_command}"

def execute_command(run_command:str):
    os.system(run_command)
