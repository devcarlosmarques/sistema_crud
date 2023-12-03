import sqlite3

#criando conexao com o banco de dados criado
bd = sqlite3.connect('bancodedados.db')

#funcao menu - responsavel pelo layout das opcões
def menu():
    print('---------------------------------')
    print('[1] CADASTRAR USUÁRIO')
    print('[2] CONSULTAR CADASTRO')
    print('[3] ALTERAR USUÁRIO')
    print('[4] DELETAR USUÁRIO')
    print('[5] SAIR DO SISTEMA')

    opcao = int(input('Digite a sua opção: '))

    #opcao 1 - responsavel pela chamada da funcao cadastro
    if opcao == 1:
        cadastro()
        return menu()
    
    #opcao 2 - responsavel pela chamada da funcao de consultar
    elif opcao == 2:
        consultar_usuario()
        return menu()
    
    #opcao 3 - responsavel pela chamada da funcao altera dados de usuario
    elif opcao == 3:
        alterar_dado()
        return menu()
    
    #opcao 4 - responsavel pela chamda da funcao de deletar usuario
    elif opcao == 4:
        deletar_usuario()
        return menu()
    
    #opcao 5 - responsavel por sair do programa
    elif opcao == 5:
        print('Volte sempre...\n')
        exit()
    
    #caso a opção digitada for diferente das acima, ele retorna com o erro abaixo
    else:
        print('Opção incorreta, tente novamente!')
        return menu()

#funcao responsavel pelo cadastro de usuario
def cadastro():
        login = input('\nDigite um nome de usuário: ')
        senha = input('Digite uma senha: ')
        nome = input('Digite seu nome e sobrenome: ')
        email = input('Digite seu E-mail: ')

        bd.execute(f"INSERT INTO usuario (login, senha, nome, email) VALUES ('{login}', '{senha}', '{nome}', '{email}')")
        bd.commit()
        print("Usuário cadastrado com sucesso.\n")
        
#funcao responsavel por deletar o usuario
def deletar_usuario():
        usuario_deletado = input('\nInforme o usuário a ser deletado: ')
        cursor = bd.execute(f"DELETE FROM usuario WHERE login = '{usuario_deletado}'")
        bd.commit()
        
        if cursor.rowcount > 0:
            print(f'\nUsuário {usuario_deletado} foi deletado com sucesso!\n')
        else:
                print(f'\nUsuário {usuario_deletado} não foi encontrado e não pôde ser deletado.\n')
        
#funcao responsavel consultar os dados do usuario
def consultar_usuario():
        consultar_usuario = input('\nQual usuário deseja consultar? ')
        cursor = bd.execute(f"SELECT * from usuario WHERE login = '{consultar_usuario}'")
        print(f'Segue os dados do usuário {consultar_usuario}:\n')
        linha = cursor.fetchone()
        
        if linha:
            print(f'Segue os dados do usuário {consultar_usuario}:\n')
            print(f'Login: {linha[0]}')
            print(f'Senha: {linha[1]}')
            print(f'Nome: {linha[2]}')
            print(f'Email: {linha[3]}\n')
        else:
            print(f'Usuário {consultar_usuario} não encontrado.\n')

#funcao responsavel por alterar dados do usuario.
def alterar_dado():
        print('\n[1] USUARIO')
        print('[2] SENHA')
        print('[3] EMAIL')
        user_consult = int(input('Escolha uma opção: '))

        if user_consult == 1:
            login = input('\nDigite o login: ')
            novo_login = input('Digite seu novo login: ')
            bd.execute(f"UPDATE usuario SET login = '{novo_login}' WHERE login = '{login}'")
            bd.commit()

            print(f'\nO usuário {login} alterou o login para {novo_login}.\n')
        
        elif user_consult == 2:
            login = input('\nDigite o login: ')
            nova_senha = input('Digite sua nova senha: ')
            bd.execute(f"UPDATE usuario SET login = '{nova_senha}' WHERE login = '{login}'")
            bd.commit()

            print(f'\nO usuário {login} alterou a senha para {nova_senha}.\n')
             
        elif user_consult == 3:
            login = input('\nDigite o usuário: ')
            novo_email = input('Digite seu novo email: ')
            bd.execute(f"UPDATE usuario SET email = '{novo_email}' WHERE login = '{login}'")
            bd.commit()

            print(f'\nO usuário {login} alterou o email para {novo_email}.\n')

menu()