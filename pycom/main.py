import pycom
import time
from SI7006A20 import SI7006A20
from pysense import Pysense
from network import WLAN
import machine
from mqtt import MQTTClient
import json

pycom.heartbeat(False)

pycom.rgbled(0x0000f0)
time.sleep(4)
pycom.rgbled(0x000000)

py = Pysense()
st = SI7006A20(py)


# Conectar no WIFI
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == 'lucheol':
        print('Network found!')
        wlan.connect(net.ssid, auth=(net.sec, 'valentina'), timeout=5000)
        while not wlan.isconnected():
            wifi_conected = True
            machine.idle()  # save power while waiting
        print('WLAN connection succeeded!')
        # pycom.rgbled(0x00ff00)
        break


def mqtt_command(topic, msg):
    print('recebi a mensagem', msg)

    if int(msg) == 1:
        pycom.rgbled(0xff0000)
    else:
        pycom.rgbled(0x000000)


client = MQTTClient("in242-teste", "192.168.43.105", port=1883)
client.set_callback(mqtt_command)
client.connect()
client.subscribe(topic="in242/luz/#")

while True:
    # pycom.rgbled(0x00000f)
    # time.sleep(1)
    # pycom.rgbled(0x000000)
    temp = st.temperature()
    humidade = st.humidity()
    print(temp, humidade)
    dados = {
        'temperatura': temp,
        'humidade': humidade
    }
    client.publish(topic="in242", msg=json.dumps(dados))
    client.check_msg()
    time.sleep(5)
