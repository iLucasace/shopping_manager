from tabulate import tabulate
from Verificacoes import *
import os

#FUNÇÃO PARA CADASTRAR CLIENTE/PRODUTO
def criar(conexao, cur, table):
    if(table == "CLIENTE"):
        os.system('clear')
        print("-> Cadastrar Cliente <-\n")
        print("Por favor, informe:\n")
    
        nome = input("Nome: ")
        telefone = input("Telefone (apenas números): ")
        tipo = input("Tipo (Telefone ou Catálogo): ")
    
        cpf = int(input("CPF (apenas números): "))
        
        if(VerificaCPF(cur, cpf) == 0):
            print("\nERRO: CPF já cadastrado!") 
            input("Pressione ENTER para voltar.")
            return 

        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        estado = input("Estado (Sigla): ")
    
        sql = "INSERT INTO ENDERECO (ID, BAIRRO, CIDADE, ESTADO) VALUES (null, %s, %s, %s)"
        data = (bairro, cidade, estado)
    
        cur.execute(sql, data)
        conexao.commit()
    
        id_endereco = cur.lastrowid
        
        sql = "INSERT INTO CLIENTE (ID, NOME, TELEFONE, CPF, TIPO, ENDERECO_ID) VALUES (null, %s, %s, %s, %s, %s)"
        data = (nome, telefone, cpf, tipo, id_endereco)
    
        cur.execute(sql, data)
        conexao.commit()
        
        print("\nCliente Cadastrado!")
        print("Cliente ID:", cur.lastrowid, '\n')
        input("Pressione ENTER para voltar.")
        return
        
    elif(table == 'PRODUTO'):
        os.system('clear')
        print("-> Cadastrar Produto <-\n")
        print("Por favor, informe:\n")
        nome = input("Nome do Produto: ")
        valor = input("Valor do Produto (apenas números separados por ponto): ")
        descricao=input("Descrição do Produto: ")
        
        sql = "INSERT INTO PRODUTO (ID, NOME, VALOR, DESCRICAO) VALUES (null, %s, %s, %s)"
        data = (nome, valor, descricao)
        
        cur.execute(sql, data)
        conexao.commit()
        
        print("\nProduto Cadastrado!")
        print("Produto ID:", cur.lastrowid, '\n')
        input("Pressione ENTER para voltar.")
        return

#FUNÇÃO PARA LER CLIENTES/PRODUTOS CADASTRADOS
def ler(cur, table):
    if(table == "CLIENTE"):
        cur.execute('''SELECT NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO, NOME_USUARIO, STATUS_USUARIO
                        FROM ( 	SELECT C.ID, NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO 
		                        FROM CLIENTE AS C
		                        INNER JOIN ENDERECO AS E
		                        ON E.ID = C.ENDERECO_ID) AS CE
                            LEFT JOIN USUARIO AS U
                            ON U.CLIENTE_ID = CE.ID''')
        resultado = cur.fetchall()
    
        print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
    elif(table == "PRODUTO"):
        cur.execute("SELECT * FROM PRODUTO")
        resultado = cur.fetchall()
        
        print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')

