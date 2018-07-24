import struct
import binascii
import json

packed_data = struct.pack('<2f', 20.1, 15.6)
unpacked_data = struct.unpack('<2f', packed_data)

print(packed_data)
print(str(packed_data))
print(len(packed_data))
print(unpacked_data)

packed_data1 = struct.pack('>f', 37.0)

print(binascii.hexlify(packed_data1))


fake_str = '01034042140000425D33334291CCCD42AECCCD42C1999A42C7CCCD42C0999A42ACCCCD428F000042573333420E00004199999A40E000003F3333333F80000040FCCCCD0E88'
fake_a2b_hex = binascii.a2b_hex(fake_str)
print(fake_a2b_hex)
print(len(fake_a2b_hex))

daq_data_length = struct.unpack('B', fake_a2b_hex[2:3])
print(daq_data_length)
daq_data = fake_a2b_hex[3:3 + daq_data_length[0]]

device_daqs = []
for i in range(int(daq_data_length[0]/4)):
    packed_data = daq_data[4*i:4*i + 4]
    print('-----packed_data-----'* 3)

    print(binascii.hexlify(packed_data))

    unpacked_data = struct.unpack('>f', packed_data)
    device_daqs.append([str(i), unpacked_data[0]])

    print(packed_data)
    print(unpacked_data)

device_daqs_json = json.dumps(device_daqs)
print(device_daqs_json)

