# Configuração do Projeto

Este repositório foi configurado utilizando o gerenciador de pacotes e dependências [Poetry](https://python-poetry.org), visando sua fácil configuração e gerenciamento de diferentes grupos de dependências, como desenvolvimento, documentação e testes.

## Estrutura do Projeto

1. Para criar o diretório e estrutura básica do projeto:
  ```
  bash
  poetry new mvp-scrapping
  ```

2. Para instalar as dependências de desenvolvimento:
  ```
  bash
  poetry add --group dev pytest pytest-cov blue isort taskipy python-dotenv
  ```

3. Para instalar as dependências de documentação:
  ```
  bash
  poetry add --group dev mkdocs-material mkdocstrings mkdocstrings-python
  ```

4. Dependências do projeto:
  ```
  bash
  poetry add praw pandas
  ```

5. Para rodar os testes:
  ```
  bash
  task test
  ```

6. Para rodar os linters:
  ```
  bash
  task lint
  ```

## Como Executar
1. Clone o repositório
```
bash 
git clone https://github.com/JhonataAugust0/mvc-scrapping.git
```

2. Acesse o repositório
```
bash 
cd /mvc-scrapping/
```

3. Configure suas credenciais da API do Reddit no arquivo .env.

2. Execute o script principal:
```bash
poetry run python mvc-scrapping/app/main.py
```
O script coletará os dados anonimizados e salvará em um arquivo reddit_skeptic_posts.csv e reddit_skeptic_posts.json.