#FUNÇÃO PARA ALTERAR DADOS DOS CLIENTES/PRODUTOS
def alterar(conexao, cur, table):
    if(table == "CLIENTE"):
        print("\nPor favor, informe:\n")
        
        cpf_cliente = input("CPF do Cliente: ")
        verificacao = VerificaCPF(cur, cpf_cliente)
        if(verificacao == 0):
            cur.execute('''SELECT NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO, NOME_USUARIO, STATUS_USUARIO
                                FROM ( 	SELECT C.ID, NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO 
		                                FROM CLIENTE AS C
		                                INNER JOIN ENDERECO AS E
		                                ON E.ID = C.ENDERECO_ID) AS CE
                                LEFT JOIN USUARIO AS U
                                ON U.CLIENTE_ID = CE.ID
                                WHERE CPF = "'''+cpf_cliente+'''"''')
            resultado = cur.fetchall()
            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
        
            cur.execute("SELECT ID FROM CLIENTE WHERE CPF = '"+cpf_cliente+"'")
            for linha in cur.fetchall(): #...
                id_cliente = linha[0]    # TRANSFORMA ID_CLIENTE EM STRING
        
            escolha = 1
            while(escolha != 0):
                print("0. Voltar")
                print("1. Alterar Nome")
                print("2. Alterar Telefone")
                print("3. Alterar CPF")
                print("4. Alterar Bairro")
                print("5. Alterar Cidade")
                print("6. Alterar Estado")
                print("7. Alterar Nome de Usuário")
                print("8. Alterar Status do Usuário")
        
                escolha = int(input("\nDigite sua escolha: "))
                if(escolha == 0):
                    return
                if(escolha == 1):
                    os.system('clear')
                    print("-> Atualizar Nome <-\n")
                    nome = input("Novo Nome: ")
                
                    sql = ("UPDATE CLIENTE SET NOME = %s WHERE ID = %s")
                    data = (nome, id_cliente)
                        
                    cur.execute(sql, data)
                    conexao.commit()
                
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                
                if(escolha == 2):
                    os.system('clear')
                    print("-> Atualizar Telefone <-\n")
                    telefone = input("Novo Telefone: ")
                
                    sql = ("UPDATE CLIENTE SET TELEFONE = %s WHERE ID = %s")
                    data = (telefone, id_cliente)
                        
                    cur.execute(sql, data)
                    conexao.commit()
                
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                
                if(escolha == 3):
                    os.system('clear')
                    print("-> Atualizar CPF <-\n")
                    cpf = int(input("Novo CPF: "))
                        
                    if(VerificaCPF(cur, cpf) == 0):
                        print("\nERRO: CPF já cadastrado!")
                        input("Pressione ENTER para voltar.")
                        return
                        
                    sql = ("UPDATE CLIENTE SET CPF = %s WHERE ID = %s")
                    data = (cpf, id_cliente)
                        
                    cur.execute(sql, data)
                    conexao.commit()
                
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                
                if(escolha == 4):
                    os.system('clear')
                    print("-> Atualizar Bairro <-\n")
                    bairro = input("Novo Bairro: ")
                        
                    sql = ("SELECT ENDERECO_ID FROM CLIENTE WHERE ID = %s")
                        
                    cur.execute(sql, (id_cliente,))
                    for linha in cur.fetchall(): #...
                        endereco_id = linha[0]   # TRANSFORMA ENDERECO ID EM STRING
                        
                    sql = ("UPDATE ENDERECO SET BAIRRO = %s WHERE ID = %s")
                    data = (bairro, endereco_id)
                        
                    cur.execute(sql, data)
                    conexao.commit()
                        
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                    
                if(escolha == 5):
                    os.system('clear')
                    print("-> Atualizar Cidade <-\n")
                    cidade = input("Nova Cidade: ")
                        
                    sql = ("SELECT ENDERECO_ID FROM CLIENTE WHERE ID = %s")
                        
                    cur.execute(sql, (id_cliente,))
                    for linha in cur.fetchall(): #...
                        endereco_id = linha[0]   # TRANSFORMA ENDERECO ID EM STRING
                        
                    sql = ("UPDATE ENDERECO SET CIDADE = %s WHERE ID = %s")
                    data = (cidade, endereco_id)
                        
                    cur.execute(sql, data)
                    conexao.commit()
                        
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                
                if(escolha == 6):
                    os.system('clear')
                    print("-> Atualizar Estado <-\n")
                    estado = input("Novo Estado: ")
                        
                    sql = ("SELECT ENDERECO_ID FROM CLIENTE WHERE ID = %s")
                        
                    cur.execute(sql, (id_cliente,))
                    for linha in cur.fetchall(): #...
                        endereco_id = linha[0]   # TRANSFORMA ENDERECO ID EM STRING
                        
                    sql = ("UPDATE ENDERECO SET ESTADO = %s WHERE ID = %s")
                    data = (estado, endereco_id)
                        
                    cur.execute(sql, data)
                    conexao.commit()
                        
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                
                if(escolha == 7):
                    os.system('clear')
                    print("-> Atualizar Nome de Usuário <-\n")
                        
                    sql = ("SELECT TIPO FROM CLIENTE WHERE ID = %s")
                        
                    cur.execute(sql, (id_cliente,))
                    for linha in cur.fetchall():
                        tipo = linha[0]
                            
                    if(tipo == "Cliente Web"):
                        nome_usuario = input("Novo Nome de Usuário: ")
                            
                        if(VerificaUsuario(cur, nome_usuario == 0)):
                            print("\nERRO: Username já cadastrado!")
                            input("Pressione ENTER para voltar.")
                            return
                                    
                        sql = ("UPDATE USUARIO SET NOME_USUARIO = %s WHERE CLIENTE_ID = %s")
                        data = (nome_usuario, id_cliente)
                            
                        cur.execute(sql, data)
                        conexao.commit()
                            
                        print("\nAlterado com sucesso!")
                        input("Pressione ENTER para voltar.")
                        return
                        
                    else:
                        print("ERRO: Cliente não é do Tipo Web!")
                        input("Pressione ENTER para voltar.")
                        return
                    
                if(escolha == 8):
                    os.system('clear')
                    print("-> Atualizar Status do Usuário <-\n")
                        
                    sql = ("SELECT TIPO FROM CLIENTE WHERE ID = %s")
                        
                    cur.execute(sql, (id_cliente,))
                    for linha in cur.fetchall():
                            tipo = linha[0]
                            
                    if(tipo == "Cliente Web"):
                        status = input("Novo Status (Novo / Ativo / Bloqueado / Banido): ")
                            
                        sql = ("UPDATE USUARIO SET STATUS_USUARIO = %s WHERE CLIENTE_ID = %s")
                        data = (status, id_cliente)
                            
                        cur.execute(sql, data)
                        conexao.commit()
                            
                        print("\nAlterado com sucesso!")
                        input("Pressione ENTER para voltar.")
                        return
                        
                    else:
                        print("ERRO: Cliente não é do Tipo Web!")
                        input("Pressione ENTER para voltar.")
                        return
                        
        elif(verificacao == -1):
            print("\nERRO: CPF não cadastrado!")
            input("Pressione ENTER para voltar.")
            return
        
    elif(table == "PRODUTO"):
        print("\nPor favor, informe:\n")
        
        id_produto = input("ID do Produto: ")
        
        verificacao = VerificaProduto(cur, id_produto)
        if(verificacao == 0):
            cur.execute("SELECT NOME, VALOR, DESCRICAO FROM PRODUTO WHERE ID = '"+id_produto+"'")
            
            resultado = cur.fetchall()
            print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
            
            escolha = 1
            while(escolha != 0):
                print("0. Voltar")
                print("1. Alterar Nome")
                print("2. Alterar Valor")
                print("3. Alterar Descrição")
                
                escolha = int(input("\nDigite sua escolha: "))
                if(escolha == 0):
                    return
                
                if(escolha == 1):
                    os.system('clear')
                    print("-> Atualizar Nome do Produto <-\n")
                    nome_produto = input("Novo Nome: ")
                    
                    sql = ("UPDATE PRODUTO SET NOME = %s WHERE ID = %s")
                    data = (nome_produto, id_produto)
                    
                    cur.execute(sql, data)
                    conexao.commit()
                    
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                
                if(escolha == 2):
                    os.system('clear')
                    print("-> Atualizar Valor do Produto <-\n")
                    valor_produto = input("Novo Valor (apenas números separados por ponto): ")
                    
                    sql = ("UPDATE PRODUTO SET VALOR = %s WHERE ID = %s")
                    data = (valor_produto, id_produto)
                    
                    cur.execute(sql, data)
                    conexao.commit()
                    
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                
                if(escolha == 3):
                    os.system('clear')
                    print("-> Atualizar Descrição do Produto <-\n")
                    descricao_produto = input("Nova Descrição: ")
                    
                    sql = ("UPDATE PRODUTO SET DESCRICAO = %s WHERE ID = %s")
                    data = (descricao_produto, id_produto)
                    
                    cur.execute(sql, data)
                    conexao.commit()
                    
                    print("\nAlterado com sucesso!")
                    input("Pressione ENTER para voltar.")
                    return
                    
        elif(verificacao == -1):
            print("\nERRO: Produto não cadastrado!")
            input("Pressione ENTER para voltar.")
            return

