from apscheduler.scheduler import Scheduler

# Start the scheduler
sched = Scheduler()
sched.start()

def job_function():
	print("Hello World")

sched.add_cron_job(job_function, hour=0)

while (42):
	pass