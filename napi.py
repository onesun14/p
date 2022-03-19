import os
import sys
import requests
from bs4 import BeautifulSoup
import json
import urllib.request
ip = input("종류: ko, en, ja, zh-CN\n입력언어: ")
op = input("종류: ko, en, ja, zh-CN\n출력언어: ")
num = input("번역할 문장({})을 입력해 주세요: ".format(ip))
client_id = "ieAsulav6hyW71QQpIo9" # 개발자센터에서 발급받은 Client ID 값
client_secret = "fQU030a9GP" # 개발자센터에서 발급받은 Client Secret 값
encText = urllib.parse.quote(num)
data = "source={}&target={}&text=".format(ip, op) + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    body = response_body.decode('utf-8')
    data = json.loads(body)
    #print(data)
    print(data['message']['result']['translatedText'])

else:
    print("Error Code:" + rescode)