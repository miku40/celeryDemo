from celery import Celery

app = Celery('demo',broker='redis://localhost',backend='redis://localhost')

@app.task
def run():
    return 1+2