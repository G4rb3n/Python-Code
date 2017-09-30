#coding=UTF-8

import threading
import socket
import time
import random

def scanner(ip,port) :
    try :
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        result = s.connect_ex((ip,port))
        if result == 0 :
            print ip,u':',port,u'端口开放'
        s.close()
    except :
        print u'端口扫描异常'
    
def port_scan(ip) :
    try :
        print u'开始扫描 %s' % ip
        start_time = time.time()
        buf = range(0,65535)
        threads = []
       #random.shuffle(buf)
        for i in buf :
            t = threading.Thread(target = scanner,args = (ip,int(i)))
            threads.append(t)
        for t in threads :
            t.start()
        for t in threads :
            t.join()
        print u'端口扫描完毕，总共用时 : %.2f' % (time.time() - start_time)
        raw_input("Press Enter to Exit")
    except :
        print u'扫描ip出错'

if __name__ == '__main__' :
    target = raw_input('Input the ip you want to scan : ')
    port_scan(target)
        
            
