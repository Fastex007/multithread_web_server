from datetime import datetime


class ServiceMonitoring:
    """Мониторинт сервис"""

    def __init__(self) -> None:
        self.__request_count = 0
        self.__request_processing_total_time = 0

    def get_request_count(self) -> int:
        return self.__request_count

    def get_request_processing_total_time(self) -> float:
        return self.__request_processing_total_time

    def add_data(self, time: int) -> None:
        self.__request_count += 1
        self.__request_processing_total_time += time

    def reset_data(self) -> bool:
        self.__request_count = 0
        self.__request_processing_total_time = 0
        return True


def duration_monitoring(method):
    def wrapped(self, *args):
        start_time = datetime.now()
        method(self, *args)
        time_value = (datetime.now() - start_time).total_seconds()
        from run import Parameters
        Parameters.monitoring.add_data(time=time_value)
    return wrapped
