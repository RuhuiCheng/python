import urllib.request
from lxml import etree
import os

url1 ='http://www.ximalaya.com/47398747/album/5399359/?page=1'
url2 ='http://www.ximalaya.com/47398747/album/5399359/?page=2'
basePath = 'D:\BaiduYunDownload\赖氏英语语法完全讲解'
def GetURLData(url):
    req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    )
    f = urllib.request.urlopen(req)
    html = etree.HTML(f.read())
    result = html.xpath('//*[@id="mainbox"]/div[1]/div[1]/div/div[2]/div[4]/ul/li/div/a/@title')
    # print(result)
    return result
u1 = GetURLData(url1)
# print(len(u1))
u2 = GetURLData(url2)
# print(len(u2))
u3 = u1 + u2
# print(u3)
def RenameFile(file,dt):
    f1 = file.replace('.mp3','')
    # print(f1)
    for item in dt:
        # print(item.startswith(f1))
        if(item.startswith(f1)):
            fileX = basePath+'\\' + file
            # print(fileX)
            fileY = basePath+'\\' + item + '.mp3'
            # print(fileY)
            os.rename(fileX,fileY)
            break
def GetFileList(dt):
    basePath ='D:\BaiduYunDownload\赖氏英语语法完全讲解'
    fileList = os.listdir(basePath)
    for file in fileList:
        RenameFile(file,dt)

GetFileList(u3)