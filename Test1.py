# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import jwt
import uuid


import requests

access_key = "WLWxUlC4QOTGiudrxWFpN7XoaKxgDQCDc5YvPVUD"
secret_key = "76jmH7Oyiq6CExxKOBfQ1ExrkFVPPhhw2Rs0yz5G"
server_url = "https://api.upbit.com/v1/accounts"

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
}

jwt_token = jwt.encode(payload, secret_key)
authorize_token = 'Bearer {}'.format(jwt_token)
headers = {"Authorization": authorize_token}

res = requests.get(server_url, headers=headers)

data = res.json()
my_balance = float(data[0]["balance"])
print(my_balance)