import asyncio
import bisect

from collections import defaultdict


def run_server(host, port):  
    loop = asyncio.get_event_loop()

    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


class Storage:
    def __init__(self):
        self._data = defaultdict(dict)

    def put(self, key, value, timestamp):
        self._data[key][timestamp] = value

    def get(self):
        return self._data
    
class ClientServerProtocol(asyncio.Protocol):  
    storage = Storage()   
    
    def __init__(self):
        super().__init__()
        
    def put(self, data):
        try:
            key, value, timestamp = data.split()
            
            self.storage.put(key, float(value), int(timestamp));
            
            return "ok\n\n"
        except:
            return "error\nwrong command\n\n"

    def get(self, data):
        line_answer = 'ok\n' 
        
        if len(data.split()) > 1:
            return "error\nwrong command\n\n"
        
        try: 
            value = data.strip() 
            if value == "*":
                for key, value in self.storage.get().items() :
                    for time, val in value.items():
                        line_answer += key + ' ' + str(val) +' ' + str(time) +'\n'
                return line_answer + '\n'
        

            if value not in self.storage.get():
                return line_answer + '\n'
                
            for time, val in self.storage.get()[value].items():
                line_answer += value + ' ' + str(val) +' ' + str(time) +'\n'
                    
            return line_answer + '\n'
                
        except:
            return "error\nwrong command\n\n"
    
    def process_data(self, data):        
        if data.startswith('put') is False and data.startswith('get') is False:
            return "error\nwrong command\n\n"
        
        if data.endswith('\n') is False:
            return "error\nwrong command\n\n"
        
        command, payload = data.split(' ', 1)
         
        if command == 'put':
            return self.put(payload)
         
        if command == 'get':
            return self.get(payload)
            
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):  
        resp = ''      
        if data == b'get\n' or data == b'get  \n':
            resp = "error\nwrong command\n\n"
        else :
            resp = self.process_data(data.decode())  
                
        self.transport.write(resp.encode())
        
       
# def main():
#     run_server('127.0.0.1', 8888)
# main()
