#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import requests
import urllib3

def poc(url):
    portlist = ['21','22','23','25','53','110','137','161','389','445','873','1090','1099','1433','1521','2049','2181','2222','2375','3306','3389','5432','5901','5984','6379','11211','27017']    
    if url.split(':')[1] in portlist:
        return False
    elif int(url.split(':')[1]) == 443:
        url = 'https://' + url.split(':')[0]
    elif int(url.split(':')[1]) == 8443:
        url = 'https://' + url
    else:
        url = 'http://' + url
    
    header = dict()
    header['User-Agents'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:75.0) Gecko/20100101 Firefox/75.0'
    try:
    	requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        response = requests.get(url, timeout=5, cookies={"rememberMe": 'test'}, headers=header, verify=False, allow_redirects=False)
        if 'rememberMe=deleteMe' in response.headers['Set-Cookie']:
            return '[shiro rememberMe]' + '\t' + url
        else:
            return False
    except Exception:
        return False