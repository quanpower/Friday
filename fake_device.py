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

import json

# stm32 芯片id+sim800c 标识作为序列号
device_id = 'stm32009_sim800c009'
client_id = device_id
username = 'iiot'
password = 'smartlinkcloud'
strBroker = '101.200.158.2'
port = 1883

 
# 成功连接后的操作
def on_connect(client, userdata, flags, rc):
    print("OnConnetc, rc: " + str(rc))
 
#成功发布消息的操作
def on_publish(client,msg, rc):
    if rc == 0:
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
    on_exec(str(msg.payload))
 

def on_exec(strcmd):
    print("------Exec:---------")

    # {"DeviceId":"8YIHioUqFc1rCQCgBFtn","DeviceName":"stm32005_sim800c005","RequestId":"869FF8FC-A0E7-4D16-9951-654C66645EF7","DeviceSecret":"umbnJHfrdfqV89L8VQ1n18XYmWtqJ9FW","Success":true}
    # todo: save this result to local
 
if __name__ == '__main__':
    mqttc = mqtt.Client(client_id)
    mqttc.username_pw_set(username, password)
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log
    mqttc.connect(strBroker, port, 120)
    # mqttc.loop_start()
    time.sleep(1)
    
    # mqttc.subscribe("/a1nwrypxWbP/RTU_test1/data", qos=1)  # 换成自己的
    # haven't checked!
    # todo: check
    msg_dict = {'device_id':device_id, 'time':datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")}
    send_msg = json.dumps(msg_dict)
    
    # stm32_rtu's productKey:a1nwrypxWbP
    mqttc.publish("a1nwrypxWbP.register", payload=send_msg, qos=1, retain=False)
    
    # subscribe a1nwrypxWbP.register." + device_id
    mqttc.subscribe("a1nwrypxWbP.register." + device_id, qos=1)
    mqttc.loop_forever()
