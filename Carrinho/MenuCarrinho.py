from tabulate import tabulate
from Carrinho.Carrinho import *
from Verificacoes import VerificaCarrinho, VerificaProduto
import os

#FUNÇÃO DO MENU PARA MANIPULAÇÃO DO CARRINHO
def InfoCarrinho(conexao, cur, id_cliente):
    escolha = 1
    while(escolha != 0):
        os.system('clear')
        print("-> Informações do Carrinho <-\n")
        print("0. Voltar")
        print("1. Visualizar Carrinho")
        print("2. Adicionar Produto")
        print("3. Remover Produto")

        escolha = int(input("\nDigite sua escolha: "))
        if(escolha == 1):
            os.system('clear')
            print("-> Visualizar Carrinho <-")

            resultado = LerCarrinho(cur, id_cliente)
            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            total = TotalCarrinho(cur, id_cliente)

            if(total != None):
                print("Total = R$", total)
            else:
                print("Total = R$ 0")

            input("\nPressione ENTER para voltar.")

        if(escolha == 2):
            os.system('clear')
            print("-> Adicionar Produto <-\n")
            id_produto = input("Digite o ID do Produto: ")
            quantidade = input("Digite a Quantidade: ")

            if(int(quantidade) <= 0):
                print("\nERRO: A quantidade deve ser um número maior que 0!")
                input("Pressione ENTER para voltar.")
                return

            verifica = VerificaProduto(cur, id_produto)
            if(verifica == 0):
                sql = ("INSERT INTO CARRINHO VALUES (null, %s, %s, null, %s)")
                data = (id_cliente, id_produto, quantidade)

                cur.execute(sql, data)
                conexao.commit()

                print("\nAdicionado com sucesso!")
                input("Pressione ENTER para voltar.")
            elif(verifica == -1):
                print("\nERRO: ID de produto não existente!")
                input("Pressione ENTER para voltar.")

        if(escolha == 3):
            os.system('clear')
            print("-> Remover Produto <-\n")
            id_produto = input("Digite o ID do Produto: ")

            if(VerificaCarrinho(cur, id_cliente, id_produto) == 0):

                sql = ("DELETE FROM CARRINHO WHERE PRODUTO_ID = %s AND PEDIDO_ID IS NULL")
            
                cur.execute(sql, [id_produto])
                conexao.commit()

                print("\nRemovido com sucesso!")
                input("Pressione ENTER para voltar.")

            elif(VerificaCarrinho(cur, id_cliente, id_produto == -1)):
                print("\nERRO: Produto não está no carrinho!")
                input("Pressione ENTER para voltar.")