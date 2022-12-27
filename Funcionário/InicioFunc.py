from getpass import getpass
from Funcionário.MenuFunc import *
from Funcionário.Consultas import *
import os

#FUNÇÃO DO MENU PARA OS FUNCIONÁRIOS
def Funcionario(conexao, cur):
    os.system('clear') #LIMPA A TELA
    print("-> Funcionário <-\n")
    senha = getpass("Senha: ")
    escolha_funcionario = 1
    if(senha == "ADMIN"):
        while(escolha_funcionario != 0):
            os.system('clear')
            print("-> Funcionário <-\n")
            print("0. Voltar")
            print("1. Consultas")
            print("2. Informações Clientes")
            print("3. Informações Produtos")
            print("4. Informações Carrinhos")
            print("5. Informações Pedidos")

            escolha_funcionario = int(input("\nDigite sua escolha: "))
            if(escolha_funcionario == 1):
                Consulta(cur)
                
            if(escolha_funcionario == 2):
                ManipulacaoCliente(conexao, cur)
                 
            if(escolha_funcionario == 3):
                ManipulacaoProduto(conexao, cur)
            
            if(escolha_funcionario == 4):
                os.system('clear')
                print("-> Informações dos Carrinhos <-\n")

                print("Por favor, informe:\n")
                cpf_cliente = input("CPF do Cliente: ")
        
                if(VerificaCPF(cur, cpf_cliente) == 0):
                    ManipulacaoCarrinho(conexao, cur, cpf_cliente)

                else: 
                    print("\nERRO: CPF não cadastrado!")
                    input("Pressione ENTER para voltar.")
            
            if(escolha_funcionario == 5):
                os.system('clear')
                print("-> Informações dos Pedidos <-\n")

                print("Por favor, informe:\n")
                cpf_cliente = input("CPF do Cliente: ")
        
                if(VerificaCPF(cur, cpf_cliente) == 0):
                    ManipulacaoCompra(conexao, cur, cpf_cliente)

                else: 
                    print("\nERRO: CPF não cadastrado!")
                    input("Pressione ENTER para voltar.")

    else:
        print("\nSenha incorreta!")
        input("Pressione ENTER para voltar.")