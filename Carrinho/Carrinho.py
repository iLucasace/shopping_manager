#FUNÇÃO PRA VER OS ITENS EM UM CARRINHO
def LerCarrinho(cur, id_cliente):
    sql = ('''  SELECT P.ID, NOME, VALOR, DESCRICAO, QUANTIDADE
                FROM CARRINHO C
                INNER JOIN PRODUTO P
                ON C.PRODUTO_ID = P.ID
                WHERE PEDIDO_ID is NULL 
                AND CLIENTE_ID = %s''')
            
    cur.execute(sql, [id_cliente]) 
    resultado = cur.fetchall()
    
    return resultado

#FUNÇÃO PARA VER O VALOR TOTAL DE UM CARRINHO
def TotalCarrinho(cur, id_cliente):
    sql = ('''  SELECT sum(VALOR * QUANTIDADE) as TOTAL
                FROM CARRINHO C
                INNER JOIN PRODUTO P
                ON C.PRODUTO_ID = P.ID
                WHERE PEDIDO_ID is null
                AND CLIENTE_ID = %s''')
    data = (id_cliente,)

    cur.execute(sql, data)
    for lista in cur.fetchall():
        return lista[0]