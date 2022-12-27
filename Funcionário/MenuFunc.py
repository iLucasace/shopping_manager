from Manipulacoes import *
from Carrinho.MenuCarrinho import *
from Carrinho.Carrinho import *
from Pedidos.VerPedidos import VerPedidos
from Pedidos.Comprar import RealizarCompra
import os

#FUNÇÃO DO MENU PARA MANIPULAÇÃO DOS CLIENTES
def ManipulacaoCliente(conexao, cur):
    escolha = 1
    while(escolha != 0):
        os.system('clear')
        print("-> Informações dos Clientes <-\n")
        print("0. Voltar")
        print("1. Visualizar Clientes")
        print("2. Cadastrar Clientes")
        print("3. Remover Clientes")
        print("4. Atualizar Clientes")
        
        escolha = int(input("\nDigite sua escolha: "))
        if(escolha == 1):
            os.system('clear')
            print("-> Visualizar Clientes <-")
            ler(cur, "CLIENTE")
            input("Pressione ENTER para voltar.")
            
        if(escolha == 2):
            os.system('clear')
            print("-> Cadastrar Clientes <-")
            criar(conexao, cur, "CLIENTE")
            
        if(escolha == 3):
            os.system('clear')
            print("-> Remover Clientes <-")
            deletar(conexao, cur, "CLIENTE")
            
        if(escolha == 4):
            os.system('clear')
            print("-> Atualizar Clientes <-")
            alterar(conexao, cur, "CLIENTE")

#FUNÇÃO DO MENU PARA MANIPULAÇÃO DOS PRODUTOS   
def ManipulacaoProduto(conexao, cur):
    escolha = 1
    while(escolha != 0):
        os.system('clear')
        print("-> Informações dos Produtos <-\n")
        print("0. Voltar")
        print("1. Visualizar Produtos")
        print("2. Cadastrar Produtos")
        print("3. Remover Produtos")
        print("4. Atualizar Produtos")
        
        escolha = int(input("\nDigite sua escolha: "))
        if(escolha == 1):
            os.system('clear')
            print("-> Visualizar Produtos <-")
            ler(cur, "PRODUTO")
            input("Pressione ENTER para voltar.")
            
        if(escolha == 2):
            os.system('clear')
            print("-> Cadastrar Produtos <-")
            criar(conexao, cur, "PRODUTO")
            
        if(escolha == 3):
            os.system('clear')
            print("-> Remover Produtos <-")
            deletar(conexao, cur, "PRODUTO")
            
        if(escolha == 4):
            os.system('clear')
            print("-> Atualizar Produtos <-")
            alterar(conexao, cur, "PRODUTO")

#FUNÇÃO PARA MANIPULAÇÃO DOS CARRINHOS
def ManipulacaoCarrinho(conexao, cur, cpf_cliente):
    os.system('clear')
    print("-> Informações do Carrinho <-\n")

    cur.execute("SELECT TIPO FROM CLIENTE WHERE CPF = '"+cpf_cliente+"'")
    for linha in cur.fetchall(): #...
        tipo_cliente = linha[0]    # TRANSFORMA ID_CLIENTE EM STRING

    if(tipo_cliente != "Cliente Web"):
        cur.execute("SELECT ID FROM CLIENTE WHERE CPF = '"+cpf_cliente+"'")
        for linha in cur.fetchall(): #...
            id_cliente = linha[0]    # TRANSFORMA ID_CLIENTE EM STRING
        
        InfoCarrinho(conexao, cur, id_cliente)

    else:
        print("ERRO: O cliente é do tipo web!")
        input("Pressione ENTER para voltar.")

#FUNÇÃO DO MENU PARA MANIPULAÇÃO DAS COMPRAS
def ManipulacaoCompra(conexao, cur, cpf_cliente):
    os.system('clear')
    print("-> Informações dos Pedidos <-\n")

    cur.execute("SELECT ID FROM CLIENTE WHERE CPF = '"+cpf_cliente+"'")
    for linha in cur.fetchall(): #...
        id_cliente = linha[0]    # TRANSFORMA ID_CLIENTE EM STRING
    
    escolha = 1
    while(escolha != 0):
        os.system('clear')
        print("-> Informações dos Pedidos <-\n")
        print("0. Voltar")
        print("1. Visualizar Pedidos")
        print("2. Cadastrar Pedido")

        escolha = int(input("\nDigite sua escolha: "))
        if(escolha == 1):
            os.system('clear')
            print("-> Visualizar Pedidos <-\n")

            VerPedidos(cur, id_cliente)
            input("Pressione ENTER para voltar.")

        if(escolha == 2):
            cur.execute("SELECT TIPO FROM CLIENTE WHERE CPF = '"+cpf_cliente+"'")
            for linha in cur.fetchall(): #...
                tipo_cliente = linha[0]    # TRANSFORMA ID_CLIENTE EM STRING

            if(tipo_cliente != "Cliente Web"):
                carrinho = LerCarrinho(cur, id_cliente)
                print('\n', tabulate(carrinho, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
                total = TotalCarrinho(cur, id_cliente)

                if(total != None):
                    print("Total = R$", total)
                    escolha_pedido = 1
                    while(escolha_pedido != 0):
                        print("\nDeseja confirmar a compra?")
                        print("0. Não")
                        print("1. Sim")
            
                        escolha_pedido = int(input("\nDigite sua escolha: "))
                        if(escolha_pedido == 1):
                            RealizarCompra(conexao, cur, id_cliente)

                            print("\nComprado!")
                            input("Pressione ENTER para voltar.")
                            escolha_pedido = 0
                else:
                    print("ERRO: Carrinho não possui produtos!")
                    input("Pressione ENTER para voltar.")

            else:
                print("\nERRO: O cliente é do tipo web!")
                input("Pressione ENTER para voltar.")