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


# strMqttBroker = 'test.mosquitto.org'
strMqttBroker = 'broker.hivemq.com'

def pub_utctime():
         
    # curtime = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    curtime = int(time.time())
    curtime_dict = {'utctime': curtime}
    curtime_json = json.dumps(curtime_dict)

    print('--------------curtime------------')
    print(datetime.datetime.now())
    print(curtime_json)    
    print('\n' * 2)

    # publish.single('utctime', curtime_json, hostname=strMqttBroker, auth={'username': 'iiot', 'password': 'smartlinkcloud'})
    publish.single('utctime', curtime_json, hostname=strMqttBroker)


if __name__ == '__main__':


    while 1:
        pub_utctime()
        time.sleep(1)
