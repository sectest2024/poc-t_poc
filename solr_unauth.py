#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import requests
from plugin.useragent import firefox
from plugin.urlparser import iterate_path


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
    
    fileList = r"""
    /
    /solr/
    """
    paths = fileList.strip().splitlines()
    for path in paths:
        try:
            url = url + path.strip()
            requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
            g = requests.get(url, headers={'User-Agent': firefox()}, verify=False, timeout=5)
            if g.status_code == 200 and 'Solr Admin' in g.content and 'Dashboard' in g.content:
                return '[solr unauth]\t' + url
            else:
                continue
        except Exception:
            return False
