from flasgger import Swagger, swag_from
from flask import Flask, redirect, url_for, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from app import db
from app.models import Project, Product, Device, Daq, Alarm
from sqlalchemy import and_
import json
import random
import datetime, time

import bitstring
import json
import urllib
from app.email import send_email
from app.utils import index_color


# api = Api(app)
#
# swagger = Swagger(app)



avatars = [
  'https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png', 
  # // Alipay
  'https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png', 
  # // Angular
  'https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png', 
  # // Ant Design
  'https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png', 
  # // Ant Design Pro
  'https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png', 
  # // Bootstrap
  'https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png', 
  # // React
  'https://gw.alipayobjects.com/zos/rmsportal/ComBAopevLwENQdKWiIn.png', 
  # // Vue
  'https://gw.alipayobjects.com/zos/rmsportal/nxkuOJlFJuAUhzlMTCEe.png', 
  # // Webpack
]

avatars2 = [
  'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png',
  'https://gw.alipayobjects.com/zos/rmsportal/cnrhVkzwxjPwAaCfPbdc.png',
  'https://gw.alipayobjects.com/zos/rmsportal/gaOngJwsRYRaVAuXXcmB.png',
  'https://gw.alipayobjects.com/zos/rmsportal/ubnKSIfAJTxIgXOKlciN.png',
  'https://gw.alipayobjects.com/zos/rmsportal/WhxKECPNujWoWEFNdnJE.png',
  'https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png',
  'https://gw.alipayobjects.com/zos/rmsportal/psOgztMplJMGpVEqfcgF.png',
  'https://gw.alipayobjects.com/zos/rmsportal/ZpBqSxLxVEXfcUNoPKrz.png',
  'https://gw.alipayobjects.com/zos/rmsportal/laiEnJdGHVOhJrUShBaJ.png',
  'https://gw.alipayobjects.com/zos/rmsportal/UrQsqscbKEpNuJcvBZBu.png',
]

covers = [
  'https://gw.alipayobjects.com/zos/rmsportal/uMfMFlvUuceEyPpotzlq.png',
  'https://gw.alipayobjects.com/zos/rmsportal/iZBVOIhGJiAnhplqjvZW.png',
  'https://gw.alipayobjects.com/zos/rmsportal/uVZonEtjWwmUZPBQfycs.png',
  'https://gw.alipayobjects.com/zos/rmsportal/gLaIAoVWTtLbBWZNYEMg.png',
]

desc = [
  '那是一种内在的东西， 他们到达不了，也无法触及的',
  '希望是一个好东西，也许是最好的，好东西是不会消亡的',
  '生命就像一盒巧克力，结果往往出人意料',
  '城镇中有那么多的酒馆，她却偏偏走进了我的酒馆',
  '那时候我只会想自己想要什么，从不想自己拥有什么',
]

user = [
  '付小小',
  '曲丽丽',
  '林东东',
  '周星星',
  '吴加好',
  '朱偏右',
  '鱼酱',
  '乐哥',
  '谭小仪',
  '仲尼',
]


class Projects(Resource):
    '''
        get the projects.
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
    '''

    def get(self):

        projects = db.session.query(Project.id, Project.project_name, Project.avatar, Project.status, 
            Project.project_href, Project.percent, Project.gmt_create, Project.gmt_update, Project.project_description ).order_by(
            Project.id.asc()).all()

        projectLists = []

        for project in projects:
            project_id = project[0]
            project_name = project[1]
            owner = project.owner.username
            avatar = project[2]
            status = project[3]
            project_href = project[4]
            percent = project[5]
            gmt_create = project[6]
            gmt_update = project[7]
            project_description = project[8]
            devices = project.devices

            projectLists.append({
                'id':project_id,
                'owner':owner,
                'title':project_name,
                'avatar':avatar,
                # 'status': ['active', 'exception', 'normal'][random.randint(0, 2)],
                'status':status,
                # 'percent': random.randint(0, 40) + 60,
                'percent': percent,
                'logo': avatar,
                'href': project_href,
                'updatedAt': gmt_update,
                'createdAt': gmt_create,
                'subDescription': project_description,
                'description':project_description,
                'devices': devices,
                })

        print(projectLists)
        return jsonify(projectLists) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass


