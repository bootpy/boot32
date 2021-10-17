#!/bin/python3

import socket

HOST = '127.0.0.1'
PORTA = 9292
#socket.socket = chamando a funcao socket dentro da importacao
#socket.AF_INET = dizendo que vai usar o ipv4
#socket.SOCK_STREAM = dizendoq ue ta usando o modo TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST,PORTA))
