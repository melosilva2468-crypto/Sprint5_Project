import streamlit as st
import pandas as pd
import plotly.express as px

# Título
st.header("Dashboard de Anúncios de Veículos")

# Descrição
st.write(
    "Este aplicativo permite explorar um conjunto de dados sobre anúncios de veículos nos Estados Unidos."
)

# Carrega os dados
car_data = pd.read_csv("vehicles_us.csv")

# Mostrar dados
if st.checkbox("Mostrar tabela de dados"):
    st.dataframe(car_data.head())

# Histograma
if st.checkbox("Mostrar histograma da quilometragem"):
    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribuição da Quilometragem"
    )
    st.plotly_chart(fig)

# Gráfico de dispersão
if st.checkbox("Mostrar gráfico de dispersão"):
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Preço x Quilometragem"
    )
    st.plotly_chart(fig)