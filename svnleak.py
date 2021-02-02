#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import requests

def poc(url):
    headers = {
            "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }
    portlist = ['21','22','23','25','53','110','137','161','389','445','873','1090','1099','1433','1521','2049','2181','2222','2375','3306','3389','5432','5901','5984','6379','11211','27017']    
    if url.split(':')[1] in portlist:
        return False
    elif int(url.split(':')[1]) == 443:
        url = 'https://' + url.split(':')[0]
    elif int(url.split(':')[1]) == 8443:
        url = 'https://' + url
    else:
        url = 'http://' + url
    svnurl = url + "/.svn/entries"

    try:
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        req = requests.get(svnurl, headers=headers, timeout=8, allow_redirects=False, verify=False)
        if req.status_code == 200 and 'octet-stream' in req.headers['Content-Type'] and 'Nothing to see here' not in req.text:
            return "[svn leak]" + '\t' + svnurl
        else:
            return False
    except:
        return False