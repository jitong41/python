import paramiko
import HSS_01



def get_combox_data(self):
    host_ip ="0.0.0.0"
    host_adm = {"HSS3": "10.91.134.84", "HSS4": "10.91.134.148", "HSS5": "10.91.136.212", "HSS6": "10.91.135.20",
                "ALL": ["10.91.134.84", "10.91.134.148", "10.91.136.212", "10.91.135.20"]}
    text = str(HSS_01.Ui_MainWindow.get_combox)
    host_ip = host_adm.get(text)
    return host_ip

def get_hss_data(self):
    h_ip = get_combox_data(self)
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(h_ip, port=22, username='sdfrun', password='sdfrun1', timeout=20)
    client.exec_command("ls -ltr")

def display_data():
