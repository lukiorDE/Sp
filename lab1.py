import socket
import http.client
import uuid, re

print("Имя ПК: " + socket.gethostname())
conn=http.client.HTTPConnection("ifconfig.me")
conn.request("GET","/ip")
print("External IP: " + str(conn.getresponse().read()))

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('77.88.8.8', 80))
print("Ip ПК: " + s.getsockname()[0])
print("MAC-Адрес: "+":".join(re.findall('..', '%012x' % uuid.getnode())))