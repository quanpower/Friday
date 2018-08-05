# !/usr/bin/python3
 
import datetime
import time
import hmac
import hashlib
import math
 
TEST = 0
 
ProductKey = "a1nwrypxWbP"
ClientId = "12345"  # 自定义clientId
DeviceName = "RTU_test1"
DeviceSecret = "KbucmMMgeNLP30zQL9sZHHjSCplm0G28"
 
# signmethod
signmethod = "hmacsha1"
# signmethod = "hmacmd5"
 
# 当前时间毫秒值
us = math.modf(time.time())[0]
ms = int(round(us * 1000))
timestamp = str(ms)
 
data = "".join(("clientId", ClientId, "deviceName", DeviceName,
                "productKey", ProductKey, "timestamp", timestamp
                ))
# print(round((time.time() * 1000)))
print("data:", data)
 
if "hmacsha1" == signmethod:
    ret = hmac.new(bytes(DeviceSecret, encoding="utf-8"),
                   bytes(data, encoding="utf-8"),
                   hashlib.sha1).hexdigest()
elif "hmacmd5" == signmethod:
    ret = hmac.new(bytes(DeviceSecret, encoding="utf-8"),
                   bytes(data, encoding="utf-8"),
                   hashlib.md5).hexdigest()
else:
    raise ValueError
 
sign = ret
print("sign:", sign)
 
# ======================================================
 
strBroker = ProductKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"
port = 1883
 
client_id = "".join((ClientId,
                     "|securemode=3",
                     ",signmethod=", signmethod,
                     ",timestamp=", timestamp,
                     "|"))
username = "".join((DeviceName, "&", ProductKey))
password = sign
 
print("="*30)
print("client_id:", client_id)
print("username:", username)
print("password:", password)
print("="*30)
 
def secret_test():
    DeviceSecret = "secret"
    data = "clientId12345deviceNamedeviceproductKeypktimestamp789"
    ret = hmac.new(bytes(DeviceSecret, encoding="utf-8"),
                   bytes(data, encoding="utf-8"),
                   hashlib.sha1).hexdigest()
    print("test:", ret)
 
 
# ======================================================
# MQTT Initialize.--------------------------------------
 
try:
    import paho.mqtt.client as mqtt
except ImportError:
    print("MQTT client not find. Please install as follow:")
    print("git clone https://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git")
    print("cd org.eclipse.paho.mqtt.python")
    print("sudo python setup.py install")
 
 
# ======================================================
def on_connect(mqttc, obj, flags, rc):
    print("OnConnetc, rc: " + str(rc))
 
    mqttc.subscribe("test", 0)
 
 
def on_publish(mqttc, obj, mid):
    print("OnPublish, mid: " + str(mid))
 
 
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
 
 
# =====================================================
if __name__ == '__main__':
    if TEST:
        secret_test()
        exit(0)
 
    mqttc = mqtt.Client(client_id)
    mqttc.username_pw_set(username, password)
    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe
    mqttc.on_log = on_log
 
    mqttc.connect(strBroker, port, 120)

    time.sleep(1)
    # mqttc.subscribe("xxxxx", qos=1)  # 换成自己的
    send_mseg = '{"pm_25": %s,"area":"%s","time":"%s"}'%(0,0,datetime.datetime.now())
    mqttc.publish("/a1nwrypxWbP/RTU_test1/data",payload=send_mseg, qos=1, retain=False)  # 换成自己的
    mqttc.loop_forever()