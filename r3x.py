from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer

def execute(r3xFunc):
    class RubiXServer(BaseHTTPRequestHandler):        
        def do_POST(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(r3xFunc())
        
    def run(server_class=HTTPServer, handler_class=RubiXServer, port=8080):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print 'Starting httpd...'
        httpd.serve_forever()

    r3xFunc()
    run()

