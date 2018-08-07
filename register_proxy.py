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

from aliyunsdkcore import client
from aliyunsdkiot.request.v20170420 import RegistDeviceRequest
from aliyunsdkiot.request.v20180120 import QueryDeviceDetailRequest

Endpoint = 'iot.cn-shanghai.aliyuncs.com'

accessKeyId = 'LTAIAquKjgwHPNsX'
accessKeySecret = '7Of0XiOIITOw2rmYUt4nUTSQOEKyK2'

ProductKey = 'a1nwrypxWbP'
client_id = 'register_proxy_' + ProductKey
username = 'iiot'
password = 'smartlinkcloud'
strBroker = '101.200.158.2'
port = 1883

# 成功连接后的操作
def on_connect(client, userdata, flags, rc):
    print("OnConnetc, rc: " + str(rc))

    client.subscribe("a1nwrypxWbP.register", qos=1)
 
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
    on_exec(msg.payload)


    # 计算密码（签名值）
def calculation_sign(signmethod, ClientId, DeviceName, ProductKey, timestamp, DeviceSecret):
    data = "".join(("clientId", ClientId, "deviceName", DeviceName,
                    "productKey", ProductKey, "timestamp", timestamp))
    if "hmacsha1" == signmethod:
        ret = hmac.new(bytes(DeviceSecret),
                   bytes(data),hashlib.sha1).hexdigest()
    elif "hmacmd5" == signmethod:
        ret = hmac.new(bytes(DeviceSecret, encoding="utf-8"),
                       bytes(data, encoding="utf-8"),hashlib.md5).hexdigest()
    else:
        raise ValueError
    return ret

 
def on_exec(strcmd):
    print("------Exec:---------")
    try:
        json_dict = json.loads(strcmd)
        deviceName_stm32_sim = json_dict['device_name']
        deviceName = deviceName_stm32_sim.split('_')[0]

        print('-----deviceName------')
        print(deviceName)

        # Register on the ALIIOT and get the result
        clt = client.AcsClient(accessKeyId, accessKeySecret, 'cn-shanghai')

        request = RegistDeviceRequest.RegistDeviceRequest()
        request.set_ProductKey(ProductKey)
        request.set_DeviceName(deviceName)

        result = clt.do_action_with_exception(request)

        print('-------register-result------')
        print(result)

        result_dict = json.loads(result)

        isSuccess = result_dict['Success']
        print('-----register isSuccess------')
        print(isSuccess)

        strBroker = ProductKey + ".iot-as-mqtt.cn-shanghai.aliyuncs.com"
        port = '1883'

        if isSuccess:

            # 设置连接信息
            ClientId = result_dict['DeviceName'] # DeviceId
            DeviceName = result_dict['DeviceName']  # DeviceName
            DeviceSecret = result_dict['DeviceSecret'] # DeviceSecret
             
            # 获取时间戳（当前时间毫秒值）
            us = math.modf(time.time())[0]
            ms = int(round(us * 1000))
            timestamp = str(ms)

            client_id = "".join((ClientId,
                                 "|securemode=3",
                                 ",signmethod=", "hmacsha1",
                                 ",timestamp=", timestamp,
                                 "|"))
            username = "".join((DeviceName, "&", ProductKey))
            password = calculation_sign("hmacsha1", ClientId, DeviceName, ProductKey, timestamp, DeviceSecret)

            return_dcit = {'Success': True, 'strBroker': strBroker, 'port':port, 'client_id':client_id, 'username':username, 'password':password}
            return_json = json.dumps(return_dcit)
            print(return_json)

        else:
            if result_dict['Code'] == 'iot.device.AlreadyExistedDeviceName':
                request = QueryDeviceDetailRequest.QueryDeviceDetailRequest()
                request.set_ProductKey(ProductKey)
                request.set_DeviceName(deviceName)

                result = clt.do_action_with_exception(request)

                print('-------device-detail-result------')
                print(result)

                result_dict = json.loads(result)

                isSuccess = result_dict['Success']
                print('-----device-detail-isSuccess------')
                print(isSuccess)

                if isSuccess:
                    print('query device detail successed!')
                    ClientId = result_dict['Data']['DeviceName'] # DeviceId
                    DeviceName = result_dict['Data']['DeviceName']  # DeviceName
                    DeviceSecret = result_dict['Data']['DeviceSecret'] # DeviceSecret
                     
                    # 获取时间戳（当前时间毫秒值）
                    us = math.modf(time.time())[0]
                    ms = int(round(us * 1000))
                    timestamp = str(ms)

                    client_id = "".join((ClientId,
                                         "|securemode=3",
                                         ",signmethod=", "hmacsha1",
                                         ",timestamp=", timestamp,
                                         "|"))
                    username = "".join((DeviceName, "&", ProductKey))
                    password = calculation_sign("hmacsha1", ClientId, DeviceName, ProductKey, timestamp, DeviceSecret)
                    return_dcit = {'Success': True, 'strBroker': strBroker, 'port':port, 'client_id':client_id, 'username':username, 'password':password}
                    return_json = json.dumps(return_dcit)
                    print(return_json)
                else:
                    return_json = result
                    print(return_json)

            else:
                return_json = result
                print(return_json)
         
        # use mqtt publish return to device the result
        strMqttBroker = "101.200.158.2"
        # Be care of deviceName_stm32_sim
        # strMqttChannel = "a1nwrypxWbP.register." + deviceName_stm32_sim
        strMqttChannel = "a1nwrypxWbP.register." + deviceName_stm32_sim
        print('----------------strMqttChannel-----------')
        print(strMqttChannel)
        publish.single(strMqttChannel, return_json, hostname=strMqttBroker, auth={'username': 'iiot', 'password': 'smartlinkcloud'})

    except:
        print('devicename error!')

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
    
    # mqttc.subscribe("a1nwrypxWbP.register", qos=1)

    mqttc.loop_forever()

