import datetime
from demo.databases import db
from demo.databases import Model
from demo.databases import SurrogatePK


class AdminUser(SurrogatePK, Model):

    __tablename__ = "admin_user"

    mobile = db.Column(db.String(16), nullable=False, doc=u"钉钉手机号")
    password = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(32), nullable=False, doc=u"姓名")
    email = db.Column(db.String(32), nullable=False, doc=u"工作邮箱")
    department = db.Column(db.String(32), nullable=False, doc=u"所在部门")
    status = db.Column(db.Integer(), nullable=False, default=True, doc=u"是否在职")
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)