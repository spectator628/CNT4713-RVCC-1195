#this code was written by brandon lee with the help of ruben Balmaceda
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

PORT_NUMBER = 8080

#this class will handle any incoming requests from the browser

class myHandler(BaseHTTPRequestHandler):
    #handler for get requests
    def do_GET(self):
        if self.path=="/":
            self.path="/index_examples2.html"

        try:
            #check the file extension and correct mime type

            sendReply = False
            #recieving and playing video mp4 format files
            if self.path.endswith(".mp4"):
                mimetype='video/mp4'
                sendReply = True

            #recieving and playing audio files in mp4 format
            if self.path.endswith(".m4a"):
                mimetype='audio/m4a'
                sendReply = True
            
            if sendReply == True:
                #open the static file request and send it
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('content-type',mimetype)
                seld.end_headers()
                self.wfile.write(f.read())
                f.close()
            return

        except IOError:
            sled.send_error(404, 'File not found: %s'self.path)
try:
    #Create a web server and define the hanbdler to manage the imcoming requests
    server = HTTPServer (('', PORT_NUMBER), myHandler)
    print 'Started httpserver on port', PORT_NUMBER

    #wait forever for imconing htto requests
    server.server_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()