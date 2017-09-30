#coding=utf-8

import os  
import sys  
import requests  
import json  
import time  
page = 1  
# ZoomEye' Info (Person)  
# 输入个人账号密码  
user = '979784643@qq.com'  
passwd = 'FKP19960317'
  
def Check():  
    #POST get access_token  
    data_info = {'username' : user,'password' : passwd}  
  
    #dumps() -> python'object cast the type of json  
    data_encoded = json.dumps(data_info)  
  
    #POST   
    respond = requests.post(url = 'https://api.zoomeye.org/user/login',data = data_encoded)  
      
    try:  
        # loads() -> json cast python'object  
        r_decoded = json.loads(respond.text)   
  
        #get access_token  
        access_token = r_decoded['access_token']  
    except KeyError:  
        return 'ErrorInfo'  
      
    return access_token  
  
      
# 查询语法  
def search():  
    num = 1
    global kindDev   
    kindDev = num  
    search = ''  
    search = 'app:weblogic port:7001'
    global query  
      
    query = 'page=' + str(page) + '&' + 'query=' + search
  
# 获取Respose对象  
def getRespose():  
    # get request'header  
    headers = {'Authorization' : 'JWT ' + access_token}  
      
    # format token and add to HTTP Header  
    respond = requests.get(url = 'https://api.zoomeye.org/host/search?' + query,headers = headers)   
    if respond.status_code == 401:  
        print('需要授权登陆\n')  
        sys.exit()  
    return respond  
          
def getIp():  
    result = json.loads(getRespose().text)  
    output = open('ip.txt','a+')  
    for i in range(0,10):  
        #print(str(result['matches'][i]['ip']) + ':' + str(result['matches'][i]['portinfo']['port']))  
        output.write(str(result['matches'][i]['ip']) + ':' + str(result['matches'][i]['portinfo']['port']) + '\n')  
    output.close()  
      
def ZoomEye():  
    # get access_token from Check()  
    global access_token  
    access_token = Check()  
    if 'ErrorInfo' == access_token:  
        print('请正确输入用户名和密码，以便获取access_token')  
        sys.exit()  
    #print(access_token)  
    # 查询语法  
    search();  
  
    # 搜索设备  
    if kindDev:  
        page = 100 
        while True:  
            getIp()  
            time.sleep(0.5)  
            page = page - 1  
            if page == 0:  
                sys.exit()  
              
              
    # 搜索网站    
    elif kindDev:  
        print('网站 :\n')  
  
    #for i in range(0,10):  
    #   print(str(result['matches'][i]['ip']) + ':' + str(result['matches'][i]['portinfo']['port']))  
  
if __name__ == '__main__':  
    ZoomEye()
