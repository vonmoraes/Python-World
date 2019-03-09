# -*- coding: utf-8 -*-
"""
Imports
"""
from chat_funcoes import *
import json 
import sys
import os
import subprocess as subp

"""
O Básico do chatbot:
 Escuta
 Pensa
 Fala
"""
class Chatbot():
    """
    TODO: 
        * Melhorar os comentários
        * Colocar dicionário no json
    
    """
    def __init__(self,nome_chatbot):
        self.nome_chatbot = nome_chatbot
        self.nome_pessoa = "null"
        self.database_name = nome_chatbot + '.json'
        try:
            """
            try: Verifica a existencia do banco json
            except: Cria o banco caso não exista 
                    Adiciona uma pequena lista de nomes conhecidos
            """
            database = open(self.database_name, 'r+') # Abrir o banco para leitura
        except FileNotFoundError:
            database = open(self.database_name, 'w+')
            database.write('["Lucas","Moraes"]')
            database.close()
            database = open(self.database_name, 'r+')
        pass
        self.nomes_conhecidos = json.load(database)
        database.close()
        self.historico = []
        self.dicionario = {"oi":"Olá, qual o seu nome?",
        "sair":"sair"}
    pass
    """
    ####################
    """
    def escutar(self):
        return readString()
    pass
    """
    ####################
    """
    def pensar(self,frase_lida):
        #
        frase_lida = normalizar_frase(frase_lida)
        # Verifica se já foi respondido isso antes
        if(frase_lida in self.dicionario):
            return self.dicionario[frase_lida]
        #
        elif frase_lida == "aprender":
            keyword = readString("O que eu deveria aprender? \n>>: ")
            aws = readString("Qual a resposta disto? \n>>: ")
            self.dicionario[normalizar_frase(keyword)] = aws
            return "Aprendido!"
        #
        elif self.historico[-1] == "Olá, qual o seu nome?":
            self.nome_pessoa = self.ler_Nome(frase_lida)
            self.verificar_nome_conhecido(self.nome_pessoa)
            return "None"
        #
        elif (frase_lida == "historico"):
            print(self.historico)
            return "Mostrando Histórico"
        pass
        # Execultando código diretamente no bot
        """
        A função eval executa códigos de python
        """
        try:
            return(eval(frase_lida))
        except:
            pass
        return "Não entendi o que quer dizer :/"
    pass
    """
    ####################
    """
    def ler_Nome(self,nome_pessoa):
        if('o meu nome e ' in nome_pessoa):
            nome_pessoa = nome_pessoa[13:]
        pass
        self.inserir_no_historico(nome_pessoa.title())
        return nome_pessoa.title() # Capitalizacao do nome
    pass
    """
    ####################
    """
    def verificar_nome_conhecido(self,nome_pessoa):
        if (nome_pessoa in self.nomes_conhecidos):
            print(self.inserir_no_historico("Fala %s! Precisando de algo só falar" %nome_pessoa))
        else:
            print(self.inserir_no_historico("Muito prazer %s" %nome_pessoa))
            self.nomes_conhecidos.append(nome_pessoa)
            database = open(self.database_name, 'w+') # Abrir o banco para escrita
            # Salvar lista de conhecidos no database
            json.dump(self.nomes_conhecidos,database)
            database.close()
        pass
    pass
    """
    ####################
    """
    def fala(self,frase_lida):
        frase_lida = str(frase_lida)
        if frase_lida != "None":
            # Execultando comandos no bot
            """
            Execultando comandos do terminal no bot
            TODO: Não está funcionando até então
            """
            if ("executa " in frase_lida):
                plataforma_os = sys.platform
                comando = frase_lida.replace("executa ","")
                if "win" in plataforma_os:
                    os.startfile(comando)
                pass
                if "linux" in plataforma_os:
                    try:
                        subp.Popen(comando)
                    except FileNotFoundError:
                        subp.Popen(['xdg-open',comando])
                pass
            pass
            print(frase_lida)
            self.inserir_no_historico(frase_lida)
        pass
    pass
    """
    ####################
    """
    def inserir_no_historico(self,insercao):
        self.historico.append(insercao)
        return insercao
    pass
pass