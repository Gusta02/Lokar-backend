# Lokar - Sistema de Gestão Imobiliária

O **Lokar** é um sistema voltado para consultores e imobiliárias gerenciarem imóveis, visitas, contratos, locações, vendas e integração com redes sociais.  
O projeto é desenvolvido com **FastAPI** no backend e será integrado futuramente a um frontend responsivo, além de contar com banco de dados PostgreSQL e ambiente Docker.

---

## 📌 Funcionalidades previstas (MVP)
- Cadastro e gerenciamento de imóveis (com fotos e características detalhadas).
- Controle de visitas e agendamentos.
- Registro e acompanhamento de contratos.
- Gestão de locações e vendas.
- Organização e postagem de conteúdo para redes sociais.
- Controle de usuários com diferentes permissões (consultor, gerente, administrador).

---

## 🚀 Tecnologias Utilizadas
- **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
- **Frontend:** (Futuro) Lovable ou outro framework
- **Banco de Dados:** PostgreSQL (futuro)
- **Autenticação:** JWT
- **Controle de Versão:** Git + GitHub

---

## 📂 Estrutura de Pastas (fase inicial)

```bash
  lokar/
  │── app/
  │ ├── main.py # Ponto de entrada da aplicação FastAPI
  │ ├── routers/ # Rotas da aplicação
  │ ├── models/ # Modelos Pydantic (futuro: ORM)
  │ ├── schemas/ # Schemas de entrada e saída
  │ ├── services/ # Lógica de negócio
  │ ├── core/ # Configurações, segurança, middlewares
  │ └── utils/ # Funções utilitárias
  │
  │── tests/ # Testes automatizados
  │── .env.example # Variáveis de ambiente (modelo)
  │── .gitignore # Arquivos e pastas ignorados pelo Git
  │── README.md # Documentação do projeto
  │── requirements.txt # Dependências do projeto
```

---

## 📦 Como rodar o projeto localmente

1. **Clonar o repositório**
```bash
   git clone https://github.com/seu-usuario/lokar.git
   cd lokar
```

---

2. **Criar e ativar um ambiente virtual**

```bash
  python -m venv venv
  source venv/bin/activate   # Linux/Mac
  venv\Scripts\activate      # Windows
```

---

3. **Instalar as dependências**

```bash
pip install -r requirements.txt
```

---

4. **Rodar a aplicação**

```bash
uvicorn app.main:app --reload
```

--

6. **Acessar no navegador**

Documentação Swagger:[Doc](http://127.0.0.1:8000/docs)

Documentação Redoc: [Doc](http://127.0.0.1:8000/redoc)

--

## 🗺 Roadmap Inicial (Sprints)

**Sprint 1**
  Estrutura base do projeto com FastAPI.
  
  Rota de teste (/health).
  
  Configuração de autenticação JWT.
  
  CRUD básico de usuários (apenas memória, sem banco).
  
**Sprint 2**
  CRUD de imóveis.
  
  Upload de fotos (armazenamento local).
  
  Integração inicial com autenticação de usuários.

**Sprint 3**
  CRUD de visitas e contratos.
  
  Implementar permissões por nível de usuário.
  
  Preparação para integração com banco PostgreSQL.

## 📜 Licença
**Este projeto está licenciado sob a MIT License.**

## 🤝 Contribuição
Contribuições são bem-vindas!
Abra uma issue ou envie um pull request.

