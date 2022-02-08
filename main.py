import socket
import json
import time

transform_data = {
  "id":"player id_here",
  "data": {
    "pos": (1.23456, 1.23456, 1.23456),
    "rot": (1.23456, 1.23456, 1.23456)
  }
}

sensor_data_1 = {
  "id":"octave",
  "data": {
    "type":"temp",
    "value":23
  }
}

sensor_data_2 = {
  "id":"octave",
  "data": {
    "type":"motion",
    "value":1
  }
}

def send_data(uri : str, port : int, data : dict):
  payload = {
    'id': data['id'],
    'data': json.dumps(data['data'])
  }
  payload = bytes(json.dumps(payload), 'utf-8')
  connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  connection.sendto(payload, (uri, port))

def send_all(uri : str, port : int):
  packets = [transform_data, sensor_data_1, sensor_data_2]

  for packet in packets:
    send_data(uri, port, packet)

def move_player(uri : str, port : int):
  x = 0
  y = 0
  z = 0
  while True:
    data = transform_data
    data['data']['pos'] = {'x':x, 'y':y, 'z':z}
    data['data']['rot'] = {'x':0, 'y':0, 'z':0}
    print(data)
    send_data(uri, port, data)

    x += 0.1
    z += 0.1

    time.sleep(1)

#send_all("localhost", 9000)
move_player("localhost", 9000)