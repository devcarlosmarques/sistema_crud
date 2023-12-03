import sqlite3

#criando conexao com o banco de dados
bd = sqlite3.connect('bancodedados.db')

#comando sqlite para criar a tabela no banco de dados
bd.execute('''CREATE TABLE usuario (login text, senha text, email text, nome text)''')

#salvando a execução no banco de dados
bd.commit()

#fechando conexão com o banco de dados
bd.close()