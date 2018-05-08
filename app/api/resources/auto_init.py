from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import json

import logging
from app import db
import random
import datetime, time
import bitstring

from app.models import Project, Worker, Temperature, Power


class AutoInit(Resource):
    def get(self):

        log = logging.getLogger(__name__)

        time_now = datetime.datetime.now()


        try:
            daq_projects = list()
            daq_projects.append(Project(name='project1'))
            daq_projects.append(Project(name='project2'))
            daq_projects.append(Project(name='project3'))
            db.session.add(daq_projects[0])
            db.session.add(daq_projects[1])
            db.session.add(daq_projects[2])
            db.session.commit()
        except Exception as e:
            log.error("Creating daq_projects: %s", e)
            db.session.rollback()


        try:
            daq_workers = list()
            daq_workers.append(Worker(name='worker1', project=daq_projects[0]))
            daq_workers.append(Worker(name='worker2', project=daq_projects[0]))
            daq_workers.append(Worker(name='worker1', project=daq_projects[1]))
            daq_workers.append(Worker(name='worker2', project=daq_projects[1]))
            daq_workers.append(Worker(name='worker1', project=daq_projects[2]))
            daq_workers.append(Worker(name='worker2', project=daq_projects[2]))

            db.session.add(daq_workers[0])
            db.session.add(daq_workers[1])
            db.session.add(daq_workers[2])
            db.session.add(daq_workers[3])
            db.session.add(daq_workers[4])
            db.session.add(daq_workers[5])
            db.session.commit()
        except Exception as e:
            log.error("Creating daq_workers: %s", e)
            db.session.rollback()



        for i in range(1, 100):
            gt = Temperature()

            gt.project = daq_projects[0]
            gt.worker = daq_workers[0]
            gt.datetime = datetime.datetime.now()
            gt.value = json.dumps([[x,round(random.uniform(250,300),2)] for x in range(20)])

            db.session.add(gt)
            try:
                db.session.commit()
                print("inserted", gt)
            except Exception as e:
                log.error("Creating Temperature: %s", e)
                db.session.rollback()


        for i in range(1, 10):
            power = Power()
            power.project = daq_projects[0]
            power.worker = daq_workers[0]
            power.datetime = datetime.datetime.now()

            powerValue1 = [round(random.uniform(0, 30),2) for x in range(0,8)]
            powerValue2 = [round(random.uniform(0, 30),2) for x in range(0,8)]
            powerMoudle1 = [1, powerValue1]
            powerMoudle2 = [2, powerValue2]

            power.value = json.dumps([powerMoudle1,powerMoudle2])


            db.session.add(power)
            try:
                db.session.commit()
                print("inserted", power)
            except Exception as e:
                log.error("Creating Power: %s", e)
                db.session.rollback()

        return jsonify({'success': 'auto insert init datas!'})
