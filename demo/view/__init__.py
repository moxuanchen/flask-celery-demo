from flask import Blueprint
from demo.models import AdminUser
from flask_login import UserMixin
from demo.extensions import login_manager


class LoginUser(UserMixin):
    def __init__(self, user):
        self.user = user

    def get_id(self):
        return self.user.id


@login_manager.user_loader
def load_user(userid):
    user = AdminUser.get_by_id(userid)
    return LoginUser(user)


xxx_blueprint = Blueprint('xxx', __name__, url_prefix="/xxx/", static_folder='static', template_folder='templates')
