from demo.app import create_app
from demo.models import AdminUser
from demo.extensions import celery


app = create_app()
celery.conf.update(
    broker_url=app.config["CELERY_BROKER_URL"],
    result_backend=app.config["CELERY_RESULT_BACKEND"]
)


@celery.task()
def do_async_task_xxx(user_id, **kwargs):
    with app.app_context():
        user = AdminUser.get_by_id(user_id)
        user.update(**kwargs)