class Products(Resource):
    '''
        get the products.
        id = db.Column(db.Integer,primary_key = True, autoincrement=True)
        user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        product_name = db.Column(db.String(100),nullable = False)
        product_key = db.Column(db.String(100),nullable = False)
        data_format = db.Column(db.Integer, nullable = False)
        node_type = db.Column(db.Integer, nullable = False)
        aliyun_commodity_code = db.Column(db.String(100))
        gmt_create = db.Column(db.DateTime())
        gmt_update = db.Column(db.DateTime())
        product_description = db.Column(db.String(500))
        devices = db.relationship('Device',backref='product', lazy='dynamic')
    '''

    def get(self):

        products = db.session.query(Product.id, Product.product_name, Product.product_key, Product.data_format, 
            Product.node_type, Product.aliyun_commodity_code, Product.gmt_create, Product.gmt_update, Product.product_description ).order_by(
            Product.id.asc()).all()

        productLists = []

        for product in products:
            product_id = product[0]
            product_name = product[1]
            owner = product.owner.username
            product_key = product[2]
            data_format = product[3]
            node_type = product[4]
            aliyun_commodity_code = product[5]
            gmt_create = product[6]
            gmt_update = product[7]
            product_description = product[8]
            devices = product.devices

            productLists.append({
                'id':product_id,
                'owner':owner,
                'product_name':product_name,
                'product_key':product_key,
                'data_format':data_format,
                'node_type': node_type,
                'aliyun_commodity_code': aliyun_commodity_code,
                'gmt_update': gmt_update,
                'gmt_create': gmt_create,
                'product_description': product_description,
                'devices': devices,
                })

        print(productLists)
        return jsonify(productLists) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass


class Devices(Resource):
    '''
        get the devices.
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
    '''

    def get(self):

        devices = db.session.query(Device.id, Device.name, Device.device_name, Device.device_secret, 
            Device.gmt_create, Device.gmt_active, Device.gmt_online, Device.status, Device.firmware_version, 
            Device.ip_address, Device.node_type, Device.region).order_by(
            Device.id.asc()).all()

        deviceLists = []

        for device in devices:
            device_id = device[0]
            owner = device.owner.username

            name = device[1]
            device_name = device[2]
            device_secret = device[3]
            gmt_create = device[4]
            gmt_active = device[5]
            gmt_online = device[6]
            status = device[7]
            firmware_version = device[8]
            ip_address = device[9]
            node_type = device[10]
            region = device[11]

            deviceLists.append({
                'id':device_id,
                'owner':owner,
                'name':name,
                'device_name':device_name,
                'device_secret':device_secret,
                'gmt_create':gmt_create,
                'gmt_active':gmt_active,
                'gmt_online':gmt_online,
                'status': status,
                'firmware_version': firmware_version,
                'ip_address': ip_address,
                'node_type': node_type,
                'region': region,
                })

        print(deviceLists)
        return jsonify(deviceLists) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass


class DeviceDaqRealtime(Resource):
    '''
        get the lates daq.
    '''

    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('device_id', type=str)
        args = parser.parse_args()

        print('--------device_id-------', args)

        deviceId = args['device_id']

        print('----deivceID---' * 5)
        print(deivceId)

        device_daq_realtime = db.session.query(Daq.gmt_daq, Daq.daq_value).filter(
            Daq.device_id == deviceId).order_by(
            Daq.gmt_daq.desc()).first()



        print('--------device_daq_realtime--------\n' * 3)
        print(device_daq_realtime)

        daq_values = json.loads(device_daq_realtime[1])
        gmt_daq = device_daq_realtime[0]
        gmt_daq_str = datetime.datetime.strftime(gmt_daq, "%H-%M-%S")
        daq_dict = {'name':gmt_daq_str}

        print('---------daq_values--------')
        print(daq_values)

        daq_dict_list = []
        for daq_value in daq_values:

            daq_dict[daq_value[0]] = daq_value[1]
        daq_dict_list.append(daq_dict)

        print('--------daq_dict_list---- \n' *3)
        print(daq_dict_list)

        realtimeBars = []
        # for temp_value in temp_values:
        for i in range(len(daq_values)):
            daq_value = daq_values[i]
            realtimeBars.append({'dataKey': daq_value[0], 'fill':index_color(i)})

        return jsonify({'daqRealtimeData': daq_dict_list, 'realtimeBars': realtimeBars}) 

    def post(self):
        pass


    def delete(self):
        pass

    def put(self):
        pass


