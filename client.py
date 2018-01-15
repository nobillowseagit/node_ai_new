import sys
import operator
import struct
import socket

ip_port = ('127.0.0.1',9000);
BUFSIZE = 1024;
msg = 'start';

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
s.connect_ex(ip_port);  #拨电话
while True:
	#新增通信循环,客户端可以不断发收消息
	msg = input('>>:').strip();
	print(msg);
	print(len(msg));
	if len(msg) == 0:
		continue;
	if msg == 'exit1':
		break;

	print("send start");
	s.send(msg.encode('utf-8'));  #发消息,说话(只能发送字节类型)
	print("send completed");
	
	feedback = s.recv(BUFSIZE);  #收消息,听话
	print(feedback.decode('utf-8'));
s.close();  #挂电话
sys.exit(1);

