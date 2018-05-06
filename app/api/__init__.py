from flask import Blueprint
api = Blueprint('api', __name__)

# from . import authentication, posts, users, comments, errors

from flask_restful import Api
from app.api.resources import Login, Logout, GetUser, Temperatures, AutoInit


api_resource = Api(api)

api_resource.add_resource(Login, '/user/login')
api_resource.add_resource(Logout, '/user/logout')
api_resource.add_resource(GetUser, '/user')


api_resource.add_resource(Temperatures, '/temperatures')

api_resource.add_resource(AutoInit, '/auto_init')

