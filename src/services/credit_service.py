from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.config import Config

def analise_credit_card(card_url):
   
    credential = AzureKeyCredential(Config.KEY)
    document_Client = DocumentIntelligenceClient(endpoint=Config.ENDPOINT, credential=credential)
    card_info = document_Client.begin_analyze_document("prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
    result = card_info.result()
        

    for document in result.documents:
        fields = document.get("fields",{})
        return{
            "card_name": fields.get("CardHolderName").content if fields.get("CardHolderName") else None,
            "card_number": fields.get("CardNumber").content if fields.get("CardNumber") else None,
            "expiry_date": fields.get("ExpirationDate").content if fields.get("ExpirationDate") else None,
            "bank_name": fields.get("IssuingBank").content if fields.get("IssuingBank") else None,
        }  
    
       
                                                        

