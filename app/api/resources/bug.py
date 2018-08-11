from flasgger import Swagger, swag_from
from flask import Flask, redirect, url_for, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from app import db
from app.models import BugOrderOfSeverity, BugPriority, Models, Version, TestingEnvironment, BugStatus, BugComment, Bug
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


class Bugs(Resource):
    '''
    get the bugs.

    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    title = db.Column(db.String(100), nullable = False)
    order_of_severity_id = db.Column(db.Integer,db.ForeignKey('bug_order_of_severity.id'))
    priority_id = db.Column(db.Integer,db.ForeignKey('bug_priority.id'))
    model_id = db.Column(db.Integer,db.ForeignKey('models.id'))
    version_id = db.Column(db.Integer,db.ForeignKey('versions.id'))
    testing_environment_id = db.Column(db.Integer,db.ForeignKey('testing_environment.id'))
    developer_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    tester_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    status_id = db.Column(db.Integer,db.ForeignKey('bug_status.id'))
    procedure_description = db.Column(db.String(1000), nullable = False)
    expected_result = db.Column(db.String(100))
    actual_result = db.Column(db.String(100))
    gmt_bug = db.Column(db.DateTime(), default=datetime.utcnow())
    gmt_report = db.Column(db.DateTime(), default=datetime.utcnow())
    screenshot = db.Column(db.JSON)
    reason = db.Column(db.String(200))
    solution = db.Column(db.String(300))
    note = db.Column(db.String(300))
    bug = db.relationship('BugComment',backref='bug', lazy='dynamic')
    '''

    def get(self):
        bugs = Bug.query.all()

        bugLists = []

        for bug in projects:
            bug_id = bug.id
            bug_title = bug.title
            order_of_severity = bug.severity.name
            priority = bug.priority.name
            model = bug.models.name
            version = bug.version.name
            testing_environment = bug.environment.name
            developer = bug.developer.email
            tester = bug.tester.email
            status = bug.status.name
            procedure_description = bug.procedure_description
            expected_result = bug.expected_result
            actual_result = bug.actual_result
            gmt_bug = bug.gmt_bug
            gmt_report = bug.gmt_report
            screenshot = bug.screenshot
            reason = bug.reason
            solution = bug.solution
            note = bug.note


            bugLists.append({
                'id':bug_id,
                'title':bug_title,
                'severity':order_of_severity,
                'priority':priority,
                'model': model,
                'version': version,
                'environment': testing_environment,
                'tester': tester,
                'status': status,
                'description': procedure_description,
                'expected_result':expected_result,
                'actual_result':actual_result,
                'gmt_bug':gmt_bug,
                'gmt_report':gmt_report,
                'screenshot':screenshot,
                'reason':reason,
                'solution':solution,
                'note':note,
                # 'devices': devices,
                })

        print('---------bugLists-------')
        print(bugLists)
        return jsonify(bugLists) 

    def post(self):
        pass


    def delete(self):
        pass


    def put(self):
        pass

