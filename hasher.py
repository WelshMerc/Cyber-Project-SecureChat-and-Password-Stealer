import random

def salt_create():
    blank_string = ''
    salt_alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(16):
        blank_string = blank_string + random.choice(salt_alphabet)
    return blank_string

def add_to(message, salt):
    message = message + salt
    return message

def check_ip_for_pass(ip_address, ip_dict):
    if ip_address in ip_dict.keys() == True:
        ip_dict[ip_address] = ip_dict[ip_address] + 1
        if ip_dict[ip_address] > 3:
            print('{ip} may be attacking you. They have entered in {num} false passwords.'.format(ip=ip_address, num=ip_dict[ip_address]))
    elif ip_address in ip_dict.keys() == False:
        ip_dict[ip_address] = 1
