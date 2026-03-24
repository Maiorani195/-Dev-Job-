import _sqlite3 #conexao com o banco de dados SQLite

def criar_banco(): #criando def para colocarmos o banco de dados dentro dela, para que seja criado somente quando chamarmos a função.

    print("="*50)
    print("Criando o banco de dados...")
    print("="*50)

    conn = _sqlite3.connect("devjob.db") #conecta ao banco de dados, se o arquivo não existir, ele será criado
    cursor = conn.cursor() #cursor é o objeto que permite executar comandos SQL

    print("Conexão estabelecida com o banco de dados.")

    print("Criando a tabela de vagas...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS VAGAS(
                   ID INT PRIMARY KEY AUTOINCREMENT,
                   EXTERNAL_ID TEXT UNIQUE NOT NULL,
                   TITLE TEXT NOT NULL,
                   EMPRESA TEXT,
                   LOCALIZAÇAO TEXT,
                   SALARIO MIN REAL,
                   SALARIO MAX REAL,
                     DESCRIÇAO TEXT,
                   URL TEXT,
                   FONTE TEXT NOT NULL,
                   DATA POSTAGEM TEXT,
                   DATA COLETADA DATETIME DEFAULT CURRENT_TIMESTAMP
                   )
                   """)
    #NOT NULL É OBRIGATORIO.
    #UNIQUE VAGAS DUPLICADAS.
    #REAL É DECIMAL.

    print("Tabela de vagas criada com sucesso.")

    print("Criando tabela de candidaturas")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS CANDIDATURAS(
            ID INT PRIMARY KEY AUTOINCREMENT,
            VAGA_ID INT NOT NULL,
            STATUS TEXT,
            NOTAS TEXT,
            DATA_DE_APLICAÇAO DATE
            DATA_ATUALIZAÇAO DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (VAGA_ID) REFERENCES VAGAS(ID) 
        )
    """)
    #REFERENCIANDO O VAGA_ID COM A TABELA DE VAGAS , COM O ID UNICO DA VAGA.


    print("Tabela de candidaturas criada com sucesso.")

    conn.commit() #salvo
    conn.close()#fecho a conexão


    print("Banco de dados criado com sucesso.")
    print("✅ Pronto para usar!")

    if __name__ == "__main__":
        criar_banco() # chamando a funçao para criar o banco de dados


