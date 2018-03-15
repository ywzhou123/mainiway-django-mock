#-*- coding:utf-8 -*-
import paramiko
import os

transport = paramiko.Transport(('192.168.220.135', 22))
transport.connect(username='root', password='hacker')

sftp = paramiko.SFTPClient.from_transport(transport)  # 如果连接需要密钥，则要加上一个参数，hostkey="密钥"

sftp.put('Windows.txt', '/root/Windows.txt')  # 将本地的Windows.txt文件上传至服务器/root/Windows.txt

transport.close()  # 关闭连接

class SFTP(object):
    def __init__(self, ip, username, password, timeout=30):
        self.ip = ip
        self.username = username
        self.password = password
        self.timeout = timeout
        self.try_times = 3

    def close(self):
        pass

    def sftp_put(self, localfile, remotefile):
        transport = paramiko.Transport(sock=(self.ip, 22))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(localfile, remotefile)
        transport.close()

    def __get_all_files_in_local_dir(self, local_dir):
        # 保存所有文件的列表
        all_files = list()

        # 获取当前指定目录下的所有目录及文件，包含属性值
        files = os.listdir(local_dir)
        for x in files:
            # local_dir目录中每一个文件或目录的完整路径
            filename = os.path.join(local_dir, x)
            # 如果是目录，则递归处理该目录
            if os.path.isdir(x):
                all_files.extend(self.__get_all_files_in_local_dir(filename))
            else:
                all_files.append(filename)
        return all_files

    def sftp_put_dir(self, local_dir, remote_dir):
        transport = paramiko.Transport(sock=(self.ip, 22))
        transport.connect(username=self.username, password=self.password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # 去掉路径字符穿最后的字符'/'，如果有的话
        if remote_dir[-1] == '/':
            remote_dir = remote_dir[0:-1]

        # 获取本地指定目录及其子目录下的所有文件
        all_files = self.__get_all_files_in_local_dir(local_dir)
        # 依次put每一个文件
        for x in all_files:
            filename = os.path.split(x)[-1]
            remote_filename = remote_dir + '/' + filename
            print(u'Put文件%s传输中...' % filename)
            sftp.put(x, remote_filename)

if __name__ == '__main__':
    remote_path = r'/home/sea'
    local_path = r'E:\PythonFiles\Learn\testsftp'
    host = SFTP('192.168.11.6', 'root', 'youshiker')
    host.sftp_put_dir(remote_path, local_path)
