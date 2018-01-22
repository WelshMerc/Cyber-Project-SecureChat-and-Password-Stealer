# Ian Casker
# Last Edited 9/25/2017

import random
import truffle_shuffle
import ast
import logs

def message_input():
    message = input('\t -> ')
    return message

def message_input_without_password():
    message = input('\t Please enter in the server password here -> ')
    return message

def welcome_to_server():
    message = 'Congrats your authorized'
    return message

def message_input_decimal(message):
    decimal_list = []
    for i in message:
        decimal_list.append(ord(i))
    return decimal_list


def one_time_pad_creator(decimal_list):
    one_time_pad = []
    new_num_list = []
    for i in decimal_list:
        otp_num = random.randint(0, i)
        new_num = i - otp_num
        one_time_pad.append(otp_num)
        new_num_list.append(new_num)
    return one_time_pad, new_num_list


def new_message_thing(new_num):
    new_message = ''
    for i in new_num:
        new_message = new_message + chr(i)
    return new_message

def final_message(new_message, otp):
    combined_list = truffle_shuffle.combination(list(new_message), list(otp))
    return combined_list

def message_unscrambler(combined_list, message, otp):
    truffle_shuffle(combined_list, message, otp)
    return message, otp

def un_one_time_pad(one_time_pad, new_message):
    old_message = ''
    i = 0
    while i <= len(new_message) - 1:
        new_decimal = one_time_pad[i] + ord(new_message[i])
        old_message = old_message + chr(new_decimal)
        i = i + 1
    return old_message

"""
# This code below is an example of the things
message = message_input()
print(message)
decimal_message = message_input_decimal(message)
print(decimal_message)
one_time_pad, new_num = one_time_pad_creator(decimal_message)
new_message = new_message_thing(new_num)
old_message = un_one_time_pad(one_time_pad, new_message)
print(old_message)
"""

"""
def everything():
    message = message_input()
    decimal_message = message_input_decimal(message)
    one_time_pad, new_num = one_time_pad_creator(decimal_message)
    new_message = new_message_thing(new_num)
    message_list = list(new_message)
    super_message = truffle_shuffle.combination(message_list, one_time_pad)
    super_message = str(super_message)
    return super_message

def everything_without_password_server():
    message = 'SERVER MESSAGE: INCORRECT PASSWORD'
    decimal_message = message_input_decimal(message)
    one_time_pad, new_num = one_time_pad_creator(decimal_message)
    new_message = new_message_thing(new_num)
    message_list = list(new_message)
    super_message = truffle_shuffle.combination(message_list, one_time_pad)
    super_message = str(super_message)
    return super_message

def everything_without_password():
    message = message_input_without_password()
    decimal_message = message_input_decimal(message)
    one_time_pad, new_num = one_time_pad_creator(decimal_message)
    new_message = new_message_thing(new_num)
    message_list = list(new_message)
    super_message = truffle_shuffle.combination(message_list, one_time_pad)
    super_message = str(super_message)
    return super_message

def everything_congrats():
    message = welcome_to_server()
    decimal_message = message_input_decimal(message)
    one_time_pad, new_num = one_time_pad_creator(decimal_message)
    new_message = new_message_thing(new_num)
    message_list = list(new_message)
    super_message = truffle_shuffle.combination(message_list, one_time_pad)
    super_message = str(super_message)
    return super_message

def m8_ur_blacklisted():
    message = 'M8 ur blacklisted for trying to break into this chat. Like go fuggity fuck urself'
    decimal_message = message_input_decimal(message)
    one_time_pad, new_num = one_time_pad_creator(decimal_message)
    new_message = new_message_thing(new_num)
    message_list = list(new_message)
    super_message = truffle_shuffle.combination(message_list, one_time_pad)
    super_message = str(super_message)
    return super_message

"""

def fixed(num):
    global message
    if num == 0: message = message_input()
    if num == 1: message = 'SERVER MESSAGE: INCORRECT PASSWORD'
    if num == 2: message = message_input_without_password()
    if num == 3: message = welcome_to_server()
    if num == 4: message = 'Blacklisted'
    logs.writer('From Host: ' + message)
    decimal_message = message_input_decimal(message)
    one_time_pad, new_num = one_time_pad_creator(decimal_message)
    new_message = new_message_thing(new_num)
    message_list = list(new_message)
    super_message = truffle_shuffle.combination(message_list, one_time_pad)
    super_message = str(super_message)
    return super_message

def message_confirmed():
    message = 'Confirmed'
    decimal_message = message_input_decimal(message)
    one_time_pad, new_num = one_time_pad_creator(decimal_message)
    new_message = new_message_thing(new_num)
    message_list = list(new_message)
    super_message = truffle_shuffle.combination(message_list, one_time_pad)
    super_message = str(super_message)
    return super_message

def virus_message(mess):
    message = mess
    decimal_message = message_input_decimal(message)
    one_time_pad, new_num = one_time_pad_creator(decimal_message)
    new_message = new_message_thing(new_num)
    message_list = list(new_message)
    super_message = truffle_shuffle.combination(message_list, one_time_pad)
    super_message = str(super_message)
    return super_message

def decoding_el_message(message):
    message = ast.literal_eval(message)
    encoded_message = []
    otp = []
    truffle_shuffle.splitter(message, encoded_message, otp)
    original_message = un_one_time_pad(otp, encoded_message)
    original_message = original_message[1:]
    logs.writer('From Other Machine: ' + original_message)
    return original_message
