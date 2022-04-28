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
  with open('./packets/sample_data.log', 'r') as f:
    messages = f.readlines()
  return messages

def send_string(data):
  result = bytemessage()
  result = result.string(data).get()
  send_bytes('localhost', 9000, result)

def send_motion(roomName):
  data = r'''{"topic":"rooms/''' + roomName + r'''/motion/d1f61303-e2b2-40c2-a203-b752926b93fc","data":{"payload":{"type":"motionSensor","roomName":"haskell","roomId":"04fba3a7-a0c4-4058-8b76-282c2d9f2da3","timestamp":1650969558487},"signatures":[{"protected":{"timestamp":1650969558487,"messageid":"mQPLV7D4XfAr","alg":"ES512","kid":"2rCGPtxCjl3uTns6U6mMtjwAD3vjVlL1OcfgXP_Llk8"},"signature":"APmFqjpdBLUPv4H4Oq_RvmSZX4oM320kgeqCTEL3q_g9mp2GoGLlDvpDvfw28RslNIjN8szb7cEERbkbg_Z89ZfIAeTxn2x68EWb_JcxmTXLvkXumdWCDwj1MeOTVK5yhtGgzeRaqpz6X3kjJOweqGKcMR0c2DoOtrvFnbAS-fcWnERe"}]}}'''
  send_string(data)

def send_reservation(roomName, reserved = True):
  reservation = "VARATTU" if reserved else "VAPAA"
  data = r'''{"topic":"rooms/''' + roomName + r'''/reservation/d1f61303-e2b2-40c2-a203-b752926b93fc","data":{"payload":{"currentEndTime":1645704000000,"currentStartTime":1645696800000,"currentId":"495-1645696800000","currentTopic":"''' + reservation + r'''\\u2022RESERVERAT\\u2022RESERVED"},"signatures":[{"protected":{"timestamp":1650969558487,"messageid":"mQPLV7D4XfAr","alg":"ES512","kid":"2rCGPtxCjl3uTns6U6mMtjwAD3vjVlL1OcfgXP_Llk8"},"signature":"APmFqjpdBLUPv4H4Oq_RvmSZX4oM320kgeqCTEL3q_g9mp2GoGLlDvpDvfw28RslNIjN8szb7cEERbkbg_Z89ZfIAeTxn2x68EWb_JcxmTXLvkXumdWCDwj1MeOTVK5yhtGgzeRaqpz6X3kjJOweqGKcMR0c2DoOtrvFnbAS-fcWnERe"}]}}'''
  send_string(data)

#send_motion('java')
send_reservation('java')
#messages = get_stock_messages()
#send_string(messages[0])

exit()

while True:
  #catalog_message = build_catalog_message([random_room_status()])
  #send_bytes('localhost', 9000, catalog_message)
  time.sleep(1)