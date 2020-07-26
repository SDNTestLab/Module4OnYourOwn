"""

This is a script that prompts the user to enter email addresses which adds them to
a list and prints the list.

"""
#import requests
#from requests.auth import HTTPBasicAuth

#from webexteamssdk import WebexTeamsAPI

#api = WebexTeamsAPI()
#import requests
#from requests.auth import HTTPBasicAuth
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


token = NDQzYTYwZTMtOTg0My00MTExLTgxNjAtYzA3YTNmZjA1ZTBjZGZiZTIzYzItMTE5_PF84_consumer
postResponse = requests.post(URL2, headers=getHeader, verify=True)
devices = postResponse.json()

addresses = []

more = input("Do you have an email address to enter (y/n)? ")

while more == "y":
    email = input("Enter the address: ")
    addresses.append(email)
    more = input("Do you have another address(y/n)? ")
    while more != "y":
        if more == "n":
            break
        else:
            more = input("Please enter a y or n: ")
    
 
 
for device in devices:
    text = device["addresses"]
 
"""curl --request POST \
  --header "Authorization: Bearer ACCESS_TOKEN" \ 
  --header "Content-Type: application/json" \
  --data '{"roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vMDNjMTc2YTAtY2M0ZC0xMWVhLTg5ZDEtNTE2YzQ2OTliZmI1","text":"addresses"}' \
  https://webexapis.com/v1/messages"""
  
m = MultipartEncoder({'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vMDNjMTc2YTAtY2M0ZC0xMWVhLTg5ZDEtNTE2YzQ2OTliZmI1',
                      'text': "addresses",})
                      

r = requests.post('https://webexapis.com/v1/messages', data=m,
                  headers={'Authorization': 'Bearer ACCESS_TOKEN',
                  'Content-Type': m.content_type})
                  
#token = "NDQzYTYwZTMtOTg0My00MTExLTgxNjAtYzA3YTNmZjA1ZTBjZGZiZTIzYzItMTE5_PF84_consumer"
#URL = "https://webexapis.com/v1/messages"
#roomId = "Y2lzY29zcGFyazovL3VzL1JPT00vMDNjMTc2YTAtY2M0ZC0xMWVhLTg5ZDEtNTE2YzQ2OTliZmI1"


#response = addresses


#getHeader = {'Accept': 'application/json', 'X-auth-token': token}

#postresponse = requests.get(URL, headers=getHeader, verify=True)

#postbody = response.post(roomId, text)
#emailaddresses = postResponse.json(URL, body=postbody)

#print(emailaddresses)

#print(addresses)

#api.messages.create(roomId="Y2lzY29zcGFyazovL3VzL1JPT00vMDNjMTc2YTAtY2M0ZC0xMWVhLTg5ZDEtNTE2YzQ2OTliZmI1", text=addresses)
