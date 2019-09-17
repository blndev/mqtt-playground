docker run -d \
    -p 1883:1883 \
    -p 9001:9001 \
    -v mosquitto.conf:/mosquitto/mosquitto.conf \
    --name mosquitto \
    eclipse-mosquitto


docker run    \
    -d           \
    -p 1880:1880  \
    --name nodered \
    --link mosquitto  \
    nodered/node-red-docker