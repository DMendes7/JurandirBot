import os
from langchain_community.document_loaders import PyPDFLoader

def carregar_conteudo_pdfs(pasta="data"):
    conteudo_total = ""
    for arquivo in os.listdir(pasta):
        if arquivo.lower().endswith(".pdf"):
            caminho = os.path.join(pasta, arquivo)
            try:
                loader = PyPDFLoader(caminho)
                paginas = loader.load()
                conteudo_total += f"\n\n===== {arquivo} =====\n\n"
                conteudo_total += "\n".join([p.page_content for p in paginas])
            except Exception as e:
                print(f"❌ Erro ao carregar {arquivo}: {e}")
    return conteudo_total
