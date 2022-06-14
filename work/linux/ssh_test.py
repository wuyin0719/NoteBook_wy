import paramiko

'''
Author: LiLe
Date: 20190905
Version: V2.0
Contact: 15274326058
Description: Paramiko库登录远程主机执行命令并返回结果
Document: http://docs.paramiko.org/en/2.6/
'''


class ParamikoClient:
    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
        self.username = config['username']
        self.key = config['key']

    # 连接
    def connects(self):
        try:
            # 使用自定义秘钥
            # private_key = paramiko.RSAKey.from_private_key_file(self.key)
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=self.host, port=self.port, username=self.username,password=self.key)
            # self.client.connect(hostname=self.host, port=self.port, username=self.username,pkey=private_key)
        except Exception as err:
            print(err)

    # 关闭
    def close(self):
        try:
            self.client.close()
        except:
            pass

    # 执行命令
    def exec_command(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        stdout_result = stdout.readlines()
        stderr_result = stderr.readlines()
        if stderr_result:
            print(stderr_result)
            return False
        else:
            return stdout_result
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
    result = paramik.exec_command('cd /usr/local/openstreetmap-website')
    print(result)

    result = paramik.exec_command('docker-compose exec web bash')
    print(result)

    result = paramik.exec_command(
        'osmosis --read-apidb host="db" database="openstreetmap" user="openstreetmap" password="openstreetmap" validateSchemaVersion="no" --write-pbf baktest.osm.pbf')  # stdout 为正确输出，stderr为错误输出，同时是有1个变量有值

    print(result)
    paramik.close()