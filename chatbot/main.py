# -*- coding: utf-8 -*-
"""
Inicio de chatbot
Primeiramente deve ler o nome e reconhecer o nome da pessoa
"""
"""
Imports
"""
from Chatbot import * # Separação das funcões principais do chatbot
from chat_funcoes import *
"""
Globais
"""
chatbot = Chatbot("Teste")
"""
##########
"""
def main():
    while True:
        frase = normalizar_frase(chatbot.escutar())
        resposta = chatbot.pensar(frase)
        if (frase == "sair"):
            break
        else:
            chatbot.fala(resposta)
        pass
    pass
    print("Até mais %s" %(chatbot.nome_pessoa))
pass
#
main()
print("...")