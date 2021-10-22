import sys
import time
import ttn
import datetime as dt

from influxdb import InfluxDBClient

app_id = "maker-session"
access_key = "ttn-account-v2.ymC4-oojWZMYdAKJfmjTk-SL8OdZuvenjgpaJvP5yFo"

GTW_ID = 'iot-mashinani' # gateway of interest

db_client = InfluxDBClient(host='localhost', port=8086)
db_client.create_database('indaba_session')
db_client.switch_database('indaba_session')

def uplink_callback(msg, client):

  print("Received uplink from ", msg.dev_id)

  influxdb_entry = {}

  influxdb_entry['time'] = msg.metadata.time
  fields = {}

  fields['data_rate'] = msg.metadata.data_rate


  for gtw in msg.metadata.gateways:
    if gtw.gtw_id == GTW_ID:
      fields['rssi'] = float(gtw.rssi)
      fields['snr'] = float(gtw.snr)

  try:
    fields['Temperature'] = float(msg.payload_fields.temperature_2)
    fields['Relative Humidity'] = float(msg.payload_fields.relative_humidity_3)
  except:
    pass

  try:
    fields['Soil Moisture'] = float(msg.payload_fields.analog_in_4)
  except:
    pass

  influxdb_entry['fields'] = fields
  influxdb_entry['measurement'] = 'Indaba Session'
  influxdb_entry['tags'] = {'sensor': msg.dev_id}

  print(influxdb_entry)


  db_client.write_points([influxdb_entry])

handler = ttn.HandlerClient(app_id, access_key)

# using mqtt client
mqtt_client = handler.data()
mqtt_client.set_uplink_callback(uplink_callback)
mqtt_client.connect()

while True:
  try:
    time.sleep(60)
  except KeyboardInterrupt:
    print('Closing ...')
    mqtt_client.close()
    sys.exit(0)
