import json
from converters import float_to_uint8, int_to_uint8, char_to_uint8, string_to_uint8, default_encoding

class bytemessage:
  def __init__(self):
    self.message = bytearray()
  
  def int(self, value):
    self.message.extend(int_to_uint8(value))
    return self
  
  def float(self, value):
    self.message.extend(float_to_uint8(value))
    return self

  def char(self, value):
    self.message.extend(char_to_uint8(value))
    return self

  def string(self, value):
    self.message.extend(string_to_uint8(value))
    return self

  def json(self, data):
    payload = bytes(json.dumps(data), default_encoding)
    self.message.extend(payload)
    return self

  def bytes(self, bytes):
    self.message.extend(bytes)
    return self

  def get(self):
    return self.message