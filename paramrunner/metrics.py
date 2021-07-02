from datetime import datetime

class Metrics:
    def __init__(self, measure:int, timestamp) -> None:
        self.measure = measure

        self.timestamp = timestamp
        self.metrics = None

        if self.measure > 0:
            self._create_metrics()
    
    def _create_metrics(self) -> None:
        if self.timestamp == None:
            self._create_timestamp()
        self.metrics = f"ParamRunner_Metrics_{self.timestamp}.csv"

    def _create_timestamp(self) -> None:
        self.timestamp = datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

    def write_header_line(self, params:list) -> None:
        self.header_info = f"Run,{','.join(params)}"
        header = f"{self.header_info},Elapsed Time,CPU Usage,Average Memory,Max Memory,Exit Status"
        with open(self.metrics, "w") as file:
            file.write(header)
