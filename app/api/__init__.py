from flask import Blueprint
api = Blueprint('api', __name__)

# from . import authentication, posts, users, comments, errors

from flask_restful import Api
from app.api.resources import Login, Logout, GetUser, Register, Users, Projects, Products, Devices, DeviceDaqRealtime, DeviceDaqAlarm, DeviceDaqHistory, DeviceDaqRecord, AutoInit, FakeNotices


api_resource = Api(api)


api_resource.add_resource(Register, '/register', endpoint='register')
api_resource.add_resource(Login, '/login/account', endpoint='login')
api_resource.add_resource(Logout, '/logout', endpoint='logout')
api_resource.add_resource(GetUser, '/currentUser', endpoint='getUser')
api_resource.add_resource(Users, '/users', endpoint='users')


api_resource.add_resource(Projects, '/projects', endpoint='projects')
api_resource.add_resource(Products, '/products', endpoint='products')
api_resource.add_resource(Devices, '/devices', endpoint='devices')
api_resource.add_resource(DeviceDaqRealtime, '/daq/realtime', endpoint='daq_realtime')
api_resource.add_resource(DeviceDaqHistory, '/daq/history', endpoint='daq_history')
api_resource.add_resource(DeviceDaqRecord, '/daq/record', endpoint='daq_record')
api_resource.add_resource(DeviceDaqAlarm, '/daq/alarm', endpoint='daq_alarm')


api_resource.add_resource(AutoInit, '/auto_init', endpoint='autoInit')


api_resource.add_resource(FakeNotices, '/project/notice', endpoint='projectNotice')
api_resource.add_resource(FakeNotices, '/notices', endpoint='notices')

