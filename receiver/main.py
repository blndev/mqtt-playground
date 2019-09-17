import paho.mqtt.client as mqtt
import time

############
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################

def on_log(client, userdata, level, buf):
    print("log: ",buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

mqtt.Client.connected_flag=False#create flag in class
mqtt.Client.connection_wait=0#create flag in class


broker_address="127.0.0.1"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("receiver-01") 
client.on_message=on_message #attach function to callback
client.on_connect=on_connect
client.on_log=on_log

client.loop_start() #start the loop
print("connecting to broker")
try:
    client.connect(broker_address) #connect to broker
except:
    print ("connection failed")
    exit(2)
    
while not client.connected_flag: #wait in loop until conected
    # in worst case there is an exit after 5 try
    if client.connection_wait>=10: 
        print("connection issue")
        exit(1)
    print("In wait loop")
    time.sleep(1)
    client.connection_wait+=1

print("Subscribing to topic","house/bulbs/+")
client.subscribe("house/bulbs/+")
client.subscribe("house/main-light")

# TODO: replace with console.read
time.sleep(3600) # wait
client.loop_stop() #stop the loop
client.disconnect() # disconnect
