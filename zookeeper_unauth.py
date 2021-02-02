#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import socket

def poc(url):  
    socket.setdefaulttimeout(8)
    try:
        host = url.split(':')[0]
        port = int(url.split(':')[1])
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send("envi".encode())
        recv_data = s.recv(1024)
        s.close()
        if b'zookeeper.version' in recv_data:
            return "[zookeeper unauth]\t" + url
    except:
        return False