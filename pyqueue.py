import os
import uuid
from collections import Counter


def count_words(filename, most_common=10):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    with open(os.path.join(data_dir, filename), 'r') as f:
        word_count = Counter(f.read().split())
    return dict(word_count.most_common(most_common))


class Queue(object):
    def __init__(self):
        self.queue = list()

    def enqueue_job(self, func, *args, **kwargs):
        job = Job(func, *args, **kwargs)
        self.queue.append(job)
        return job.id

    def dequeue_job(self):
        job = self.queue.pop(0)
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
