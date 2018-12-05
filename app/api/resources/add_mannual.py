from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import json

import logging
from app import db, security
import random
import datetime, time
import bitstring

from app.models import User, Role, Project, Product, Device, Daq, Alarm


time_now = datetime.datetime.now()

class AddUser(Resource):
    def get(self):
        user_datastore = security.datastore

        try:
            
            admin = user_datastore.create_user(email='tester@qq.com', password='123456')
            # 生成普通用户角色和admin用户角色
            user_datastore.create_role(name='User', description='Generic user role')
            admin_role = user_datastore.create_role(name='Admin', description='Admin user role')
            # 为admin添加Admin角色
            user_datastore.add_role_to_user(admin, admin_role)

            db.session.commit()

            return 'insert ok'
        except Exception as e:
            log.error("Creating user: %s", e)
            db.session.rollback()
            return 'insert error'



class AddProject(Resource):
    def get(self):

        try:
            projects = list()
            projects.append(Project(user_id = 1, project_name='20180906', avatar='https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png',
                status='active', project_href='www.qq.com', percent=45, gmt_create=time_now, project_description='Second test projet'))

            db.session.add(projects[0])

            db.session.commit()
            return 'insert ok'
        except Exception as e:
            log.error("Creating projects: %s", e)
            db.session.rollback()
            return 'insert error'



class AddProduct(Resource):
    def get(self):

        try:
            products = list()
            products.append(Product(user_id=1, product_name='Handsome_1', product_key='a1nwrypxWbP', product_secret='', 
                data_format=0, node_type=0, aliyun_commodity_code='iothub' , gmt_create=time_now, product_description='HandSome_1'))

            db.session.add(products[0])

            db.session.commit()
            return 'insert ok'
        except Exception as e:
            log.error("Creating products: %s", e)
            db.session.rollback()
            return 'insert error'


class AddDevice(Resource):
    def get(self):

        try:
            devices = list()
            devices.append(Device(user_id=1, product_id=4, project_id=2, iot_id='', name='Handsome_1-test1', 
                device_name='05DCFF383939415351017542', device_secret='0XbeMGO7iuUAFhUJpR9ApWrjvzbXkY2h', 
                gmt_create=time_now, status='ONLINE', firmware_version='0.0.1', ip_address='117.136.8.234', node_type=0, region='华东 2'))

            db.session.add(devices[0])

            db.session.commit()
            return 'insert ok'
        except Exception as e:
            log.error("Creating devices: %s", e)
            db.session.rollback()
            return 'insert error'

        # id = db.Column(db.Integer, primary_key = True, autoincrement=True)
        # device_id = db.Column(db.Integer,db.ForeignKey('devices.id'))
        # gmt_daq = db.Column(db.DateTime())
        # daq_value = db.Column(db.JSON)

        # for i in range(1, 100):
        #     gt = Daq()

        #     gt.device_id = 1
        #     gt.gmt_daq = datetime.datetime.utcnow()
        #     gt.daq_value = json.dumps([[str(x), round(random.uniform(25,30),2)] for x in range(16)])

        #     db.session.add(gt)

        #     try:
        #         db.session.commit()
        #         print("inserted", gt)
        #     except Exception as e:
        #         log.error("Creating Daq: %s", e)
        #         db.session.rollback()

        # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        # device_id = db.Column(db.Integer,db.ForeignKey('devices.id'))
        # gmt_alarm = db.Column(db.DateTime)
        # alarm_value = db.Column(db.JSON)

