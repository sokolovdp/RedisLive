import datetime


def convert_to_epoch(timestamp):
    if type(timestamp) is datetime.date:
        timestamp = datetime.datetime.fromordinal(timestamp.toordinal())
    timestamp = timestamp.replace(tzinfo=None)
    diff = (timestamp - datetime.datetime(1970, 1, 1))
    seconds = int(diff.total_seconds())
    return seconds
