from flasgger import Swagger, swag_from
from flask import Flask, redirect, url_for, request, jsonify, make_response
from flask_restful import reqparse, abort, Api, Resource
from app import db
from app.models import Temperature, Power
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

    def post(self):
        pass


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

    def post(self):
        pass


    def delete(self):
        pass

    def put(self):
        pass


class CurrentPower(Resource):
    '''
        get the power voltage and current value. 
    '''

    def get(self):

        current_power = db.session.query(Power.datetime, Power.voltage1, Power.current1, Power.voltage2, Power.current2, Power.voltage3, Power.current3, Power.voltage4, Power.current4).order_by(
            Power.datetime.desc()).first()

        history_power = db.session.query(Power.datetime, Power.voltage1, Power.current1, Power.voltage2, Power.current2, Power.voltage3, Power.current3, Power.voltage4, Power.current4).order_by(
            Power.datetime.desc()).all()

        mini_area_data1 = []
        mini_area_data2 = []
        mini_area_data3 = []
        mini_area_data4 = []

        for i in range(len(history_power[0])):
            voltage_dict1 = {'x': history_power[i][0].strftime("%Y-%m-%d %H:%M:%S"),
                            'y': history_power[i][1]}
            mini_area_data1.append(voltage_dict1)

            voltage_dict2= {'x': history_power[i][0].strftime("%Y-%m-%d %H:%M:%S"),
                            'y': history_power[i][3]}
            mini_area_data2.append(voltage_dict2)

            voltage_dict3 = {'x': history_power[i][0].strftime("%Y-%m-%d %H:%M:%S"),
                            'y': history_power[i][5]}
            mini_area_data3.append(voltage_dict3)

            voltage_dict4 = {'x': history_power[i][0].strftime("%Y-%m-%d %H:%M:%S"),
                            'y': history_power[i][7]}
            mini_area_data4.append(voltage_dict4)

        current_time = current_power[0].strftime("%Y-%m-%d %H:%M:%S")
        
        channel1_dict ={'bordered':False,
        'title':'电压1',
        'tooltip_title':'通道1',
        'voltage':current_power[1],
        'footer_label':'时间',
        'footer_value':current_time,
        'contentHeight':46,
        'mini_area_color':'#DC143C',
        'mini_area_data':mini_area_data1,
        }
        

        channel2_dict ={'bordered':False,
        'title':'电压2',
        'tooltip_title':'通道2',
        'voltage':current_power[3],
        'footer_label':'时间',
        'footer_value':current_time,
        'contentHeight':46,
        'mini_area_color':'#975FE4',
        'mini_area_data':mini_area_data2,
        }
        

        channel3_dict ={'bordered':False,
        'title':'电压3',
        'tooltip_title':'通道3',
        'voltage':current_power[5],
        'footer_label':'时间',
        'footer_value':current_time,
        'contentHeight':46,
        'mini_area_color':'#0000FF',
        'mini_area_data':mini_area_data3,
        }
        

        channel4_dict ={'bordered':False,
        'title':'电压4',
        'tooltip_title':'通道4',
        'voltage':current_power[7],
        'footer_label':'时间',
        'footer_value':current_time,
        'contentHeight':46,
        'mini_area_color':'#00FFFF',
        'mini_area_data':mini_area_data4,
        }
        
        current_power_list = []
        current_power_list.append(channel1_dict)
        current_power_list.append(channel2_dict)
        current_power_list.append(channel3_dict)
        current_power_list.append(channel4_dict)

        return jsonify({'currentPower': current_power_list}) 

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass


 
class HistoryPower(Resource):
    '''
        get the power voltage and current value history records.  
    '''

    def get(self):


        current_power = db.session.query(Power.datetime, Power.voltage1, Power.current1, Power.voltage2, Power.current2, Power.voltage3, Power.current3, Power.voltage4, Power.current4).order_by(
            Power.datetime.desc()).first()

        power_log = []
        for i in range(len(temp_records)):
            temp_log.append(
                {"key": i, "time": temp_records[i][3].strftime("%Y-%m-%d %H:%M:%S"), "Temp1": temp_records[i][0],
                 "Temp2": temp_records[i][1], "Temp3": temp_records[i][2]})

        temps_reverse = temp_log[::-1]
        print('------------temps_records--------------')
        # print(temps_reverse)

        temps_record_dict = {"airConTempRecord": temps_reverse}
        return temps_record_dict

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass

