from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import time
import datetime
import json
from app.models import User
from app import db


tokens = {
  'admin': {
    'token': 'admin-token'
  },
  'editor': {
    'token': 'editor-token'
  }
}


users = {
  'admin-token': {
    'roles': ['admin'],
    'introduction': 'I am a super administrator',
    'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
    'name': 'Super Admin',
    'flicketToken': '4eJD8FYiehXS0jXZMcoDhLW3bdMOY1Pv'
  },
  'editor-token': {
    'roles': ['editor'],
    'introduction': 'I am an editor',
    'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',
    'name': 'Normal Editor',
    'flicketToken': '4eJD8FYiehXS0jXZMcoDhLW3bdMOY1Pv'
  }
}


class Register(Resource):

    def get(self):
        pass

    def post(self):

        # parser = reqparse.RequestParser()
        # parser.add_argument('userName', type=str)
        # parser.add_argument('password', type=str)
        # parser.add_argument('email', type=str)
        # parser.add_argument('phone', type=str)

        # args = parser.parse_args()

        # username = args['userName']
        # password = args['password']
        # email = args['email']
        # phone = args['phone']

        # user = User(email=email,
        #             username=username,
        #             password=password,
        #             about_me=phone)
        # db.session.add(user)
        # db.session.commit()

        return jsonify({ 'status': 'ok', 'currentAuthority': 'user' })

    def delete(self):
        pass

    def put(self):
        pass



class Login(Resource):

    def get(self):
        pass

    def post(self):
        data = request.get_data()
        json_data = json.loads(data)
        print(json_data)
        username = json_data.get('username')

        print(username)
        # post_type = args['type']

        # user = User.query.filter_by(email=username).first()
        # if user is not None and user.verify_password(password):
        # todo: auth
        if True:
            print('-----verify success!-----')
            # user_id = user.id
            # print(user_id)


            if username == 'admin':
                return jsonify({
                    'code': 20000,
                    'data': tokens['admin']['token']
                  })
            else:
                return jsonify({
                    'code': 20000,
                    'data': tokens['editor']['token']
                  })
        else:
            return jsonify({
              code: 60204,
              message: 'Account and password are incorrect.'
            })

    def delete(self):
        pass

    def put(self):
        pass


class Logout(Resource):

    def get(self):
        resp = make_response("Delete cookie")
        resp.delete_cookie('token')
        return resp

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass


class Users(Resource):

    def get(self):
        users = User.query.all()
        resp = []
        for user in users:
            user_dict = {
            'key':user.id,
            'name':user.username,
            'age':user.name,
            'address':user.location,
            }
            resp.append(user_dict)
        return jsonify(resp)

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass


class GetUser(Resource):
    def get(self):

        return jsonify({
                      'name': 'William Zhang',
                      'avatar': 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png',
                      'userid': '00000001',
                      'notifyCount': 12,
                  })

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass


class UserInfo(Resource):
    def get(self):

        parser = reqparse.RequestParser()
        parser.add_argument('token', type=str)
        # parser.add_argument('type', type=str)

        args = parser.parse_args()

        token = args['token']

        print(token)

        # info = users[token]
        info = users['admin-token']

        print('----info-----')
        print(info)

        if(not info):
            return jsonify({
            'code': 50008,
            'message': 'Login failed, unable to get user details.'
            })
        else:
            return jsonify({
                    'code': 20000,
                    'data': info
            })


    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass