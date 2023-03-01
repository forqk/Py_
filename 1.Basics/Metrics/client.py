import socket
import time

class Client:
    socket_ = None
    
    def __init__(self, host, port, timeout = None):
        self.host = host;
        self.port = port
        self.timeout = timeout
        self.CreateConnection()
        
    def CreateConnection(self):
        self.socket_ = socket.create_connection((self.host, self.port))
        
    #<команда> <данные запроса><\n>
    def put(self, command, date, timestamp = int(time.time())):
        line_ = command + " " + str(date) + " " +  str(timestamp) + '\n'
        self.socket_.sendall(line_.encode("utf8"))
        

def main():
    client = Client("127.0.0.1", 8888, timeout=15)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)
    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)
main()