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

broker='localhost'
client=mqtt.Client('spvm_gui')

# def on_log(client,userdata,level,buf):
#     print('log: '+buf)

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print('Connected OK')
        client.subscribe('gui_msg')
    else:
        print('Not connected : ',rc)

def on_message(client, userdata, msg):
    print('Got message')

client.on_connect=on_connect
client.on_message=on_message
# client.on_log=on_log

print('Connecting to broker : ',broker)
client.connect(broker)
client.loop_start()

def getInput():
    while True:
        recorded = keyboard.record(until='enter')
        time.sleep(1)
        string=keyboard.get_typed_strings(recorded)
        rf_id=next(string)
        client.publish('spvm/rfid',str(rf_id))
        # print('Tag ID is : ',rf_id)
        ui.lbl_sts.setText('Updating...')
        time.sleep(0.5)
        ui.lbl_sts.setText(rf_id)

def updateDateTime():
    today=qtc.QDate.currentDate().toString(qtc.Qt.ISODate)
    now=qtc.QTime.currentTime().toString()

    # print(today.toString(qtc.Qt.ISODate))
    # print(now.toString())

    ui.lbl_time.setText(now)
    ui.lbl_date.setText(today)

rfid_thr = threading.Thread(target=getInput,daemon=True)
rfid_thr.start()

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

    Form.showFullScreen()
    # Form.show()
    sys.exit(app.exec_())