#写文件
# with open('D:\\task\\预警.txt','wt') as out_file:
#     out_file.write('sdfdsfds')
#
#     # Read a file
# with open("D:\\task\\预警.txt", "rt") as in_file:
#     text = in_file.read()
#
# print(text)

import requests
import urllib
#openurl = "http://www.xxx.com/zz.rar"     #普通下载
#saveurl = "d:/99999.rar"
#urllib.request.urlretrieve(openurl, saveurl)

# openurl = "magnet:?xt=urn:btih:52683ab303e16ff22e9e1abd44af129cb24b661a"
# saveurl = "d:/task/1.mp4"
# r = requests.get(openurl, stream=True)    #流式下载
# f = open(saveurl, "wb")
# for chunk in r.iter_content(chunk_size=512):
#     if chunk:
#         f.write(chunk)

        # 榜单歌曲批量下载
#http://music.163.com/discover/toplist?id=3779629    id来自于 http://music.163.com/ 的“云音乐新歌榜”
r = requests.get('http://music.163.com/api/playlist/detail?id=3779629')
arr = r.json()['result']['tracks']    # 共有100首歌

for i in range(10,20):    # 输入要下载音乐的数量，1到100。
    name = str(i+1) + ' ' + arr[i]['name'] + '.mp3'
    link = arr[i]['mp3Url']
    urllib.request.urlretrieve(link, 'd:\\task\\' + name)    # 提前要创建文件夹
    print(name + ' 下载完成')