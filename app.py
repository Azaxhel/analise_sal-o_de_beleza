import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configurações iniciais
st.set_page_config(page_title="Dashboard - Salão de Beleza", layout="wide")
st.title("💇 Dashboard de Análise - Salão de Beleza")

# Carregamento de dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv("atendimentos_salao.csv")
    df["Data"] = pd.to_datetime(df["Data"])
    df["Dia da Semana"] = df["Data"].dt.day_name()
    df["Mes"] = df["Data"].dt.month_name()
    df["Mes_Num"] = df["Data"].dt.month
    return df

df = carregar_dados()

# KPIs principais
col1, col2, col3 = st.columns(3)
col1.metric("Faturamento Total (R$)", f"{df['Valor'].sum():.2f}")
col2.metric("Atendimentos", df.shape[0])
col3.metric("Ticket Médio (R$)", f"{df['Valor'].mean():.2f}")

st.markdown("---")

# Gráficos
st.subheader("Serviços Mais Realizados")
servico_count = df["Serviço"].value_counts().reset_index()
servico_count.columns = ["Serviço", "Quantidade"]
fig1, ax1 = plt.subplots()
sns.barplot(data=servico_count, x="Serviço", y="Quantidade", ax=ax1)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)
st.pyplot(fig1)

st.subheader("Distribuição por Profissional")
fig2, ax2 = plt.subplots()
sns.countplot(data=df, x="Profissional", ax=ax2)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
st.pyplot(fig2)

st.subheader("Atendimentos por Dia da Semana")
dias = df["Dia da Semana"].value_counts().reindex(
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
).dropna().reset_index()
dias.columns = ["Dia", "Atendimentos"]
fig3, ax3 = plt.subplots()
sns.barplot(data=dias, x="Dia", y="Atendimentos", ax=ax3)
ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
st.pyplot(fig3)

st.subheader("Evolução do Faturamento Mensal")
faturamento_mensal = df.groupby(["Mes_Num", "Mes"])["Valor"].sum().reset_index()
faturamento_mensal = faturamento_mensal.sort_values("Mes_Num")
fig4, ax4 = plt.subplots()
sns.lineplot(data=faturamento_mensal, x="Mes", y="Valor", marker="o", ax=ax4)
st.pyplot(fig4)

# Botão para baixar o relatório em PDF
with open("relatorio_salao_beauty_final_clean.pdf", "rb") as pdf_file:
    st.download_button(
        label="📄 Baixar Relatório em PDF",
        data=pdf_file,
        file_name="relatorio_salao_beauty_final_clean.pdf",
        mime="application/pdf"
    )

st.markdown("---")
st.caption("Projeto com dados fictícios para fins educacionais e de portfólio.")
