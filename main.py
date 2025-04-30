from functions.loader import carregar_conteudo_pdfs
from functions.chat_logic import inicializar_chat, responder
from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente
load_dotenv()
chat = inicializar_chat()
conteudo = carregar_conteudo_pdfs()

# Caminhos de histórico
caminho_historico = os.path.join("data", "history", "historico.txt")
os.makedirs(os.path.dirname(caminho_historico), exist_ok=True)

# Carrega histórico anterior, se existir
def carregar_historico():
    mensagens = []
    if os.path.exists(caminho_historico):
        with open(caminho_historico, "r", encoding="utf-8") as f:
            linhas = f.readlines()
            for i in range(0, len(linhas), 3):  # A cada 3 linhas: pergunta, resposta, quebra
                if i + 1 < len(linhas):
                    pergunta = linhas[i].replace("Usuário: ", "").strip()
                    resposta = linhas[i + 1].replace("JurandirBot: ", "").strip()
                    mensagens.append(("user", pergunta))
                    mensagens.append(("assistant", resposta))
    return mensagens

# Salva nova interação
def salvar_interacao(usuario, resposta):
    with open(caminho_historico, "a", encoding="utf-8") as f:
        f.write(f"Usuário: {usuario}\n")
        f.write(f"JurandirBot: {resposta}\n\n")

# Início
print("🧓 Fala, meu chapa! Aqui é o JurandirBot, o rei dos PDFs e das respostas.")
print("Tô de volta e lembro da nossa última resenha, viu?")
print('Digite "x" para sair.\n')

mensagens = carregar_historico()

while True:
    entrada = input("Você: ")
    if entrada.lower().strip() == "x":
        break

    mensagens.append(("user", entrada))
    resposta = responder(chat, mensagens, conteudo)
    mensagens.append(("assistant", resposta))

    print(f"\n📘 JurandirBot: {resposta}\n")
    salvar_interacao(entrada, resposta)

print("\n📂 Histórico atualizado em 'data/history/historico.txt'")
print("👋 Até mais, parceiro! JurandirBot se despede com sabedoria.")
