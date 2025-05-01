import streamlit as st
from functions.loader import carregar_conteudo_pdfs
from functions.chat_logic import inicializar_chat, responder
from dotenv import load_dotenv
import os

# Configurações iniciais
st.set_page_config(page_title="JurandirBot", page_icon="🤖")
st.title("🤖 JurandirBot - O véi dos PDF")
st.caption("Seu assistente carismático que entende de tudo e ainda lê seus arquivos PDF.")

# Carrega variáveis de ambiente e PDFs
load_dotenv()
chat = inicializar_chat()
conteudo_pdf = carregar_conteudo_pdfs()

# Caminho do histórico
caminho_historico = os.path.join("data", "history", "historico.txt")
os.makedirs(os.path.dirname(caminho_historico), exist_ok=True)

# Inicializa histórico de conversa
if "mensagens" not in st.session_state:
    st.session_state["mensagens"] = []

    # Carrega histórico do .txt, se existir
    if os.path.exists(caminho_historico):
        with open(caminho_historico, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            for i in range(0, len(linhas), 3):
                if i + 1 < len(linhas):
                    pergunta = linhas[i].replace("Usuário: ", "").strip()
                    resposta = linhas[i + 1].replace("JurandirBot: ", "").strip()
                    st.session_state["mensagens"].append(("user", pergunta))
                    st.session_state["mensagens"].append(("assistant", resposta))

# Se não há histórico salvo, Jurandir inicia a conversa
if not st.session_state["mensagens"]:
    mensagem_inicial = "🧓 Opa! Que bom que você chegou por aqui, meu chapa. Eu sou o JurandirBot — o véi que lê até bula de remédio em PDF. Manda sua pergunta aí que o vô responde!"
    st.session_state["mensagens"].append(("assistant", mensagem_inicial))

# Exibe todo o histórico
for remetente, conteudo in st.session_state["mensagens"]:
    if remetente == "user":
        with st.chat_message("user"):
            st.markdown(conteudo)
    else:
        with st.chat_message("assistant", avatar="img/Jurandir.png"):
            st.markdown(conteudo)

# Entrada do usuário
pergunta = st.chat_input("Digite sua pergunta aqui...")
if pergunta:
    st.chat_message("user").markdown(pergunta)
    st.session_state["mensagens"].append(("user", pergunta))

    resposta = responder(chat, st.session_state["mensagens"], conteudo_pdf)
    st.session_state["mensagens"].append(("assistant", resposta))

    with st.chat_message("assistant", avatar="img/Jurandir.png"):
        st.markdown(resposta)

    # Salva nova interação no arquivo
    with open(caminho_historico, "a", encoding="utf-8") as f:
        f.write(f"Usuário: {pergunta}\n")
        f.write(f"JurandirBot: {resposta}\n\n")
