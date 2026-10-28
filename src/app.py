import streamlit as st
from agent import answer, load_data, summary, brl

st.set_page_config(page_title="BIA Planeja", page_icon="💬", layout="centered")
st.title("💬 BIA Planeja")
st.caption("Assistente de organização financeira — protótipo com dados fictícios")

@st.cache_data
def get_data():
    return load_data()

data = get_data()
with st.sidebar:
    st.header("Configuração")
    use_ai = st.toggle("Usar IA via API (opcional)", value=False)
    if use_ai:
        st.info("Requer OPENAI_API_KEY no ambiente ou no campo abaixo. Dados de exemplo e perguntas podem ser enviados ao provedor da API.")
        key = st.text_input("Chave API", type="password")
        model = st.text_input("Modelo", value="gpt-4.1-mini")
    else:
        key, model = None, "gpt-4.1-mini"
    st.divider()
    st.write("Fontes: arquivos da pasta `data/`.")
    st.write("A base é histórica; não há conexão bancária nem transações reais.")
    if st.button("Limpar conversa"):
        st.session_state.messages = []
        st.rerun()

s = summary(data)
a,b,c = st.columns(3)
a.metric("Entradas (out/2025)", brl(s['entradas']))
b.metric("Saídas (out/2025)", brl(s['saidas']))
c.metric("Diferença do período", brl(s['saldo']))
st.caption("Diferença calculada apenas com as transações fictícias disponíveis; não é saldo em conta.")

if "messages" not in st.session_state:
    st.session_state.messages = []
for item in st.session_state.messages:
    with st.chat_message(item["role"]):
        st.markdown(item["text"])

question = st.chat_input("Ex.: Quanto gastei em outubro de 2025?")
if question:
    st.session_state.messages.append({"role": "user", "text": question})
    with st.chat_message("user"):
        st.markdown(question)
    result, source = answer(question, data, use_ai=use_ai, api_key=key, model=model)
    rendered = result + f"\n\n*Fonte: {source}*"
    st.session_state.messages.append({"role": "assistant", "text": rendered})
    with st.chat_message("assistant"):
        st.markdown(rendered)
