#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, urllib2

USER_NAME = ''                                       #修改该变量作为登陆名
PASSWORD = ''                                        #修改该变量作为登陆密码，密码用明文的话，是在太2b了

LOGIN_URL = 'http://172.27.16.1/webAuth/index.htm'   #这是需要登陆的页面地址

need_redirect = False

u'''
定义一个重定向的处理类，处理301、302返回码作为需登陆的依据
'''
class MyRedirectHandler(urllib2.HTTPRedirectHandler) :
    def http_error_301(self, req, fp, code, msg, headers) : 
        global need_redirect

        need_redirect = True
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, headers)
        return result

    def http_error_302(self, req, fp, code, msg, headers) :
        global need_redirect

        need_redirect = True
        result = urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)
        return result

def check_need_login() :
    check_url = 'http://www.baidu.com'

    req = urllib2.Request(check_url)
    opener = urllib2.build_opener(MyRedirectHandler)
    urllib2.install_opener(opener)
    urllib2.urlopen(req)

def login() :
    values = {'username' : USER_NAME, 'password' : PASSWORD, 'pwd' : PASSWORD, 'secret' : 'true'}
    data = urllib.urlencode(values)
    headers = {'Content-type': 'application/xhtml+xml', 'Accept': 'text/html', 'User-agent': 'Mozilla/7.0'}
    req = urllib2.Request(LOGIN_URL, data, headers)
    response = urllib2.urlopen(req)

    code = response.getcode()
    if code == 200 :
        print 'Login may be success, try yourself'
    else :
        print 'Login failed'

if __name__ == '__main__' :
    check_need_login()

    if need_redirect == False :
        print 'No need to login, bye!'
    else :
        print 'U need to login'
        print 'Logining ...'
        login()
