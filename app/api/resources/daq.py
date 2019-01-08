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
        userId = 1


        # projects = db.session.query(Project.id, Project.project_name, Project.avatar, Project.status, 
        #     Project.project_href, Project.percent, Project.gmt_create, Project.gmt_update, Project.project_description).filter(Project.user_id == userId).order_by(
        #     Project.id.asc()).all()

        projects = Project.query.filter_by(user_id=userId).all()

        projectLists = []

        for project in projects:
            project_id = project.id
            project_name = project.project_name
            owner = project.owner.email
            # owner = 'owner'
            avatar = project.avatar
            status = project.status
            project_href = project.project_href
            percent = project.percent
            gmt_create = project.gmt_create
            gmt_update = project.gmt_update
            project_description = project.project_description
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
                # 'devices': devices,
                })

        print('---------projectLists-------')
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

    '''

    def get(self, user_id):

        products = Product.query.filter_by(user_id=user_id).all()

        # products = db.session.query(Product.id, Product.product_name, Product.product_key, Product.data_format, 
        #     Product.node_type, Product.aliyun_commodity_code, Product.gmt_create, Product.gmt_update, Product.product_description).filter(Product.user_id == userId).order_by(
        #     Product.id.asc()).all()

        productLists = []

        for product in products:
            product_id = product.id
            product_name = product.product_name
            owner = product.owner.email
            product_key = product.product_key
            product_pic = product.product_pic
            data_format = product.data_format
            node_type = product.node_type
            aliyun_commodity_code = product.aliyun_commodity_code
            gmt_create = product.gmt_create
            gmt_update = product.gmt_update
            product_description = product.product_description
            devices = product.devices

            productLists.append({
                'id':product_id,
                'owner':owner,
                # todo:add product_avatar to database
                # 'product_avatar': 'http://image.cn.made-in-china.com/2f0j01NMlQWPFanirm/%E6%97%A0%E7%BA%B8%E8%AE%B0%E5%BD%95%E4%BB%AA.jpg',
                # 'product_avatar': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1536274077257&di=e78e9726a2c63a53ed28c2b85c41a6cf&imgtype=0&src=http%3A%2F%2Fimg2.everychina.com%2Fimg%2F55%2Fd2%2F99e0c324514dfd7d3d0be1026e01-600x600c0-8b6b%2Fgsm_rtu_remote_control_and_alarm_4digi_in_4relay_output.jpg',
                # 'product_avatar': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1539579523063&di=28c5ff0e19bf6fb65d9f04bbe4bd64aa&imgtype=0&src=http%3A%2F%2Fhcff.com.cn%2FFileLoad%2F2012110714779.JPG',
                'product_avatar':product_pic,
                'product_name':product_name,
                'product_key':product_key,
                'data_format':data_format,
                'node_type': node_type,
                'aliyun_commodity_code': aliyun_commodity_code,
                'gmt_update': gmt_update,
                'gmt_create': gmt_create,
                'product_description': product_description,
                'members': [
                    {
                      'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png',
                      'name': '曲丽丽',
                    },
                    {
                      'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png',
                      'name': '王昭君',
                    },
                    {
                      'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png',
                      'name': '董娜娜',
                    },
                  ],
                # 'devices': devices,
                })

        print(productLists)
        return jsonify(productLists) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass




class ProductDistribute(Resource):
    '''
        get the products.

    '''

    def get(self):
        productLists = [
                {'value':35, 'name':'protduct1'},
                {'value':310, 'name':'protduct2'},
                {'value':234, 'name':'protduct3'},
                {'value':135, 'name':'protduct4'},
                {'value':148, 'name':'protduct5'}
            ]
        print(productLists)
        return jsonify({'product_distribute': productLists}) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass



class RegionDistribute(Resource):
    '''
        get the products.

    '''

    def get(self):
        regionLists = [
                {'value':35, 'name':'city1'},
                {'value':10, 'name':'city2'},
                {'value':34, 'name':'city3'},
                {'value':35, 'name':'city4'},
                {'value':48, 'name':'city5'}
            ]
        print(regionLists)
        return jsonify({'region_distribute': regionLists}) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass




class ProductProfile(Resource):
    '''
        get the ProductProfile.

    '''

    def get(self):
        userId = 1

        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=str)
        args = parser.parse_args()

        print('--------product_id-------', args)

        productID = args['product_id']

        print('----productID---' * 5)
        print(productID)

        products = Product.query.filter_by(user_id=userId, id=productID).all()

        # products = db.session.query(Product.id, Product.product_name, Product.product_key, Product.data_format, 
        #     Product.node_type, Product.aliyun_commodity_code, Product.gmt_create, Product.gmt_update, Product.product_description).filter(Product.user_id == userId).order_by(
        #     Product.id.asc()).all()

        productLists = []

        for product in products:
            product_id = product.id
            product_name = product.product_name
            owner = product.owner.email
            product_key = product.product_key
            data_format = product.data_format
            node_type = product.node_type
            aliyun_commodity_code = product.aliyun_commodity_code
            gmt_create = product.gmt_create
            gmt_update = product.gmt_update
            product_description = product.product_description
            devices = product.devices

            productLists.append({
                'id':product_id,
                'owner':owner,
                # todo:add product_avatar to database
                'product_avatar': 'http://image.cn.made-in-china.com/2f0j01NMlQWPFanirm/%E6%97%A0%E7%BA%B8%E8%AE%B0%E5%BD%95%E4%BB%AA.jpg',
                'product_name':product_name,
                'product_key':product_key,
                'data_format':data_format,
                'node_type': node_type,
                'aliyun_commodity_code': aliyun_commodity_code,
                'gmt_update': gmt_update,
                'gmt_create': gmt_create,
                'product_description': product_description,
                'members': [
                    {
                      'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe.png',
                      'name': '曲丽丽',
                    },
                    {
                      'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/tBOxZPlITHqwlGjsJWaF.png',
                      'name': '王昭君',
                    },
                    {
                      'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/sBxjgqiuHMGRkIjqlQCd.png',
                      'name': '董娜娜',
                    },
                  ],
                # 'devices': devices,
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

    '''

    def get(self, user_id):


        devices = Device.query.filter_by(user_id=user_id).all()


        deviceLists = []

        for device in devices:
            device_id = device.id
            owner = device.owner.email

            name = device.name
            device_name = device.device_name
            device_secret = device.device_secret
            gmt_create = device.gmt_create
            gmt_active = device.gmt_active
            gmt_online = device.gmt_online
            status = device.status
            firmware_version = device.firmware_version
            ip_address = device.ip_address
            node_type = device.node_type
            region = device.region

            deviceLists.append({
                'id':device_id,
                'owner':owner,
                'name':name,
                'avatar':"http://dummyimage.com/48x48/{0}/757575.png&text={1}".format(index_color(device_id), device_id),
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
                'running_status':'/conf2d/gojs/' + str(device_id)
                })

        print(deviceLists)
        return jsonify(deviceLists) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass


