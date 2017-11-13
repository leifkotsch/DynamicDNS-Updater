import requests

#DDNS_LIST syntax: [[username,password],[...,...],...] all entrys must be strings
DDNS_LIST = []
DDNS_LOGIN_URL = ""
CONSOLE_OUTPUT = false

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
