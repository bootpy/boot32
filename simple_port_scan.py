#!/bin/python3

import socket
import sys

rHost = input("Insira o IP: ")
rHostIP = socket.gethostbyname(rHost)
rPosts = [80,53,22,80,22,111,139,443]

print("-" * 50)
print("Por favor espere, scanning em progresso... " + str(rHostIP))
print("-" * 50)

try:
    for ports in rPosts:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.1)

        resultado = s.connect_ex((rHost,ports)) #if a porta estiver aberta = 0, fechara = 1

        if resultado == 0:
            print("Porta {} aberta!".format(ports))

        s.close()
except KeyboardInterrupt:
    print("\nPrograma fechado pelo User")
    sys.exit()



# while ip <= 1000:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     socket.setdefaulttimeout(0.1)

#     resultado = s.connect_ex((rHost, ip))
#     print(ip)

#     if resultado == 0:
#         print("Porta {} esta aberta!!".format(ip))
    
#     s.close()
#     ip+=1
