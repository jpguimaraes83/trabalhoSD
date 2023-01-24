import rpyc
import random
import paho.mqtt.client as mqtt
import time

#hostname
broker="localhost"
#port
port=1884


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("pubcatraca")
    
    
list_usuario = ['0','1','2','3','4','5']  
list_quantidade = []


def on_message(client, userdata, msg):
        state = msg.payload.decode()
        if str(state) in list_usuario and str(state) in list_quantidade: 
            mess = "Saída Liberada"
            client.publish("msgcatraca",mess)
            list_quantidade.remove(state)
            mens = "Exitem " + str(len(list_quantidade)) + " usuários na sala" 
            client.publish("contagem",mens)
        elif str(state) in list_usuario: 
            mess = "Acesso Liberado"
            client.publish("msgcatraca",mess)
            list_quantidade.append(state)
            mens = "Exitem " + str(len(list_quantidade)) + " usuários na sala" 
            client.publish("contagem",mens)
        else:
            mess = "Acesso Negado - Código não cadastrado"
            client.publish("msgcatraca",mess)
   
client = mqtt.Client()
client.connect(broker,port)
client.on_connect = on_connect
client.on_message = on_message
client.loop_start()

time.sleep(2)

class MeuServico(rpyc.Service):
      
    mensagem = []
    
    def exposed_listar_quantidade(self):
        return ("Exitem " + str(len(list_quantidade)) + " usuários na sala\n")
        
    def exposed_cadastrar_cod(self,teste): 
        list_usuario.append(teste)
            
    def exposed_listar_cod_sala(self):
        return (str(list_quantidade) + "\n")
        
       
    def exposed_listar_usuarios(self):
        return(str(list_usuario) + "\n")
       

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MeuServico, port=18861)
t.start()