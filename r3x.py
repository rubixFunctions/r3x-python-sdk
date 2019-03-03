from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os
import logging

PORT = os.environ.get("PORT", None)

def execute(r3xFunc):
    if PORT == None:
        print("PORT environment variable was not set, r3x exit")
        return

    class RubiXServer(BaseHTTPRequestHandler):        
        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(r3xFunc())
        
    def run(server_class=HTTPServer, handler_class=RubiXServer, port=int(PORT)):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print 'Starting httpd...'
        httpd.serve_forever()

    r3xFunc()
    run()

