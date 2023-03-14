from http.server import HTTPServer, BaseHTTPRequestHandler
Host="169.254.152.45"
Port=100
class NafeaHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path='/index.html'
        try:
            with open(self.path[1:],'rb') as file:
                c=file.read()
            self.send_response(200)
            self.send_header('content-type','text/html')
            self.end_headers()
            self.wfile.write(c)
        except FileNotFoundError:
            self.send_error(404, 'File Not Found: {}'.format(self.path))

server1=HTTPServer((Host,Port),NafeaHTTP)
print("Server is now running")
server1.serve_forever()
server1.server_close()
print("server closed")
