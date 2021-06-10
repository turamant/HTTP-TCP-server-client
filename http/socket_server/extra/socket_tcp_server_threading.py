import socketserver



class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        data = self.request.recv(1024).strip()
        print('Adsress: {}'.format(self.client_address[0]))
        print("Data: {}".format(data.decode()))
        self.request.sendall(data)

if __name__=='__main__':
    with ThreadingTCPServer(('', 8888), EchoTCPHandler) as server:
        server.serve_forever()