class DevicesOfProduct(Resource):
    '''
        get the devices of some product.

    '''

    def get(self, product_id):

        devices = Device.query.filter_by(product_id=product_id).order_by(
            Device.gmt_create.desc()).all()

        print('--------devices--------\n' * 3)
        print(devices)
        devices_list = []
        for device in devices:
            print(device.device_name)
            devices_list.append(device)

        print(devices_list)

        deviceLists = []

        for device in devices:
            device_id = device.id
            owner = device.owner.email

            name = device.name
            device_name = device.device_name
            device_secret = device.device_secret
            gmt_create = device.gmt_create
            gmt_active = device.gmt_active
            gmt_online = device.gmt_online
            status = device.status
            firmware_version = device.firmware_version
            ip_address = device.ip_address
            node_type = device.node_type
            region = device.region

            deviceLists.append({
                'id':device_id,
                'owner':owner,
                'name':name,
                'avatar':"http://dummyimage.com/48x48/{0}/757575.png&text={1}".format(index_color(device_id), device_id),
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
                'running_status':'/conf2d/gojs/' + str(device_id)

                })

        print(deviceLists)
        return jsonify(deviceLists) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass



class DeviceProfile(Resource):
    '''
        get the DeviceProfile.

    '''

    def get(self):

        userId = 1


        parser = reqparse.RequestParser()
        parser.add_argument('device_id', type=str)
        args = parser.parse_args()

        print('--------device_id-------', args)

        deviceID = args['device_id']

        print('----deviceID---' * 5)
        print(deviceID)

        devices = Device.query.filter_by(user_id=userId, id=deviceID).all()
        # devices = db.session.query(Device.id, Device.name, Device.device_name, Device.device_secret, 
        #     Device.gmt_create, Device.gmt_active, Device.gmt_online, Device.status, Device.firmware_version, 
        #     Device.ip_address, Device.node_type, Device.region).filter(Device.user_id == userId).order_by(
        #     Device.id.asc()).all()

        deviceLists = []

        for device in devices:
            device_id = device.id
            owner = device.owner.email

            name = device.name
            device_name = device.device_name
            device_secret = device.device_secret
            gmt_create = device.gmt_create
            gmt_active = device.gmt_active
            gmt_online = device.gmt_online
            status = device.status
            firmware_version = device.firmware_version
            ip_address = device.ip_address
            node_type = device.node_type
            region = device.region

            deviceLists.append({
                'id':device_id,
                'owner':owner,
                'name':name,
                'avatar':"http://dummyimage.com/48x48/{0}/757575.png&text={1}".format(index_color(device_id), device_id),
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
                'running_status':'/conf2d/gojs/' + str(device_id)
                
                })

        print(deviceLists)
        return jsonify(deviceLists) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass




