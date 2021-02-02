#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = carrypan

import socket
import binascii

def poc(url):
    if int(url.split(':')[1]) == 5432:
        socket.setdefaulttimeout(8)
        payload = binascii.a2b_hex("00000029000300007573657200706f73746772657300646174616261736500706f7374677265730000")
        try:
            host = url.split(':')[0]
            port = int(url.split(':')[1])
            s = socket.socket()
            s.connect((host, port))
            s.send(payload)
            recv_data = s.recv(1024)
            s.close()
            if b"70675f6862612e636f6e66" in binascii.b2a_hex(recv_data):
                return "[postgresql service detected (local login only)]\t" + url
            # R
            elif binascii.b2a_hex(recv_data).startswith(b"520000000c0000000"):
                return "[postgresql service detected (need password)]\t" + url
            # server_version
            elif b"7365727665725f76657273696f6e" in binascii.b2a_hex(recv_data):
                return "[postgresql is unauthorized]\t" + url
        except:
            return False
    else:
        return False