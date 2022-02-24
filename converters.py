import struct

default_encoding = 'ascii'
is_little_endian = True

def float_to_uint8(value):
  hex_string = '00000000'
  if (value > 0):
    hex_string = hex(struct.unpack('<I', struct.pack('<f', value))[0])[2:]
  
  if is_little_endian:
    bubblegum_reverse = str(hex_string[6:8]) + str(hex_string[4:6]) + str(hex_string[2:4]) + str(hex_string[0:2])
    return bytes.fromhex(bubblegum_reverse)
  return bytes.fromhex(hex_string)

def int_to_uint8(value):
  return int.to_bytes(value, 1, 'little')

def char_to_uint8(value):
  return bytes(value, 'ascii')

def string_to_uint8(value):
  return bytes(value, default_encoding)