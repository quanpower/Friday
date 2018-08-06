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
 
# 设置连接信息
ProductKey = "a1nwrypxWbP" # ProductKey
DeviceName = "stm32009_sim800c009"  # DeviceName

 
strBroker = 'a1nwrypxWbP.iot-as-mqtt.cn-shanghai.aliyuncs.com'
port = 1883
 
client_id = "We9mDB5oUA95aomeTet5|securemode=3,signmethod=hmacsha1,timestamp=709|"
username = "stm32009_sim800c009&a1nwrypxWbP"
password = '93c000d17eec6ece3c08aaa010c0982418a5be0e'
# print("="*30)
# print("client_id:", client_id)
# print("username:", username)
# print("password:", password)
# print("="*30)
 
 
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
    print(strcurtime + ": " + msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    on_exec(str(msg.payload))
 
def on_exec(strcmd):
    print("Exec:", strcmd)
    strExec = strcmd
 
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
    while 1:
        # send senser data to aliiot
        send_mseg = '{"AI1": %s, "AI2": %s, "AI3": %s, "AI4": %s, time":"%s"}'%(1.1, 2.2, 3.3, 4.4, datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
        mqttc.publish("/{0}/{1}/data".format(ProductKey, DeviceName),payload=send_mseg, qos=1, retain=False)  # 换成自己的
        time.sleep(60)

    # mqttc.loop_forever()
