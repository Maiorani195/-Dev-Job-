# 🚀 Dev Job Tracker

Bem-vindo ao **Dev Job Tracker**, uma ferramenta automatizada para busca, análise e armazenamento de vagas de emprego voltadas para desenvolvedores. Este projeto utiliza a API da Adzuna para encontrar as melhores oportunidades e mantê-las organizadas em um banco de dados local.

---

## 🛠️ Tecnologias Utilizadas

O projeto foi construído com ferramentas modernas do ecossistema Python:

- **[Python](https://www.python.org/)**: Linguagem principal do projeto.
- **[SQLite](https://www.sqlite.org/)**: Banco de dados leve e eficiente para armazenamento local.
- **[FastAPI](https://fastapi.tiangolo.com/)**: Preparado para integração e visualização de dados.
- **[Requests](https://requests.readthedocs.io/)**: Para consumo de APIs REST.
- **[Python-Dotenv](https://pypi.org/project/python-dotenv/)**: Gerenciamento seguro de variáveis de ambiente.
- **[Selenium](https://www.selenium.dev/)**: Para automações de navegação web.

---

## ✨ Funcionalidades

- 🔍 **Busca Automatizada**: Pesquisa vagas baseadas em palavras-chave (ex: "Python", "React").
- 📊 **Normalização de Dados**: Transforma os retornos da API em um formato limpo e padronizado.
- 💾 **Persistência Inteligente**: Salva as vagas no banco de dados e evita duplicidade automaticamente.
- 🔐 **Segurança**: Configuração de chaves de API via variáveis de ambiente (`.env`).
- 📈 **Relatórios de Processamento**: Exibe um resumo detalhado de novas vagas encontradas vs. duplicadas.

---

## 🚀 Como Começar

### 1. Pré-requisitos
Certifique-se de ter o Python 3.9+ instalado em sua máquina.

### 2. Instalação
Clone o repositório e instale as dependências necessárias:

```bash
pip install -r dev-job/requirements.txt
```

### 3. Configuração
Crie um arquivo `.env` na pasta `dev-job/` com suas credenciais da Adzuna:

```env
ADZUNA_APP_ID=seu_app_id
ADZUNA_APP_KEY=sua_app_key
```

### 4. Executando a Busca
Para iniciar a coleta de vagas, execute o script principal:

```bash
python dev-job/testes/primeiro_teste.py
```

---

## 📁 Estrutura do Projeto

```text
dev.job/
├── dev-job/
│   ├── testes/
│   │   ├── db/                 # Scripts de criação e manipulação do banco
│   │   ├── primeiro_teste.py   # Script principal de busca e integração
│   │   └── testar_banco.py     # Verificação de integridade dos dados
│   ├── .env                    # Configurações sensíveis (Ignorado pelo Git)
│   └── requirements.txt        # Dependências do projeto
└── README.md                   # Documentação do projeto
```

---

## 🤝 Contribuição

Sinta-se à vontade para abrir PRs ou sugerir melhorias. Toda ajuda é bem-vinda para tornar o **Dev Job Tracker** ainda mais potente!

---

Desenvolvido com 💙 para a comunidade de desenvolvedores.
