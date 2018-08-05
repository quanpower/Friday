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
request.set_ProductKey('a1nwrypxWbP')
request.set_DeviceName('RTU_test2')


result = clt.do_action_with_exception(request)
print(result)
# print('result : ' + result)


# {"DeviceId":"Pxm7GkyB41qUhv8huJGo","DeviceName":"RTU_test1","RequestId":"BD3F80FF-FC0E-462E-A67D-6E65F04CDA33","DeviceSecret":"uRBgiGO8HJZMjvQHOI85tI0skvl52Yeb","Success":true}