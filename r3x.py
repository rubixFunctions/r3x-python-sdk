from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import os
import logging
import cgi
import json

PORT = os.environ.get("PORT", None)

def execute(r3xFunc):
    if PORT == None:
        print("PORT environment variable was not set, r3x exit")
        return

    class RubiXServer(BaseHTTPRequestHandler):        
        def do_POST(self):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()
                return

            length = int(self.headers.getheader('content-length'))
            
            if length > 0:
                message = json.dumps(json.loads(self.rfile.read(length)))
            else:
                res = {'rubix' : 'no request body found'}
                json_res = json.dumps(res)
                message = json_res
                
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(r3xFunc(message))
        
    def run(server_class=HTTPServer, handler_class=RubiXServer, port=int(PORT)):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print 'Starting httpd...'
        httpd.serve_forever()

    run()

