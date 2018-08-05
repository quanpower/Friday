import requests
from hashlib import sha1
import hmac

url = 'https://iot-auth.cn-shanghai.aliyuncs.com/auth/register/device'

productKey='a1nwrypxWbP'
productSecret='TxV8mZGsZw4Dnd1f'
deviceName='RTU_test3'
randomStr='smartlinkcloud'

paramatersDict = {'productKey': productKey, 'deviceName': deviceName, 'random': randomStr }
# items = paramatersDict.items() 
# sortedParamatersDict=items.sort()
# print(sortedParamatersDict)

keys = paramatersDict.keys() 
keys.sort() 

print(keys)

sortedStr = ''
for key in keys:
	sortedStr += key + paramatersDict[key]

print('-----sortedStr-----')
print(sortedStr)

sign= hmac.new(productSecret, sortedStr, sha1).hexdigest()
print('----sign----')
print(sign)

signMethod='hmacsha1'

# headers = {'Content-Type': 'application/x-www-form-urlencoded'}

# r = requests.post(url, headers=headers, data = {'productKey':productKey, 'deviceName':deviceName, 'random':randomStr, 'sign':sign, 'signMethod':signMethod })
r = requests.post(url, data = {'productKey':productKey, 'deviceName':deviceName, 'random':randomStr, 'sign':sign, 'signMethod':signMethod })
print(r.headers)
print(r.text)
