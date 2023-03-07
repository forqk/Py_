import asyncio
import bisect

    

class ClientServerProtocol(asyncio.Protocol): 
    data_ = {}
    
    def process_data(self, data):
        if data.startswith('put') is False or data.startswith('get') is False:
            return "error\nwrong command\n\n"
    
        if data.startswith('put'): #key, value, timestamp
            data = data[4::]
            try:
                key, value, timestamp = data.split()
                if key not in self.data_:
                    self.data_[key] = []
                self.data_[key].append((float(value), int(timestamp)))
                return "ok\n\n"
            except:
                print('pls')
                return "error\nwrong command\n\n"
     
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())
        


loop = asyncio.get_event_loop()

coro = loop.create_server(
    ClientServerProtocol,
    '127.0.0.1', 8888
)

server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
