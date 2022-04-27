import time
import random
import socket
from array import array
from multiprocessing import connection
from bytemessage import bytemessage

def send_bytes(uri : str, port : int, bytes : bytearray):
  print(bytes)
  connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  connection.sendto(bytes, (uri, port))

def build_room_message(targetName : str, data : array = []):
  result = bytemessage()

  result.string(targetName).char('\n')

  for entry in data:
    result.json(entry).char('\n')

  return result.char('\n').get()


def build_catalog_message(rooms : array):
  result = bytemessage()
  result.int(1)

  for room in rooms:
    segment = build_room_message(room[0], room[1])
    result.bytes(segment)

  return result.get()

octave_sensors = [{'type':'motionSensor', 'value':1}, {'type':'temperature', 'value':39}]
lisp_sensors = [{'type':'humidity', 'value':85}]

example_catalog = [('Kotlin', octave_sensors), ('lisp', lisp_sensors)]

def random_sensor():
  sensor_types = [('motionSensor', 1), ('reserved', random.randrange(0, 2))]
  #sensor_types = [('reserved', random.randrange(0, 2))]
  #sensor_types = [('motionSensor', 1), ('temperature', random.randrange(10, 32)), ('reserved', random.randrange(0, 2))]
  index = random.randrange(0, len(sensor_types))
  sensor = sensor_types[index]
  return {'type':sensor[0], 'value':sensor[1]}

def random_room_status():
  rooms = ['Kotlin', 'Lisp', 'Modula', 'Neko', 'Octave', 'Python', 'Q', 'Java', 'Ada', 'Basic', 'Cobol', 'Dart', 'Erlang', 'Fortran', 'Go', 'Haskell', 'Idris']
  #rooms = ['Java', 'Ada', 'Basic', 'Cobol', 'Dart', 'Erlang', 'Fortran']
  index = random.randrange(0, len(rooms))
  return (rooms[index], [random_sensor()])

def get_stock_messages():
  messages = []
  with open('./sample_data.log', 'r') as f:
    messages = f.readlines()
  return messages

def send_string(data):
  result = bytemessage()
  result = result.string(data).get()
  send_bytes('localhost', 9000, result)

messages = get_stock_messages()
send_string(messages[1])

exit()

while True:
  #catalog_message = build_catalog_message([random_room_status()])
  #send_bytes('localhost', 9000, catalog_message)
  time.sleep(1)