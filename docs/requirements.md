# Requisitos do Projeto

Este projeto tem como objetivo a criação de um scrapper para coletar e anonimizar dados do Reddit de maneira eficiente e ética.

## Requisitos Funcionais

1. **Coletar dados de postagens do Reddit**
    - O sistema deve ser capaz de coletar postagens de um subreddit, de acordo com os critérios de "top posts".
    
2. **Coletar dados de comentários**
    - O sistema deve coletar os comentários das publicações.

3. **Anonimizar informações**
    - O sistema deve anonimizar o nome dos autores de postagens e comentários utilizando um hash (SHA-256).
    - O sistema deve substituir URLs presentes nos textos das postagens e comentários por "[REDACTED]".

4. **Salvar dados anonimizados**
    - O sistema deve salvar os dados anonimizados em formatos `CSV` e `JSON`.

## Requisitos Não Funcionais

1. **Manutenibilidade**
    - O código deve ser modular e seguir a arquitetura hexagonal, permitindo que novos adaptadores sejam facilmente implementados.
    
2. **Testabilidade**
    - O código deve ser testado com testes unitários utilizando `pytest`.

3. **Documentação**
    - O projeto deve incluir documentação clara sobre como configurar, executar e testar a aplicação.
