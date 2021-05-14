import time
import threading
import paho.mqtt.client as mqtt
from gpiozero import Motor

mot_u_a_pin = 1
mot_u_b_pin = 2
mot_d_a_pin = 3
mot_d_b_pin = 4

# mot_u= Motor(mot_u_a_pin,mot_u_b_pin)
# mot_d = Motor(mot_d_a_pin, mot_d_b_pin)

broker='npi.local'
client=mqtt.Client('spvm_actuactors')

def on_connect(client,userdata,flags,rc):
	if rc==0:
		print('Connected OK')
		client.subscribe('spvm/vending_cmd')
	else:
		print('[ERROR] Not connected : ',rc)

def on_message(client, userdata, msg):
	if msg.topic=='spvm/vending_cmd':
		rfid=msg.payload.decode()
		threading.Thread(target=runMotor(rfid),daemon=True).start()

def runMotor(rfid):
	print('[INF] Vending from the machine')
	time.sleep(2)
	client.publish('spvm/vending_response',rfid)
	print('[OK] Vending complete\n')

client.on_connect=on_connect
client.on_message=on_message
# client.on_log=on_log

print('[INF] Connecting to broker : ',broker)
client.connect(broker)
# client.loop_start()
client.loop_forever()
