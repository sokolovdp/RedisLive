#! /usr/bin/env python

import redis
# from time import strftime
# import time
import random


def monitor():
    redis_host = "127.0.0.1"
    redis_port = 6379
    redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=0)

    while True:

        x = random.randint(1, 100)
        y = random.randint(1, 20)

        if y == 1:
            for z in range(1, x):
                redis_client.set("Key:" + 'x', x)
        elif y == 2:
            for z in range(1, x):
                redis_client.get("Key:" + 'x')
        elif y == 4:
            for z in range(1, x):
                redis_client.hset("HashKey:" + 'x', x, x)
        elif y == 5:
            for z in range(1, int((x / 2)) + 2):
                redis_client.setex("Key:" + 'x', 1000, x)
        elif y == 6:
            for z in range(1, x):
                redis_client.hexists("HashKey:" + 'x', y)
        elif y == 7:
            for z in range(1, x):
                redis_client.setbit("BitSet:" + 'x', 1, 1)
        elif y == 8:
            for z in range(1, x):
                redis_client.getbit("BitSet:" + 'x', 1)
        elif y == 9:
            for z in range(1, x):
                redis_client.expire("Key:" + 'x', 2000)
        elif y == 11:
            redis_client.flushall()


if __name__ == '__main__':
    monitor()
