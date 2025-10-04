import requests

html = requests.get("https://httpbin.org/json").text
print(html)

input("回车退出")