class DeviceDetail(Resource):
    '''
        get the DeviceDetail.

    '''

    def get(self, device_id):


        device = Device.query.filter_by(id=device_id).first()


        device_id = device.id
        owner = device.owner.email

        name = device.name
        device_name = device.device_name
        device_secret = device.device_secret
        gmt_create = device.gmt_create
        gmt_active = device.gmt_active
        gmt_online = device.gmt_online
        status = device.status
        firmware_version = device.firmware_version
        ip_address = device.ip_address
        node_type = device.node_type
        region = device.region

        deviceDict = {
            'device_id':device_id,
            'owner':owner,
            'name':name,
            'avatar':"http://dummyimage.com/48x48/{0}/757575.png&text={1}".format(index_color(device_id), device_id),
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
            }

        print(deviceDict)
        return jsonify(deviceDict) 

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

        deviceID = args['device_id']

        print('----deivceID---' * 5)
        print(deviceID)

        device_daq_realtime = Daq.query.filter_by(device_id=deviceID).order_by(
            Daq.gmt_daq.desc()).first()

        # device_daq_realtime = db.session.query(Daq.gmt_daq, Daq.daq_value).filter(
        #     Daq.device_id == deviceID).order_by(
        #     Daq.gmt_daq.desc()).first()



        print('--------device_daq_realtime--------\n' * 3)
        print(device_daq_realtime)

        daq_values = device_daq_realtime.daq_value
        # daq_values = json.loads(device_daq_realtime.daq_value)
        gmt_daq = device_daq_realtime.gmt_daq
        gmt_daq_str = datetime.datetime.strftime(gmt_daq, "%H-%M-%S")
        daq_dict = {'name':gmt_daq_str}

        daq_dict_list = []
        for daq_value in daq_values:
            daq_dict[daq_value[0]] = daq_value[1]
        daq_dict_list.append(daq_dict)

        print(daq_dict_list)

        current_time = gmt_daq.strftime("%Y-%m-%d %H:%M:%S")
        

        daq_digital_dict_list = []

        for i in range(len(daq_values)):
            daq_value = daq_values[i]
            daq_digital_dict_list.append({
                'bordered':True,
                'title':'通道' + daq_value[0],
                'tooltip_title':'通道' + daq_value[0],
                'value':float('%.3f' % daq_value[1]),
                'footer_label':'时间',
                'footer_value':current_time,
                'contentHeight':46,
                })


        realtimeBars = []
        # for temp_value in temp_values:
        for i in range(len(daq_values)):
            daq_value = daq_values[i]
            realtimeBars.append({'dataKey': daq_value[0], 'fill':index_color(i)})

        return jsonify({'deviceDaqRealtime': daq_dict_list, 'deviceDaqDigital': daq_digital_dict_list,  'realtimeBars': realtimeBars}) 

    def post(self):
        pass


    def delete(self):
        pass

    def put(self):
        pass



