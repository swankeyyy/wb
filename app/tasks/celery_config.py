from celery import Celery

celery_app = Celery(
    'tasks',
    broker='redis://localhost:6379/0',
    backend='redis://localhost:6379/0',
    include=['tasks']
)

celery_app.conf.update(
    # task_serializer='json',
    # result_serializer='json',
    # accept_content=['json'],
    # timezone='UTC',
    # enable_utc=True,
    broker_connection_retry_on_startup=True
)