from pyqueue import Queue, count_words


queue = Queue()

job1_id = queue.enqueue_job(count_words, 'declaration-of-independence.txt')
print('Queued {}'.format(job1_id))

job2_id = queue.enqueue_job(count_words, 'us-constitution.txt', most_common=5)
print('Queued {}'.format(job2_id))


print('')
print('Queue: {}'.format(queue.queue))
print('')


job1 = queue.dequeue_job()
print('Job {job_id}: {result}'.format(job_id=job1.id, result=job1.result))

job2 = queue.dequeue_job()
print('Job {job_id}: {result}'.format(job_id=job2.id, result=job2.result))
