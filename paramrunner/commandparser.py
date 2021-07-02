from typing import Union

class Command:
    def __init__(self, config, metrics, logger) -> None:
        self.config = config
        self.metrics = metrics
        self.logger = logger
        self.commands = []
        
        if self.metrics.measure > 0:
            self.metrics.write_header_line(self.config["params"])
        self._generate_commands()

    def get_commands(self) -> None:
        return self.commands

    def _generate_commands(self):
        param_length = len(self.config[self.config["params"][0]])
        for item in range(param_length):
            param_value = {key: self.config[key][item] for key in self.config["params"]}
            command = self._generate_base_command(param_value)
            if self.metrics.measure > 0:
                command = self._generate_measure_command(command, param_value)
            self._add_command(command)
    
    def _generate_base_command(self, param_value:dict) -> str:
        for param in param_value.keys():
            command = self.config["command"].replace(f"{'{' + param + '}'}", str(param_value[param]))
        return command

    def _generate_measure_command(self, command:str, param_value:dict) -> list:
        commands = []
        line_info = self._create_lineinfo(param_value)
        for run in range(self.metrics.measure):
            line_info = line_info.replace("Run", str(run+1))
            commands.append(f"command time -a -o {self.metrics.metrics} -f {line_info} {command}")
        return commands

    def _create_lineinfo(self, param_value:dict) -> str:
        command_info = self.metrics.header_info
        for param in param_value.keys():
            command_info = command_info.replace(param, param_value[param])
        return f"{command_info},%E,%P,%K,%M,%x"

    def _add_command(self, command:Union[str,list]):
        if isinstance(command, str) == True:
            self.commands.append(command)
        else:
            for com in command:
                self.commands.append(com)

