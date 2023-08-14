import requests
import re
import sys
import time
import datetime
# import wmi
# from selenium import webdriver
import socket
from os import path


# 第一步，通过http://p.njupt.edu.cn/的返回res得到ip
def getIP():
    url = "http://p.njupt.edu.cn/"
    res = requests.get(url=url)
    res.encoding = 'gbk'
    ip = re.search("v46ip=\'([^\']*)\'", res.text).group(1)
    return ip


# 通过http://p.njupt.edu.cn:801/eportal/?c=ACSetting&a=checkScanIP&wlanuserip=%s" % (ip)的返回得到的res检查登录账号或者没有登录成功。
# def check(ip,username,password):
#     wlan_ac_ip = "10.255.252.150"
#     url = "http://p.njupt.edu.cn:802/eportal/?c=ACSetting&a=checkScanIP&wlanuserip=%s" % (ip)
#     url = "https://p.njupt.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C" + username + "%40cmcc&user_password=" + password + "&wlan_user_ip=" + ip + "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=" + wlan_ac_ip + "&wlan_ac_name=XL-BRAS-SR8806-X&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2875&lang=zh"
#     res = requests.get(url = url)
#     status = re.search('\"result\":\"([^\"]*)\"', res.text).group(1)
#     if (status == 'ok'):
#         account = re.search('\"account\":\"([^\"]*)\"', res.text).group(1)
#         return account
#     else:
#         return status
# 登录，使用post向http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150发送账号密码。
def login(url):
    ip = getIP()

    # url = "https://p.njupt.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C"+username+"%40cmcc&user_password="+password+"&wlan_user_ip="+ip+"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip="+wlan_ac_ip+"&wlan_ac_name=XL-BRAS-SR8806-X&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2875&lang=zh"
    #
    # if "仙林".__eq__(Location):
    #     url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150"
    #     #wlan_ac_ip="10.255.252.150"
    #
    # elif "三牌楼".__eq__(Location):
    #     url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.253.118"
    #     #wlan_ac_ip="10.255.253.118"
    #
    # elif "物联网科技园".__eq__(Location):
    #     url = "http://10.10.244.11:801/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150"
    #     #wlan_ac_ip="10.255.253.118"

    # url = "https://p.njupt.edu.cn:802/eportal/portal/login?callback=dr1003&login_method=1&user_account=%2C0%2C" + username + "%40"+netType+"&user_password=" + password + "&wlan_user_ip=" + ip + "&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=XL-BRAS-SR8806-X&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&v=2875&lang=zh"
    # url = "http://10.255.252.150:802/eportal/?c=ACSetting&a=Login&wlanacip=10.255.252.150"

    # if "CMCC".__eq__(netType):
    #     data = {"DDDDD": ",0,%s@cmcc" % (username), "upass": password}
    # elif "CHINANET".__eq__(netType):
    #     data = {"DDDDD": ",0,%s@njxy" % (username), "upass": password}
    # elif "NJUPT".__eq__(netType):
    #     data = {"DDDDD": ",0,%s" % (username), "upass": password}
    # else:
    #     print("校园网类型错误" +netType)
    # res = requests.post(url=url, data=data)
    res = requests.post(url=url)
    return True


def read_user_inf():
    with open('url.txt', encoding='utf-8') as file_obj:
        url = file_obj.read()
        print("读取url成功：" + url.rstrip())

    return url


def isNetOK(testserver):
    s = socket.socket()
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


def isConnected():
    q = ('www.baidu.com', 443)
    return isNetOK(q)


if __name__ == "__main__":

    print("南京邮电大学校园网登录助手脚本V1.4 2023年7月22日更新")
    print("更新日志：2023年7月22日，post专用版本")
    print("")
    print("作者：张家宾，特别感谢：张乔楚")
    print("交流群：873779462")
    url = read_user_inf()
    # username, password, netType, wlan_ac_ip= "1221056113","Mss1003..","CMCC","10.255.252.150"
    while True:
        try:
            ip = getIP()
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            print("现在时间：" + now)
            print("IP：" + ip)
            # print("登录状态：" + check(ip).__str__())

            # print("ping 互联网状态：" +isConnected().__str__())
            # time.sleep(10)

            # if (check(ip) == False) or (isConnected() == False):
            #     print("登录中：" + username)
            #     login(username, password, netType)
            #
            #     time.sleep(10)
            # if (isConnected() == False):
            login(url)
            time.sleep(10)
        except:
            pass
        time.sleep(30)
