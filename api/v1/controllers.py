import random
from time import sleep

from api.v1.services import get_iso_8601_datetime, get_monitoring_data


def index() -> dict:
    from core.urls import router
    result = {
        "links": [url for url in router.keys()]
    }
    return result


def heave_calculation() -> dict:
    sleep_time = random.randint(1, 5)
    sleep(sleep_time)
    result = {
        "current_date": get_iso_8601_datetime(),
        "response_took_seconds": sleep_time,
    }
    return result


def request_count() -> dict:
    monitoring_data = get_monitoring_data()
    result = {
        "total": monitoring_data,
    }
    return result