class DeviceDaqAlarm(Resource):
    '''
        get the lates alarm.
    '''

    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('device_id', type=str)
        args = parser.parse_args()

        print('--------device_id-------', args)

        deviceId = args['device_id']

        print('----deivceID---' * 5)
        print(deivceId)

        device_daq_alarm = db.session.query(Alarm.gmt_alarm, Alarm.alarm_value).filter(
            Alarm.device_id == deviceId).first()

        device_alarms = json.loads(device_daq_alarm[1])

        alarm_dict_list = []
        for device_alarm in device_alarms:
            if device_alarm[1] == '0':
                alarm_dict = {'type': 'danger', 'icon':'warning', 'channel': device_alarm[0], 'alarm': device_alarm[1]}
            else:
                alarm_dict = {'type': 'primary', 'icon':'sync', 'channel': device_alarm[0], 'alarm': device_alarm[1]}

            alarm_dict_list.append(alarm_dict)


        return jsonify({'deviceDaqAlarm': alarm_dict_list}) 

    def post(self):
        pass


    def delete(self):
        pass

    def put(self):
        pass


class DeviceDaqHistory(Resource):
    '''
        get the lates 10 temps.
    '''

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('device_id', type=str)
        args = parser.parse_args()

        print('--------device_id-------', args)

        deviceId = args['device_id']

        print('----deivceID---' * 5)
        print(deivceId)

        device_daq_history = db.session.query(Daq.gmt_daq, Daq.daq_value).filter(
            Daq.device_id == deviceId).order_by(
            Daq.gmt_daq.desc()).limit(20).all()


        daq_dict_lists = []
        for device_daqs in device_daq_history:
            daq_datetime = device_daqs[0]
            daq_datetime_str = datetime.datetime.strftime(daq_datetime, "%H:%M:%S")
            daq_values = json.loads(device_daqs[1])

            print(daq_values)

            daq_dict = {'time':daq_datetime_str}
            for daq_value in daq_values:
                daq_dict[daq_value[0]] = daq_value[1]
            daq_dict_lists.append(daq_dict)

        print(daq_dict_lists)

        historyLines = []

        daq_value = device_daq_history[0]
        daq_lines = json.loads(daq_value[1])
        print('all lines:', daq_lines)

        for i in range(len(daq_lines)):
            daq_line = daq_lines[i]
            historyLines.append({'type': 'monotone', 'dataKey':daq_line[0], 'stroke':index_color(i)})

        return jsonify({'deviceDaqHistory': daq_dict_lists, 'historyLines': historyLines}) 

    def post(self):
        pass


    def delete(self):
        pass

    def put(self):
        pass


class DeviceDaqRecord(Resource):
    '''
        get the temp records by the input datetime. %H:%M:S%
    '''

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('device_id', type=str)
        args = parser.parse_args()

        print('--------device_id-------', args)

        deviceId = args['device_id']

        print('----deivceID---' * 5)
        print(deivceId)

        daq_records = db.session.query(Daq.gmt_daq, Daq.daq_value).filter(
            Daq.device_id == deviceId).order_by(
            Daq.gmt_daq.desc()).all()


        daq_dict_lists = []
        # for temperatures in temps_records:
        for i in range(len(daq_records)):
            daqs = daq_records[i]
            daq_datetime = daqs[0]
            daq_datetime_str = datetime.datetime.strftime(daq_datetime, "%Y-%m-%d %H:%M:%S")
            daq_values = json.loads(daqs[1])

            print(daq_values)

            daq_dict = {'key':i, 'datetime':daq_datetime_str}

            for daq_value in daq_values:
                daq_dict[daq_value[0]] = daq_value[1]

            daq_dict_lists.append(daq_dict)

        print('--daq_dict_lists---\n' * 3)
        print(daq_dict_lists)


        daq_record = daq_records[0][1]
        recordColumns = [{
                  'title': '时间',
                  'dataIndex': 'datetime',
                  'key': 'datetime',
                }]


        channels = json.loads(daq_record)
        for channel in channels:
            recordColumns.append({'title': channel[0],
                  'dataIndex': channel[0],
                  'key': channel[0],})
        print('-----recordColumns---\n' * 3)

        print(recordColumns)

        return jsonify({'deviceDaqRecord': daq_dict_lists, 'recordColumns':recordColumns}) 

    def post(self):
        pass


    def delete(self):
        pass

    def put(self):
        pass

