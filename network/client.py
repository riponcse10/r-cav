
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
DATA_PATH = "../../kitti-data/training/image_2/000010.png"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	#s.sendall(b'Hello, world')
	img = open(DATA_PATH,'rb')
	while True:
	    strng = img.read(1024)
	    if not strng:
	        break
	    s.send(strng)
	img.close()

#print('Received', repr(data))


#class Client():
#    def __init__(self, service_client, host, port):
#        reactor.connectTCP(cfg.SERVER_HOST, cfg.SERVER_PORT,
#                           ClientProtocolFactory(service_client))

#    def run(self):
#        reactor.run()

#    def stop(self):
#       reactor.callFromThread(reactor.stop)
