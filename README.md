
# 🤖 JurandirBot – O véi dos PDF!

<img src="img/Jurandir.png" alt="JurandirBot" width="250" align="right">

🧓 E aí, meu chapa! Eu sou o **JurandirBot**, seu companheiro digital de café e conversa inteligente.

Me programaram com um jeitão carismático, mas com os parafuso tudo apertado com IA de última geração. Eu não só sei bater papo, como também **leio qualquer PDF que você jogar na minha pasta `data/`** — seja aula, receita de bolo, ou até aquele relatório secreto que ninguém lê (eu leio 😎).

---

## 📚 O que eu faço?

- 🧠 Respondo perguntas com base nos PDFs da pasta `data/`
- 🤓 Mantenho o **histórico de tudo que você me pergunta** (pra não ter que repetir igual vó com neto)
- 💬 Falo como um bom mineiro velho: direto, educado e sempre disposto a ajudar
- 🔧 Sou movido a LLaMA 3 com Groq, mas com coração de avô e voz de professor de cursinho

---

## 🧪 Mas pra quê isso tudo?

Ah, é só um **projetinho de aprendizado**, sô...  
A turma aqui tá testando umas tecnologias novas aprendidas num curso arretado sobre Python e IA, e eu tô aqui pra mostrar que a teoria vira prática com jeitinho.

---

## 🛠️ Como usar o JurandirBot?

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/JurandirBot.git
   cd JurandirBot
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Crie o arquivo `.env` e coloque sua chave da Groq:
   ```
   GROQ_API_KEY=sua_chave_aqui
   ```

4. Coloque seus PDFs na pasta `data/`

5. E roda eu aí:
   ```bash
   python main.py
   ```

---

## 🗂️ Estrutura do projeto

```
JurandirBot/
├── data/
│   ├── aula1.pdf
│   └── history/
│       └── historico.txt
├── functions/
│   ├── loader.py
│   └── chat_logic.py
├── img/
│   └── Jurandir.png
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## 💾 Curiosidade

Toda vez que você conversa comigo, eu anoto tudinho no arquivo `data/history/historico.txt`. Assim a gente continua o papo de onde parou.

---

## 🧓 Considerações finais

Pode me chamar de Jurandir, mas **pode confiar em mim igual a um avô com memória boa e Wi-Fi forte**.  
Se tiver PDF, eu leio. Se tiver pergunta, eu respondo. Se tiver bug... a culpa não é minha não, viu? Foi o estagiário!

---

Feito com café e LLaMA 3 ☕🚀
