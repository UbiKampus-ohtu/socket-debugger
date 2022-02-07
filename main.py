import socket
import json

def send_data(uri : str, port : int, data : dict):
  data['data'] = json.dumps(data['data'])
  payload = bytes(json.dumps(data), 'utf-8')
  connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  connection.sendto(payload, (uri, port))

transform_data = {
  "id":"player id_here",
  "data": {
    "pos": (1.23456, 1.23456, 1.23456),
    "dir": (1.23456, 1.23456, 1.23456)
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

packets = [transform_data, sensor_data_1, sensor_data_2]

for packet in packets:
  send_data("localhost", 8000, packet)