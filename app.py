import streamlit as st
import pandas as pd
import plotly.express as px

#---- Configuração da Pagina ----
# Define o titulo da pagina, icone e o layout para ocupar a largura inteira
st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="📊",
    layout="wide"
)

# Carregamento de dados
df