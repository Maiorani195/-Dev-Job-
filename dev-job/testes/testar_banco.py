import sqlite3
import os

# Pega o caminho absoluto de onde este script está rodando
diretorio_atual = os.path.dirname(os.path.abspath(__file__))


caminho_raiz = os.path.join(diretorio_atual, "devjob.db")
caminho_db = os.path.join(diretorio_atual, "db", "devjob.db")

# Descobre onde o arquivo realmente está
if os.path.exists(caminho_db):
    banco_encontrado = caminho_db
elif os.path.exists(caminho_raiz):
    banco_encontrado = caminho_raiz
else:
    banco_encontrado = None

# Se não achar, avisa com clareza. Se achar, conecta e mostra os dados.
if not banco_encontrado:
    print("❌ O arquivo devjob.db não foi encontrado!")
    print(f"Procurei em: {caminho_raiz}")
    print(f"E também em: {caminho_db}")
else:
    print(f"✅ Banco encontrado com sucesso em:\n{banco_encontrado}\n")
    
    conn = sqlite3.connect(banco_encontrado)
    cursor = conn.cursor()
    
    try:
        # Conta as vagas
        cursor.execute("SELECT COUNT(*) FROM VAGAS")
        total = cursor.fetchone()[0]
        print(f"📊 Total de vagas gravadas: {total}")
        
        # Se tiver vagas, mostra as 5 primeiras
        if total > 0:
            print("-" * 40)
            print("🔝 ÚLTIMAS 5 VAGAS SALVAS:")
            print("-" * 40)
            cursor.execute("SELECT TITLE, EMPRESA FROM VAGAS LIMIT 5")
            for vaga in cursor.fetchall():
                print(f"💼 {vaga[0]} | 🏢 {vaga[1]}")
            print("-" * 40)
            
    except sqlite3.OperationalError as e:
        print(f"❌ Erro de tabela: {e} (A tabela VAGAS ainda não foi criada neste arquivo)")
    finally:
        conn.close()