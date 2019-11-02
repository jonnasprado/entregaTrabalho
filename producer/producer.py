import random
import time
import paho.mqtt.client as mqtt
import json

# conectar ao broker

print('Conectando ao mqtt broker...')
mqtt_client = mqtt.Client()
mqtt_client.connect('18.228.116.164', 1883, 60)

while True:
    temperatura = random.uniform(17,30)
    print(temperatura)
    msg = {
        'temperatura': temperatura
    }
    mqtt_client.publish('in242', json.dumps(msg), qos=0)
    time.sleep(1)
