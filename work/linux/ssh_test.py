import paramiko
import sys
'''
Author: LiLe
Date: 20190905
Version: V2.0
Contact: 15274326058
Description: Paramiko库登录远程主机执行命令并返回结果
Document: http://docs.paramiko.org/en/2.6/
'''

def chan_recv(chan):
    data = chan.recv(1024)            # 收1024数据

    sys.stdout.write(data.decode())   # 输出
    sys.stdout.flush()

class ParamikoClient:
    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
        self.username = config['username']
        self.key = config['key']
        self.channel=None

    # 连接
    def connects(self):
        try:
            # 使用自定义秘钥
            # private_key = paramiko.RSAKey.from_private_key_file(self.key)
            self.client = paramiko.SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.host, port=self.port, username=self.username,password=self.key, timeout=10)
            # self.client.connect(hostname=self.host, port=self.port, username=self.username,pkey=private_key)

            self.channel = self.client.invoke_shell()
            chan_recv(self.channel)

            # ssh = paramiko.SSHClient()
            # ssh.load_system_host_keys()
            # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # ssh.connect('10.10.201.81', port=22, username='root', password='Sutpco81', timeout=3)  # 3秒超时
            # channel = ssh.invoke_shell()
            #
            # chan_recv(channel)  # 开始前先收一下数据
        except Exception as err:
            print(err)

    # 关闭
    def close(self):
        try:
            self.channel.close()
            self.client.close()
        except:
            pass

    # 执行命令
    def exec_command(self, cmd):
        # invoke = self.client.invoke_shell()
        # channel=self.channel

        self.channel.send(cmd+"\n")  # \n很重要，相当于回车
        # time.sleep(2)  # 等待命令执行完毕
        # stderr_result=invoke.recv(9999).decode("utf-8")   # 提取数据然后解码
        chan_recv(self.channel)
        # print(stderr_result)
        # stdin, stdout, stderr = self.client.exec_command(cmd)
        # stdout_result = stdout.readlines()
        # stderr_result = stderr.readlines()

        # if stderr_result:
        #     print(stderr_result)
        #     return False
        # else:
        #     return stdout_result


        # return stdout.read()


if __name__ == '__main__':
    paramiko_config = {
        'host': '10.10.201.81',
        'port': 22,
        'username': 'root',
        'key': 'Sutpco81',
    }

    paramik = ParamikoClient(paramiko_config)
    paramik.connects()

    # result = paramik.exec_command('cd /usr/local/openstreetmap-website;ls')
    result = paramik.exec_command('ls')
    print(result)

    # result = paramik.exec_command('docker-compose exec web bash')
    # print(result)
    #
    # result = paramik.exec_command(
    #     'osmosis --read-apidb host="db" database="openstreetmap" user="openstreetmap" password="openstreetmap" validateSchemaVersion="no" --write-pbf baktest.osm.pbf')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值
    #
    # print(result)
    paramik.close()



# import time, paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
# ssh.connect(ip, port, username, password, timeout=10)
# invoke = ssh.invoke_shell()
# invoke.send("python3 /root/test.py \n")  # \n很重要，相当于回车
# time.sleep(2)  # 等待命令执行完毕
# # invoke.recv(9999).decode("utf-8")   # 提取数据然后解码
# ssh.close()
