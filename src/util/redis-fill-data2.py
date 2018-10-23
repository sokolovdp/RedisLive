#! /usr/bin/env python

import redis


# from time import strftime
# import time
# import random

def monitor():
    redisHost = "10.201.67.22"
    redisPort = 6363
    redisClient = redis.StrictRedis(host=redisHost, port=redisPort, db=0)

    while True:
        x = 1
        redisClient.set("Key:" + 'x', x)
        redisClient.set("KeyYU:" + 'x', x)
        redisClient.set("Key:" + 'x', x)
        redisClient.set("KeyYU:" + 'x', x)


if __name__ == '__main__':
    monitor()
