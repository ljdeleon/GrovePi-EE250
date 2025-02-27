"""EE 250L Lab 04 Starter Code

Run vm_subscriber.py in a separate terminal on your VM."""

# Luis De Leon
#Jacob Abell
#Git Hub Repository : git@github.com:ljdeleon/GrovePi-EE250.git

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    #subscribe to the ultrasonic ranger topic here
    client.subscribe("luis_deleon/ultrasonicRanger")
    client.message_callback_add("luis_deleon/ultrasonicRanger",custom_callback)
    client.subscribe("luis_deleon/button")
    client.message_callback_add("luis_deleon/button",custom_callback2)
    client.subscribe("luis_deleon/lcd")
    client.message_callback_add("luis_deleon/lcd",custom_callback3)

#Default message callback. Please use custom callbacks.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))
#Custom callbacks need to be structured with three args like on_message()
def custom_callback(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    #print("custom_callback: " + message.topic + " " + "\"" + 
    print("VM: " +  
        str(message.payload, "utf-8") + "cm")
    #print("custom_callback: message.payload is of type " + 
     #     str(type(message.payload)))
          #message.decode('base64','strict')
def custom_callback2(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    #print("custom_callback: " + message.topic + " " + "\"" + 
    print(str(message.payload, "utf-8"))
    #print("custom_callback: message.payload is of type " + 
     #     str(type(message.payload)))
          #message.decode('base64','strict')    
def custom_callback3(client, userdata, message):
    #the third argument is 'message' here unlike 'msg' in on_message 
    #print("custom_callback: " + message.topic + " " + "\"" + 
    print(str(message.payload, "utf-8"))
    #print("custom_callback: message.payload is of type " + 
     #     str(type(message.payload)))
          #message.decode('base64','strict')   

if __name__ == '__main__':
    #this section is covered in publisher_and_subscriber_example.py
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    client.loop_start()

    while True:
       # print("delete this line")
        time.sleep(1)
            

