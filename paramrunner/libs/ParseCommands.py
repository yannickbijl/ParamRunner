from .LogMessages import log_error, log_message
from .MeasureMetrics import get_commandinfo, get_metrics, get_metricsfile


def get_commands(config:dict) -> list:
    commands = []
    for values in config["values"]:
        log_message("Generating commands.")
        command = generate_base_command(config["command"], values)
        log_message("Adjusting commands for measurements.")
        commands.append(generate_measure_command(command, values))
    return [sublist for command in commands for sublist in command]

def generate_base_command(command: str, params_values: dict) -> str:
    for param in params_values.keys():
        command = command.replace(f"{'{' + param + '}'}", str(params_values[param]))
    return command

def generate_measure_command(command:str, values:dict) -> list:
    commands = []
    if get_metrics() != None:
        line_info = create_lineinfo(values)
        for run in range(get_metrics()):
            line_info = line_info.replace("Run", str(run+1))
            commands.append(f"command time -a -o {get_metricsfile()} -f {line_info} {command}")
    else:
        commands.append(command)
    return commands

def create_lineinfo(values:dict) -> str:
    command_info = get_commandinfo()
    for param in values.keys():
        command_info = command_info.replace(param, values[param])
    return f"{command_info},%E,%P,%K,%M,%x"
