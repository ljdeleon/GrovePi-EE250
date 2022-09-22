"""EE 250L Lab 04 Starter Code

Run rpi_pub_and_sub.py on your Raspberry Pi."""

import paho.mqtt.client as mqtt
import time
from grovepi import*

#connecting led to d3
led = 3

pinMode(led,"output")


# set I2C to use the hardware bus
set_bus("RPI_1")

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4


    
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to topics of interest here
    client.subscribe("luis_deleon/led")
#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
#Custom callbacks need to be structured with three args like on_message()
def custom_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    print("custom_callback: " + message.topic + " " + "\"" + 
        str(message.payload, "utf-8") + "\"")
    print("custom_callback: message.payload is of type " + 
          str(type(message.payload)))
    if str(type(message.payload)) == 'LED_ON':
        digitalWrite(led,1)
    elif str(type(message.payload)) == 'LED_OFF':
        digitalWrite(led,0)

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
        time.sleep(1)
        distance = (ultrasonicRead(ultrasonic_ranger))
        client.publish("luis_deleon/ultrasonicRanger", str(distance))
            