class CurrentPower(Resource):
    '''
        get the power voltage and current value. 
    '''

    def get(self):

        current_power = db.session.query(Power.datetime, Power.value).order_by(Power.datetime.desc()).first()
        # current_power = db.session.query(Power.datetime, Power.value).filter(
        #     and_(Power.project == 1, Power.worker == 1)).order_by(Power.datetime.desc()).first()

        history_power = db.session.query(Power.datetime, Power.value).order_by(
            Power.datetime.desc()).limit(10).all()

        # history_power = db.session.query(Power.datetime, Power.value).filter(
        #     and_(Power.project == 1, Power.worker == 1)).order_by(
        #     Power.datetime.desc()).limit(10).all()

        powerValues = json.loads(current_power[1])

        # first power
        powerValues1 = powerValues[0]
        print('-----------powerValues1------------')
        print(powerValues1)


        mini_area_data1 = []
        mini_area_data2 = []
        mini_area_data3 = []
        mini_area_data4 = []



        for i in range(0,len(history_power)):
            historyPowerValues = history_power[i]
            datetime = historyPowerValues[0].strftime("%H:%M:%S")

            print(datetime)

            # first power
            historyPowerValue = json.loads(historyPowerValues[1])[0]


            print('-----------historyPowerValue-------------')
            print(historyPowerValue)

            
            voltage_dict1 = {'x': datetime,
                            'y': historyPowerValue[1][1]}
            mini_area_data1.append(voltage_dict1)

            voltage_dict2= {'x': datetime,
                            'y': historyPowerValue[1][3]}
            mini_area_data2.append(voltage_dict2)

            voltage_dict3 = {'x': datetime,
                            'y': historyPowerValue[1][5]}
            mini_area_data3.append(voltage_dict3)

            voltage_dict4 = {'x': datetime,
                            'y': historyPowerValue[1][7]}
            mini_area_data4.append(voltage_dict4)

        print('------mini_area_data1-----')
        print(mini_area_data1)
        print(mini_area_data2)
        print(mini_area_data3)
        print(mini_area_data4)


        print(current_power[0])

        current_time = current_power[0].strftime("%Y-%m-%d %H:%M:%S")
        
        channel1_dict ={'bordered':True,
        'title':'电压1',
        'tooltip_title':'通道1',
        'voltage':powerValues1[1][1],
        'footer_label':'时间',
        'footer_value':current_time,
        'contentHeight':46,
        'mini_area_color':'#DC143C',
        'mini_area_data':mini_area_data1,
        }
        

        channel2_dict ={'bordered':True,
        'title':'电压2',
        'tooltip_title':'通道2',
        'voltage':powerValues1[1][3],
        'footer_label':'时间',
        'footer_value':current_time,
        'contentHeight':46,
        'mini_area_color':'#975FE4',
        'mini_area_data':mini_area_data2,
        }
        

        channel3_dict ={'bordered':False,
        'title':'电压3',
        'tooltip_title':'通道3',
        'voltage':powerValues1[1][5],
        'footer_label':'时间',
        'footer_value':current_time,
        'contentHeight':46,
        'mini_area_color':'#0000FF',
        'mini_area_data':mini_area_data3,
        }
        

        channel4_dict ={'bordered':False,
        'title':'电压4',
        'tooltip_title':'通道4',
        'voltage':powerValues1[1][7],
        'footer_label':'时间',
        'footer_value':current_time,
        'contentHeight':46,
        'mini_area_color':'#00FFFF',
        'mini_area_data':mini_area_data4,
        }
        
        current_power_list = []
        current_power_list.append(channel1_dict)
        current_power_list.append(channel2_dict)
        current_power_list.append(channel3_dict)
        current_power_list.append(channel4_dict)

        return jsonify({'currentPower': current_power_list}) 

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

        deviceID = args['device_id']

        print('----deivceID---' * 5)
        print(deviceID)
        userId = 1

        device_daq_alarm = Alarm.query.order_by(Alarm.gmt_alarm.desc()).first()

        # device_daq_alarm = db.session.query(Alarm.gmt_alarm, Alarm.alarm_value).filter(
        #     Alarm.device_id == deviceID).first()
        print('-----device_daq_alarm----')
        print(device_daq_alarm)
        device_alarms = device_daq_alarm.alarm_value
        print('-----device_alarms----')

        print(device_alarms)
        print(type(device_alarms))
        # todo:
        device_alarms_list = json.loads(device_alarms)
        print(device_alarms_list)


        alarm_dict_list = []

        for device_alarm in device_alarms_list:
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

        deviceID = args['device_id']

        print('----deivceID---' * 5)
        print(deviceID)

        # device_daq_history = db.session.query(Daq.gmt_daq, Daq.daq_value).filter(
        #     Daq.device_id == deviceID).order_by(
        #     Daq.gmt_daq.desc()).limit(20).all()

        device_daq_history = Daq.query.filter_by(device_id=deviceID).order_by(
            Daq.gmt_daq.desc()).limit(10).all()


        daq_dict_lists = []
        for device_daqs in device_daq_history:
            daq_datetime = device_daqs.gmt_daq
            daq_datetime_str = datetime.datetime.strftime(daq_datetime, "%H:%M:%S")
            daq_values = device_daqs.daq_value

            print(daq_values)

            daq_dict = {'time':daq_datetime_str}
            for daq_value in daq_values:
                daq_dict[daq_value[0]] = float('%.3f' % daq_value[1])
            daq_dict_lists.append(daq_dict)

        print(daq_dict_lists)

        historyLines = []

        daq_value = device_daq_history[0]
        daq_lines = daq_value.daq_value
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

        deviceID = args['device_id']

        print('----deivceID---' * 5)
        print(deviceID)

        # daq_records = db.session.query(Daq.gmt_daq, Daq.daq_value).filter(
        #     Daq.device_id == deviceID).order_by(
        #     Daq.gmt_daq.desc()).all()

        device_daq_records = Daq.query.filter_by(device_id=deviceID).order_by(
            Daq.gmt_daq.desc()).limit(20).all()


        daq_dict_lists = []
        # for temperatures in temps_records:
        for i in range(len(device_daq_records)):
            daqs = device_daq_records[i]
            daq_datetime = daqs.gmt_daq
            daq_datetime_str = datetime.datetime.strftime(daq_datetime, "%Y-%m-%d %H:%M:%S")
            daq_values = daqs.daq_value

            print(daq_values)

            daq_dict = {'key':i, 'datetime':daq_datetime_str}

            for daq_value in daq_values:
                daq_dict[daq_value[0]] = float('%.3f' % daq_value[1])

            daq_dict_lists.append(daq_dict)

        print('--daq_dict_lists---\n' * 3)
        print(daq_dict_lists)


        daq_record = device_daq_records[0].daq_value
        recordColumns = [{
                  'title': '时间',
                  'dataIndex': 'datetime',
                  'key': 'datetime',
                }]


        channels = daq_record
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




