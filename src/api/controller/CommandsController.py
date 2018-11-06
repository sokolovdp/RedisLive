from .BaseController import BaseController

from datetime import datetime, timedelta

from src.api.util.timeutils import convert_time_string_to_datetime


class CommandsController(BaseController):

    def get(self):
        """Serves a GET request.
        """
        return_data = dict(data=[], timestamp=datetime.now().isoformat())

        server = self.get_argument("server")
        from_date = self.get_argument("from", None)
        to_date = self.get_argument("to", None)

        if not from_date or not to_date:
            end = datetime.now()
            delta = timedelta(seconds=120)
            start = end - delta
        else:
            start = convert_time_string_to_datetime(from_date)
            end = convert_time_string_to_datetime(to_date)

        difference = end - start
        difference_total_seconds = difference.total_seconds()

        minutes = int(difference_total_seconds // 60)
        hours = int(minutes // 60)
        seconds = int(difference_total_seconds)

        if hours > 120:
            group_by = "day"
        elif minutes > 120:
            group_by = "hour"
        elif seconds > 120:
            group_by = "minute"
        else:
            group_by = "second"

        combined_data = []
        stats = self.stats_provider.get_command_stats(server, start, end, group_by)
        for data in stats:
            combined_data.append([data[1], data[0]])

        for data in combined_data:
            return_data['data'].append([self.datetime_to_list(data[0]), data[1]])

        self.write(return_data)
