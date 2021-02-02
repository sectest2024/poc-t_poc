#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import request

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
        # hadoop_YARN
        url1 = url + '/cluster'
        r = requests.get(url1, timeout=5, allow_redirects=True, verify=False)
        if "Hadoop" in r.content:
            return "[hadoop yarn unauth]\t" + url1
        else:
            # hadoop_HDFS
            url2 = url + '/explorer.html#/'
            r = requests.get(url2, timeout=10, allow_redirects=True, verify=False)
            if "Browse Directory" in r.content:
                return "[hadoop hdfs unauth]\t" + url2
            else:
                return False
    except:
        return False
