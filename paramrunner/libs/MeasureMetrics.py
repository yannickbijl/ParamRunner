from datetime import datetime

from .LogMessages import get_log_timestamp, log_error, log_message

metrics = None
metricsfile = None
commandinfo = None

def make_metricsfile(measure:int):
    if measure > 0:
        global metrics  
        global metricsfile
        metrics = measure
        timestamp = create_timestamp()
        metricsfile = f"ParamRunner_Metrics_{timestamp}.csv"
        
def create_timestamp() -> str:
    timestamp = get_log_timestamp()
    if timestamp == None:
        timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")
    return timestamp

def create_command_info(params:list):
    global command_info
    command_info = "Run," + ",".join(params)

def write_info_header():
    metricsfile = get_metricsfile()
    command_info = get_commandinfo()
    performance_info = "Elapsed Time,CPU Usage,Average Memory,Max Memory,Exit Status"
    header = f"{command_info},{performance_info}\n"
    log_message(f"Write header to {metricsfile}.")
    with open(metricsfile, "w") as file:
        file.write(header)

def get_metrics() -> int:
    global metrics
    return metrics

def get_metricsfile() -> str:
    global metricsfile
    return metricsfile

def get_commandinfo() -> str:
    global commandinfo
    return commandinfo