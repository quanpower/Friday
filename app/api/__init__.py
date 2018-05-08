from flask import Blueprint
api = Blueprint('api', __name__)

# from . import authentication, posts, users, comments, errors

from flask_restful import Api
from app.api.resources import Login, Logout, GetUser, Register, Users, TemperatureRealtime, TemperatureHistory, CurrentPower, HistoryPower, AutoInit, FakeNotices


api_resource = Api(api)


api_resource.add_resource(Register, '/register', endpoint='register')
api_resource.add_resource(Login, '/login/account', endpoint='login')
api_resource.add_resource(Logout, '/logout', endpoint='logout')
api_resource.add_resource(GetUser, '/currentUser', endpoint='getUser')
api_resource.add_resource(Users, '/users', endpoint='users')


api_resource.add_resource(TemperatureRealtime, '/temperature/realtime', endpoint='temperature_realtime')
api_resource.add_resource(TemperatureHistory, '/temperature/history', endpoint='temperature_history')
api_resource.add_resource(CurrentPower, '/power/current', endpoint='current_power')
api_resource.add_resource(HistoryPower, '/power/history', endpoint='history_power')

api_resource.add_resource(AutoInit, '/auto_init', endpoint='autoInit')


api_resource.add_resource(FakeNotices, '/project/notice', endpoint='projectNotice')
api_resource.add_resource(FakeNotices, '/notices', endpoint='notices')

