# Prototype Reddit Scrapper 

## Objetivo do projeto

O presente projeto é um mínimo produto viável (MVP) construído para validar a viabilidade e eficiência técnica em scrappar a rede social Reddit através da biblioteca [Python Reddit API Wrapper](https://praw.readthedocs.io/en/stable/). O objetivo é coletar postagens e comentários de um subreddit e anonimizá-los.

### Sumário
- [Configuração do projeto](./config.md)
- [Uso da Aplicação](./docs/usage.md)
- [Requisitos do Projeto](./docs/requirements.md)
- [Testes](./docs/tests.md)

## Estrutura do Projeto
A arquitetura do projeto segue o padrão de arquitetura hexagonal (Ports and Adapters), o que permite um design desacoplado e fácil de manter.

1. /adapters
    - Implementações externas (PRAW e persistência de dados) 

2. /domain 
    - Lógica central do projeto 

3. /ports 
    - Interfaces (Portas) que conectam o domínio às dependências externas 

4. Testes do projeto 
    - /tests 

5. main.py 
    - Ponto de entrada da aplicação
