from fastapi import Depends

import rq
from rq.job import Job

from api.app import config
from api.app.cache import Cache

settings = config.get_settings()


class BackgroundTask:
    def __init__(self, cache: Cache = Depends()):
        self.redis_conn = cache.client
        self.queue = rq.Queue("my_queue", connection=self.redis_conn)

    def run_in_queue(self, f, *args) -> Job:
        return self.queue.enqueue(f, args=args, ttl=20)

    def get_job_by_id(self, job_id) -> Job:
        return self.queue.fetch_job(job_id)
