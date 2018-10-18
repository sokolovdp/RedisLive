
from src.api.util import settings, timeutils
from datetime import datetime
import json


class StatsProvider:
    """A simple file based persistence to store and fetch stats
    """

    def __init__(self):
        self.filename = settings.get_dummy_stats_store()
        self.file = open(self.filename, 'w')

    def save_memory_info(self, server, timestamp, used, peak):
        """Saves used and peak memory stats,

        Args:
            server (str): The server ID
            timestamp (datetime): The time of the info.
            used (int): Used memory value.
            peak (int): Peak memory value.
        """
        data = {"server": server,
                "timestamp": str(timeutils.convert_to_epoch(timestamp)),
                "used": used,
                "peak": peak}
        self.file.write(json.dumps(data) + '\n')

    def save_info_command(self, server, timestamp, info):
        """Save Redis info command dump

        Args:
            server (str): id of server
            timestamp (datetime): Timestamp.
            info (dict): The result of a Redis INFO command.
        """
        data = {"server": server,
                "timestamp": str(timeutils.convert_to_epoch(timestamp)),
                "info": json.dumps(info)}
        self.file.write(json.dumps(data) + '\n')

    def save_monitor_command(self, server, timestamp, command, keyname):
        """save information about every command

        Args:
            server (str): Server ID
            timestamp (datetime): Timestamp.
            command (str): The Redis command used.
            keyname (str): The key the command acted on.
            argument (str): The args sent to the command.
        """
        data = {"server": server,
                "timestamp": str(timeutils.convert_to_epoch(timestamp)),
                "command": command,
                "keyname": keyname}
        self.file.write(json.dumps(data) + '\n')

    def get_info(self, server):
        """Get info about the server

        Args:
            server (str): The server ID
        """
        return ""

    def get_memory_info(self, server, from_date, to_date):
        """Get stats for Memory Consumption between a range of dates

        Args:
            server (str): The server ID
            from_date (datetime): Get memory info from this date onwards.
            to_date (datetime): Get memory info up to this date.
        """
        return ""

    def get_command_stats(self, server, from_date, to_date, group_by):
        """Get total commands processed in the given time period

        Args:
            server (str): The server ID
            from_date (datetime): Get data from this date.
            to_date (datetime): Get data to this date.
            group_by (str): How to group the stats.
        """

        return ""

    def get_top_commands_stats(self, server, from_date, to_date):
        """Get top commands processed in the given time period

        Args:
            server (str): Server ID
            from_date (datetime): Get stats from this date.
            to_date (datetime): Get stats to this date.
        """
        return ""

    def get_top_keys_stats(self, server, from_date, to_date):
        """Gets top comm processed

        Args:
            server (str): Server ID
            from_date (datetime): Get stats from this date.
            to_date (datetime): Get stats to this date.
        """
        return ""
