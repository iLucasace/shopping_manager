from getpass import getpass
from Cliente.MenuCliente import *
from Verificacoes import *
import os

#FUNÇÃO PARA CADASTRAR UM USUÁRIO
def Cadastro(conexao, cur):
    os.system('clear') #LIMPA A TELA
    print("-> Cadastro Cliente Web <-\n")
    print("Por favor, informe:\n")
    
    nome=input("Nome: ") #RECEBE O NOME
    username = input("Username: ") #RECEBE O USERNAME
    
    if(VerificaUsuario(cur, username) == 0): #VERIFICA SE O USUÁRIO DIGITADO EXISTE NO BANCO DE DADOS (0 = SIM)
        print("\nERRO: Username já cadastrado!") #MENSAGEM DE ERRO PARA USUÁRIO JÁ CADASTRADO
        input("Pressione ENTER para voltar.")
        return
    
    cpf = input("CPF (apenas números): ") #RECEBE O CPF
    
    if(VerificaCPF(cur, cpf) == 0): #VERIFICA SE O CPF DIGITADO EXISTE NO BANCO DE DADOS (0 = SIM)
        print("\nERRO: CPF já cadastrado!") #MENSAGEM DE ERRO PARA CPF JÁ CADASTRADO
        input("Pressione ENTER para voltar.")
        return
    
    senha = getpass("Senha: ") #RECEBE A SENHA
    telefone = input("Telefone (apenas números): ") #RECEBE O TELEFONE
    tipo = "Cliente Web" #PRÉ-DETERMINA O TIPO
    

    bairro=input("Bairro: ") #RECEBE O BAIRRO
    cidade=input("Cidade: ") #RECEBE A CIDADE
    estado=input("Estado (Sigla): ") #RECEBE O ESTADO
    
    sql = "INSERT INTO ENDERECO (ID, BAIRRO, CIDADE, ESTADO) VALUES (null, %s, %s, %s)" #INSERT NA TABELA ENDEREÇO
    data = (bairro, cidade, estado) #UTILIZA OS DADOS CORRESPONDENTES NO INSERT
    
    cur.execute(sql, data) #EXECUTA O COMANDO (SQL+DATA)
    conexao.commit() #SALVA A ALTERAÇÃO NO BANCO DE DADOS
    
    id_endereco = cur.lastrowid #RECEBE O ID DO ENDERECO CRIADO NA LINHA #36
        
    sql = "INSERT INTO CLIENTE (ID, NOME, TELEFONE, CPF, TIPO, ENDERECO_ID) VALUES (null, %s, %s, %s, %s, %s)" #INSERT NA TABELA CLIENTE
    data = (nome, telefone, cpf, tipo, id_endereco) #UTILIZA OS DADOS CORRESPONDENTES NO INSERT
    
    cur.execute(sql, data) #EXECUTA O COMANDO (SQL+DATA)
    conexao.commit() #SALVA A ALTERAÇÃO NO BANCO DE DADOS
    
    id_cliente = cur.lastrowid #RECEBE O ID DO CLIENTE CRIADO NA LINHA #44
    status_conta = "Ativo" #STATUS DA CONTA = "ATIVO"
    
    sql = "INSERT INTO USUARIO (ID, NOME_USUARIO, SENHA_USUARIO, STATUS_USUARIO, CLIENTE_ID) VALUES (null, %s, %s, %s, %s)" #INSERT NA TABELA USUARIO
    data = (username, senha, status_conta, id_cliente) #UTILIZA OS DADOS CORRESPONDENTES NO INSERT
    
    cur.execute(sql, data) #EXECUTA O COMANDO (SQL+DATA)
    conexao.commit() #SALVA A ALTERAÇÃO NO BANCO DE DADOS

    sql = "INSERT INTO CARRINHO (ID, CLIENTE_ID, PEDIDO_ID, PRODUTO_ID, QUANTIDADE) VALUES (null, %s, null, null, null)" #INSERT NA TABELA CARRINHO
    data = [id_cliente] #UTILIZA OS DADOS CORRESPONDENTES NO INSERT
    
    cur.execute(sql, data) #EXECUTA O COMANDO (SQL+DATA)
    conexao.commit() #SALVA A ALTERAÇÃO NO BANCO DE DADOS
    
    print("\nCadastrado com sucesso!")
    input("Pressione ENTER para voltar.")

#FUNÇÃO PARA REALIZAR O LOGIN DE UM USUÁRIO
def Login(conexao, cur):
    os.system('clear') #LIMPA A TELA
    print("-> Login Cliente Web <-\n")
    
    username = input("Username: ") #RECEBE O USERNAME
    verificao = VerificaUsuario(cur, username) #VERIFICA SE O USUÁRIO DIGITADO EXISTE NO BANCO DE DADOS (0 = SIM / -1 = NÃO)
    
    if(verificao == 0):
        sql = "SELECT cast(SENHA_USUARIO as CHAR) FROM USUARIO WHERE NOME_USUARIO = %s" #SELECT NA SENHA CORRESPONDENTE AO USERNAME
        cur.execute(sql, [username]) #EXECUTA O COMANDO (SQL + USERNAME)
        for row in cur.fetchall(): # ...
            senha = row[0]         # TRANSFORMA A SENHA SELECIONADA EM STRING
        senha_digitada = getpass("Senha: ") #RECEBE A SENHA
        if(senha == senha_digitada): #COMPARA A SENHA DIGITADA COM A SELECIONADA NO BANCO DE DADOS
            cur.execute("SELECT CLIENTE_ID FROM USUARIO WHERE NOME_USUARIO = '"+username+"'")
            for linha in cur.fetchall(): #...
                id_cliente = linha[0]    # TRANSFORMA ID_USUARIO EM STRING

            MenuCliente(conexao, cur, id_cliente, username) #CHAMA A FUNÇÃO DO MENU DO CLIENTE
        
        else:
            print("\nSenha incorreta!") #MENSAGEM DE ERRO PARA SENHA INCORRETA
            input("Pressione ENTER para voltar.")
            return
        
    elif(verificao == -1):
        print("\nERRO: Usuário não cadastrado.") #MENSAGEM DE ERRO PARA USUÁRIO NÃO CADASTRADO
        input("Pressione ENTER para voltar.")
        return