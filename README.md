# Pokédex com Django

Projeto web desenvolvido com **Python e Django**, integrado à [PokéAPI](https://pokeapi.co/) para consultar informações sobre Pokémon.

## Funcionalidades

- Busca de Pokémon por nome ou número.
- Exibição de imagem, altura, peso, tipos e atributos básicos.
- Tradução dos tipos e atributos para português.
- Listagem de Pokémon com paginação de 10 itens por página.
- Interface responsiva em HTML e CSS.
- Tratamento de Pokémon não encontrados.

## Tecnologias

- **Python** e **Django** — aplicação web.
- **HTML** e **CSS** — interface.
- **Requests** — consumo de API REST.
- **PokéAPI** — dados dos Pokémon.

## Como executar

Requisitos: **Python 3.12 ou superior**.

1. Clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:

   - Windows (PowerShell): `venv\Scripts\Activate.ps1`
   - Windows (Prompt): `venv\Scripts\activate.bat`
   - Linux/macOS: `source venv/bin/activate`

5. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

6. Execute as migrações:

   ```bash
   python manage.py migrate
   ```

7. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

8. Acesse **http://127.0.0.1:8000/**.

> A consulta depende de acesso à internet e da disponibilidade da PokéAPI.

## Configurações

Para desenvolvimento local, o projeto usa configurações padrão de desenvolvimento. Para ambientes públicos, defina `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False`, `DJANGO_ALLOWED_HOSTS` (hosts separados por vírgula) e configure HTTPS, segurança e distribuição dos arquivos estáticos adequadamente.

O banco SQLite local, a pasta `venv/` e arquivos temporários não são versionados.

## Sobre o projeto

Este projeto foi desenvolvido para praticar desenvolvimento web com Django, integração com APIs e construção de interfaces usando HTML e CSS.
