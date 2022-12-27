from Carrinho.Carrinho import TotalCarrinho
from tabulate import tabulate
import os

#FUNÇÃO PARA REALIZAR COMPRA DO CARRINHO DE DETERMINADO CLIENTE
def RealizarCompra(conexao, cur, id_cliente):
    total = TotalCarrinho(cur, id_cliente)
    sql = ("INSERT INTO PEDIDO (ID, DATA_PEDIDO, STATUS_PEDIDO, TOTAL) VALUES (null, NOW(), 'Em Processamento', %s)")

    cur.execute(sql, [total])
    conexao.commit()

    id_pedido = cur.lastrowid

    sql = ("UPDATE CARRINHO SET PEDIDO_ID = %s WHERE CLIENTE_ID = %s AND PEDIDO_ID IS NULL")
    data = (id_pedido, id_cliente)

    cur.execute(sql, data)
    conexao.commit()

    escolha_pagamento = 1
    while(escolha_pagamento != 0):
        os.system('clear')
        print("\nEscolha a(s) forma(s) de pagamento:")
        print("0. Finalizar")
        print("1. PIX")
        print("2. Boleto")
        print("3. Cartão de Crédito")
        print("4. Cartão de Débito")
        
        escolha_pagamento = int(input("\nDigite sua escolha: "))
        if(escolha_pagamento == 1):
            sql = ("INSERT INTO FORMA_PAGAMENTO VALUES (null, 'PIX', %s)")
            data = (id_pedido,)

            cur.execute(sql, data)
            conexao.commit()

        if(escolha_pagamento == 2):
            sql = ("INSERT INTO FORMA_PAGAMENTO VALUES (null, 'Boleto', %s)")
            data = (id_pedido,)

            cur.execute(sql, data)
            conexao.commit()

        if(escolha_pagamento == 3):
            sql = ("INSERT INTO FORMA_PAGAMENTO VALUES (null, 'Cartão de Crédito', %s)")
            data = (id_pedido,)

            cur.execute(sql, data)
            conexao.commit()

        if(escolha_pagamento == 4):
            sql = ("INSERT INTO FORMA_PAGAMENTO VALUES (null, 'Cartão de Débito', %s)")
            data = (id_pedido,)

            cur.execute(sql, data)
            conexao.commit()