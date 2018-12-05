from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.fileadmin import FileAdmin
from flask_babelex import Babel
from flask_security import SQLAlchemyUserDatastore, Security, UserMixin, RoleMixin, login_required
from importlib import import_module
from logging import basicConfig, DEBUG, getLogger, StreamHandler

import os.path as op


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()
flas_admin = Admin(name='smart-iiot')
babel = Babel()
security = Security()


# flask-login
# login_manager = LoginManager()
# login_manager.login_view = 'base.login'

# # flask-admin add views
# from app.admin import TestAdminView,  TemperatureModelView 

# #, UserModelView, UserAdminView, 

# # flas_admin.add_view(UserAdminView(name='UserAdmin', category='UserAdmin'))
# flas_admin.add_view(TestAdminView(name='test', endpoint='test', category='UserAdmin'))

# flas_admin.add_view(TemperatureModelView(db.session, name='Temperature', endpoint='daq_temperatures', category='DAQAdmin'))

# # flas_admin.add_view(UserModelView(db.session, name='User', endpoint='user', category='UserAdmin'))


path = op.join(op.dirname(__file__), 'static')
flas_admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    # bable config for i18n
    app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'


    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    configure_extensions(app)
    register_blueprints(app)
    configure_database(app)
    configure_logs(app)

    return app



def configure_extensions(app):
    """configure flask extensions
    """
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    # login_manager.init_app(app)
    pagedown.init_app(app)
    babel.init_app(app)
    flas_admin.init_app(app)

    from .models import User, Role
    # Setup Flask-Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)


def register_blueprints(app):
    """register all blueprints for application
    """
    for module_name in ('base', 'forms', 'ui', 'home', 'tables', 'additional', 'data', 'conf2d', 'conf3d', 'equipment', 'tickets'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)
        print('---register module:' + module_name)

    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix='/auth')
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()
        # user_datastore.create_user(email='252527676@qq.com', password='123456')
        # db.session.commit()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def configure_logs(app):
    basicConfig(filename='error.log', level=DEBUG)
    logger = getLogger()
    logger.addHandler(StreamHandler())

