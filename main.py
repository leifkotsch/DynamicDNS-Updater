import requests
#import json
#import os

#DDNS_LIST syntax: [[username,password],[...,...],...]


DDNS_LIST = []
DDNS_LOGIN_URL = ""
CONSOLE_OUTPUT = false
#JSON_LIST = ""


#if(not os.path.isfile(JSON_LIST)):
#  if(CONSOLE_OUTPUT):
#    print("JSON-List dosn´t exist. ")

#with open(JSON_LIST) as temp_json_file:
#  json_data = json.load(temp_json_file)
#  temp_json_file.close()
  
      
      
for _temp in DDNS_LIST:
  temp_request = requests.get(DDNS_LOGIN_URL, auth=(_temp[0],_temp[1]))
  if(not temp_request.status_code == "200"):
    if(CONSOLE_OUTPUT):
      print("Request failed. User: {}; Statuscode: {};".format(_temp[0],temp_request.status_code))
  else:
    if(CONSOLE_OUTPUT):
      print("Request succeeded. User: {}".format(_temp[0]))
      
if(CONSOLE_OUTPUT):
  print("Done.")
