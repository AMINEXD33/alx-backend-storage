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

    def store(self, data: Union[str, bytes,  int,  float]) -> str:
        """store data and return the random unique key used to store it"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key
