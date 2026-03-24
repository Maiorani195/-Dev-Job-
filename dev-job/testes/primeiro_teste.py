import os
import requests
from dotenv import load_dotenv
from db.salvar_vagas import salvar_vagas 


load_dotenv()

APP_ID = os.getenv("ADZUNA_APP_ID")
APP_KEY = os.getenv("ADZUNA_APP_KEY")

# Configurações da busca
PAIS = "br"  
URL = f"https://api.adzuna.com/v1/api/jobs/{PAIS}/search/1"

def buscar_vagas(query="Python"):
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "results_per_page": 10,
        "what": query,
        "content-type": "application/json"
    }

    print(f"🔍 Buscando vagas de '{query}' na Adzuna...")
    
    try:
        response = requests.get(URL, params=params)
        
        if response.status_code == 200:
            dados = response.json()
            return dados.get("results", [])
        elif response.status_code == 401:
            print("❌ Erro 401: Falha na autenticação. Verifique suas chaves no .env")
            return []
        else:
            print(f"❌ Erro na API: {response.status_code}")
            return []
    except Exception as e:
        print(f"❌ Erro na requisição: {e}")
        return []

def normalizar_vagas(vagas_api):
    vagas_formatadas = []
    for v in vagas_api:
      
        vaga = {
            "external_id": v.get("id"),
            "titulo": v.get("title"),
            "empresa": v.get("company", {}).get("display_name"),
            "localizaçao": v.get("location", {}).get("display_name"),
            "salario_min": v.get("salary_min"),
            "salario_max": v.get("salary_max"),
            "descriçao": v.get("description"),
            "url": v.get("redirect_url"),
            "fonte": "adzuna",
            "data_postagem": v.get("created")
        }
        vagas_formatadas.append(vaga)
    return vagas_formatadas


if __name__ == "__main__":
    # 1. BUSCA
    vagas_api = buscar_vagas("Python")

    if not vagas_api:
        print("⚠️ Nenhuma vaga encontrada ou erro na API.")
    else:
        
        print(f"✅ {len(vagas_api)} vagas encontradas. Formatando dados...")
        vagas_normalizadas = normalizar_vagas(vagas_api)

        
        print("💾 Salvando no banco de dados...")
        
       # capturamos o retorno da função 
        novas_cont, duplicadas_cont = salvar_vagas(vagas_normalizadas)
        
        print("✅ Processo de salvamento concluído!")
        print()

       
        print("=" * 60)
        print("📊 RESUMO DO PROCESSO")
        print("=" * 60)
        print(f"   Vagas recebidas da API: {len(vagas_api)}")
        print(f"   Novas vagas no banco:  {novas_cont}")
        print(f"   Vagas duplicadas:      {duplicadas_cont}")
        print("=" * 60)
        print()

  
        if novas_cont > 0:
            print(f"🎉 Sucesso! {novas_cont} novas oportunidades registradas no devjob.db")
        else:
            print(" O banco já estava atualizado com estas vagas.")

    print("✅ Processo finalizado.")