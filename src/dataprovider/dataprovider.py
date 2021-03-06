from src.api.util import settings
from . import redisprovider, sqliteprovider


class RedisLiveDataProvider:

    @staticmethod
    def get_provider():
        """Returns a data provider based on the settings file.

        Valid providers are currently Redis and SQLite.
        """
        data_store_type = settings.get_data_store_type()

        # FIXME: Should use a global variable for "redis" here.
        if data_store_type == "redis":
            return redisprovider.StatsProvider()
        elif data_store_type == "sqllite":
            return sqliteprovider.StatsProvider()
        else:
            print('No database provider in configuration!')
            exit(3)
