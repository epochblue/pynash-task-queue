from pyqueue import Queue

queue = Queue()

job = queue.dequeue_job()
print('Job {job_id}: {result}'.format(job_id=job.id, result=job.result))
