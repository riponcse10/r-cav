import socket
from yolo_model import YOLOv3
import time

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

yolo = YOLOv3()
model = yolo.load()
q = []

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	conn, addr = s.accept()
	print('Connected by', addr)
	start_time = time.time()
	with conn:
		fname = '000.png'
		#data = s.recv(1024)
		fp = open(fname,'wb')
		while True:
			strng = conn.recv(1024)
			if not strng:
				break
			fp.write(strng)
    
		fp.close()
		q.append(fname)
		
		yolo.calculate(model, q.pop(0))
		
	end_time = time.time()
	print(end_time-start_time)

#class Server:
#    def __init__(self):