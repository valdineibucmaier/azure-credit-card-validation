import os
from azure.storage.blob import BlobServiceClient
import streamlit as st
from utils.config import Config


def upload_to_blob(file, file_name):
    try:
        # Cria o cliente do BlobService
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORAGE_CONNECTION_STRING)
        
        # Obtém o cliente do contêiner
        container_client = blob_service_client.get_container_client(Config.CONTAINER_NAME)
        
        # Faz o upload do arquivo
        blob_client = container_client.get_blob_client(file_name)
        blob_client.upload_blob(file, overwrite=True)
        
        # Retorna a URL do blob
        blob_url = f"{blob_client.url}"
        return blob_url
    except Exception as e:
        st.error(f"Erro ao fazer upload para o Azure Blob Storage: {e}")
        return None