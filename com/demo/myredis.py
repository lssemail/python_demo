#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class RedisManager(object):

    def __init__(self):
        print("init")
        self._host = 'localhost'
        self._port = 6379
        self._db = 0
        self._decode_responses = True
        self._client = redis.StrictRedis(self._host, self._port, self._db)

    def redis_client(self):

        return self._client

    def redis_setex(self, key, value, ex=-1):

        self._client.set(key, value, ex)

    def redis_get(self, key):

        return self._client.get(key)

    def redis_ttl(self, key):

        return self._client.ttl(key)


if __name__ == '__main__':

    key1 = "redis_python_1"
    print(RedisManager().redis_ttl(key1))



