# Projeto de Registro de Aprendizado

Este é um site onde as pessoas podem registrar o que estão aprendendo. Elas podem adicionar um tema e, em seguida, registrar os progressos feitos em relação a esse tema.

## Tecnologias Usadas

- **Python**: 3.8.10
- **Django**: 4.2.19
- **Virtualenv**: Para gerenciamento de ambiente virtual

## Pré-requisitos

Antes de rodar o projeto, você precisa ter o Python 3.8.10 e o pip 20.0.2 instalados no seu computador. Também é recomendada a criação de um ambiente virtual para evitar conflitos com outros projetos.

Se você ainda não tem o Python instalado, você pode baixá-lo [aqui](https://www.python.org/downloads/release/python-3810/).

### Instalando o pip e o Virtualenv

1. Instale o pip e p virtualenv (se ainda não os tiver instalado):

   ```bash
   python -m ensurepip --upgrade
   pip install virtualenv
   ```

### Instalando o Projeto

1. Clone o repositório para o seu computador:

1.1 -Entre no diretorio principal do projeto.

2. Crie e ative um ambiente virtual (recomendado):

### No Windows:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

### No Linux/Mac:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instale as dependências do projeto:

   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados para configurar o banco de dados do projeto:
-SQLite (padrão do Django) foi o banco de dados utilizado Caso deseje usar outro banco  consulte a documentação do Django para configurações alternativas.
   
   ```bash
   python manage.py migrate
   ```

5. Se necessário, crie um superusuário para acessar o painel de administração do Django:

   ```bash
   python manage.py createsuperuser
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

## Contribuição

Sinta-se à vontade para contribuir com melhorias e novos exemplos! Para isso:

1. Faça um **fork** do repositório.
2. Crie um **branch** para suas alterações.
3. Envie um **pull request**.

---

** Qualquer dúvida, sinta-se à vontade para entrar em contato!**
