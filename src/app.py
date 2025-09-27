
import streamlit as st
from services.blob_service import upload_to_blob
from services.credit_service import analise_credit_card

def configure_interface():
    st.title("Upload de arquivo DIO - Desafio 1 - Azure - Fake Docs")
    uploaded_file = st.file_uploader("Escolha um arquivo para fazer o upload", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        #Envia o arquivo para o Azure Blob Storage
        blob_url = upload_to_blob(uploaded_file, fileName)
        if blob_url:
            st.success(f"Arquivo {fileName} enviado com sucesso!")
            credit_card_info = analise_credit_card(blob_url)
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Falha no upload do arquivo {fileName}.")


def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada",use_container_width=True)
    st.write("Resultado da validação do cartão de crédito:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartão Válido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Cartão: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")       
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartão Inválido</h1>", unsafe_allow_html=True)
        st.write("Este cartão é inválido ou não pôde ser processado.")


if __name__ == "__main__":
    configure_interface()
