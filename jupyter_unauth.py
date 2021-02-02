#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author = carrypan

import requests

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

    try:
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        r = requests.get(url, timeout=5, allow_redirects=False, verify=False)
        if "clusters" in r.text:
            return "[jupyter unauth]\t" + url
        else:
            return False
    except:
        return False
