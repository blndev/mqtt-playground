import paho.mqtt.client as mqtt
import time

# clientMOQ(clientMOQ_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")

# clientMOQ =mqtt.clientMOQ(clientMOQ_name)
# #connect(host, port=1883, keepalive=60, bind_address="")
# clientMOQ.connect(host_name)

# publish(topic, payload=None, qos=0, retain=False)


import paho.mqtt.client as mqtt #import the clientMOQ1
broker_address="127.0.0.1" 
#broker_address="iot.eclipse.org" #use external broker
clientMOQ = mqtt.Client("iot-1-c1") #create new instance
clientHMQ = mqtt.Client("iot-1-c2") #create new instance

print("connecting to broker")
clientMOQ.connect(broker_address) #connect to broker
clientHMQ.connect(broker_address, 1884) #connect to broker
time.sleep(10) # we should have a proper connection validation instead of waiting
# see http://www.steves-internet-guide.com/client-connections-python-mqtt/
clientMOQ.publish("house/main-light","OFF")#publish


#no need to subscribe when you just want to send messages
#print("Subscribing to topic","house/bulbs/bulb1")
#clientMOQ.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
clientMOQ.publish("house/bulbs/bulb1","OFF")
print("Publishing message to topic","house/bulbs/bulb2")
clientMOQ.publish("house/bulbs/bulb2","ON")
print("Publishing message to topic","house/bulbs/bulb3")
clientHMQ.publish("house/bulbs/bulb3","ON")

time.sleep(60) # wait
