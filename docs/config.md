# Configuração 

Este repositório foi configurado utilizando o gerenciador de pacotes e dependências [Poetry](https://python-poetry.org), visando sua fácil configuração de diferentes grupos de dependências, facilitando a criação de seções de documentação, testes, e linters.

Portanto, a configuração foi feita através do seguinte processo: 

```
1. Para criar o diretório e estrutura básica do projeto: 
  poetry new mvc-scrapping

2. Para instalar as dependências de desenvolvimento:
  poetry add --group dev pytest
  poetry add --group dev pytest-cov
  poetry add --group dev blue
  poetry add --group dev isort
  poetry add --group dev taskipy

3. Para instalar as dependências de documentação:
  poetry add --group dev mkdocs-material
  poetry add --group dev pytest-cov

4. Para instalar a dependências de teste:

```