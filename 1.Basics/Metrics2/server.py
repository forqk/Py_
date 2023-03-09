import asyncio
import bisect

    
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


class ClientServerProtocol(asyncio.Protocol): 
    data_ = {}
    _buff = b''
    
    def process_data(self, data):        
        if data.startswith('put') is False and data.startswith('get') is False:
            return "error\nwrong command\n\n"
    
        if data.startswith('put'): #key, value, timestamp
            data = data[4::]
            try:
                key, value, timestamp = data.split()
                if key not in self.data_:
                     self.data_[key] = []
                          
                for i in range(len(self.data_[key])):
                    if self.data_[key][i][1] == int(timestamp):
                        self.data_[key].pop(i)
                        
                self.data_[key].append((float(value), int(timestamp))) 
                              
                return "ok\n\n"
            except:
                return "error\nwrong command\n\n"
            
        for key, value in self.data_.items():
            value.sort(key=lambda x: x[1])
        
        if data.startswith('get'): 
            line_answer = 'ok\n' 
            try: 
                key, value = data.split()            
                if value == "*": 
                    for key, value in self.data_.items():
                        for val in value:
                            line_answer += key + ' ' + str(val[0]) +' ' + str(val[1]) +'\n'
                    return line_answer + '\n'

                if value not in self.data_:
                    return line_answer + '\n'
                
                for val in self.data_[value]:
                    line_answer += value + ' ' + str(val[0]) +' ' + str(val[1]) + '\n'
                    
                return line_answer + '\n'
                
            except:
                return "error\nwrong command\n\n"
                
            
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self._buff += data
        
        
        request = self._buff.decode()
        
    
        if request.endswith('\n') is False:
            return
        
     #   print('request', request)    
        resp = self.process_data(request)  
     #   print('resp', resp)    
        self.transport.write(resp.encode())
        
        self._buff = b''
        


# def main():
#     run_server('127.0.0.1', 8888)
    
# main()

