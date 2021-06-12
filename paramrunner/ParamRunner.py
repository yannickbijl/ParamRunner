from .libs.ExecuteSoftware import execute_software
from .libs.LogMessages import log_message, make_logger
from .libs.MeasureMetrics import make_metricsfile
from .libs.ParseArguments import get_arguments
from .libs.ParseCommands import get_commands
from .libs.ParseConfig import get_config


############ MAIN
def main():
    # Argument Options
    args = get_arguments()
    make_logger(args.logging)
    make_metricsfile(args.measure)

    log_message("Loading Configfile")
    config = get_config(args.configfile, args.format)
    log_message("Generating Commands")
    commands = get_commands(config)
    log_message("Executing Commands")
    execute_software(commands)

if __name__ == "__main__":
    main()
