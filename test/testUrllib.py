# @Time : 2021/12/9 20:35
# @Author : klenq
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request

# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding = "utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post", data)
# print(response.read().decode('utf-8'))

# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.read().decode('utf-8'))

# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding = "utf-8")
#
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
# }
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
#
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
url = "http://www.douban.com"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))

