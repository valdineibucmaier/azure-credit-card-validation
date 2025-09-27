# 💳 Azure Credit Card Reader com Streamlit

Este projeto demonstra uma aplicação web simples, desenvolvida em Python (Streamlit), capaz de extrair informações estruturadas de cartões de crédito a partir de imagens. A solução utiliza o serviço de **Azure Document Intelligence (Form Recognizer)** para processar documentos e o Azure Blob Storage para gerenciar o upload de imagens.

---

## 🎯 Objetivo do Projeto

O objetivo principal desta aplicação é utilizar o poder da **Inteligência Artificial (IA) da Microsoft** para realizar a **análise e validação automatizada de imagens de cartões de crédito**.

O aplicativo faz o seguinte:
1.  Permite ao usuário carregar uma imagem (upload) de um cartão.
2.  Envia o arquivo para o **Azure Document Intelligence** para processamento.
3.  **Extrai e estrutura dados críticos** como o nome do titular, número do cartão e data de validade.
4.  Exibe esses dados em uma **interface web Streamlit**, simulando um processo de verificação rápida ou triagem de documentos.

---

## ✨ Tecnologias Utilizadas

* **Python 3.x:** Linguagem principal de desenvolvimento.
* **Streamlit:** Framework para criação rápida da interface web (dashboard).
* **Azure Document Intelligence (Antigo Form Recognizer):** Serviço de IA para análise e extração de dados de documentos.
* **Azure Blob Storage:** Utilizado para armazenamento temporário das imagens enviadas.
* **`python-dotenv`:** Para gerenciamento seguro das credenciais de ambiente.

---

## ⚙️ Como Rodar o Projeto Localmente

Para clonar e executar esta aplicação em sua máquina local, siga os passos abaixo:

### 1. Pré-requisitos

* **Python 3.8+** instalado.
* Uma conta e um recurso ativo no **Azure Document Intelligence** (necessário para obter KEY e ENDPOINT).
* Uma conta de **Azure Storage** (necessário para obter AZURE_STORAGE_CONNECTION_STRING).

### 2. Configuração Inicial

Clone este repositório e navegue até o diretório:

```bash
git clone [https://github.com/valdineibucmaier/azure-credit-card-reader.git](https://github.com/valdineibucmaier/azure-credit-card-reader.git)
cd azure-credit-card-reader
