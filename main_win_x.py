import sys
import threading
import keyboard
import time
import PyQt5.QtCore as qtc
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

from PyQt5 import QtGui, QtWidgets
from layout.main_win_layout import Ui_Form

import paho.mqtt.client as mqtt

from database_handler import queryByRfid,getPdataVal


block_input=False

def updateStatusLabel(idsts):
    global block_input
    block_input=True
    policy_limit=int(getPdataVal(1))  #From database	[1]	[ploicy_val]
    rfid,sts=idsts
    qry = queryByRfid(rfid)
    nam = qry.name
    cu_count = int(qry.curr_count)
    remaining = (policy_limit - cu_count)
    print('Remaininjg = ',remaining)
    if sts:
        ui.lbl_sts.setText('Vending for '+nam+', '+str(remaining)+' remaining')
        time.sleep(3)
        ui.lbl_sts.setText('Ready for vending')

    if not sts:
        ui.lbl_sts.setText('Cannot vend for '+nam+', '+str(remaining)+' remaining')
        time.sleep(3)
        ui.lbl_sts.setText('Ready for vending')
    block_input=False
################################### MQTT ###################################

broker='localhost'
client=mqtt.Client('spvm_gui')

# def on_log(client,userdata,level,buf):
#     print('log: '+buf)
def on_connect(client,userdata,flags,rc):
    if rc==0:
        print('Connected OK')
        client.subscribe('spvm/vending_false')
        client.subscribe('spvm/vending_true')
    else:
        print('Not connected : ',rc)

def on_message(client, userdata, msg):

    if msg.topic=='spvm/vending_true':
        rfid=msg.payload.decode()
        updateStatusLabel((rfid,True))
        # threading.Thread(target=updateStatusLabel((rfid,True)),daemon=True).start()
    
    elif msg.topic=='spvm/vending_false':
        rfid=msg.payload.decode()
        updateStatusLabel((rfid,False))
        # threading.Thread(target=updateStatusLabel((rfid,False)),daemon=True).start()

client.on_connect=on_connect
client.on_message=on_message
# client.on_log=on_log

print('Connecting to broker : ',broker)
client.connect(broker)
client.loop_start()

################################### MQTT ###################################

def getInput():
    while True:
        if not block_input:
            recorded = keyboard.record(until='enter')
            string=keyboard.get_typed_strings(recorded)
            rf_id=next(string)
            client.publish('spvm/rfid',str(rf_id))
            # print('Tag ID is : ',rf_id)
            # ui.lbl_sts.setText('Updating...')
            # time.sleep(0.5)
            # ui.lbl_sts.setText(rf_id)
        time.sleep(0.5)

def updateDateTime():
    today=qtc.QDate.currentDate().toString(qtc.Qt.ISODate)
    now=qtc.QTime.currentTime().toString()

    # print(today.toString(qtc.Qt.ISODate))
    # print(now.toString())

    ui.lbl_time.setText(now)
    ui.lbl_date.setText(today)

################################### Threads ###################################
rfid_thr = threading.Thread(target=getInput,daemon=True)
rfid_thr.start()
################################### Threads ###################################

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    ui.lbl_logo.setPixmap(QtGui.QPixmap('logo.png'))

    font=qtg.QFont()
    font.setPointSize(20)
    font.setBold(True)
    
    ui.lbl_date.setFont(font)
    ui.lbl_time.setFont(font)

    date_time_timer=qtc.QTimer()
    date_time_timer.timeout.connect(updateDateTime)
    date_time_timer.start(999)

    # Form.showFullScreen()
    Form.show()
    sys.exit(app.exec_())