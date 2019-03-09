# -*- coding: utf-8 -*-
"""
Inicio de chatbot
Primeiramente deve ler o nome e reconhecer o nome da pessoa
"""
print("Olá!")
print("Qual o seu nome?")
nome_pessoa = input(">>: ")
"""
Slice :: Para filtrar os nomes
"""
if('O meu nome é ' in nome_pessoa 
or 'o meu nome é ' in nome_pessoa):
    nome_pessoa = nome_pessoa[13:]
pass
#
if (nome_pessoa == "Moraes"):
    print("Coé %s cê tá bão?" %nome_pessoa)
else:
    print("Muito prazer %s" %nome_pessoa)
pass
#

#
print("...")