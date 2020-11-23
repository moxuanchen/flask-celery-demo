from flask import request
from demo.models import AdminUser
from async_worker import do_async_task_xxx
from . import xxx_blueprint


@xxx_blueprint.route("/async/task/xxx", methods=["POST"])
def user_update():
    data = request.json or {}
    user_id = data.get("user_id")
    do_async_task_xxx(user_id, **data)
    return "well done."