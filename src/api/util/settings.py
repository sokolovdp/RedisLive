import os
import json


def get_settings():
    """Parses the settings from redis-live-conf.json.
    """
    # TODO: Consider YAML. Human writable, machine readable.
    with open(os.getenv("REDISLIVE_CONFIG", "redis-live-conf.json")) as config:
        return json.load(config)


def get_redis_servers():
    config = get_settings()
    return config["RedisServers"]


def get_redis_stats_server():
    config = get_settings()
    return config["RedisStatsServer"]


def get_data_store_type():
    config = get_settings()
    return config["DataStoreType"]


def get_sqlite_stats_store():
    config = get_settings()
    return config["SqliteStatsStore"]


def get_dummy_stats_store():
    config = get_settings()
    return config["DummyStatsStore"]["filename"]
