from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
from app.exceptions import ValidationError
from app import db, login_manager
from sqlalchemy.dialects.mysql import JSON


from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required

# Define models
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('users.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('roles.id')))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    projects = db.relationship('Project', backref='owner', lazy='dynamic')
    products = db.relationship('Product', backref='owner', lazy='dynamic')
    devices = db.relationship('Device', backref='owner', lazy='dynamic')
    bugs = db.relationship('Bug', backref='tester', lazy='dynamic')
    bug_comments = db.relationship('BugComment', backref='author', lazy='dynamic')



class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    project_name = db.Column(db.String(100))
    avatar = db.Column(db.String(100),nullable = False)
    status = db.Column(db.String(20))
    project_href = db.Column(db.String(100))
    percent = db.Column(db.Integer)
    gmt_create = db.Column(db.DateTime())
    gmt_update = db.Column(db.DateTime())
    project_description = db.Column(db.String(500))
    devices = db.relationship('Device', backref='project', lazy='dynamic')


    def __repr__(self):
        return str(self.project_name)     



class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer,primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    product_name = db.Column(db.String(100),nullable = False)
    product_key = db.Column(db.String(100),nullable = False)
    product_secret = db.Column(db.String(100))
    data_format = db.Column(db.Integer, nullable = False)
    node_type = db.Column(db.Integer, nullable = False)
    aliyun_commodity_code = db.Column(db.String(100))
    gmt_create = db.Column(db.DateTime())
    gmt_update = db.Column(db.DateTime())

    product_description = db.Column(db.String(500))
    devices = db.relationship('Device',backref='product', lazy='dynamic')

    def __repr__(self):
        return str(self.product_name) 


class Device(db.Model):
    __tablename__ = 'devices'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer,db.ForeignKey('products.id'))
    project_id = db.Column(db.Integer,db.ForeignKey('projects.id'))
    name = db.Column(db.String(100), nullable = False)
    iot_id = db.Column(db.String(100))
    device_name = db.Column(db.String(100), nullable = False)
    device_secret = db.Column(db.String(100), nullable = False)
    gmt_create = db.Column(db.DateTime())
    gmt_active = db.Column(db.DateTime())
    gmt_online = db.Column(db.DateTime())
    status = db.Column(db.String(20))
    firmware_version = db.Column(db.String(20))
    ip_address = db.Column(db.String(30))
    node_type = db.Column(db.Integer, nullable = False)
    region = db.Column(db.String(100))
    daq = db.relationship('Daq',backref='device', lazy='dynamic')
    alarm = db.relationship('Alarm',backref='device', lazy='dynamic')

    def __repr__(self):
        return str(self.name) 


class Daq(db.Model):
    __tablename__ = 'daqs'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    device_id = db.Column(db.Integer,db.ForeignKey('devices.id'))
    gmt_daq = db.Column(db.DateTime())
    daq_value = db.Column(db.JSON)

    def __repr__(self):
        return str(self.id) 


class Alarm(db.Model):
    __tablename__ = 'daq_alarm'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    device_id = db.Column(db.Integer,db.ForeignKey('devices.id'))
    gmt_alarm = db.Column(db.DateTime)
    alarm_value = db.Column(db.JSON)

    def __repr__(self):
        return str(self.device_id)


class BugOrderOfSeverity(db.Model):
    __tablename__ = 'bug_order_of_severity'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable = False, unique=True)
    name_en = db.Column(db.String(20), nullable = False, unique=True)
    bugs = db.relationship('Bug', backref='severity', lazy='dynamic')

    def __repr__(self):
        return str(self.severity_name)


class BugPriority(db.Model):
    __tablename__ = 'bug_priority'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable = False, unique=True)
    name_en = db.Column(db.String(20), nullable = False, unique=True)
    bugs = db.relationship('Bug', backref='priority', lazy='dynamic')


    def __repr__(self):
        return str(self.name)


class Models(db.Model):
    __tablename__ = 'models'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable = False, unique=True)
    bugs = db.relationship('Bug', backref='models', lazy='dynamic')


    def __repr__(self):
        return str(self.name)


class Version(db.Model):
    __tablename__ = 'versions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable = False, unique=True)
    bugs = db.relationship('Bug', backref='versions', lazy='dynamic')


    def __repr__(self):
        return str(self.name)


class TestingEnvironment(db.Model):
    __tablename__ = 'testing_environment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable = False, unique=True)
    bugs = db.relationship('Bug', backref='environment', lazy='dynamic')


    def __repr__(self):
        return str(self.name)


class BugStatus(db.Model):
    __tablename__ = 'bug_status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable = False, unique=True)
    name_en = db.Column(db.String(50), nullable = False, unique=True)
    bugs = db.relationship('Bug', backref='status', lazy='dynamic')


    def __repr__(self):
        return str(self.name)


class Bug(db.Model):
    __tablename__ = 'bugs'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(100), nullable = False)
    order_of_severity_id = db.Column(db.Integer,db.ForeignKey('bug_order_of_severity.id'))
    priority_id = db.Column(db.Integer,db.ForeignKey('bug_priority.id'))
    model_id = db.Column(db.Integer,db.ForeignKey('models.id'))
    version_id = db.Column(db.Integer,db.ForeignKey('versions.id'))
    testing_environment_id = db.Column(db.Integer,db.ForeignKey('testing_environment.id'))
    developer_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    tester_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    status_id = db.Column(db.Integer,db.ForeignKey('bug_status.id'))
    procedure_description = db.Column(db.String(1000), nullable = False)
    expected_result = db.Column(db.String(100))
    actual_result = db.Column(db.String(100))
    gmt_bug = db.Column(db.DateTime(), default=datetime.utcnow())
    gmt_report = db.Column(db.DateTime(), default=datetime.utcnow())
    screenshot = db.Column(db.JSON)
    reason = db.Column(db.String(200))
    solution = db.Column(db.String(300))
    note = db.Column(db.String(300))
    bug_comment = db.relationship('BugComment',backref='bug', lazy='dynamic')
    # resolve sqlalchemy.exc.AmbiguousForeignKeysError:
    developer = db.relationship("User", foreign_keys=[developer_id])
    tester = db.relationship("User", foreign_keys=[tester_id])

    def __repr__(self):
        return str(self.title) 


class BugComment(db.Model):
    __tablename__ = 'bug_comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    bug_id = db.Column(db.Integer,db.ForeignKey('bugs.id'))
    comment = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return str(self.comment)


# db.create_all()