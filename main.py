import time
import socket
from array import array
from multiprocessing import connection
from bytemessage import bytemessage

def send_bytes(uri : str, port : int, bytes : bytearray):
  connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  connection.sendto(bytes, (uri, port))

def build_room_message(targetName : str, data : array = []):
  result = bytemessage()

  result.string(targetName)
  result.char('\n')

  for entry in data:
    result.json(entry)
    result.char('\n')

  result.char('\n')
  return result.get()


def build_catalog_message(rooms : array):
  result = bytemessage()
  result.int(1)

  for room in rooms:
    segment = build_room_message(room[0], room[1])
    result.bytes(segment)

  return result.get()

octave_sensors = [{'type':'motionSensor', 'value':1}, {'type':'temperature', 'value':39}]
lisp_sensors = [{'type':'humidity', 'value':85}]

example_catalog = [('octave', octave_sensors), ('lisp', lisp_sensors)]

message = build_catalog_message(example_catalog)

while True:
  send_bytes('localhost', 9000, message)
  time.sleep(1)