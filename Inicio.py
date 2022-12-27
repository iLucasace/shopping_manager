import mysql.connector as mysql
from Cliente.InicioCliente import *
from Funcionário.InicioFunc import *
import os

#INICIA A CONEXÃO COM O BANCO DE DADOS
#LEIA O README.txt
conexao = mysql.connect( 
        host="lucasace-Aspire5",
        user="root",
        password="lACE1311",
        database="SISTEMA_LOJA"
)
cur = conexao.cursor()

#MENU PARA ESCOLHA ENTRE CLIENTE E FUNCIONÁRIO
escolha_inicial = 1
while(escolha_inicial != 0):
    os.system('clear')
    print("-> Sistema de Gerenciamento de Compras <-\n")
    print("0. Sair")
    print("1. Cliente Web")
    print("2. Funcionário")
        
    escolha_inicial = int(input("\nDigite sua escolha: "))
    if(escolha_inicial == 1):
        ClienteWeb(conexao, cur) #CHAMA A FUNÇÃO DO MENU DO CLIENTE
            
    if(escolha_inicial == 2):
        Funcionario(conexao, cur) #CHAMA A FUNÇÃO DO MENU DO FUNCIONÁRIO

#ENCERRA A CONEXÃO COM O BANCO DE DADOS 
cur.close()
conexao.close()