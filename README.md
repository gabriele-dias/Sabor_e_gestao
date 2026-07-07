# Sabor e Gestão

Projeto inicial em Django para a gestão de produtos e operações do restaurante/empresa Sabor e Gestão.

## Visão geral

Este repositório contém a base inicial de um sistema web desenvolvido com Django, com foco na organização e gestão de produtos.

## Status atual

Até o momento, foram implementados os seguintes pontos:

- Estrutura inicial do projeto Django criada.
- Aplicativo principal configurado em `core`.
- Modelo `Produto` criado com os campos `nome` e `preco`.
- Registro do modelo no painel administrativo.
- Configuração inicial das rotas do projeto.
- Migrações iniciais já disponibilizadas no repositório.

## Tecnologias utilizadas

- Python
- Django
- SQLite

## Requisitos

- Python 3.10 ou superior
- Django
- Ambiente virtual (recomendado)

## Como executar o projeto

1. Entre na pasta do projeto:
   ```powershell
   cd C:\Users\taboo\Sabor_e_gestao
   ```

2. Ative o ambiente virtual:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Instale as dependências:
   ```powershell
   python -m pip install django
   ```

4. Aplique as migrações:
   ```powershell
   python manage.py migrate
   ```

5. Crie um superusuário para acessar o painel administrativo:
   ```powershell
   python manage.py createsuperuser
   ```

6. Inicie o servidor:
   ```powershell
   python manage.py runserver
   ```

7. Acesse as páginas:
   - Aplicação: http://127.0.0.1:8000/
   - Painel administrativo: http://127.0.0.1:8000/admin/

## Estrutura do projeto

- `core/` - aplicação principal do sistema
- `core/models.py` - definição dos modelos
- `core/admin.py` - configuração do painel administrativo
- `core/views.py` - implementação das views
- `setup/` - configuração geral do projeto Django

## Próximos passos

- Implementar o CRUD de produtos.
- Criar telas de cadastro e listagem.
- Melhorar a experiência no painel administrativo.
- Expandir as funcionalidades de gestão.

Este README será atualizado conforme o projeto evoluir.
