
import streamlit as st
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="B3 Analytics", layout="wide")

st.title("B3 Analytics")
st.write("Histórico de preços de Ações e Criptomoedas")

tipoticker = st.selectbox(
    "Tipo de ativo",
    ["Criptomoeda", "Ação"]
)

tipo = tipoticker

ticker = st.text_input("Código do ativo", value="").strip().upper()

periodo = st.selectbox(
    "Período",
    ["1 mês", "3 meses", "6 meses", "1 ano", "6 anos"]
)

periodos = {
    "1 mês": "1mo",
    "3 meses": "3mo",
    "6 meses": "6mo",
    "1 ano": "1y",
    "6 anos": "6y"
}

if st.button("Consultar Ativo"):
    if tipo == "Criptomoeda":
        codigo = ticker
        
        with st.spinner("Buscando histórico..."):
            dados = yf.Ticker(codigo).history(
                period=periodos[periodo],
                auto_adjust=True
            )

        if dados.empty:
            st.error("Não foi possível encontrar os dados dessa ação.")
        else:
            grafico = px.line(
                dados,
                x=dados.index,
                y="Close",
                title=f"Variação de {ticker} em {periodo}",
                labels={"Close": "Preço (R$)", "Date": "Data"}
            )

            grafico.update_layout(
                xaxis_title="Data",
                yaxis_title="Preço (R$)",
                hovermode="x unified"
            )

            st.plotly_chart(grafico, use_container_width=True)


    else:
        
        codigo = ticker if ticker.endswith(".SA") else ticker + ".SA"
        
        with st.spinner("Buscando histórico..."):
            dados = yf.Ticker(codigo).history(
                period=periodos[periodo],
                auto_adjust=True
            )

        if dados.empty:
            st.error("Não foi possível encontrar os dados dessa ação.")
        else:
            grafico = px.line(
                dados,
                x=dados.index,
                y="Close",
                title=f"Variação de {ticker} em {periodo}",
                labels={"Close": "Preço (R$)", "Date": "Data"}
            )

            grafico.update_layout(
                xaxis_title="Data",
                yaxis_title="Preço (R$)",
                hovermode="x unified"
            )

            st.plotly_chart(grafico, use_container_width=True)
