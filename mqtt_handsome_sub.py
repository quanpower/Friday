# -*- coding:utf-8 -*-
import os
import sys
import datetime
import socket, sys
import struct
from bitstring import BitArray, BitStream
import binascii
import logging
import pymysql
import json
import random

from dotenv import find_dotenv,load_dotenv
import os


load_dotenv(find_dotenv())

print(os.environ.get('PYMYSQL_HOST'))


# from app import db
# from utils import crc_func, sign


# from sqlalchemy import create_engine, and_
# from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///data.sqlite')
# # 创建DBSession类型:
# Session = sessionmaker(bind=engine)
# db_session=Session()


# 第一步，创建一个logger  
logger = logging.getLogger()  
logger.setLevel(logging.INFO)    # Log等级总开关  
  
# 第二步，创建一个handler，用于写入日志文件  
parent_dir = os.path.dirname(__file__)
logfile = os.path.join(parent_dir, 'log/handsome_sub_logger.txt')
fh = logging.FileHandler(logfile, mode='w')  
fh.setLevel(logging.DEBUG)   # 输出到file的log等级的开关  
  
# 第三步，再创建一个handler，用于输出到控制台  
ch = logging.StreamHandler()  
ch.setLevel(logging.WARNING)   # 输出到console的log等级的开关  
  
# 第四步，定义handler的输出格式  
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")  
fh.setFormatter(formatter)  
ch.setFormatter(formatter)  
  
# 第五步，将logger添加到handler里面  
logger.addHandler(fh)  
logger.addHandler(ch)  
  
# 日志  
logger.debug('this is a logger debug message')  
logger.info('this is a logger info message')  
logger.warning('this is a logger warning message')  
logger.error('this is a logger error message')  
logger.critical('this is a logger critical message') 

#======================================================    

#MQTT Initialize.--------------------------------------
try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("MQTT client not find. Please install as follow:")
    print("git clone http://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git")
    print("cd org.eclipse.paho.mqtt.python")
    print("sudo python setup.py install")


host = os.environ.get('PYMYSQL_HOST')
db = os.environ.get('PYMYSQL_DB')
user = os.environ.get('PYMYSQL_USER')
password = os.environ.get('PYMYSQL_PASSWORD')



db= pymysql.connect(host=host,user=user,
    password=password,db=db)
cursor = db.cursor()

#======================================================
# def on_connect(mqttc, obj, rc):
def on_connect(client, userdata, flags, rc):
    logger.info("OnConnetc, rc: "+str(rc))

