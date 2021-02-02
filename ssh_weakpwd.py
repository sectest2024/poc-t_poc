#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author : carrypan

import paramiko

def ssh_login(ip,port,user,pwd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,user,pwd,timeout=5)
        print '[ssh weak password]\t'+ user + ':' + pwd
        flag = 1
        ssh.close()
    except:
        return False

def poc(url):
    global flag
    flag = 0
    portlist = ['22','2222']
    if url.split(':')[1] not in portlist:
        return False
    else:
        pwdlist = ['root','123456','root@123']
        for pwd in pwdlist:
            ssh_login(url.split(':')[0],int(url.split(':')[1]),'root',pwd)
            if flag == 1:
                break