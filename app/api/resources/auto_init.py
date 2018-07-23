from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import json

import logging
from app import db, security
import random
import datetime, time
import bitstring

from app.models import User, Role, Project, Product, Device, Daq, Alarm


class AutoInit(Resource):
    def get(self):

        log = logging.getLogger(__name__)

        time_now = datetime.datetime.utcnow()

        user_datastore = security.datastore

        try:
            
            admin = user_datastore.create_user(email='252527676@qq.com', password='123456')
            # 生成普通用户角色和admin用户角色
            user_datastore.create_role(name='User', description='Generic user role')
            admin_role = user_datastore.create_role(name='Admin', description='Admin user role')
            # 为admin添加Admin角色
            user_datastore.add_role_to_user(admin, admin_role)

            db.session.commit()
        except Exception as e:
            log.error("Creating user: %s", e)
            db.session.rollback()

        # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        # user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        # project_name = db.Column(db.String(100))
        # avatar = db.Column(db.String(100),nullable = False)
        # status = db.Column(db.String(20))
        # project_href = db.Column(db.String(100))
        # percent = db.Column(db.Integer)
        # gmt_create = db.Column(db.DateTime())
        # gmt_update = db.Column(db.DateTime())
        # project_description = db.Column(db.String(500))
        # devices = db.relationship('Device', backref='project', lazy='dynamic')

        try:
            projects = list()
            projects.append(Project(user_id = 1, project_name='20180723', avatar='https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png',
                status='active', project_href='www.baidu.com', percent=75, gmt_create=time_now, project_description='First test projet'))

            db.session.add(projects[0])

            db.session.commit()
        except Exception as e:
            log.error("Creating projects: %s", e)
            db.session.rollback()


        # id = db.Column(db.Integer,primary_key = True, autoincrement=True)
        # user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        # product_name = db.Column(db.String(100),nullable = False)
        # product_key = db.Column(db.String(100),nullable = False)
        # product_secret = db.Column(db.String(100))
        # data_format = db.Column(db.Integer, nullable = False)
        # node_type = db.Column(db.Integer, nullable = False)
        # aliyun_commodity_code = db.Column(db.String(100))
        # gmt_create = db.Column(db.DateTime())
        # gmt_update = db.Column(db.DateTime())

        # product_description = db.Column(db.String(500))
        # devices = db.relationship('Device',backref='product', lazy='dynamic')

        try:
            products = list()
            products.append(Product(user_id=1, product_name='绎捷无纸记录仪', product_key='a14MQd3lS1y', product_secret='', 
                data_format=0, node_type=0, aliyun_commodity_code='iothub' , gmt_create=time_now, product_description='yijie_recorder product_description'))

            db.session.add(products[0])

            db.session.commit()
        except Exception as e:
            log.error("Creating products: %s", e)
            db.session.rollback()

        # id = db.Column(db.Integer, primary_key = True, autoincrement=True)
        # user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        # product_id = db.Column(db.Integer,db.ForeignKey('products.id'))
        # project_id = db.Column(db.Integer,db.ForeignKey('projects.id'))
        # name = db.Column(db.String(100), nullable = False)
        # iot_id = db.Column(db.String(100))
        # device_name = db.Column(db.String(100), nullable = False)
        # device_secret = db.Column(db.String(100), nullable = False)
        # gmt_create = db.Column(db.DateTime())
        # gmt_active = db.Column(db.DateTime())
        # gmt_online = db.Column(db.DateTime())
        # status = db.Column(db.String(20))
        # firmware_version = db.Column(db.String(20))
        # ip_address = db.Column(db.String(30))
        # node_type = db.Column(db.Integer, nullable = False)
        # region = db.Column(db.String(100))
        # daq = db.relationship('Daq',backref='device', lazy='dynamic')
        # alarm = db.relationship('Alarm',backref='device', lazy='dynamic')

        try:
            devices = list()
            devices.append(Device(user_id=1, product_id=1, project_id=1, iot_id='', name='绎捷无纸记录仪test1', 
                device_name='yj_recoder_test1', device_secret='XxcAmTt8H6f5MP5l4nhoyK9t8x5JqOek', 
                gmt_create=time_now, status='ONLINE', firmware_version='0.0.1', ip_address='117.132.196.24', node_type=0, region='华东 2'))

            db.session.add(devices[0])

            db.session.commit()
        except Exception as e:
            log.error("Creating devices: %s", e)
            db.session.rollback()

        # id = db.Column(db.Integer, primary_key = True, autoincrement=True)
        # device_id = db.Column(db.Integer,db.ForeignKey('devices.id'))
        # gmt_daq = db.Column(db.DateTime())
        # daq_value = db.Column(db.JSON)

        for i in range(1, 100):
            gt = Daq()

            gt.device_id = 1
            gt.gmt_daq = datetime.datetime.utcnow()
            gt.daq_value = json.dumps([[str(x), round(random.uniform(25,30),2)] for x in range(16)])

            db.session.add(gt)

            try:
                db.session.commit()
                print("inserted", gt)
            except Exception as e:
                log.error("Creating Daq: %s", e)
                db.session.rollback()

        # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        # device_id = db.Column(db.Integer,db.ForeignKey('devices.id'))
        # gmt_alarm = db.Column(db.DateTime)
        # alarm_value = db.Column(db.JSON)

        try:
            alarms = list()
            alarms.append(Alarm(device_id=1, gmt_alarm=datetime.datetime.utcnow(),
             alarm_value=json.dumps([[str(x), random.choice(['0', '1'])] for x in range(16)])))

            db.session.add(alarms[0])

            db.session.commit()
        except Exception as e:
            log.error("Creating alarms: %s", e)
            db.session.rollback()


        return jsonify({'success': 'auto insert init datas!'})
