from flask import request, jsonify
import requests as r
from requests.structures import CaseInsensitiveDict
def api1():
#-------GET PHONE------#
  args = request.args.to_dict()
  phone = args.get("phone")
#----------------------#
  url = "https://api.eat-z.com/auth/customer/signin"
  headers = CaseInsensitiveDict()
  headers["Content-Type"] = "application/json"
  data = '{"username": "+88'+phone+'"}'
  resp = r.post(url, headers=headers, data=data)
  rcode = resp.status_code
  if resp.status_code == 400:
    rdata = resp.json()['invalid_params']['username']
    return {'STATUS':'FAILED', 'SEND':'FALSE', 'STATUS_CODE':+rcode, 'DEVELOPER':'SIAMRAHMAN', 'API_NO':'1', 'ERROR':rdata}
  elif resp.status_code == 429:
    redata = resp.json()['detail']
    return {'STATUS':'FAILED', 'SEND':'FALSE', 'STATUS_CODE':+rcode, 'DEVELOPER':'SIAMRAHMAN', 'API_NO':'1', 'ERROR':redata}
    


  else:
    return {'STATUS':'SUCCESS', 'SEND':'TRUE', 'STATUS_CODE':+rcode, 'DEVELOPER':'SIAMRAHMAN', 'API_NO':'1'}
  
