#!/usr/bin/env python3
"""this module has a class cache that
implements some basic ideas of caching"""
import redis
from uuid import uuid4
from typing import Any, Callable, Optional, Union
from functools import wraps

"""
    a cache implementation
"""


def count_calls(method: Callable) -> Callable:
    """counts the number of times a method has been called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the history of inputs and outputs for a method"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        input = str(args)
        self._redis.rpush(f"{method.__qualname__}:inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(f"{method.__qualname__}:outputs", output)

        return output

    return wrapper


def replay(fn: Callable) -> None:
    """Check redis for how many times a function was called and display:
    - How many times it was called
    - Function args and output for each call
    """
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode("utf-8")
    inputs = [
        input.decode("utf-8")
        for input in client.lrange(f"{fn.__qualname__}:inputs", 0, -1)
    ]
    outputs = [
        output.decode("utf-8")
        for output in client.lrange(f"{fn.__qualname__}:outputs", 0, -1)
    ]
    print(f"{fn.__qualname__} was called {calls} times:")
    for input, output in zip(inputs, outputs):
        print(f"{fn.__qualname__}(*{input}) -> {output}")


class Cache:
    def __init__(self) -> None:
        """a constructor function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data and return the random unique key used to store it"""
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
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

    def get_int(self, value: bytes) -> int:
        """this function convert data from bytes to int"""
        return int(value)

    def get_str(self, value: bytes) -> str:
        """this function convert data from bytes to str"""
        return value.decode("utf-8")
