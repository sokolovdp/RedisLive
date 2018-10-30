import datetime
from dateutil.parser import parse
import pytz

CURRENT_ZONE = pytz.timezone('Europe/Moscow')


def convert_to_epoch(timestamp):
    if type(timestamp) is datetime.date:
        timestamp = datetime.datetime.fromordinal(timestamp.toordinal())
    timestamp = timestamp.replace()
    diff = (timestamp - datetime.datetime(1970, 1, 1))
    seconds = int(diff.total_seconds())
    return seconds


def convert_time_string_to_datetime(timestr):
    if timestr[-1] == 'Z':
        datetime_value = CURRENT_ZONE.localize(parse(timestr, ignoretz=True))
    else:
        datetime_value = parse(timestr)
    return datetime_value
