
# 💳 Azure Credit Card Reader com Streamlit

Este projeto implementa uma aplicação web interativa para a **validação e extração automatizada de dados de cartões de crédito** a partir de imagens.

A aplicação utiliza serviços de Inteligência Artificial do Azure para processar o upload de imagens de cartões, extrair dados críticos (nome do titular, número e validade) e exibir o resultado em tempo real em um dashboard Streamlit.

---

## 🎯 Funcionalidades e Objetivo

O objetivo principal desta aplicação é utilizar o poder da **Inteligência Artificial (IA) da Microsoft** para realizar a **análise e validação automatizada de imagens de cartões de crédito**.

O aplicativo faz o seguinte:
1.  **Processa Imagens:** Permite ao usuário carregar uma imagem (upload) de um cartão.
2.  **Extração de IA:** Envia o arquivo para o **Azure Document Intelligence** para processamento.
3.  **Estrutura Dados:** Extrai e estrutura dados críticos como o nome do titular, número do cartão e data de validade.
4.  **Exibe o Resultado:** Apresenta os dados extraídos em uma **interface web Streamlit**, simulando um processo de verificação rápida ou triagem de documentos.

---

## ✨ Tecnologias Utilizadas

| Tecnologia | Finalidade |
| :--- | :--- |
| **Python 3.x** | Linguagem principal do projeto. |
| **Streamlit** | Framework para construção da interface web e dashboard. |
| **Azure Document Intelligence** | Serviço de IA para análise e extração de dados de documentos. |
| **Azure Blob Storage** | Serviço utilizado para gerenciar o upload e acesso às imagens via URL. |
| **`python-dotenv`** | Gerenciamento seguro das chaves de acesso. |

---

## ⚙️ Como Rodar o Projeto Localmente

Siga estas instruções para configurar e executar a aplicação em sua máquina local.

### 1. Pré-requisitos

* **Python 3.8+** instalado.
* Credenciais ativas para **Azure Document Intelligence** (KEY e ENDPOINT).
* Credenciais ativas para **Azure Storage** (STRING DE CONEXÃO).

### 2. Configuração e Execução

Clone o repositório para sua máquina local e navegue até a pasta:

```
git clone [https://github.com/valdineibucmaier/azure-credit-card-reader.git](https://github.com/valdineibucmaier/azure-credit-card-reader.git)
cd azure-credit-card-reader

#Ambiente e Dependências
Crie e ative um ambiente virtual (venv) e instale as bibliotecas necessárias:

# Cria o ambiente virtual
python -m venv venv

# Ativa o ambiente (Windows PowerShell)
.\venv\Scripts\activate

# Instala todas as dependências
pip install -r requirements.txt

#Configuração das Chaves de Acesso
Renomeie o arquivo env.example para .env.

Preencha o arquivo .env com suas credenciais reais do Azure:

Snippet de código

# Conteúdo do seu arquivo .env
ENDPOINT="SUA_URL_DO_COGNITIVE_SERVICE"
SUBSCRIPTION_KEY="SUA_CHAVE_SECRETA_DA_AZURE"
AZURE_STORAGE_CONNECTION_STRING="SUA_STRING_DE_CONEXAO_DO_BLOB_STORAGE"
CONTAINER_NAME="cartoes"

# Execução do Aplicativo
Com o ambiente ativado e as chaves configuradas, execute o Streamlit a partir da raiz do projeto:
streamlit run src/app.py
O aplicativo será aberto automaticamente no seu navegador, geralmente em http://localhost:8501.
