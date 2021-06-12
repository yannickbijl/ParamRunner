import os

from .LogMessages import log_error, log_message
from .MeasureMetrics import get_metrics, write_info_header


############ Execute commands
def execute_software(commands:list):
    if get_metrics() != None:
        write_info_header()
    for command in commands:
        execute_command(command)

def execute_command(run_command:str):
    log_message(f"Executing following command: {run_command}")
    os.system(run_command)
