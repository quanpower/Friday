#!/usr/bin/python2
# coding=utf-8
import datetime
import time
import hmac
import hashlib
import math
try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("MQTT client not find. Please install as follow:")
    print("pip install paho-mqtt")
import paho.mqtt.publish as publish

import json


productKey = 'a1nwrypxWbP'
# stm32 芯片id+sim800c 标识作为序列号
device_name = 'stm320012_sim800c0012'


client_id = device_name
username = 'iiot'
password = 'smartlinkcloud'
strBroker = '101.200.158.2'
port = 1883

 
# 成功连接后的操作
def on_connect(client, userdata, flags, rc):
    print("OnConnetc, rc: " + str(rc))

    # subscribe on connect!
    client.subscribe("utctime", qos=1)
    client.subscribe(productKey +'.register.' + device_name, qos=1)

#成功发布消息的操作
def on_publish(client,msg, rc):
    if rc == 0:
        print("---------in publish--------")
        print("publish success, msg = " + msg)
 
#成功订阅消息的操作
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))
 
 
def on_log(mqttc, obj, level, string):
    print("Log:" + string)
 
 
def on_message(mqttc, obj, msg):
    curtime = datetime.datetime.now()
    strcurtime = curtime.strftime("%Y-%m-%d %H:%M:%S")
    print("------on_message:---------")

    print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if msg.topic.split('/')[0] == productKey:
        payload_dict = json.loads(msg.payload)
        # 1.Register successed!
        if payload_dict['Success'] :
            print('Register successed!')
            # unsubscribe {productKey}/register/devicename
            mqttc.unsubscribe(productKey +'.register.' + device_name)
        else:
            # 2.Register failure!

            # fake utctime
            utctime = int(time.time())
            # msg_dict = {'device_name':device_name, 'time':datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}
            msg_dict = {'device_name':device_name, 'time':utctime}
            send_msg = json.dumps(msg_dict)
            topic = productKey + '.register'
            mqttc.publish(topic, payload=send_msg, qos=1, retain=False)

    elif msg.topic == 'utctime':
        # get the utctime from server and pub the first register request!
        print('-------msg utc--------')
        utctime = json.loads(msg.payload)['utctime']
        print('-----#######utctime########-----')
        print(utctime)
        # msg_dict = {'device_name':device_name, 'time':datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}
        msg_dict = {'device_name':device_name, 'time':utctime}
        send_msg = json.dumps(msg_dict)
        topic = productKey + '.register'
        # pub request
        mqttc.publish(topic, payload=send_msg, qos=1, retain=False)
        # unsubscribe utctime,maybe need judge!
        mqttc.unsubscribe('utctime')
    else:
        print('Unkown topic!')
 
if __name__ == '__main__':
    mqttc = mqtt.Client(client_id)
    mqttc.username_pw_set(username, password)
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log

    mqttc.connect(strBroker, port, 120)
    
    mqttc.loop_forever()
