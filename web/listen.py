#!/usr/local/bin/python
from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

class SimpleEcho(WebSocket):

    def handleMessage(self):
        # echo message to stdout / back to client
        print(self.data, flush=True)
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('0.0.0.0', 8000, SimpleEcho)
server.serveforever()
