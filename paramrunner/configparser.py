import csv
import json
import os
import re

import yaml


class Config:
    def __init__(self, configfile:str, configformat:str, logger) -> None:
        self.logger = logger
        self.configfile = configfile
        self.configformat = configformat

        self._check_configfile()
        self._parse_config()
        self._check_config()

    def get_config(self) -> dict:
        return self.config

    def _get_function_dict(self) -> dict:
        return {"csv":self._parse_csv, "tsv":self._parse_tsv, "json":self._parse_json,
                "yml":self._parse_yaml, "yaml":self._parse_yaml}
    
    def _parse_params_from_command(self) -> None:
        self.config["params"] = tuple(dict.fromkeys(re.findall("\{(.*?)\}", self.config["command"])))

    def _check_configfile(self) -> None:
        self._check_path_exist()
        self._check_file_exist()
        self._check_format()
    
    def _check_path_exist(self) -> None:
        if not os.path.exists(self.configfile):
            self.logger.log_error("Invalid path to configfile.")
            raise FileNotFoundError("Invalid path to configfile.")

    def _check_file_exist(self) -> None:
        if not os.path.isfile(self.configfile):
            self.logger.log_error("Configfile does not exist.")
            raise FileNotFoundError("Configfile does not exist.")

    def _check_format(self) -> None:
        if self.configformat == "":
            self.configformat = os.path.splitext(self.configfile)[1][1:]  # Use [1:] to get everything but the first character '.' so .csv becomes csv
        if self.configformat not in self._get_function_dict().keys():
            self.logger.log_error(f"The file format {self.configformat} is not supported.")
            raise ValueError(f"The file format {self.configformat} is not supported.")

    def _parse_config(self) -> None:
        self.logger.log_message(f"File {self.configfile} can be opened")
        self.config = self._get_function_dict().get(self.configformat)()  # Equivalent to 'config = parse_<format>()'

    def _parse_csv(self) -> dict:
        self.logger.log_message("Parsing file {self.configfile} in csv format.")
        data = dict()
        with open(self.configfile) as file:
            reader = csv.reader(file)
            for row in reader:
                data[row[0]] = row[1:]
        return data

    def _parse_tsv(self) -> dict:
        self.logger.log_message("Parsing file {self.configfile} in tsv format.")
        data = dict()
        with open(self.configfile) as file:
            reader = csv.reader(file, delimiter="\t")
            for row in reader:
                data[row[0]] = row[1:]
        return data

    def _parse_json(self) -> dict:
        self.logger.log_message("Parsing file {self.configfile} in json format.")
        with open(self.configfile) as file:
            data = json.load(file)
        return data

    def _parse_yaml(self) -> dict:
        self.logger.log_message("Parsing file {self.configfile} in yaml format.")
        with open(self.configfile) as file:
            data = yaml.full_load(file)
        return data
    
    def _check_config(self) -> None:
        self._check_presence_command()
        self._check_type_command()
        self._parse_params_from_command()
        self._check_presence_params()
        self._check_length_params()

    def _check_presence_command(self) -> None:
        if "command" not in self.config.keys():
            self.logger.log_error("The required field 'command' is not present in the configfile.")
            raise KeyError("The required field 'command' is not present in the configfile.")

    def _check_type_command(self):
        if isinstance(self.config["command"], list) == True:
            self.logger.log_message("")
            self.config["command"] = str(self.config["command"][0])

    def _check_presence_params(self) -> None:
        for param in self.config["params"]:
            if param not in self.config["command"]:
                self.logger.log_error("The field for parameter '{param}' is not present in the configfile.")
                raise ValueError("The field for parameter '{param}' is not present in the configfile.")

    def _check_length_params(self) -> None:
        params_lists = {key: self.config[key] for key in self.config["params"]}
        if len(set(map(len, params_lists.values()))) != 1: # Ensure all params lists are of the same length
            self.logger.log_error("Not all parameters have an equal number of values.")
            raise ValueError("Not all parameters have an equal number of values.")
