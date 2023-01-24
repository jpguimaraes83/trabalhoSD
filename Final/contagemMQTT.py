#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import time

#hostname
broker="localhost"
#port
port=1884

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("contagem")
    
def on_message(client, userdata, msg):
    state = msg.payload.decode()
    print(state)
    
    
client = mqtt.Client()
client.connect(broker,port)
client.on_connect = on_connect
client.on_message = on_message      
client.loop_forever()







