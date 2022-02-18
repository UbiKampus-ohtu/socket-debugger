import json
from converters import float_to_uint8, int_to_uint8, char_to_uint8, string_to_uint8, default_encoding

class bytemessage:
  def __init__(self):
    self.message = bytearray()
  
  def int(self, value):
    self.message.extend(int_to_uint8(value))
  
  def char(self, value):
    self.message.extend(char_to_uint8(value))

  def string(self, value):
    self.message.extend(string_to_uint8(value))

  def json(self, data):
    payload = bytes(json.dumps(data), default_encoding)
    self.message.extend(payload)

  def bytes(self, bytes):
    self.message.extend(bytes)

  def get(self):
    return self.message