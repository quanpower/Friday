from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import time
import datetime
import json
import markdown

import os

# print(os.path.abspath(__file__))

base_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), "../../../.."))
# print(base_dir)



class ChangeLog(Resource):

    def get(self):
        with open(os.path.join(base_dir, 'CHANGELOG.md'), 'r') as f:
            # python markdowm
            # html = markdown.markdown(f.read())
            md = f.read()
            print(md)
            return md

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass



class TodoList(Resource):

    def get(self):
        with open(os.path.join(base_dir, 'TODOLIST.md'), 'r') as f:
            md = f.read()
            print(md)
            return md

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass