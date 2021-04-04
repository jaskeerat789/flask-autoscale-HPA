import time

from app.app import celery


@celery.task(name="report", acks_late=True)
def report():
    print("Genrating report")
    """
    Emulating long running async task usning time.sleep
    """
    time.sleep(30)
    return {"state": "completed"}
