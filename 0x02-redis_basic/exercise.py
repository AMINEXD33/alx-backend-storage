#!/usr/bin/env python3
"""this module has a class cache that
implements some basic ideas of caching"""
import redis
from uuid import uuid4
from typing import Any, Callable, Optional, Union

"""
    a cache implementation
"""


class Cache:
    def __init__(self) -> None:
        """a constructor function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data and return the random unique key used to store it"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """this function gets a value from redis with respect to the type"""
        value = self._redis.get(key)
        if not value:
            return None
        elif fn is int:
            return self.get_int(value)
        elif fn is str:
            return self.get_str(value)
        elif callable(fn):
            return fn(value)
        return value

    @staticmethod
    def get_int(self, value: bytes) -> int:
        """this function convert data from bytes to int"""
        return int(value)

    @staticmethod
    def get_str(self, value: bytes) -> str:
        """this function convert data from bytes to str"""
        return value.decode("utf-8")
