#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis


class RedisManager(object):
    _host = 'localhost'
    _port = 6379
    _db = 0
    _client = redis.StrictRedis(_host, _port, _db)

    @classmethod
    def redis_client(cls):

        return cls._client

    @classmethod
    def redis_setex(cls, key, value, ex=-1):
        cls._client.set(key, value, ex)

    @classmethod
    def redis_get(cls, key):

        return cls._client.get(key)

    @classmethod
    def redis_ttl(cls, key):

        return cls._client.ttl(key)


if __name__ == '__main__':

    RedisManager.redis_setex("night", "working!!!", 200)



