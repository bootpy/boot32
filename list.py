#!/bin/python3

#Trabalhando com listas

cursos = ["Ethical Hacking","Network Enginner","Help Desk Enginner","Exploit Development"]
x = len(cursos)
print("Tamanho do array: "+str(x))
print(cursos)

print(cursos[1])
print(cursos[1:3]) #irar imprimir valor entre a posicao 1-2

for x in cursos:
	print(x)
	
	
print("####################################################")

cursos.append("other value")

print(cursos)

cursos.pop(4)
print(cursos)