class DeviceHistoryRecord(Resource):
    '''
        get the device records device_id
    '''

    def get(self, device_id):

        device_daq_records = Daq.query.filter_by(device_id=device_id).order_by(
            Daq.gmt_daq.desc()).limit(50).all()


        daq_dict_lists = []
        # for temperatures in temps_records:
        for i in range(len(device_daq_records)):
            daqs = device_daq_records[i]
            daq_datetime = daqs.gmt_daq
            daq_datetime_str = datetime.datetime.strftime(daq_datetime, "%Y-%m-%d %H:%M:%S")
            daq_values = daqs.daq_value

            print('-----daq_values----')
            print(daq_values)

            # value_list = []
            # for daq_value in daq_values:
            #     print(daq_value)
            #     value_dict={daq_value[0]:daq_value[1]}
            #     print('---value_dict---')
            #     print(value_dict)
            #     # value_dict={daq_value[0]:float('%.2f' % daq_value[1])}
            #     # value_dict[daq_value[0]] = float('%.2f' % daq_value[1])
            #     value_list.append(value_dict)

            # print(value_list)

            value_json = json.dumps(daq_values)
            print(value_json)

            daq_dict = {'key':i, 'datetime':daq_datetime_str, 'daq_values':value_json}

            daq_dict_lists.append(daq_dict)

        print('--daq_dict_lists---\n' * 3)
        print(daq_dict_lists)

        return jsonify(daq_dict_lists) 

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass



