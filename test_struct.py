import struct
import binascii

packed_data = struct.pack('<2f', 20.1, 15.6)
unpacked_data = struct.unpack('<2f', packed_data)

print(packed_data)
print(str(packed_data))
print(len(packed_data))
print(unpacked_data)

packed_data1 = struct.pack('>f', 37.0)

print(binascii.hexlify(packed_data1))

