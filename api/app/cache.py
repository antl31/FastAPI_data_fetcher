import json

import redis

from api.app import config

settings = config.get_settings()


class Cache:
    def __init__(self):
        self.client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
        )

    def get(self, key):
        val = self.client.get(key)
        try:
            return json.loads(val)
        except (json.decoder.JSONDecodeError, TypeError):
            return val

    def create(self, key, value):
        if isinstance(value, str):
            return self.client.set(key, value)
        if isinstance(value, (list, dict)):
            self.client.set(key, json.dumps(value, default=str))

    def delete(self, key):
        return self.client.delete(key)