class DeviceAlarmRecord(Resource):
    '''
        get the temp records by the input datetime. %H:%M:S%
    '''

    def get(self, device_id):


        device_alarm_records = Alarm.query.filter_by(device_id=device_id).order_by(
            Alarm.gmt_alarm.desc()).limit(20).all()


        alarm_dict_lists = []
        # for temperatures in temps_records:
        for i in range(len(device_alarm_records)):
            alarms = device_alarm_records[i]
            alarm_datetime = alarms.gmt_alarm
            alarm_datetime_str = datetime.datetime.strftime(alarm_datetime, "%Y-%m-%d %H:%M:%S")
            alarm_values = alarms.alarm_value

            print('-------alarm_values------')
            print(alarm_values)

            alarm_list = []
            for alarm_value in alarm_values:
                print(alarm_value)
                print(alarm_value[0])
                print(alarm_value[1])
                alarm_dict={alarm_value[0]: alarm_value[1]}
                alarm_list.append(alarm_dict)

            print(alarm_list)

            alarm_json = json.dumps(alarm_list)
            print(alarm_json)

            alarm_dict = {'key':i, 'datetime':alarm_datetime_str, 'alarm_values':alarm_json}

            alarm_dict_lists.append(alarm_dict)

        print('--alarm_dict_lists---\n' * 3)
        print(alarm_dict_lists)

        return jsonify(alarm_dict_lists) 

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass



