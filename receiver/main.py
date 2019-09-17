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



broker_address="127.0.0.1"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("receiver-01") 
client.on_message=on_message #attach function to callback
client.on_log=on_log

print("connecting to broker")
client.connect(broker_address) #connect to broker
client.loop_start() #start the loop
print("Subscribing to topic","house/bulbs/+")
client.subscribe("house/bulbs/+")
client.subscribe("house/main-light")

time.sleep(3600) # wait
client.loop_stop() #stop the loop