import datetime
from .BaseController import BaseController

from src.api.util.timeutils import convert_time_string_to_datetime


class TopCommandsController(BaseController):

    def get(self):
        return_data = dict(data=[], timestamp=datetime.datetime.now().isoformat())

        server = self.get_argument("server")
        from_date = self.get_argument("from", None)
        to_date = self.get_argument("to", None)

        if not from_date or not to_date:
            end = datetime.datetime.now()
            delta = datetime.timedelta(seconds=120)
            start = end - delta
        else:
            start = convert_time_string_to_datetime(from_date)
            end = convert_time_string_to_datetime(to_date)

        for data in self.stats_provider.get_top_commands_stats(server, start, end):
            return_data['data'].append([data[0], data[1]])

        self.write(return_data)
