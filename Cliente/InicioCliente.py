from Cliente.LoginCadastro import *
import os

#FUNÇÃO DO MENU PARA LOGIN OU CADASTRO
def ClienteWeb(conexao, cur):
    escolha_cliente = 1
    while(escolha_cliente != 0):
        os.system('clear')
        print("-> Cliente Web <-\n")
        print("0. Voltar")
        print("1. Cadastro")
        print("2. Login")
        
        escolha_cliente = int(input("\nDigite sua escolha: "))
        if(escolha_cliente == 1):
            Cadastro(conexao, cur)
        if(escolha_cliente == 2):
            Login(conexao, cur)