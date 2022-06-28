#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 9:08
# @Author  : 5in
import paramiko
import sys
import time
def chan_recv(chan):
    data = chan.recv(9999)  # 收1024数据
    sys.stdout.write(data.decode())  # 输出
    sys.stdout.flush()


# def shell81():

if __name__ == '__main__':
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.10.201.81', port=22, username='root', password='Sutpco81', timeout=3)  # 3秒超时
    channel = ssh.invoke_shell()

    chan_recv(channel)  # 开始前先收一下数据
    cmds=['cd /usr/local/openstreetmap-website \n','docker-compose exec web bash \n','osmosis --read-apidb host="db" database="openstreetmap" user="openstreetmap" password="openstreetmap" validateSchemaVersion="no" --write-pbf bak%s.osm.pbf \n'%'test']
    for cmd in cmds:
        # channel.send(d + '\n')
        # for i in range(2):
        channel.send(cmd)
        chan_recv(channel)
        time.sleep(2)
    time.sleep(10)
    # for cmd in cmds:
    #     # channel.send(d + '\n')
    #     channel.send(cmd)
    #     chan_recv(channel)
    #     time.sleep(1)
    # while True:  # 监听输入
    #     d = input()
    #     if d == 'quit':  # 如果输入quit，就退出
    #         break
    #     channel.send(d + '\n')
    #     chan_recv(channel)

    channel.close()
    ssh.close()


import re
import time
from paramiko import SSHClient, AutoAddPolicy
# from func_timeout import func_set_timeout, exceptions

# import paramiko
# import threading
#
#
# class MyThread(threading.Thread):
#
#     def __init__(self, func, args=()):
#         super(MyThread, self).__init__()
#         self.func = func
#         self.args = args
#
#     def run(self):
#         self.result = self.func(*self.args)
#
#     def get_result(self):
#         try:
#             return self.result
#         except Exception:
#             return None
#
#
# def chan_recv(chan):
#     resp = ''
#     while True:
#         data = chan.recv(1024)
#         if not data:
#             break
#         resp += data.decode()
#     return resp
#
#
# def shell(commands, host, port, username, password, timeout=3):
#     ssh = paramiko.SSHClient()
#     ssh.load_system_host_keys()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(host, port=port, username=username, password=password, timeout=timeout)
#     channel = ssh.invoke_shell()
#     writer = MyThread(chan_recv, args=(channel,))
#     writer.start()
#     for cmd in commands:
#         channel.send(cmd)
#     writer.join()
#     channel.close()
#     ssh.close()
#     return writer.get_result()
#
#
# if __name__ == '__main__':
#     # cmds = ['enable\n', 'cisco\n', 'terminal length 0\n', 'show ip int br\n',
#     #         'show run\n', 'show version\n', 'show inventory\n',
#     #         'sh cdp nei\n', 'conf t\n', 'router ospf 110\n',
#     #         'network 10.10.10.2 0.0.0.0 area 0\n',
#     #         'end\n', 'exit\n']
#
#     cmds = ['cd /usr/local/openstreetmap-website \n','ls \n']
#
#     # ssh.connect('10.10.201.81', port=22, username='root', password='Sutpco81', timeout=3)  # 3秒超时
#     res = shell(cmds, '10.10.201.81', '22', 'root', 'Sutpco81')
#     print(res)