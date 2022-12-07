### Aula sobre CI/CD - Evolução de Software P8

A aplicação ira consumir uma API de CEP (viacep.com.br/ws/{cep-numero}/json/) e preencher os models

- Status da branch main -> ![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/ejrgeek/aula-p8-evolucao-cicd/Aula%20P8%20CI-CD/main)
- Status da branch develop -> ![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/ejrgeek/aula-p8-evolucao-cicd/Aula%20P8%20CI-CD/develop)

---

### Setup:
Requisitos -> dev:
* Python 3.10+
* SQLite3

Requisitos -> homol:
* Python 3.10+
* PostgreSQL 14.5+


( Homol/sem heroku) Recomendação - configurando o PostgreSQL (mude nome do banco, nome do usuário e senha):

    sudo -i -u postgres psql
    CREATE DATABASE nome_do_banco;
    CREATE USER nome_usuario WITH PASSWORD 'sua_senha';
    ALTER ROLE nome_usuario SET client_encoding TO 'utf8';
    ALTER ROLE nome_usuario SET default_transaction_isolation TO 'read committed';
    ALTER ROLE nome_usuario SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE nome_do_banco TO nome_usuario;
    
Agora você precisa clonar o repositório

    git clone link-do-repo

Depois caso queira, pode criar um novo ambiente virtual para rodar a aplicação, você pode ler aqui para saber mais caso não tenha conhecimento sobre: https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais

Depois de criado, você entra no ambiente e roda os comandos

    pip install -r requirements-dev.txt

Agora vá no arquivo *core/settings/homol.py* e altere o bloco de acordo com os dados que você criou anteriormente ou altere o arquivo *.env*:

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": config("HOMOL_DATABASE_NAME"),
            "USER": config("HOMOL_DATABASE_USERNAME"),
            "PASSWORD": config("HOMOL_DATABASE_PASSWORD"),
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }


É necessário configurar as variáveis de ambiente, siga o exemplo do arquivo *.env-sample* e crie um arquivo *.env* atribuindo os valores informados pelo engenheiro responsável. Exemplo do arquivo:
```
SECRET_KEY=
ENV=
DEBUG=

# ADDRS
ALLOWED_HOSTS=
INTERNAL_IPS=
CORS_ORIGIN_WHITELIST=
ALLOWED_CORS_ORIGIN_HOSTS=

# HOMOL DATABASE
HOMOL_DATABASE_NAME=
HOMOL_DATABASE_USERNAME=
HOMOL_DATABASE_PASSWORD=

# SENTRY KEY
SENTRY_KEY=

# REDIS
REDIS=redis://redis:6379/0

# APP VERSION
VERSION=0.0.0+build-setup
```

Pronto, agora rode os comandos:

    python manage.py makemigrations
    python manage.py migrate
    

Para fazer a migração das tabelas do banco de dados baseados nos Models do Django gerado pelo ORM. Depois você pode rodar o comando para criar um super usuario:
    
    python manage.py createsuperuser

Depois você pode rodar um:

    python manage.py runserver
    
A aplicação está no ar (localmente pelo menos rs). Ainda é necessário algumas configurações.

Caso você deseje fazer consumo da Api, pesque no arquivo *core/settings/base.py* a lista **CORS_ORIGIN_WHITELIST** e adicione o endereço:porta na lista para não ter problemas.

Para os testes nos models você precisa usar um token válido, foi utilizado o [Faker](https://faker.readthedocs.io/en/master/) para gerar dados fictícios, TestCase do Django. 

Para rodar os testes, use o comando *python manage.py test*.

