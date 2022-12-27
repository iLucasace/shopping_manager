from tabulate import tabulate
import os

#FUNÇÃO PARA VER PEDIDOS DE DETERMINADO CLIENTE
def VerPedidos(cur, id_cliente):
    sql = ('''  SELECT DISTINCT PEDIDO_ID, DATA_PEDIDO, TOTAL AS TOTAL_R$
                FROM CARRINHO C
                INNER JOIN PEDIDO P
                ON C.PEDIDO_ID = P.ID
                WHERE CLIENTE_ID = %s''')

    cur.execute(sql, (id_cliente,))
    pedidos = cur.fetchall()

    print('\n', tabulate(pedidos, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    id_pedido = input("Digite o ID do pedido: ")
    for linhas in pedidos:
        if(int(id_pedido) == linhas[0]):
            os.system('clear')
            print("-> Verificar Pedidos <-")
            sql = ('''  SELECT NOME, DESCRICAO, QUANTIDADE, VALOR * QUANTIDADE AS VALOR, DATA_PEDIDO, STATUS_PEDIDO
                        FROM (  SELECT PEDIDO_ID, PRODUTO_ID, QUANTIDADE, DATA_PEDIDO, STATUS_PEDIDO
                                FROM CARRINHO C
                                INNER JOIN PEDIDO P
                                ON P.ID = C.PEDIDO_ID
                                WHERE CLIENTE_ID = %s
                                AND PEDIDO_ID = %s ) AS T1
                        INNER JOIN PRODUTO AS P
                        ON P.ID = T1.PRODUTO_ID
                        ORDER BY PEDIDO_ID ASC''')
            data = (id_cliente, id_pedido)

            cur.execute(sql, data)
            pedido = cur.fetchall()

            print('\n', tabulate(pedido, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            break
    else:
        print("\nERRO: Pedido não existente!")