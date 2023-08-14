import requests
import re
#import sys
import time
import datetime
#import wmi
#import socket
#from os import path

def getIP():
    url = "http://p.njupt.edu.cn/"
    res = requests.get(url = url)
    res.encoding = 'gbk'
    ip = re.search("v46ip=\'([^\']*)\'", res.text).group(1)
    return ip

def check(ip):
    url = "http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=checkScanIP&wlanuserip=%s" % (ip)
    res = requests.get(url = url)
    status = re.search('\"result\":\"([^\"]*)\"', res.text).group(1)
    if (status == 'ok'):
        account = re.search('\"account\":\"([^\"]*)\"', res.text).group(1)
        return account
    else:
        return False
#登录，使用post向http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150发送账号密码。
def login(username, password,netType):
    url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150"
    if "CMCC".__eq__(netType):
        data = {"DDDDD": ",0,%s@cmcc" % (username), "upass": password}
    elif "CHINANET".__eq__(netType):
        data = {"DDDDD": ",0,%s@njxy" % (username), "upass": password}
    elif "NJUPT".__eq__(netType):
        data = {"DDDDD": ",0,%s" % (username), "upass": password}
    else:
        print("校园网类型错误" +netType)
    res = requests.post(url=url, data=data)
    return True


def isNetOK(testserver):
    s=socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False


if __name__ == "__main__":


    username, password, netType = "","",""

    while True:
        try:
            ip = getIP()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print("现在时间：" + now)
            print("IP："+ip)
            print("登录状态：" + check(ip).__str__())
            time.sleep(2)
                
            if (check(ip) == False):
                print("登录中：" + username)
                login(username, password, netType)
                time.sleep(2)
        except:
            pass
        time.sleep(2)
