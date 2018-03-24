import redis

from pyqueue import Queue


r = redis.StrictRedis()
queue = Queue(r, 'pynash')

print('Starting worker...')
while True:
    print(' --> Waiting for work...')

    job = queue.dequeue_job()
    print('Job {job_id}: {result}'.format(job_id=job.id, result=job.result))
