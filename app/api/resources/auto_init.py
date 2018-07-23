from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import json

import logging
from app import db
import random
import datetime, time
import bitstring

from app.models import User, Project, Product, Device, Daq, Alarm


class AutoInit(Resource):
    def get(self):

        log = logging.getLogger(__name__)

        time_now = datetime.datetime.now()


        try:
            daq_projects = list()
            daq_projects.append(Project(name='20180719'))
            daq_projects.append(Project(name='20180720'))
            daq_projects.append(Project(name='20180721'))
            db.session.add(daq_projects[0])
            db.session.add(daq_projects[1])
            db.session.add(daq_projects[2])
            db.session.commit()
        except Exception as e:
            log.error("Creating daq_projects: %s", e)
            db.session.rollback()


        try:
            daq_workers = list()
            daq_workers.append(Worker(name='20180719_01', project=daq_projects[0]))
            daq_workers.append(Worker(name='20180719_02', project=daq_projects[0]))
            daq_workers.append(Worker(name='20180720_01', project=daq_projects[1]))
            daq_workers.append(Worker(name='20180720_02', project=daq_projects[1]))
            daq_workers.append(Worker(name='20180721_01', project=daq_projects[2]))
            daq_workers.append(Worker(name='20180721_02', project=daq_projects[2]))

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
            gt = DAQ()

            gt.project = daq_projects[0]
            gt.worker = daq_workers[0]
            gt.datetime = datetime.datetime.now()
            gt.value = json.dumps([[str(x), round(random.uniform(25,30),2)] for x in range(16)])

            db.session.add(gt)
            try:
                db.session.commit()
                print("inserted", gt)
            except Exception as e:
                log.error("Creating Temperature: %s", e)
                db.session.rollback()


        for i in range(1, 10):
            gt = Alarm()

            gt.project = daq_projects[0]
            gt.worker = daq_workers[0]
            gt.datetime = datetime.datetime.now()
            gt.value = json.dumps([[str(x), random.choice(['0', '1'])] for x in range(16)])

            db.session.add(gt)
            try:
                db.session.commit()
                print("inserted", gt)
            except Exception as e:
                log.error("Creating Temperature: %s", e)
                db.session.rollback()




        return jsonify({'success': 'auto insert init datas!'})