#FUNÇÃO PARA DELETAR CLIENTES/PRODUTOS    
def deletar(conexao, cur, table):
    if(table == "CLIENTE"):
        print("\nPor favor, informe:\n")
        cpf_cliente = input("CPF do Cliente: ")
        
        if(VerificaCPF(cur, cpf_cliente) == -1):
            print("\nERRO: CPF não cadastrado!")
            input("Pressione ENTER para voltar.")
            return
        
        cur.execute('''SELECT NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO, NOME_USUARIO, STATUS_USUARIO
                        FROM ( 	SELECT C.ID, NOME, TELEFONE, CPF, TIPO, BAIRRO, CIDADE, ESTADO 
		                        FROM CLIENTE AS C
		                        INNER JOIN ENDERECO AS E
		                        ON E.ID = C.ENDERECO_ID) AS CE
                        LEFT JOIN USUARIO AS U
                        ON U.CLIENTE_ID = CE.ID
                        WHERE CPF = "'''+cpf_cliente+'''"''')
        resultado = cur.fetchall()
        print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
        
        print("Deseja deletar?")
        print("0. Não")
        print("1. Sim")
        escolha = int(input("\nDigite sua escolha: "))
        
        if(escolha == 0):
            return
        elif(escolha == 1):
            sql = ("SELECT ENDERECO_ID FROM CLIENTE WHERE CPF = '"+cpf_cliente+"'")
        
            cur.execute(sql)
            endereco_id = cur.fetchall()
        
            sql = ("DELETE FROM ENDERECO WHERE ID = %s")
        
            cur.execute(sql, *endereco_id)
            conexao.commit()
        
            sql = ("SELECT ID FROM CLIENTE WHERE CPF = '"+cpf_cliente+"'")
        
            cur.execute(sql)
            id_cliente = cur.fetchall()
        
            sql = ("DELETE FROM USUARIO WHERE CLIENTE_ID = %s") 
        
            cur.execute(sql, *id_cliente)
            conexao.commit()
        
            sql = ("DELETE FROM CLIENTE WHERE ID = %s")
        
            cur.execute(sql, *id_cliente)
            conexao.commit()
            
            print("\nDeletado com sucesso!")
            input("Pressione ENTER para voltar.")
            return
        
    elif(table == "PRODUTO"):
        print("\nPor favor, informe:\n")
        id_produto = input("ID do Produto: ")
        
        if(VerificaProduto(cur, id_produto) == -1):
            print("\nERRO: Produto não cadastrado!")
            input("Pressione ENTER para voltar.")
            return
        
        cur.execute("SELECT * FROM PRODUTO WHERE ID = '"+id_produto+"'")
        resultado = cur.fetchall()
        
        print('\n', tabulate(resultado, headers=[linha[0] for linha in cur.description], tablefmt='psql'), '\n')
        
        print("Deseja deletar?")
        print("0. Não")
        print("1. Sim")
        escolha = int(input("\nDigite sua escolha: "))
        
        if(escolha == 0):
            return
        elif(escolha == 1):
            cur.execute("DELETE FROM PRODUTO WHERE ID = '"+id_produto+"'")
            conexao.commit()
    
            print("\nDeletado com sucesso!")
            input("Pressione ENTER para voltar.")
            return