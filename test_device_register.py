from aliyunsdkcore import client
from aliyunsdkiot.request.v20170420 import RegistDeviceRequest
from aliyunsdkiot.request.v20170420 import PubRequest
from aliyunsdkiot.request.v20180120 import QueryProductListRequest

Endpoint = 'iot.cn-shanghai.aliyuncs.com'

accessKeyId = 'LTAIAquKjgwHPNsX'
accessKeySecret = '7Of0XiOIITOw2rmYUt4nUTSQOEKyK2'

clt = client.AcsClient(accessKeyId, accessKeySecret, 'cn-shanghai')

# request = QueryProductListRequest.QueryProductListRequest()
# request.set_PageSize('10')  
# request.set_CurrentPage('1')

request = RegistDeviceRequest.RegistDeviceRequest()
request.set_ProductKey('a14MQd3lS1y')
request.set_DeviceName('yj_recoder_test2')


result = clt.do_action_with_exception(request)
print(result)
# print('result : ' + result)


