# _*_ coding: utf-8 _*_
import os
import sys
import socket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

ACCOUNTS_FILE = os.path.join(BASE_DIR,'config','account.ini')

address_family = socket.AF_INET
socket_type = socket.SOCK_STREAM

BIND_HOST = '127.0.0.1'
BIND_PORT = 9999
ip_port = (BIND_HOST,BIND_PORT)
coding = 'utf-8'
listen_count = 5
max_recv_bytes = 8192
allow_reuse_address = False