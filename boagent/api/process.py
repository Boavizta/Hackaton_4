import json


class Process:
    def __init__(self, metrics_data, pid):
        self.metrics_data = metrics_data
        self.pid = pid
        self.processed_metrics = self.process_metrics()
        self.process_info = self.get_process_info()
        self.total_ram_in_bytes = self.get_total_ram_in_bytes()
        self.ram_shares = self.get_ram_shares()
        self.ram_embedded_impact_shares = self.get_component_embedded_impact_shares(
            "ram", self.ram_shares
        )
        self.cpu_load_shares = self.get_cpu_load_shares()
        self.cpu_embedded_impact_shares = self.get_component_embedded_impact_shares(
            "cpu", self.cpu_load_shares
        )

    def process_metrics(self):

        with open(self.metrics_data, "r") as metrics_data_file:
            metrics_data = json.load(metrics_data_file)

        return metrics_data

    def get_process_info(self):

        process_info = list()
        for timestamp in self.processed_metrics["raw_data"]["power_data"]["raw_data"]:
            for process in timestamp["consumers"]:
                if process["pid"] == self.pid:
                    process_info.append(process)
        return process_info

    def get_total_ram_in_bytes(self):

        ram_data = self.processed_metrics["raw_data"]["hardware_data"]["rams"]
        total_ram_in_bytes = (
            sum(ram_unit["capacity"] for ram_unit in ram_data) * 1073741824
        )

        return total_ram_in_bytes

    def get_ram_shares(self):
        process_ram_shares = list()
        for timestamp in self.process_info:
            process_ram_share = (
                int(timestamp["resources_usage"]["memory_usage"]) / self.total_ram_bytes
            )
            process_ram_shares.append(process_ram_share)

        return process_ram_shares

    def get_cpu_load_shares(self):

        process_cpu_load_shares = list()
        for timestamp in self.process_info:
            process_cpu_load_share = timestamp["resources_usage"]["cpu_usage"]
            process_cpu_load_shares.append(process_cpu_load_share)

        return process_cpu_load_shares

    def get_component_embedded_impact_shares(self, queried_component, component_shares):

        component = f"{queried_component.upper()}-1"
        component_impacts_data = self.processed_metrics["raw_data"]["boaviztapi_data"][
            "verbose"
        ][component]["impacts"]
        component_embedded_impact_shares = list()
        for impact in component_impacts_data:
            impact_embedded_value = component_impacts_data[impact]["embedded"]["value"]
            for process_component_share in component_shares:
                if process_component_share == 0.0:
                    component_embedded_impact = {
                        f"{impact}_embedded_share": process_component_share
                    }
                    component_embedded_impact_shares.append(component_embedded_impact)
                else:
                    component_embedded_impact_share = round(
                        impact_embedded_value * process_component_share, 2
                    )
                    component_embedded_impact = {
                        f"{impact}_embedded_share": component_embedded_impact_share
                    }
                    component_embedded_impact_shares.append(component_embedded_impact)
        return component_embedded_impact_shares
