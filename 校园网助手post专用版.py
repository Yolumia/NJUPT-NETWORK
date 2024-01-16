import requests
import re
import sys
import time
import datetime
# import wmi
# from selenium import webdriver
import socket
from os import path


# 通过http://p.njupt.edu.cn/的返回res得到ip
def getIP():
    url = "http://p.njupt.edu.cn/"
    res = requests.get(url=url)
    res.encoding = 'gbk'
    ip = re.search("v46ip=\'([^\']*)\'", res.text).group(1)
    return ip

def login(url):
    ip = getIP()
    requests.post(url=url)
    return True


def read_user_inf():
    with open('url.txt', encoding='utf-8') as file_obj:
        url = file_obj.read()
        print("读取url成功：" + url.rstrip())
    return url


# def isNetOK(testserver):
#     s = socket.socket()
#     s.settimeout(3)
#     try:
#         status = s.connect_ex(testserver)
#         if status == 0:
#             s.close()
#             return True
#         else:
#             return False
#     except Exception as e:
#         return False

#通过访问百度，检查网络是否连上了
def isConnected():
    q = ('www.baidu.com', 443)
    return isNetOK(q)

if __name__ == "__main__":

    print("南京邮电大学校园网登录助手脚本V24.1.16")
    print("更新日志：2024年1月16日，抓包专用版本")
    print("")
    print("作者：张家宾（B站：技术宅学长），特别感谢：张乔楚")
    print("交流群：873779462")
    
    url = read_user_inf()#从url.txt文件读取url
    #或者直接写url="你抓包的url"

    while True:
        try:
            ip = getIP()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print("现在时间：" + now)
            print("IP：" + ip)
            login(url)
            time.sleep(10)#休眠10秒
        except:
            print("登录失败")
            pass
        time.sleep(30)
