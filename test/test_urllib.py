#-*- coding = utf-8 -*-
#@Time : 6/12/20 3:31 PM
#@Author : Sean Zhang
#@File : test_urllib.py
#@Software : PyCharm


#httpbin.org
# get request
import urllib.request
# 
# response = urllib.request.urlopen("http://www.google.com")
# print(response.read())

#If you want to use requests
# import requests
# response = requests.get("http://www.google.com")
# print(type(response))

#Get post request #模拟用户登陆
import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
# try:
#     response = urllib.request.urlopen("http://httpbin.org/post", data=data, timeout=0.01)
# except urllib.error.URLError as e:
#     print("time out")
#     
# print(response.read().decode("utf-8"))

 #response.status # status bar # 418 means they know you are a crawler
 #reponse.getheader("Server")
 
url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    # You can add all the accept parameters, cookies, etc there as well. 
}
data = bytes(urllib.parse.urlencode({"hello":"world"}), encoding="utf-8")
#封装好的request object
req = urllib.request.Request(url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))


