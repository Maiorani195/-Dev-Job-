import sqlite3
import os

def salvar_vagas(lista_vagas):
    # Força o caminho para a pasta 'db' onde este script está
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_db = os.path.join(diretorio_atual, "devjob.db")
    
    print(f"\n--- 💾 SALVANDO EM: {caminho_db} ---")

    conn = sqlite3.connect(caminho_db) #conecta ao banco de dados, se o arquivo não existir, ele será criado
    cursor = conn.cursor()#cursor é o objeto que permite executar comandos SQL  

    #criando tabela vagas caso nao exista e dentro coloca as especifiaçoes 
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS VAGAS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        EXTERNAL_ID TEXT UNIQUE,
        TITLE TEXT,
        EMPRESA TEXT,
        LOCALIZAÇAO TEXT,
        SALARIO_MIN REAL,
        SALARIO_MAX REAL,
        DESCRIÇAO TEXT,
        URL TEXT,
        FONTE TEXT,
        DATA_POSTAGEM TEXT
    )
    """)

    novas_cont = 0
    duplicadas_cont = 0

    for vaga in lista_vagas:
        try:
            cursor.execute("""
                INSERT INTO VAGAS 
                (EXTERNAL_ID, TITLE, EMPRESA, LOCALIZAÇAO, 
                 SALARIO_MIN, SALARIO_MAX, DESCRIÇAO, URL, 
                 FONTE, DATA_POSTAGEM)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                str(vaga.get("external_id")),
                vaga.get("titulo"),
                vaga.get("empresa"),
                vaga.get("localizaçao"),
                vaga.get("salario_min"),
                vaga.get("salario_max"),
                vaga.get("descriçao"),
                vaga.get("url"),
                vaga.get("fonte", "adzuna"),
                vaga.get("data_postagem")
            ))
            novas_cont += 1#conta as vagas novas que foram inseridas
        except sqlite3.IntegrityError:
            duplicadas_cont += 1
        except Exception as e:
            print(f"⚠️ Erro ao inserir: {e}")

    conn.commit() #salva as mudanças no banco
    conn.close()#fecha o banco de dados
    return novas_cont, duplicadas_cont#retorna a quantidade de vagas novas e duplicadas para o resumo final