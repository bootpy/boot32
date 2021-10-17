#!/bin/python3

#Trabalhando com funcoes

def quem_sou_eu():
	name = "Higor"
	idade = 21
	altura = 1.82
	
	print(name + " " + str(idade) + " " + str(altura))
	
print("Testing")

quem_sou_eu()

#Trabalhando com parametros

def myName(name):
	print("meu nome e" + name)
	
myName("Higor")

def dois_parametros(numero,name):
	print("meu nome e "+name+" e tenho "+ str(numero)+ " anos de idade")
	
dois_parametros(21, "Higor")
