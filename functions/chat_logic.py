import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate

def inicializar_chat():
    api_key = os.getenv("GROQ_API_KEY")
    return ChatGroq(model="llama3-70b-8192", api_key=api_key)

def responder(chat, mensagens, conhecimento_pdf):
    template = ChatPromptTemplate.from_messages([
        ("system", 
         "Você é o JurandirBot, um assistente carismático e bem-humorado. "
         "Você domina assuntos gerais com LLaMA e também conhece profundamente os documentos abaixo:\n\n"
         "{conteudo_pdf}\n\n"
         "Responda com clareza, simpatia e sempre de forma útil. Pode fazer resumos, tirar dúvidas e explicar conteúdos."),
        *mensagens,
        ("user", "{pergunta}")
    ])

    # A última pergunta do usuário
    ultima_pergunta = [msg[1] for msg in mensagens if msg[0] == "user"][-1]

    chain = template | chat
    return chain.invoke({
        "conteudo_pdf": conhecimento_pdf[:3000],
        "pergunta": ultima_pergunta
    }).content
