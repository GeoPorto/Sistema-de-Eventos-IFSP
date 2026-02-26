#Sistema de Eventos – Projeto Python + MySQL

Sistema desenvolvido em Python utilizando arquitetura com DAO e banco de dados MySQL.

##Pré-requisitos

Antes de rodar o projeto, você precisa ter instalado:

✅ Python 3.10+

✅ MySQL Server

✅ MySQL Workbench (opcional, mas recomendado)

✅ Git

##Clonar o Projeto

git clone https://github.com/GeoPorto/Sistema-de-Eventos-IFSP
cd Sistema-de-Eventos-IFSP

##Criar e Ativar Ambiente Virtual (Recomendado)

#Windows
python -m venv venv
venv\Scripts\activate

#Linux / Mac
python3 -m venv venv
source venv/bin/activate

##Instalar Dependências

A partir do arquivo requirements.txt:

pip install -r requirements.txt

##Configurar Banco de Dados

#Criar Banco

Abra o MySQL Workbench ou terminal MySQL e execute o script presente em *sql - tabelas/script*

##Alterar arquivo .env

Na raiz do projeto, crie um arquivo chamado:

.env

E adicione:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=db_eventos

Altere sua_senha por sua senha real do MySQL.

##Rodar o Projeto

Na raiz do Projeto, rode:

python menu.py
