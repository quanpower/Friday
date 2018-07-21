from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app.models import Daq
import flask_login as login


class TemperatureModelView(ModelView):
    def __init__(self, session, **kwargs):
        # You can pass name and other parameters if you want to
        super(TemperatureModelView, self).__init__(Daq, session, **kwargs)
    def is_accessible(self):
        return login.current_user.is_authenticated


