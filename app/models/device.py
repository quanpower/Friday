from sqlalchemy.dialects.mysql import JSON
from app import db, login_manager
from .user import User


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
    data_format = db.Column(db.Integer, nullable = False)
    node_type = db.Column(db.Integer, nullable = False)
    aliyun_commodity_code = db.Column(db.String(100))
    gmt_create = db.Column(db.DateTime())
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

