from datetime import datetime, timedelta
from dateutil.parser import parse

CURRENT_ZONE_OFFSET = +3


def convert_to_epoch(timestamp):
    if type(timestamp) is datetime.date:
        timestamp = datetime.fromordinal(timestamp.toordinal())
    timestamp = timestamp.replace()
    diff = (timestamp - datetime(1970, 1, 1))
    seconds = int(diff.total_seconds())
    return seconds


def convert_time_string_to_datetime(timestr):
    if timestr[-1] == 'Z':
        datetime_value = parse(timestr) + timedelta(hours=CURRENT_ZONE_OFFSET)
    else:
        datetime_value = parse(timestr)
    return datetime_value
