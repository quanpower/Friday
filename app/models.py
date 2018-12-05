from datetime import datetime
import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app, request, url_for
from app.exceptions import ValidationError
from app import db
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
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(63))
    current_login_ip = db.Column(db.String(63))
    login_count = db.Column(db.Integer)

    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    projects = db.relationship('Project', backref='owner', lazy='dynamic')
    products = db.relationship('Product', backref='owner', lazy='dynamic')
    devices = db.relationship('Device', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.email


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
    product_pic = db.Column(db.String(500))
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



# db.create_all()