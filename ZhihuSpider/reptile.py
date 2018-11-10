import urllib.request

#网址
url = "http://www.zhmb.gov.cn/jeecms/web/index";

#请求
request = urllib.request.Request(url);

#取得结果

response = urllib.request.urlopen(request);

data = response.read()

#设置解码方式
data = data.decode('utf-8')

#打印结果
print(data)

print(type(response))
print(response.geturl())
print(response.info())
print(response.getcode())