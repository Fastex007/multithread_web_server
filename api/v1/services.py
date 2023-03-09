from datetime import datetime


def get_iso_8601_datetime():
    return datetime.now().isoformat()
