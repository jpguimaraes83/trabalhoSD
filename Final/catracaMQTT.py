import paho.mqtt.client as mqtt
import time

#hostname
broker="localhost"
#port
port=1884

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("msgcatraca")
    
def on_message(client, userdata, msg):
    state = msg.payload.decode()
    print(state)
    
    
client = mqtt.Client()
client.connect(broker,port)
client.on_connect = on_connect
client.on_message = on_message      
client.loop_start()

time.sleep(2)

op = input('Digite seu código de acesso: \n')
while(op!= '1983'):
    client.publish("pubcatraca",op)
    time.sleep(1)
    op = input('Digite seu código de acesso: \n')





