from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import json

import logging
from app import db, security
import random
import datetime, time
import bitstring

from app.models import User, Role, Project, Product, Device, Daq, Alarm, \
BugOrderOfSeverity, BugPriority, Models, Version, TestingEnvironment, BugStatus, BugComment, Bug


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


        # name = db.Column(db.String(20), nullable = False, unique=True)
        # name_en = db.Column(db.String(20), nullable = False, unique=True)

        try:
            severity = list()
            severity.append(BugOrderOfSeverity(name='轻微', name_en='Minor'))
            severity.append(BugOrderOfSeverity(name='一般', name_en='Major'))
            severity.append(BugOrderOfSeverity(name='严重', name_en='Critical'))
            severity.append(BugOrderOfSeverity(name='致命', name_en='Blocker'))

            db.session.add(severity[0])
            db.session.add(severity[1])
            db.session.add(severity[2])
            db.session.add(severity[3])

            db.session.commit()
        except Exception as e:
            log.error("Creating severity: %s", e)
            db.session.rollback()

        try:
            priority = list()
            priority.append(BugPriority(name='低', name_en='Low'))
            priority.append(BugPriority(name='中', name_en='Normal'))
            priority.append(BugPriority(name='高', name_en='High'))
            priority.append(BugPriority(name='紧急', name_en='Urgent'))

            db.session.add(priority[0])
            db.session.add(priority[1])
            db.session.add(priority[2])
            db.session.add(priority[3])

            db.session.commit()
        except Exception as e:
            log.error("Creating priority: %s", e)
            db.session.rollback()



        try:
            models = list()
            models.append(Models(name='Dashboard'))
            models.append(Models(name='产品管理'))
            models.append(Models(name='设备管理'))
            models.append(Models(name='项目管理'))
            models.append(Models(name='用户管理'))
            models.append(Models(name='系统设置'))

            db.session.add(models[0])
            db.session.add(models[1])
            db.session.add(models[2])
            db.session.add(models[3])
            db.session.add(models[4])
            db.session.add(models[5])

            db.session.commit()
        except Exception as e:
            log.error("Creating priority: %s", e)
            db.session.rollback()


        try:
            versions = list()
            versions.append(Version(name='0.0.1'))
            versions.append(Version(name='0.0.2'))
            versions.append(Version(name='0.0.3'))
            versions.append(Version(name='0.0.4'))
            versions.append(Version(name='0.0.5'))
            versions.append(Version(name='0.0.6'))
            versions.append(Version(name='0.0.7'))
            versions.append(Version(name='0.0.8'))
            versions.append(Version(name='0.0.9'))
            versions.append(Version(name='0.1.0'))
            versions.append(Version(name='0.1.1'))
            versions.append(Version(name='0.1.2'))
            versions.append(Version(name='0.1.3'))

            db.session.add(versions[0])
            db.session.add(versions[1])
            db.session.add(versions[2])
            db.session.add(versions[3])
            db.session.add(versions[4])
            db.session.add(versions[5])
            db.session.add(versions[6])
            db.session.add(versions[7])
            db.session.add(versions[8])
            db.session.add(versions[9])
            db.session.add(versions[10])
            db.session.add(versions[11])
            db.session.add(versions[12])

            db.session.commit()
        except Exception as e:
            log.error("Creating versions: %s", e)
            db.session.rollback()


        try:
            envirments = list()
            envirments.append(TestingEnvironment(name='Chrome'))
            envirments.append(TestingEnvironment(name='Firefox'))
            envirments.append(TestingEnvironment(name='IE'))
            envirments.append(TestingEnvironment(name='Android'))
            envirments.append(TestingEnvironment(name='IOS'))
            envirments.append(TestingEnvironment(name='其他'))

            db.session.add(envirments[0])
            db.session.add(envirments[1])
            db.session.add(envirments[2])
            db.session.add(envirments[3])
            db.session.add(envirments[4])
            db.session.add(envirments[5])


            db.session.commit()
        except Exception as e:
            log.error("Creating envirments: %s", e)
            db.session.rollback()



        try:
            statuses = list()
            statuses.append(BugStatus(name='新建', name_en='New'))
            statuses.append(BugStatus(name='进行中', name_en='Open'))
            statuses.append(BugStatus(name='已修复', name_en='Fixed'))
            statuses.append(BugStatus(name='已关闭', name_en='Closed'))
            statuses.append(BugStatus(name='已拒绝', name_en='Abandoned'))
            statuses.append(BugStatus(name='反馈产品', name_en='By Design'))
            statuses.append(BugStatus(name='暂不处理', name_en='Waiting'))
            statuses.append(BugStatus(name='打回', name_en='Reopen'))

            db.session.add(statuses[0])
            db.session.add(statuses[1])
            db.session.add(statuses[2])
            db.session.add(statuses[3])
            db.session.add(statuses[4])
            db.session.add(statuses[5])
            db.session.add(statuses[6])
            db.session.add(statuses[7])

            db.session.commit()
        except Exception as e:
            log.error("Creating statuses: %s", e)
            db.session.rollback()


        # id = db.Column(db.Integer, primary_key = True, autoincrement=True)
        # title = db.Column(db.String(100), nullable = False)
        # order_of_severity_id = db.Column(db.Integer,db.ForeignKey('bug_order_of_severity.id'))
        # priority_id = db.Column(db.Integer,db.ForeignKey('bug_priority.id'))
        # model_id = db.Column(db.Integer,db.ForeignKey('models.id'))
        # version_id = db.Column(db.Integer,db.ForeignKey('versions.id'))
        # testing_environment_id = db.Column(db.Integer,db.ForeignKey('testing_environment.id'))
        # developer_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        # tester_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        # status_id = db.Column(db.Integer,db.ForeignKey('bug_status.id'))
        # procedure_description = db.Column(db.String(1000), nullable = False)
        # expected_result = db.Column(db.String(100))
        # actual_result = db.Column(db.String(100))
        # gmt_bug = db.Column(db.DateTime(), default=datetime.utcnow())
        # gmt_report = db.Column(db.DateTime(), default=datetime.utcnow())
        # screenshot = db.Column(db.JSON)
        # reason = db.Column(db.String(200))
        # solution = db.Column(db.String(300))
        # note = db.Column(db.String(300))
        # bug_comment = db.relationship('BugComment',backref='bug', lazy='dynamic')
        # # resolve sqlalchemy.exc.AmbiguousForeignKeysError:
        # developer = db.relationship("User", foreign_keys=[developer_id])
        # tester = db.relationship("User", foreign_keys=[tester_id])

        try:
            bugs = list()
            bugs.append(Bug(title='test bug', order_of_severity_id=1, priority_id=2, model_id=3, 
                version_id=10, testing_environment_id=3, tester_id=1, status_id=1, 
                procedure_description='procedure_description', expected_result='expected_result', actual_result='actual_result',
                screenshot=json.dumps([{'0': 'baidu.com'}, {'1': 'qq.com'}]), reason='reason', solution='solution', note='note' ))

            db.session.add(bugs[0])

            db.session.commit()
        except Exception as e:
            log.error("Creating bugs: %s", e)
            db.session.rollback()


        # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        # author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
        # bug_id = db.Column(db.Integer,db.ForeignKey('bugs.id'))
        # comment = db.Column(db.String(200), nullable = False)

        try:
            bug_comments = list()
            bug_comments.append(BugComment(author_id=1, bug_id=1, comment='comment' ))

            db.session.add(bug_comments[0])

            db.session.commit()
        except Exception as e:
            log.error("Creating bug_comments: %s", e)
            db.session.rollback()

        return jsonify({'success': 'auto insert init datas!'})
