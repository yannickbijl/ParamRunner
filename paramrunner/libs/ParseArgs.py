import argparse

def check_positive(value:str) -> int:
    int_value = int(value)
    if int_value <= 0:
        raise argparse.ArgumentTypeError(f"{value} is an invalid int value")
    return int_value

########### Parse input arguments
def parse_args() -> list:
    # Argument Options
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest='configfile', type=str, required=True, help="CSV formatted file with user settings.")
    parser.add_argument('-m', '--measure', dest='measure', type=check_positive, required=False, default=0, help="Number of times command with same parameter settings must be run to measure performance.")
    return(parser.parse_args())
