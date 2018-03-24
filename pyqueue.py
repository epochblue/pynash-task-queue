import pickle
import uuid


class Queue(object):
    def __init__(self, conn, queue_key):
        self.conn = conn
        self.queue_key = queue_key

    def enqueue_job(self, func, *args, **kwargs):
        job = Job(func, *args, **kwargs)
        compact_job = pickle.dumps(job, protocol=pickle.HIGHEST_PROTOCOL)
        self.conn.lpush(self.queue_key, compact_job)
        return job.id

    def dequeue_job(self):
        compact_job = self.conn.rpop(self.queue_key)
        job = pickle.loads(compact_job)
        job.execute()
        return job


class Job(object):
    def __init__(self, func, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.result = None

    def execute(self):
        self.result = self.func(*self.args, **self.kwargs)
