from src.dataprovider.dataprovider import RedisLiveDataProvider

from src.api.util.timeutils import convert_time_string_to_datetime

import tornado.web


class BaseController(tornado.web.RequestHandler):
    stats_provider = RedisLiveDataProvider.get_provider()

    def datetime_to_list(self, datetime):
        """Converts a datetime to a list.

        Args:
            datetime (datetime): The datetime to convert.
        """
        parsed_date = convert_time_string_to_datetime(datetime)
        # don't return the last two fields, we don't want them.
        return tuple(parsed_date.timetuple())[:-2]

    def average_data(self, data):
        """Averages data.

        TODO: More docstring here, once functionality is understood.
        """
        average = []

        deviation = 1024 * 1024

        start = convert_time_string_to_datetime(data[0][0])
        end = convert_time_string_to_datetime(data[-1][0])
        difference = end - start
        weeks, days = divmod(difference.days, 7)
        minutes, seconds = divmod(difference.seconds, 60)
        hours, minutes = divmod(minutes, 60)

        # TODO: These if/elif/else branches chould probably be broken out into
        # individual functions to make it easier to follow what's going on.
        if difference.days > 0:
            current_max = 0
            current_current = 0
            current_d = 0

            for dt, max_memory, current_memory in data:
                d = convert_time_string_to_datetime(dt)
                if d.day != current_d:
                    current_d = d.day
                    average.append([dt, max_memory, current_memory])
                    current_max = max_memory
                    current_current = current_memory
                else:
                    if max_memory > current_max or \
                            current_memory > current_current:
                        average.pop()
                        average.append([dt, max_memory, current_memory])
                        current_max = max_memory
                        current_current = current_memory
        elif hours > 0:
            current_max = 0
            current_current = 0
            current = -1
            keep_flag = False

            for dt, max_memory, current_memory in data:
                d = convert_time_string_to_datetime(dt)
                if d.hour != current:
                    current = d.hour
                    average.append([dt, max_memory, current_memory])
                    current_max = max_memory
                    current_current = current_memory
                    keep_flag = False
                elif abs(max_memory - current_max) > deviation or \
                        abs(current_memory - current_current) > deviation:
                    # average.pop()
                    average.append([dt, max_memory, current_memory])
                    current_max = max_memory
                    current_current = current_memory
                    keep_flag = True
                elif max_memory > current_max or \
                        current_memory > current_current:
                    if not keep_flag:
                        average.pop()
                    average.append([dt, max_memory, current_memory])
                    current_max = max_memory
                    current_current = current_memory
                    keep_flag = False
        else:
            current_max = 0
            current_current = 0
            current_m = -1
            keep_flag = False
            for dt, max_memory, current_memory in data:
                d = convert_time_string_to_datetime(dt)
                if d.minute != current_m:
                    current_m = d.minute
                    average.append([dt, max_memory, current_memory])
                    current_max = max_memory
                    current_current = current_memory
                    keep_flag = False
                elif abs(max_memory - current_max) > deviation or \
                        abs(current_memory - current_current) > deviation:
                    # average.pop()
                    average.append([dt, max_memory, current_memory])
                    current_max = max_memory
                    current_current = current_memory
                    keep_flag = True
                elif max_memory > current_max or \
                        current_memory > current_current:
                    if not keep_flag:
                        average.pop()
                    average.append([dt, max_memory, current_memory])
                    current_max = max_memory
                    current_current = current_memory
                    keep_flag = False

        return average
