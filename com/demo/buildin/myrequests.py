import requests

url = 'https://api.douban.com/v2/book/2129650'
r = requests.get(url)

print(r.status_code)
print(type(r.text))
print(type(r.json()))

# 上传图片

upload_file = {'file': open('demo.img', 'rb')}

result = requests.post(url, files=upload_file)