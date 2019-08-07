import paho.mqtt.client as mqtt

# Client(client_id="", clean_session=True, userdata=None, protocol=MQTTv311, transport="tcp")

# client =mqtt.Client(client_name)
# #connect(host, port=1883, keepalive=60, bind_address="")
# client.connect(host_name)

# publish(topic, payload=None, qos=0, retain=False)


import paho.mqtt.client as mqtt #import the client1
broker_address="127.0.0.1" 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("P1") #create new instance
print("connecting to broker")
client.connect(broker_address) #connect to broker
client.publish("house/main-light","OFF")#publish


print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("house/bulbs/bulb1")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("house/bulbs/bulb1","OFF")