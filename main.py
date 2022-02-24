import time
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

def build_player_message(id : int, transform : array):
  result = bytemessage()
  result.int(id)
  
  for fragment in transform:
    result.float(fragment)

  return result.get()

def build_players_message(players : array):
  result = bytemessage()
  result.int(2)

  for player in players:
    segment = build_player_message(player['id'], player['transform'])
    result.bytes(segment)

  return result.get()

octave_sensors = [{'type':'motionSensor', 'value':1}, {'type':'temperature', 'value':39}]
lisp_sensors = [{'type':'humidity', 'value':85}]

example_catalog = [('octave', octave_sensors), ('lisp', lisp_sensors)]

catalog_message = build_catalog_message(example_catalog)

player1 = {'id':12, 'transform': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]}
player2 = {'id':23, 'transform': [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]}

players_message = build_players_message([player1])

while True:
  send_bytes('localhost', 9000, catalog_message)
  time.sleep(1)
  send_bytes('localhost', 9000, players_message)
  time.sleep(1)