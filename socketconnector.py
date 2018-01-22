import socket
import GETIP
import securechat
import hasher
import logs

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
    ip_address_for_writer = 'The IP address of the server for authorization is ' + str(ip_display())
    logs.writer(ip_address_for_writer)
    server_pass = hasher.salt_create()
    print('The password for the server is ' + str(server_pass))
    password_for_writer = 'The password for the server is ' + str(server_pass)
    logs.writer(password_for_writer)
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print('Attempted authorization from: ' + str(addr))
    attempted_autho_for_writer = 'Attempted authorization from: ' + str(addr)
    logs.writer(attempted_autho_for_writer)
    ip_dict.append(addr)
    count = 0
    while True:
        data = conn.recv(1024).decode()
        attempted_password = securechat.decoding_el_message(str(data))
        if attempted_password != server_pass and count < 3:
            data = securechat.fixed(1)
            conn.send(data.encode())
            count += 1
        elif attempted_password == server_pass and count < 3:
            data = securechat.fixed(3)
            conn.send(data.encode())
            break
        else:
            data = securechat.fixed(4)
            conn.send(data.encode())
            print(str(addr) + ' is trying to hack you, maybe. It\'s count is ' + str(count))
            attempted_hack_for_writer = str(addr) + ' is trying to hack you, maybe. It\'s count is ' + str(count)
            logs.writer(attempted_hack_for_writer)
            conn.close()

    while True:
        data = conn.recv(1024).decode()
        message = securechat.decoding_el_message(data)
        if message == 'QUIT YOU MACHINE I NO WANT LOOP':
            break
        print(message)
        data = securechat.fixed(0)
        conn.send(data.encode())

    conn.close()


