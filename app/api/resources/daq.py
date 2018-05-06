from flasgger import Swagger, swag_from
from flask import Flask, redirect, url_for, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from app import db
from app.models import Temperature
from sqlalchemy import and_
import json
import random
import datetime, time

import bitstring
import json
import urllib
from app.email import send_email


# api = Api(app)
#
# swagger = Swagger(app)


class Temperatures(Resource):
    '''
        get the lates 10 temps.
    '''

    def get(self):
        # parser = reqparse.RequestParser()
        # parser.add_argument('gatewayAddr', type=str)
        # parser.add_argument('nodeAddr', type=str)

        # args = parser.parse_args()

        # print('-------aircontemps args---------', args)

        # gatewayAddr = args['gatewayAddr']
        # nodeAddr = args['nodeAddr']

        temp_records = db.session.query(Temperature.datetime, Temperature.channel, Temperature.value).order_by(
            Temperature.datetime.desc()).limit(100).all()

        temp_log = []
        for i in range(len(temp_records)):
            temp_log.append({"datetime": temp_records[i][0].strftime("%Y-%m-%d %H:%M:%S"), "channel": temp_records[i][1],
                             "value": temp_records[i][2]})

        temps_reverse = temp_log[::-1]
        print('------------temps_reverse--------------')
        print(temps_reverse)

        temps_dict = {"Temps": temps_reverse}
        return temps_dict

    def delete(self):
        pass

    def put(self):
        pass


class TempRecord(Resource):
    '''
        get the temp records by the input datetime. %H:%M:S%
    '''

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('gateway_addr', type=str)
        parser.add_argument('node_addr', type=str)
        parser.add_argument('start_time', type=str)
        parser.add_argument('end_time', type=str)

        args = parser.parse_args()

        print('--------AirConTempRecord-------', args)

        gatewayAddr = args['gateway_addr']
        nodeAddr = args['node_addr']
        startTime = datetime.datetime.strptime(args['start_time'], "%Y-%m-%d %H:%M:%S")
        endTime = datetime.datetime.strptime(args['end_time'], "%Y-%m-%d %H:%M:%S")

        print(startTime)
        print(endTime)

        temp_records = db.session.query(GrainTemp.temp1, GrainTemp.temp2, GrainTemp.temp3, GrainTemp.datetime).join(
            LoraNode, LoraNode.id == GrainTemp.lora_node_id).join(
            LoraGateway, LoraGateway.id == GrainTemp.lora_gateway_id).filter(
            and_(LoraNode.node_addr == nodeAddr, LoraGateway.gateway_addr == gatewayAddr,
                 GrainTemp.datetime.between(startTime, endTime))).order_by(
            GrainTemp.datetime.desc()).all()
        # print('*********temp_records*************', temp_records)

        temp_log = []
        for i in range(len(temp_records)):
            temp_log.append(
                {"key": i, "time": temp_records[i][3].strftime("%Y-%m-%d %H:%M:%S"), "Temp1": temp_records[i][0],
                 "Temp2": temp_records[i][1], "Temp3": temp_records[i][2]})

        temps_reverse = temp_log[::-1]
        print('------------temps_records--------------')
        # print(temps_reverse)

        temps_record_dict = {"airConTempRecord": temps_reverse}
        return temps_record_dict

    def delete(self):
        pass

    def put(self):
        pass



        