class DeviceRunningStatus(Resource):
    '''
        get the temp records by the input datetime. %H:%M:S%
    '''

    def get(self, device_id):

        device_daq_realtime = Daq.query.filter_by(device_id=device_id).order_by(
            Daq.gmt_daq.desc()).first()

        # device_daq_realtime = db.session.query(Daq.gmt_daq, Daq.daq_value).filter(
        #     Daq.device_id == deviceID).order_by(
        #     Daq.gmt_daq.desc()).first()



        print('--------device_daq_realtime--------\n' * 3)
        print(device_daq_realtime)

        daq_values = device_daq_realtime.daq_value
        print(daq_values)
        # daq_values = json.loads(device_daq_realtime.daq_value)
        gmt_daq = device_daq_realtime.gmt_daq
        gmt_daq_str = datetime.datetime.strftime(gmt_daq, "%Y-%m-%d %H:%M:%S")
        print(gmt_daq_str)



        injector_1_current_value_str = daq_values['injector_current_value']['injector_1_current_value_str']
        injector_2_current_value_str = daq_values['injector_current_value']['injector_2_current_value_str']
        injector_3_current_value_str = daq_values['injector_current_value']['injector_3_current_value_str']
        injector_4_current_value_str = daq_values['injector_current_value']['injector_4_current_value_str']

        motor_1_current_value_str = daq_values['motor_current_value']['motor_1_current_value_str']
        motor_2_current_value_str = daq_values['motor_current_value']['motor_2_current_value_str']
        motor_3_current_value_str = daq_values['motor_current_value']['motor_3_current_value_str']
        motor_4_current_value_str = daq_values['motor_current_value']['motor_4_current_value_str']

        work_status_1 = daq_values['work_status']['work_status_1']
        work_status_2 = daq_values['work_status']['work_status_2']
        work_status_3 = daq_values['work_status']['work_status_3']
        work_status_4 = daq_values['work_status']['work_status_4']

        input_pressure = daq_values['input_pressure']
        material_temprature = daq_values['material_temprature']
        line_speed = daq_values['line_speed']

        current_running_time_h = daq_values['current_running_time']['h']
        current_running_time_min = daq_values['current_running_time']['min']
        current_running_time_s = daq_values['current_running_time']['s']

        accumulated_running_time_h = daq_values['accumulated_running_time']['h']
        accumulated_running_time_min = daq_values['accumulated_running_time']['min']
        accumulated_running_time_s = daq_values['accumulated_running_time']['s']

        current_time=daq_values['current_time']
        mantual_auto=daq_values['mantual_auto']
        access_control=daq_values['access_control']
        emergency_button=daq_values['emergency_button']
        pressure_detect=daq_values['pressure_detect']


        injector_1_current_alarm_str = daq_values['injector_current_alarm']['injector_1_current_alarm_str']
        injector_2_current_alarm_str = daq_values['injector_current_alarm']['injector_2_current_alarm_str']
        injector_3_current_alarm_str = daq_values['injector_current_alarm']['injector_3_current_alarm_str']
        injector_4_current_alarm_str = daq_values['injector_current_alarm']['injector_4_current_alarm_str']


        master_1_error_alarm_str = daq_values['master_error']['master_1_error_str']
        master_2_error_alarm_str = daq_values['master_error']['master_2_error_str']
        master_3_error_alarm_str = daq_values['master_error']['master_3_error_str']
        master_4_error_alarm_str = daq_values['master_error']['master_4_error_str']


        def work_status_2_pic(work_status, injector_current_alarm_str, master_error_alarm_str):
            if master_error_alarm_str == '1' or injector_current_alarm_str == '1':
                return "/static/images/handsome/1_error.png"            
            elif work_status == '1':
                return "/static/images/handsome/1_start.png"
            elif work_status == '0':
                return "/static/images/handsome/1_close.png"
            else:
                return "/static/images/handsome/2_start.png"

        def alarm_2_color(alarm_str):
            if alarm_str == '1':
                return "red"
            else:
                return "green"

        dict_1 = { 'name': "1#喷头", 'color':"orange", 'source': work_status_2_pic(work_status_1, injector_1_current_alarm_str, master_1_error_alarm_str), 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':injector_1_current_value_str, 'motor_current_value':motor_1_current_value_str, 'injector_error':"喷枪息弧:", 'injector_error_fill':alarm_2_color(injector_1_current_alarm_str), 'master_error':"主机故障:", 'master_error_fill':alarm_2_color(master_1_error_alarm_str), 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_2 = { 'name': "2#喷头", 'color':"orange", 'source': work_status_2_pic(work_status_2, injector_2_current_alarm_str, master_2_error_alarm_str), 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':injector_2_current_value_str, 'motor_current_value':motor_2_current_value_str, 'injector_error':"喷枪息弧:", 'injector_error_fill':alarm_2_color(injector_2_current_alarm_str), 'master_error':"主机故障:", 'master_error_fill':alarm_2_color(master_2_error_alarm_str), 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_3 = { 'name': "3#喷头", 'color':"orange", 'source': work_status_2_pic(work_status_3, injector_3_current_alarm_str, master_3_error_alarm_str), 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':injector_3_current_value_str, 'motor_current_value':motor_3_current_value_str, 'injector_error':"喷枪息弧:", 'injector_error_fill':alarm_2_color(injector_3_current_alarm_str), 'master_error':"主机故障:", 'master_error_fill':alarm_2_color(master_3_error_alarm_str), 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_4 = { 'name': "4#喷头", 'color':"orange", 'source': work_status_2_pic(work_status_4, injector_4_current_alarm_str, master_4_error_alarm_str), 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':injector_4_current_value_str, 'motor_current_value':motor_4_current_value_str, 'injector_error':"喷枪息弧:", 'injector_error_fill':alarm_2_color(injector_4_current_alarm_str), 'master_error':"主机故障:", 'master_error_fill':alarm_2_color(master_4_error_alarm_str), 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_5 = { 'name': "5#喷头", 'color':"orange", 'source': "/static/images/handsome/1_start.png", 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':"0.5", 'motor_current_value':"1.5", 'injector_error':"喷枪息弧:", 'injector_error_fill':"green", 'master_error':"主机故障:", 'master_error_fill':"green", 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_6 = { 'name': "6#喷头", 'color':"orange", 'source': "/static/images/handsome/1_close.png", 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':"0.5", 'motor_current_value':"1.5", 'injector_error':"喷枪息弧:", 'injector_error_fill':"orange", 'master_error':"主机故障:", 'master_error_fill':"green", 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_7 = { 'name': "7#喷头", 'color':"orange", 'source': "/static/images/handsome/1_start.png", 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':"0.5", 'motor_current_value':"1.5", 'injector_error':"喷枪息弧:", 'injector_error_fill':"green", 'master_error':"主机故障:", 'master_error_fill':"green", 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_8 = { 'name': "8#喷头", 'color':"orange", 'source': "/static/images/handsome/2_start.png", 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':"0.5", 'motor_current_value':"1.5", 'injector_error':"喷枪息弧:", 'injector_error_fill':"green", 'master_error':"主机故障:", 'master_error_fill':"green", 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_9 = { 'name': "9#喷头", 'color':"orange", 'source': "/static/images/handsome/2_close.png", 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':"0.5", 'motor_current_value':"1.5", 'injector_error':"喷枪息弧:", 'injector_error_fill':"green", 'master_error':"主机故障:", 'master_error_fill':"green", 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        dict_10 = { 'name': "10#喷头", 'color':"orange", 'source': "/static/images/handsome/2_start.png", 'injector_current':"喷嘴电流:", 'motor_current':"电机电流:", 'injector_current_value':"0.5", 'motor_current_value':"1.5", 'injector_error':"喷枪息弧:", 'injector_error_fill':"green", 'master_error':"主机故障:", 'master_error_fill':"green", 'motor_error':"电机故障:", 'motor_error_fill':"green" }
        
        print('------device_id------')
        print(device_id)
        status_pic_list=[]
        if device_id == '4':
            status_pic_list.append(dict_1)
            status_pic_list.append(dict_2)
            status_pic_list.append(dict_3)
            status_pic_list.append(dict_4)
        elif device_id == '6':
            status_pic_list.append(dict_1)
            status_pic_list.append(dict_2)
            status_pic_list.append(dict_3)
            status_pic_list.append(dict_4)
            status_pic_list.append(dict_5)
            status_pic_list.append(dict_6)
        elif device_id =='8':
            status_pic_list.append(dict_1)
            status_pic_list.append(dict_2)
            status_pic_list.append(dict_3)
            status_pic_list.append(dict_4)
            status_pic_list.append(dict_5)
            status_pic_list.append(dict_6)
            status_pic_list.append(dict_7)
            status_pic_list.append(dict_8)
        elif device_id =='10':
            status_pic_list.append(dict_1)
            status_pic_list.append(dict_2)
            status_pic_list.append(dict_3)
            status_pic_list.append(dict_4)
            status_pic_list.append(dict_5)
            status_pic_list.append(dict_6)
            status_pic_list.append(dict_7)
            status_pic_list.append(dict_8)
            status_pic_list.append(dict_9)
            status_pic_list.append(dict_10)


        pressure_error_fill = "green" if pressure_detect == '1' else "red"
        gate_error_fill = "red" if access_control == '1' else "green"
        emergency_error_fill = "green" if emergency_button == '1' else "red"


        status_text_list=[{ 'pressure': "压强:", 'pressure_value':input_pressure, 'velocity':"线速度:",'velocity_value':line_speed, \
        'voltage':"电压:", 'voltage_value':"220",  'temperature': "温度:", 'temperature_value':material_temprature, 'current_running_time':"当前运行时间:", \
        'current_running_time_h':current_running_time_h, 'current_running_time_m':current_running_time_min,'current_running_time_s':current_running_time_s, \
        'total_running_time':"累计运行时间:",'total_running_time_h':accumulated_running_time_h,'total_running_time_m':accumulated_running_time_min,\
        'total_running_time_s':accumulated_running_time_s,'temperature_error':"温度异常", 'temperature_error_fill':"green", 'pressure_error':"气压异常", \
        'pressure_error_fill':pressure_error_fill, 'gate_error':"室门打开", 'gate_error_fill':gate_error_fill, 'velocity_error':"速度异常", 'velocity_error_fill':"green",\
         'emergency_error':"急停开关", 'emergency_error_fill':emergency_error_fill },]


        device_running_status={'StatusPic':status_pic_list, 'StatusText':status_text_list}
        return jsonify(device_running_status) 

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass


