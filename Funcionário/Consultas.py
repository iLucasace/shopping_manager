from Verificacoes import *
from Manipulacoes import ler
from tabulate import tabulate
import os

#FUNÇÃO COM TODAS AS CONSULTAS
def Consulta(cur):
    escolha_consulta = 1
    while(escolha_consulta != 0):
        os.system('clear')
        print("-> Consultas <-\n")
        print("0. Voltar")
        print("1. Todos os pedidos associados a uma conta.")
        print("2. Todos os produtos contidos em um determinado carrinho de compras.")
        print("3. Dados (e a quantidade) dos clientes cadastrados no sistema.")
        print("4. Forma de pagamento mais utilizada.")
        print("5. Filtrar usuários por Bairro, Cidade e Estado.")
        print("6. Média anual de vendas.")
        print("7. Mês e ano com maior número de vendas")
        print("8. Usuários que realizaram compras em todos os meses de um determinado ano.")
        print("9. Valor total gasto por um determinado cliente.")
        print("10. Total de ganhos com vendas em um determinado mês e ano.")

        escolha_consulta = int(input("\nDigite sua escolha: "))
        if(escolha_consulta == 1):
            os.system('clear')
            print("-> Todos os pedidos associados a uma conta <-\n")
            print("Por favor, informe:\n")
            cpf_cliente = input("CPF do Cliente: ")
        
            if(VerificaCPF(cur, cpf_cliente) == -1):
                print("\nERRO: CPF não cadastrado!")
                input("Pressione ENTER para voltar.")
                return

            sql = ('''  SELECT PEDIDO_ID, NOME, DESCRICAO, QUANTIDADE, VALOR * QUANTIDADE AS VALOR_TOTAL
                        FROM (  SELECT PEDIDO_ID, PRODUTO_ID, QUANTIDADE
                                FROM (  SELECT ID
                                        FROM CLIENTE
                                        WHERE CPF = %s ) AS T1
                                INNER JOIN CARRINHO AS C
                                ON C.CLIENTE_ID = T1.ID ) AS T2
                        INNER JOIN PRODUTO P
                        ON P.ID = T2.PRODUTO_ID
                        WHERE PEDIDO_ID IS NOT NULL
                        ORDER BY PEDIDO_ID ASC''')

            cur.execute(sql, [cpf_cliente])
            resultado = cur.fetchall()

            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")

        if(escolha_consulta == 2):
            os.system('clear')
            print("-> Todos os produtos contidos em um determinado carrinho de compras <-\n")
            print("Por favor, informe:\n")
            cpf_cliente = input("CPF do Cliente: ")
        
            if(VerificaCPF(cur, cpf_cliente) == -1):
                print("\nERRO: CPF não cadastrado!")
                input("Pressione ENTER para voltar.")
                return

            sql = ('''  SELECT NOME, DESCRICAO, QUANTIDADE, VALOR * QUANTIDADE AS VALOR_TOTAL
                        FROM (  SELECT PEDIDO_ID, PRODUTO_ID, QUANTIDADE
                                FROM (  SELECT ID
                                        FROM CLIENTE
                                        WHERE CPF = %s ) AS T1
                                INNER JOIN CARRINHO AS C
                                ON C.CLIENTE_ID = T1.ID ) AS T2
                        INNER JOIN PRODUTO P
                        ON P.ID = T2.PRODUTO_ID
                        WHERE PEDIDO_ID IS NULL
                        ORDER BY PEDIDO_ID ASC''')

            cur.execute(sql, [cpf_cliente])
            resultado = cur.fetchall()

            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")
        
        if(escolha_consulta == 3):
            os.system('clear')
            print("-> Dados (e a quantidade) dos clientes cadastrados no sistema <-\n")

            ler(cur, "CLIENTE")

            cur.execute("SELECT COUNT(*) AS CLIENTES_CADASTRADOS FROM CLIENTE")
            quantidade = cur.fetchall()

            print('\n', tabulate(quantidade, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")
        
        if(escolha_consulta == 4):
            os.system('clear')
            print("-> Forma de pagamento mais utilizada <-\n")

            cur.execute('''     SELECT NOME, MAX_QTD AS QUANTIDADE
                                FROM ( 	SELECT MAX(QTD) AS MAX_QTD
		                                FROM (	SELECT NOME, COUNT(*) AS QTD
		                                        FROM FORMA_PAGAMENTO
		                                        GROUP BY NOME) AS T1) AS T2,
	                                (	SELECT NOME, COUNT(*) AS QTD
		                                FROM FORMA_PAGAMENTO
                                        GROUP BY NOME ) AS T3
                                WHERE T2.MAX_QTD = T3.QTD''')
            
            resultado = cur.fetchall()

            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")

        if(escolha_consulta == 5):
            
            escolha = 1
            while(escolha != 0):
                os.system('clear')
                print("-> Filtrar usuários por Bairro, Cidade e Estado <-\n")
                print("0. Voltar")
                print("1. Bairro")
                print("2. Cidade")
                print("3. Estado")

                escolha = int(input("\nDigite sua escolha: "))
                if(escolha == 1):
                    os.system('clear')
                    print("-> Filtrar usuários por Bairro <-\n")

                    bairro = input("Digite o Bairro: ")

                    sql = ('''  SELECT NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO, NOME_USUARIO, STATUS_USUARIO
                                FROM ( 	SELECT C.ID, NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO 
		                                FROM CLIENTE AS C
		                                INNER JOIN ENDERECO AS E
		                                ON E.ID = C.ENDERECO_ID) AS CE
                                LEFT JOIN USUARIO AS U
                                ON U.CLIENTE_ID = CE.ID
                                WHERE BAIRRO = %s''')

                    cur.execute(sql, (bairro,))
                    resultado = cur.fetchall()

                    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
                    input("Pressione ENTER para voltar.")

                if(escolha == 2):
                    os.system('clear')
                    print("-> Filtrar usuários por Cidade <-\n")

                    cidade = input("Digite a Cidade: ")

                    sql = ('''  SELECT NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO, NOME_USUARIO, STATUS_USUARIO
                                FROM ( 	SELECT C.ID, NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO 
		                                FROM CLIENTE AS C
		                                INNER JOIN ENDERECO AS E
		                                ON E.ID = C.ENDERECO_ID) AS CE
                                LEFT JOIN USUARIO AS U
                                ON U.CLIENTE_ID = CE.ID
                                WHERE CIDADE = %s''')

                    cur.execute(sql, (cidade,))
                    resultado = cur.fetchall()

                    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
                    input("Pressione ENTER para voltar.")

                if(escolha == 3):
                    os.system('clear')
                    print("-> Filtrar usuários por Estado <-\n")

                    estado = input("Digite o Estado (Sigla): ")

                    sql = ('''  SELECT NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO, NOME_USUARIO, STATUS_USUARIO
                                FROM ( 	SELECT C.ID, NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO 
		                                FROM CLIENTE AS C
		                                INNER JOIN ENDERECO AS E
		                                ON E.ID = C.ENDERECO_ID) AS CE
                                LEFT JOIN USUARIO AS U
                                ON U.CLIENTE_ID = CE.ID
                                WHERE ESTADO = %s''')

                    cur.execute(sql, (estado,))
                    resultado = cur.fetchall()

                    print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
                    input("Pressione ENTER para voltar.")
        
        if(escolha_consulta == 6):
            os.system('clear')
            print("-> Média anual de vendas <-\n")

            ano = input("Digite o ano: ")

            sql = ("SELECT AVG(TOTAL) AS MEDIA_ANUAL FROM PEDIDO WHERE YEAR(DATA_PEDIDO) = %s")
            cur.execute(sql, (ano,))

            resultado = cur.fetchall()
            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")

        if(escolha_consulta == 7):
            os.system('clear')
            print("-> Mês e ano com maior número de vendas <-\n")

            cur.execute('''     SELECT T3.ANO, T3.MES, MAX_QTD AS VENDAS
                                FROM ( 	SELECT MAX(QTD) AS MAX_QTD
		                                FROM (	SELECT YEAR(DATA_PEDIDO), MONTH(DATA_PEDIDO), COUNT(TOTAL) AS QTD
				                                FROM PEDIDO
				                                GROUP BY 1, 2) AS T1) AS T2,
	                                (	SELECT YEAR(DATA_PEDIDO) as ANO, MONTH(DATA_PEDIDO) as MES, COUNT(TOTAL) AS QTD
		                                FROM PEDIDO
                                        GROUP BY 1, 2 ) AS T3
                                WHERE T2.MAX_QTD = T3.QTD
                                GROUP BY 1, 2''')
            
            resultado = cur.fetchall()
            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")

        if(escolha_consulta == 8):
            os.system('clear')
            print("-> Usuários que realizaram compras em todos os meses de um determinado ano <-\n")

            ano = input("Digite o ano: ")

            sql = ('''  SELECT NOME
                        FROM CLIENTE
                        WHERE ID IN ( 	SELECT CLIENTE_ID
				                        FROM (	SELECT CLIENTE_ID, COUNT(DISTINCT MONTH(DATA_PEDIDO)) AS QTD
						                        FROM PEDIDO P
						                        INNER JOIN CARRINHO C
						                        ON P.ID = C.PEDIDO_ID
						                        WHERE YEAR(DATA_PEDIDO) = %s
						                        GROUP BY CLIENTE_ID ) AS T1
				                        WHERE T1.QTD = 12 )''')
            
            cur.execute(sql, (ano,))

            resultado = cur.fetchall()
            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")
            
        if(escolha_consulta == 9):
            os.system('clear')
            print("-> Valor total gasto por um determinado cliente <-\n")
            print("Por favor, informe:\n")
            cpf_cliente = input("CPF do Cliente: ")

            sql = ('''  SELECT SUM(TOTAL) AS TOTAL_R$
                        FROM PEDIDO 
                        WHERE ID IN ( 	SELECT PEDIDO_ID
				                        FROM CARRINHO
				                        WHERE CLIENTE_ID IN (	SELECT ID
										                        FROM CLIENTE
										                        WHERE CPF = %s ) )''')

            cur.execute(sql, (cpf_cliente,))

            resultado = cur.fetchall()
            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")

        if(escolha_consulta == 10):
            os.system('clear')
            print("-> Total de ganhos com vendas em um determinado mês e ano <-\n")
            print("Por favor, informe:\n")
            ano = input("Ano: ")
            mes = input("Mês: ")

            sql = ('''  SELECT SUM(TOTAL) AS TOTAL_R$
                        FROM PEDIDO
                        WHERE YEAR(DATA_PEDIDO) = %s AND MONTH(DATA_PEDIDO) = %s''')
            data = (ano, mes)
            
            cur.execute(sql, data)
            
            resultado = cur.fetchall()
            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            input("Pressione ENTER para voltar.")