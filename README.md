
# Sistema de Eventos – Projeto Python + MySQL

Sistema desenvolvido em Python utilizando arquitetura com o padrão DAO (Data Access Object) e banco de dados MySQL.

## 📌 Pré-requisitos

Antes de rodar o projeto, certifique-se de ter instalado em sua máquina:

* ✅ **Python 3.10+**
* ✅ **MySQL Server**
* ✅ **MySQL Workbench** (opcional, mas recomendado para gerenciamento visual)
* ✅ **Git**

---

## Instalação e Configuração

### Clonar o Projeto

Abra o seu terminal e execute os comandos abaixo para clonar o repositório e entrar na pasta do projeto:

```bash
git clone https://github.com/GeoPorto/Sistema-de-Eventos-IFSP
cd Sistema-de-Eventos-IFSP

```

### Criar e Ativar o Ambiente Virtual (Recomendado)

Use o comando correspondente ao seu sistema operacional:

**No Windows:**

```cmd
python -m venv venv
venv\Scripts\activate

```

**No Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### Instalar Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias a partir do arquivo `requirements.txt`:

```bash
pip install -r requirements.txt

```

---

## Configurar Banco de Dados

### Criar o Banco e as Tabelas

Abra o **MySQL Workbench** ou o terminal do MySQL e execute o script SQL presente na pasta do projeto (verifique o arquivo de script dentro de `sql - tabelas/`).

### Configurar as Variáveis de Ambiente

Na raiz do projeto, altere o arquivo `.env` e adicione as seguintes credenciais para a conexão:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=db_eventos

```

> ⚠️ **Atenção:** Lembre-se de alterar `sua_senha` pela senha real configurada no seu MySQL.

---

## Executar o Projeto

Após configurar o ambiente e o banco de dados, rode o arquivo principal na raiz do projeto:

```bash
python menu.py

```
