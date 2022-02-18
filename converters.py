import struct

default_encoding = 'ascii'

def float_to_uint8(value):
  return bytes.fromhex(hex(struct.unpack('<I', struct.pack('<f', value))[0])[2:])

def int_to_uint8(value):
  return int.to_bytes(value, 1, 'little')

def char_to_uint8(value):
  return bytes(value, 'ascii')

def string_to_uint8(value):
  return bytes(value, default_encoding)