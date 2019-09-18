import paho.mqtt.client as mqtt
import time

############


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
########################################


def on_log(client, userdata, level, buf):
    print("log: ", buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.connected_flag = True  # set flag
        print("connected OK")
    elif rc == 5:
        client.connected_flag = False
        print("Authentication Error")
    else:
        print("Bad connection Returned code=", rc)


mqtt.Client.connected_flag = False  # successfull connection
mqtt.Client.bad_connection_flag = False  # connection error indictor
mqtt.Client.connection_retry = 0  # retry count


broker_address = "127.0.0.1"
# broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("receiver-01")
client.on_message = on_message  # attach function to callback
client.on_connect = on_connect
client.on_log = on_log

client.loop_start()  # start the loop
print("connecting to broker...")
try:
    client.connect(broker_address)  # connect to broker
except Exception as e:
    print("connection failed:", e)
    exit(2)


while not client.connected_flag and not client.bad_connection_flag:  # wait in loop until connected
    # in worst case there is an exit after 10 try
    if client.connection_retry >= 10:
        print("connection issue")
        exit(1)
    print("In wait loop")
    time.sleep(1)
    client.connection_retry += 1

if client.bad_connection_flag:
    client.loop_stop()  # Stop loop
    sys.exit(2)

print("Subscribing to topic", "house/bulbs/+")
client.subscribe("house/bulbs/+")
client.subscribe("house/main-light")

# TODO: replace with console.read
time.sleep(3600)  # wait
client.loop_stop()  # stop the loop
client.disconnect()  # disconnect
