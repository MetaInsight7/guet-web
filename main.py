# -*- coding:utf-8 -*-
import requests
from lxml import etree
import time

# parameters
# 账号
id = 
#密码
password = 
#运营商，校园网不填，移动填cmcc，联通填unicom，电信填telecom
operator = "" 




def login():
    url = "http://10.0.1.5/drcom/login?callback=dr1003&DDDDD={}%40{}&upass={}&0MKKey=123456&R1=0&R2=&R3=0&R6=0&para=00&v6ip=&terminal_type=1&lang=zh-cn&jsVersion=4.1&v=8928&lang=zh".format(id, operator, password)
    r = requests.get(url)
    status_index = r.text.find("result") 
    i = 0
    while r.text[status_index+8:status_index+9] == "0"and i < 5:
        i += 1
        print("登录失败，正在进行第{}次重试".format(i))
        r = requests.get(url)
    if r.text[status_index+8:status_index+9] != "1":
        print("登录失败")
        print(r.text)
    else:
        print("登陆成功！")

# 监测内网
def net_status():
    monitor_url = "http://10.0.1.5/"
    html = requests.get(monitor_url).text
    tree = etree.HTML(html)
    title = tree.xpath("/html/head/title/text()")[0]
    return title

# 监测外网
def net_status_baidu():
    monitor_url = "http://baidu.com/"
    status_code = requests.get(monitor_url).status_code
    return status_code
    

while True:
    try:
        title = net_status()
        if title =="注销页":
            pass
        else:
            login()

    except:
        status_code = net_status_baidu()
        if status_code == 200:
            pass
        else:
            login() 
    time.sleep(5)