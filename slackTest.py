# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 01:45:35 2021

@author: Owner
"""

import requests

token = "xoxb-2599288514273-2579951298582-la7B25bNuNmZFRlQ4JNi7UV8"
channel = "#코인매매"
text = "남준 ㅁㄴㅇㄹㄴㅁㅇㄹ"

requests.post("https://slack.com/api/chat.postMessage",
    headers={"Authorization": "Bearer "+token},
    data={"channel": channel,"text": text})