def on_publish(mqttc, obj, mid):
    logger.info("OnPublish, mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    logger.info("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    logger.info("Log:"+string)

def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    logger.info(strcurtime + ": " + msg.topic+" "+str(msg.qos)+" "+str(msg.payload))  
    print('\n' *3)
    print('-----------------receive time----------------------')
    print(datetime.datetime.now())

    payload_length = len(msg.payload)
    print('-------payload_length---------')
    print(payload_length)
    print('-------msg.payload---------')
    print(msg.payload)

    un_int = struct.unpack(str(payload_length) + 'B', msg.payload)
    print(un_int)
    # uints = list(un_int)
    # print(uints)

    json_data = plc_unpacking(msg.payload)
    update_current(json_data)



def on_exec(strcmd):
    logger.debug("Exec:", strcmd)
    strExec = strcmd


def plc_unpacking(packet_data):
    logger.info('--------plc_unpacking process beginning-----------')
    print('--------plc_unpacking process beginning-----------')

    # DI
    emergency_button = packet_data[0:4]
    pressure_detect = packet_data[4:8]
    encoder = packet_data[8:12]
    bak_1 = packet_data[12:16]

    error_1 = packet_data[16:20]
    error_2 = packet_data[20:24]
    error_3 = packet_data[24:28]
    error_4 = packet_data[28:32]

    access_control = packet_data[32:36]

    comprehensive_alarm = packet_data[36:40]
    abnormal_alarm = packet_data[40:44]
    normal_operation = packet_data[44:48]

    local_remote = packet_data[48:52]


    control_button_1 = packet_data[52:56]
    control_button_2 = packet_data[56:60]
    control_button_3 = packet_data[60:64]
    control_button_4 = packet_data[64:68]

    mantual_auto = packet_data[68:72]

    error_time_clear = packet_data[72:76]
    run_time_clear = packet_data[76:80]
    blow_head_time_clear = packet_data[80:84]
    board_time_clear = packet_data[84:88]
    injector_time_clear = packet_data[88:92]
    filter_time_clear = packet_data[92:96]

    blow_head_time_alarm = packet_data[96:100]
    board_time_alarm = packet_data[100:104]
    injector_time_alarm = packet_data[104:108]
    filter_time_alarm = packet_data[108:112]
    maintenance_period_alarm = packet_data[112:116]

    current_1_low_alarm = packet_data[116:120] 
    current_1_high_alarm = packet_data[120:124]
    current_2_low_alarm = packet_data[124:128]
    current_2_high_alarm = packet_data[128:132]   
    current_3_low_alarm = packet_data[132:136]
    current_3_high_alarm = packet_data[136:140]
    current_4_low_alarm = packet_data[140:144]
    current_4_high_alarm = packet_data[144:148]

    injector_1_current = packet_data[148:152]
    injector_2_current = packet_data[152:156]
    injector_3_current = packet_data[156:160]
    injector_4_current = packet_data[160:164]

    motor_1_current = packet_data[164:168]
    motor_2_current = packet_data[168:172]
    motor_3_current = packet_data[172:176]
    motor_4_current = packet_data[176:180]
    line_speed = packet_data[180:184]

    current_1_low_limit = packet_data[184:188]
    current_2_low_limit = packet_data[188:192]
    current_3_low_limit = packet_data[192:196]
    current_4_low_limit = packet_data[196:200]
    line_speed_low_limit = packet_data[200:204]

    current_1_high_limit = packet_data[204:208]
    current_2_high_limit = packet_data[208:212]
    current_3_high_limit = packet_data[212:216]
    current_4_high_limit = packet_data[216:220]
    line_speed_high_limit = packet_data[220:224]

    total_running_time = packet_data[224:228]

    blow_head_maintenance_time = packet_data[228:232]
    board_maintenance_time = packet_data[232:236]
    injector_maintenance_time = packet_data[236:240]
    filter_maintenance_time = packet_data[240:244]

    error_time = packet_data[244:248]
    current_running_time = packet_data[248:252]


    current_value1_str = "%.2f" % struct.unpack('<f', injector_1_current)[0]
    current_value2_str = "%.2f" % struct.unpack('<f', injector_2_current)[0]
    current_value3_str = "%.2f" % struct.unpack('<f', injector_3_current)[0]
    current_value4_str = "%.2f" % struct.unpack('<f', injector_4_current)[0]
    current_value5_str = "0.0"
    current_value6_str = "0.0"


    input_pressure_value_str = "%.2f" % random.uniform(2.1,2.4)
    material_temprature_value_str = "%.2f" % random.uniform(28.1,28.4)
    line_speed_value_str = "%.2f" % struct.unpack('<f', line_speed)[0]


    comprehensive_alarm_str = str(struct.unpack('i', comprehensive_alarm)[0])
    abnormal_alarm_str = str(struct.unpack('i', abnormal_alarm)[0])
    normal_operation_str = str(struct.unpack('i', normal_operation)[0])

    emergency_button_str = str(struct.unpack('i', emergency_button)[0])
    pressure_detect_str = str(struct.unpack('i', pressure_detect)[0])


    print('--emergency_button_str,pressure_detect_str---')
    print(emergency_button_str)
    print(pressure_detect_str)


    print('--comprehensive_alarm_str, abnormal_alarm_str,normal_operation_str ---')
    print(comprehensive_alarm_str)
    print(abnormal_alarm_str)
    print(normal_operation_str)


    print('--------error_1_str,error_2_strerror_3_str,error_4_str-----------')

    print(struct.unpack('i', error_1)[0])
    print(struct.unpack('i', error_2)[0])
    print(struct.unpack('i', error_3)[0])
    print(struct.unpack('i', error_4)[0])


    access_control_str = str(struct.unpack('i', error_1)[0])
    print('----access_control_str----')
    print(access_control_str)



    error_1_str = str(struct.unpack('i', error_1)[0])
    control_button_1_str = str(struct.unpack('i', control_button_1)[0])

    if error_1_str == '1':
        work_status_1 = '-1'
    else:
        if control_button_1_str == '1':
            work_status_1 = '1'
        else :
            work_status_1 = '0'


    error_2_str = str(struct.unpack('i', error_2)[0])
    control_button_2_str = str(struct.unpack('i', control_button_2)[0])
    
    if error_2_str == '1':
        work_status_2 = '-1'
    else:
        if control_button_2_str == '1':
            work_status_2 = '1'
        else :
            work_status_2 = '0'


    error_3_str = str(struct.unpack('i', error_3)[0])
    control_button_3_str = str(struct.unpack('i', control_button_3)[0])
    
    if error_3_str == '1':
        work_status_3 = '-1'
    else:
        if control_button_3_str == '1':
            work_status_3 = '1'
        else :
            work_status_3 = '0'


    error_4_str = str(struct.unpack('i', error_4)[0])
    control_button_4_str = str(struct.unpack('i', control_button_4)[0])
    
    if error_4_str == '1':
        work_status_4 = '-1'
    else:
        if control_button_4_str == '1':
            work_status_4 = '1'
        else :
            work_status_4 = '0'


    total_running_time_h_str = str(struct.unpack('i', total_running_time)[0])
    current_running_time_int = struct.unpack('i', current_running_time)[0]
    current_running_time_h_str = str(current_running_time_int//60)
    current_running_time_min_str = str(current_running_time_int%60)



    data = {
        'current_value':{    
            'current_value_1': current_value1_str,
            'current_value_2': current_value2_str,
            'current_value_3': current_value3_str,
            'current_value_4': current_value4_str,
            'current_value_5': current_value5_str,
            'current_value_6': current_value6_str,
        },
        'work_status':{
            'work_status_1':work_status_1,
            'work_status_2':work_status_2,
            'work_status_3':work_status_3,
            'work_status_4':work_status_4,
            'work_status_5':'0',
            'work_status_6':'0',
        },
        'input_pressure':input_pressure_value_str,
        'material_temprature':material_temprature_value_str,
        'line_speed':line_speed_value_str,
        'current_running_time':{
            'h':current_running_time_h_str,
            'min':current_running_time_min_str,
            's':'00',
        },
        'accumulated_running_time':{
            'h':total_running_time_h_str,
            'min':'00',
            's':'00',
        },
        'current_time':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    }

    return data



def update_current(data):
    device_daqs_json = json.dumps(data)

    print('------device_daqs_json-----')
    print(device_daqs_json)


    # # SQL 插入语句
    # # sql = 'INSERT INTO daqs(device_id, gmt_daq, daq_value) VALUES ({0}, {1}, {2})'.format(1, datetime.datetime.utcnow(), device_daqs_json)
    sql = """INSERT INTO `daqs` (`device_id`, `gmt_daq`, `daq_value`) VALUES (%s, %s, %s)"""
    # # cursor.execute(sql, ('webmaster@python.org', 'very-secret'))


    try:
        # 执行sql语句
        cursor.execute(sql, (4, datetime.datetime.now(), device_daqs_json))
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
        logger.error("Inserting device_daqs: %s", e)

        print('insert error!')
        print(e)


def lora_unpacking_ack(packet_data):
    # todo
    logger.info('-------- ack data process beginning -----------')
    print('------receive time------')
    print(datetime.datetime.now())

#=====================================================
def mqtt_handsome_sub():

    mqttc = mqtt.Client("handsome.00000001.upstream.subscriber")
    mqttc.username_pw_set("iiot", "smartlinkcloud")
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log

    #strBroker = "localhost"
    strBroker = "101.200.158.2"

    mqttc.connect(strBroker, 1883, 60)
    mqttc.subscribe("handsome.00000001.upstream", 0)
    mqttc.loop_forever()

if __name__ == '__main__':

    mqtt_handsome_sub()