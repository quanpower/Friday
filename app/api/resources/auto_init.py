from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import json

import logging
from app import db
import random
import datetime, time
import bitstring

from app.models import Temperature, Power


class AutoInit(Resource):
    def get(self):

        log = logging.getLogger(__name__)

        time_now = datetime.datetime.now()

        for i in range(1, 100):
            gt = Temperature()


            gt.datetime = datetime.datetime.now()
            gt.channel = str(random.randrange(0,20))
            gt.value = random.randrange(250, 300)

            db.session.add(gt)
            try:
                db.session.commit()
                print("inserted", gt)
            except Exception as e:
                log.error("Creating GrainTemp: %s", e)
                db.session.rollback()


        for i in range(1, 10):
            power = Power()

            power.datetime = datetime.datetime.now()
            power.voltage1 = random.randrange(0, 30)
            power.current1 = random.randrange(0, 5)
            power.voltage2 = random.randrange(0, 30)
            power.current2 = random.randrange(0, 5)
            power.voltage3 = random.randrange(0, 30)
            power.current3 = random.randrange(0, 5)
            power.voltage4 = random.randrange(0, 30)
            power.current4 = random.randrange(0, 5)

            db.session.add(power)
            try:
                db.session.commit()
                print("inserted", power)
            except Exception as e:
                log.error("Creating Power: %s", e)
                db.session.rollback()

        return jsonify({'success': 'auto insert init datas!'})
