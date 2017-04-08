import socket, sys
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

host = ''
port = 8888

try:
    s.bind((host, port))
except socket.error as msg:
    print('Bind faild. Error code: ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()
print('Socket bind complete')

s.listen(10)
print('Socket now listening')

def clientthread(conn):
    conn.send('Welcom to the server. Type something and hit enter\n')

    while 1:
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break

        conn.sendall(reply)
    conn.close()

while 1:
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
s.close()
