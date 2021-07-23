from celery import Celery
import celery

#필요한 rabbitmq의 주소를 dev/ prod 에 맞게 설정필요
# amqp://[username]:[password]@localhost:5672/
BROKER_URL = 'amqp://admin:admin@localhost/vhost-01'

def make_celery(app):
    cell =  Celery(app.import_name, broker=BROKER_URL, backend='amqp://admin:admin@localhost/vhost-01')
    TaskBase = cell.Task

    class ContextTask(TaskBase):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    cell.Task = ContextTask
    return cell