#FUNÇÃO PARA VERFIFICAR SE O CPF EXISTE NO BANCO DE DADOS
def VerificaCPF(cur, cpf):
    cur.execute("SELECT CPF FROM CLIENTE") #SELECT EM TODOS OS CPFS CADASTRADOS
    cpfs_cadastrados = cur.fetchall() #RECEBE TODOS OS CPFS CADASTRADOS
    for linha in cpfs_cadastrados: #PERCORRE TODOS OS CPFS CADASTRADOS
        if(linha[0] == cpf): #VERIFICA SE O CPF DIGITADO JÁ EXISTE NO BANCO DE DADOS
            return 0 #RETORNA 0 SE O CPF DIGITADO ESTÁ CADASTRADO
    else:
        return -1 #RETORNA -1 SE O CPF DIGITADO NÃO ESTÁ CADASTRADO

#FUNÇÃO PARA VERFIFICAR SE O USUÁRIO EXISTE NO BANCO DE DADOS
def VerificaUsuario(cur, username):
    cur.execute("SELECT NOME_USUARIO FROM USUARIO") #SELECT EM TODOS OS USERNAMES CADASTRADOS
    usuarios = cur.fetchall() #RECEBE TODOS OS USERNAMES CADASTRADOS
    for linha in usuarios: #PERCORRE TODOS OS USERNAMES CADASTRADOS
        if(linha[0] == username): #VERIFICA SE O USERNAME DIGITADO JÁ EXISTE NO BANCO DE DADOS
            return 0 #RETORNA 0 SE O USERNAME DIGITADO ESTÁ CADASTRADO
    else:
        return -1 #RETORNA -1 SE O USERNAME DIGITADO NÃO ESTÁ CADASTRADO
    
#FUNÇÃO PARA VERFIFICAR SE O PRODUTO EXISTE NO BANCO DE DADOS
def VerificaProduto(cur, id_produto):
    cur.execute("SELECT ID FROM PRODUTO") #SELECT EM TODOS OS IDS DE PRODUTOS CADASTRADOS
    produtos = cur.fetchall() #RECEBE TODOS OS IDS DE PRODUTOS CADASTRADOS
    for linha in produtos: #PERCORRE TODOS OS IDS DE PRODUTOS CADASTRADOS
        if(linha[0] == int(id_produto)): #VERIFICA SE O ID DO PRODUTO DIGITADO JÁ EXISTE NO BANCO DE DADOS
            return 0 #RETORNA 0 SE O ID DO PRODUTO DIGITADO ESTÁ CADASTRADO
    else:
        return -1 #RETORNA -1 SE O ID DO PRODUTO NÃO DIGITADO ESTÁ CADASTRADO

#FUNÇÃO PARA VERFIFICAR SE DETERMINADO PRODUTO ESTÁ EM DETERMINADO CARRINHO
def VerificaCarrinho(cur, id_cliente, id_produto):
    sql = ("SELECT PRODUTO_ID FROM CARRINHO WHERE CLIENTE_ID = %s AND PEDIDO_ID IS NULL") #SELECT EM TODOS OS IDS DOS PRODUTOS NO CARRINHO O USUÁRIO X

    cur.execute(sql, [id_cliente]) #EXECUTA O SELECT COM O ID DO USUÁRIO RECEBIDO
    produtos = cur.fetchall() #RECEBE TODOS OS IDS DOS PRODUTOS NO CARRINHO O USUÁRIO X
    for linha in produtos: #PERCORRE TODOS OS IDS DOS PRODUTOS NO CARRINHO O USUÁRIO X
        if(linha[0] == int(id_produto)): #VERIFICA SE O ID DO PRODUTO DIGITADO ESTÁ NO CARRINHO DO USUÁRIO X
            return 0 #RETORNA 0 SE O ID DO PRODUTO ESTIVER NO CARRINHO
    else:
        return -1 #RETORNA -1 SE O ID DO PRODUTO NÃO ESTIVER NO CARRINHO