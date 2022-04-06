#获取SSH隧道功能
import paramiko
    def open_tunnel(self):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname='10.97.144.13', port=8822, username='nemuadmin', password='nsn.0371')