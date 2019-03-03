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
        def _set_headers(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

        def _set_header_error_header(self):
            self.send_response(400)
            self.end_headers()
            self.wfile.write("Wrong Header Set, Request Body Needs to be JSON")

        def _set_error_header(self):
            self.send_response(400)
            self.end_headers()
        
        def do_HEAD(self):
            self._set_headers()

        def do_POST(self):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
            
            if ctype != 'application/json':
                self._set_header_error_header()
                return

            length = int(self.headers.getheader('content-length'))
         
            self._set_headers()
            self.wfile.write(r3xFunc(json_handler(length, self.rfile.read(length))))
    
    def json_handler(length, body):
        if length > 0:
            return json.dumps(json.loads(body))
        else:
            res = {'rubix' : 'no request body found'}
            json_res = json.dumps(res)
            return json_res
        
        
    def run(server_class=HTTPServer, handler_class=RubiXServer, port=int(PORT)):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print 'Starting httpd...on port {}'.format(PORT)
        httpd.serve_forever()

    run()

