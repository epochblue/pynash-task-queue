import redis

from pyqueue import Queue
from tasks import count_words


r = redis.StrictRedis()
queue = Queue(r, 'pynash')

job1_id = queue.enqueue_job(count_words, 'declaration-of-independence.txt')
print('Queued {}'.format(job1_id))

job2_id = queue.enqueue_job(count_words, 'us-constitution.txt', most_common=5)
print('Queued {}'.format(job2_id))
