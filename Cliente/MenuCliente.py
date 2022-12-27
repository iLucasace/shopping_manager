from Manipulacoes import ler
from Carrinho.MenuCarrinho import *
from Carrinho.Carrinho import *
from Pedidos.VerPedidos import VerPedidos
from Pedidos.Comprar import RealizarCompra
import os

#FUNÇÃO DO MENU PARA OS CLIENTES
def MenuCliente(conexao, cur, id_cliente, username):
    escolha = 1
    while(escolha != 0):
        os.system('clear')
        print("-> Menu do Cliente Web <-\n")
        print("Usuário:", username,"\n")
        print("0. Voltar")
        print("1. Visualizar Produtos")
        print("2. Informações Carrinho")
        print("3. Verificar Pedidos")
        print("4. Realizar Pedido")

        escolha = int(input("\nDigite sua escolha: "))
        if(escolha == 1):
            os.system('clear')
            print("-> Visualizar Produtos <-")

            ler(cur, "PRODUTO")
            
            print("Anote os IDs dos produtos que deseja adicionar ao carrinho.")
            input("Pressione ENTER para voltar.")

        if(escolha == 2):
            InfoCarrinho(conexao, cur, id_cliente)

        if(escolha == 3):
            os.system('clear')
            print("-> Verificar Pedidos <-")
            
            VerPedidos(cur, id_cliente)
            input("Pressione ENTER para voltar.")
            
        if(escolha == 4):
            os.system('clear')
            print("-> Realizar Pedido <-")

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