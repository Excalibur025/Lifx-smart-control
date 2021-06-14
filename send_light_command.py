#!/usr/bin/env python3
#This code will send commands to the light.

#import the modules.
import requests
import json

#This auth token is from the webcite, https://cloud.lifx.com/settings
token = ""

#Headers contain protocol info that appear at the beginning of the raw message that is sent over TCP connection.
headers = {
    "Authorization": "Bearer %s" % token,
}

#ask the user to set parameters. The payload only takes lowercase, so convert to lower.
powerstatus = input("on or off: ")
powerstatus = powerstatus.lower()

#brightness is an int, not a string so convert.
brightness = int(input("Brightness: "))

#saturation = int(input("Saturation: "))

#same thing as above.
color = input("Color (white, red, orange, yellow, cyan, green, blue, purple, or pink): ")
color = color.lower()



#We'll come back to this affect.
#breath = input("Breathing affect (on or off)")
#if breath == yes



#send payload
payload = {
    "power": powerstatus,
    #"color" : blue saturation:0.5
    "color" : color + " saturation:0.75",
    "brightness": brightness,
    "duration": 5,
    #"power": "off",
}

#Tell me if it worked or not.
response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
print(response)
