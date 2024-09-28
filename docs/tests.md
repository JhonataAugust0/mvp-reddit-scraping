# Testes do Projeto Prototype Reddit Scrapper

Este documento fornece uma visão geral dos testes implementados nesse projeto, falando sobre suas configurações,propósito, e execução.

## Sumário
- [Testes do Projeto Prototype Reddit Scrapper](#testes-do-projeto-prototype-reddit-scrapper)
  - [Sumário](#sumário)
  - [Configuração de Ambiente](#configuração-de-ambiente)
    - [Passo a Passo:](#passo-a-passo)
  - [Tipos de Testes](#tipos-de-testes)
    - [Testes de Coleta de Dados (Mock do PRAW)](#testes-de-coleta-de-dados-mock-do-praw)
    - [Testes de Anonimização](#testes-de-anonimização)
    - [Testes de Persistência](#testes-de-persistência)
    - [Testes de Integração](#testes-de-integração)
  - [Como Executar os Testes](#como-executar-os-testes)

---

## Configuração de Ambiente

Os testes foram configurados usando a biblioteca **pytest** com suporte para carregar variáveis de ambiente do arquivo `.env` através da biblioteca **python-dotenv**. Isso permite que os testes acessem variáveis sensíveis como credenciais da API do Reddit sem a necessidade de as definir diretamente no código.

### Passo a Passo:

1. Instale as dependências de teste e desenvolvimento:
  ```
  bash
  poetry add --group dev pytest pytest-cov python-dotenv
  ```

2. Crie um arquivo `.env` na raiz do projeto para armazenar as credenciais da API do Reddit:
  ```
  CLIENT_ID=your_client_id
  CLIENT_SECRET=your_client_secret
  USER_AGENT=your_user_agent
  ```

3. O arquivo `conftest.py` carrega automaticamente o arquivo `.env` para disponibilizar as variáveis nos testes.

```python
# tests/conftest.py
from dotenv import load_dotenv
import pytest

@pytest.fixture(scope='session', autouse=True)
def load_env():
    """Carrega variáveis de ambiente do arquivo .env para todos os testes"""
    load_dotenv()
```

## Tipos de Testes
Os testes cobrem diferentes aspectos do sistema, desde a coleta de dados, até a anonimização e a persistência.

### Testes de Coleta de Dados (Mock do PRAW)

Estes testes garantem que a API do Reddit está sendo corretamente chamada e que os dados estão sendo coletados e processados. Para evitar fazer chamadas reais para o Reddit, o que pode ser lento e imprevisível, usamos mocking para simular o comportamento da API.

**Arquivo**: tests/test_reddit_praw_adapter.py   
**Objetivo**:   
 - Simular a coleta de dados de subreddits sem fazer chamadas reais à API do Reddit.   
 - Garantir que as postagens e comentários são corretamente anonimizados durante a coleta.

### Testes de Anonimização
Estes testes verificam se os dados de autor e URLs são devidamente anonimizados, preservando a privacidade dos usuários cujas postagens e comentários são coletados.

**Arquivo**: tests/test_anonymization.py   
**Objetivo**:   
 - Garantir que o nome do autor é substituído por um hash seguro.   
 - Verificar se URLs são removidas corretamente do texto.


### Testes de Persistência
Esses testes garantem que os dados anonimizados são corretamente salvos em arquivos CSV e JSON.

**Arquivo**: tests/test_storage_adapter.py   
**Objetivo**:   
 - Verificar se os dados são salvos corretamente nos formatos CSV e JSON.   
 - Validar que o conteúdo salvo corresponde ao esperado.

### Testes de Integração
Os testes de integração garantem que todo o fluxo do sistema, desde a coleta de dados até a anonimização e salvamento, funcione corretamente como um todo.

**Arquivo**: tests/test_integration.py   
**Objetivo**:   
Simular o fluxo completo de scraping, anonimização e persistência, garantindo que todos os componentes funcionem juntos.
Verificar se os dados finais anonimizados são armazenados corretamente.

## Como Executar os Testes
Para realizar os testes, execute o seguinte comando:   
```
bash   
task test
```

Se caso bem sucedido, isso gerará um relatório de cobertura em htmlcov/, mostrando quais partes do código foram cobertas pelos testes. Do contrário, os testes serão interrompidos no ponto de erro.

