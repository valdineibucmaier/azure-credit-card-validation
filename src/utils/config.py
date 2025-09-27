import os 
from dotenv import load_dotenv
load_dotenv()

class Config:
    # URL base para um serviço, frequentemente usado em APIs
    ENDPOINT = os.getenv("ENDPOINT")
    
    # Chave secreta necessária para autenticação em um serviço
    KEY = os.getenv("SUBSCRIPTION_KEY")
    
    # String de conexão completa para acessar o Azure Blob Storage
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    
    # Nome do contêiner dentro do Azure Storage que será utilizado
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")