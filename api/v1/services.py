from datetime import datetime

from config import Parameters


def get_iso_8601_datetime():
    return datetime.now().isoformat()


def get_monitoring_data():
    return {
        "queries": Parameters.monitoring.get_request_count(),
        "seconds": Parameters.monitoring.get_request_processing_total_time(),
    }
