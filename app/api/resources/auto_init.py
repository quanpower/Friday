from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, abort
import json

import logging
from app import db
import random
import datetime, time
import bitstring

from app.models import Temperature


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

        return jsonify({'success': 'auto insert init datas!'})
