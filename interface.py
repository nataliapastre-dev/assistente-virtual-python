import tkinter as tk


def responder(pergunta):

    pergunta = pergunta.lower()

    if "erro" in pergunta:
        return "Verifique a indentação ou erros de sintaxe no código."

    elif "print" in pergunta:
        return "print() serve para mostrar informações na tela."

    elif "loop" in pergunta or "for" in pergunta or "while" in pergunta:
        return "Loops repetem um bloco de código várias vezes."

    elif "lista" in pergunta:
        return "Listas armazenam vários valores em uma única variável. Exemplo: lista = [1,2,3]"

    elif "python" in pergunta:
        return "Python é uma linguagem muito usada em automação, dados, inteligência artificial e desenvolvimento web."

    elif "java" in pergunta:
        return "Java é uma linguagem muito usada em aplicações empresariais, Android e sistemas grandes."

    elif "chatgpt" in pergunta or "chat gpt" in pergunta:
        return "ChatGPT é um assistente de inteligência artificial que ajuda a responder perguntas e gerar textos ou código."

    elif "inteligencia artificial" in pergunta or "ia" in pergunta:
        return "Inteligência Artificial é a área da tecnologia que cria sistemas capazes de aprender e tomar decisões."

    elif "dados" in pergunta:
        return "Análise de dados envolve coletar, processar e interpretar informações para ajudar na tomada de decisões."

    elif "tecnologia" in pergunta:
        return "Tecnologia envolve ferramentas e sistemas que ajudam a resolver problemas e melhorar processos."

    elif "programação" in pergunta:
        return "Programação é o processo de escrever instruções que um computador pode executar."

    else:
        return "Ainda estou aprendendo, mas posso conversar sobre programação, tecnologia, IA e dados."
def enviar(event=None):

    pergunta = entrada.get()

    if pergunta.strip() == "":
        return

    chat.config(state="normal")

    chat.insert(tk.END, "👤 Você: " + pergunta + "\n")

    resposta = responder(pergunta)

    chat.insert(tk.END, "🤖 Assistente: " + resposta + "\n\n")

    chat.config(state="disabled")

    entrada.delete(0, tk.END)

    chat.see(tk.END)


janela = tk.Tk()
janela.title("🤖 Python Dev Assistant")
janela.geometry("500x400")


chat = tk.Text(janela, height=20, width=60, state="disabled")
chat.pack(pady=10)


entrada = tk.Entry(janela, width=40)
entrada.pack(pady=5)

entrada.bind("<Return>", enviar)


botao = tk.Button(janela, text="Enviar", command=enviar)
botao.pack()


janela.mainloop()