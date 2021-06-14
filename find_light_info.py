#!/usr/bin/env python3

#This code will find the smart light.

#import the requests because curl.
import requests
import json

#This auth token is from the webcite, https://cloud.lifx.com/settings
token = ""

#Headers contain protocol info that appear at the beginning of the raw message that is sent over TCP connection.
headers = {
    "Authorization": "Bearer %s" % token,
}

#The response we want back from the reques.
response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)

#Tell me what the response was, 200 means successful.
print(response)
#Give it to me in json.
print(response.json())

#This attempt to write output to file didn't work, so I'm skipping it for now.
#respondString = str(response.json)
#writeFile = open("data_return.json", "a")
#writeFile.write(respondString)
#writeFile.close()
