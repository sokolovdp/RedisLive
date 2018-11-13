#! /usr/bin/env python

import redis


# from time import strftime
# import time
# import random

def monitor():
    redis_host = "10.201.67.22"
    redis_port = 6363
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    while True:
        x = 1
        redis_client.set("Key:" + 'x', x)
        redis_client.set("KeyYU:" + 'x', x)
        redis_client.set("Key:" + 'x', x)
        redis_client.set("KeyYU:" + 'x', x)


if __name__ == '__main__':
    monitor()
