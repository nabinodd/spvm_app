from database_handler import *
import paho.mqtt.client as mqtt
import threading

broker='npi.local'
client=mqtt.Client('spvm_processor')

policy_limit=int(getPdataVal(1)) #From database	[1]	[ploicy_val]

def checkDB(rfid):

	result=getCurrentCountOfRfid(rfid)	

	if result.count() == 1:
		current_count = result.first().curr_count
		individual_remaining = policy_limit - current_count

		print('[INF] Count of ',result.first().name,' is : ',current_count)

		if individual_remaining >= 0:
			print('[INF] ',result.first().name, 
			' have ',individual_remaining,
			' remaining now in this month. Please collect your pad')
			
			client.publish('spvm/vending_cmd',str(rfid))
		
		elif individual_remaining < 0:
			print('[INF] ',result.first().name,'have reached limit, contact administration') 


	else:
		print('[ERR] No record found with RFID : ',rfid)

def on_connect(client,userdata,flags,rc):
	if rc==0:
		print('Connected OK')
		client.subscribe('spvm/rfid')
		client.subscribe('spvm/vending_response')
	else:
		print('[ERR] Not connected : ',rc)

def on_message(client, userdata, msg):
	if msg.topic == 'spvm/rfid':
		rfid=msg.payload.decode()
		threading.Thread(target=checkDB(rfid),daemon=True).start()
	
	if msg.topic == 'spvm/vending_response':
		resp=msg.payload.decode()
		logVending(resp)
		# print('[INF] Response from vending : ',resp,'\n')

client.on_connect=on_connect
client.on_message=on_message
# client.on_log=on_log

print('[INF] Connecting to broker : ',broker)
client.connect(broker)
# client.loop_start()


client.loop_forever()

# import pdb; pdb.set_trace()
# result = session.query(User).order_by(User.id)

# for row in result:
# 	print('ID : ',row.id, 'name : ',row.name,'Serial num : ',row.serial_num)

# now=datetime.now()
# timestamp=int(datetime.timestamp(now))
# print('Timestamp : ',timestamp)

# try:
# 	stu1= Entries(str(timestamp+300000000),timestamp)
# 	session.add(stu1)
# 	session.commit()
# 	print('[OK] Commited')
# except:
# 	print('Cannot insert')