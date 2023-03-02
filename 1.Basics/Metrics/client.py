import socket
import time
import json

class ClientError(Exception):
    pass

class Client:
    socket_ = None
    
    def __init__(self, host, port, timeout = None):
        self.host = host;
        self.port = port
        self.timeout = timeout
        
        self.socket_ = socket.create_connection((self.host, self.port))
        self.socket_.settimeout(self.timeout)
        
        
    #<команда> <данные запроса><\n>
    def put(self, metric, value, timestamp = int(time.time())):
        line_ = metric + " " + str(value) + " " +  str(timestamp) + '\n'
        try:
            self.socket_.sendall(line_.encode("utf8"))
        except:
            raise ClientError
        
    def get(self, metric):
        line_ = str(metric) + '\n'
        try:
            self.socket_.sendall(line_.encode("utf8"))
            data = self.socket_.recv(1024);
        except:
            raise ClientError
        print(data)
        return data.decode()
    
    def __del__(self):
        if not self.socket_ is None:
            self.socket_.close()
        
        

def main():
    client = Client("127.0.0.1", 8888, timeout=15)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)
    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)
    print(client.get("*"))
main()