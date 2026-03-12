from colorama import Fore, init

init()

def responder(pergunta):

    if "erro" in pergunta:
        return "Verifique a indentação, parênteses ou possíveis erros de sintaxe."

    elif "print" in pergunta:
        return "A função print() é usada para exibir informações na tela."

    elif "loop" in pergunta or "for" in pergunta or "while" in pergunta:
        return "Loops são usados para repetir um bloco de código."

    elif "lista" in pergunta:
        return "Listas armazenam vários valores em uma única variável. Exemplo: lista = [1,2,3]"

    elif "python" in pergunta:
        return "Python é uma linguagem muito usada em automação, web, dados e IA."

    elif "gerar código" in pergunta or "codigo" in pergunta:

        instrucao = input(Fore.YELLOW + "Descreva o código que você quer gerar: ")

        return gerar_codigo(instrucao)

    elif pergunta == "analisar":

        codigo = input(Fore.YELLOW + "Cole seu código Python: ")

        return analisar_codigo(codigo)

    elif pergunta == "ajuda":
        return """
Comandos disponíveis:
- erro
- print
- loop
- lista
- python
- gerar codigo
- analisar
- sair
"""

    else:
        return "Ainda estou aprendendo. Digite 'ajuda'."


def gerar_codigo(instrucao):

    if "soma" in instrucao:
        return """
Exemplo de função de soma em Python:

def soma(a, b):
    return a + b
"""

    elif "tabuada" in instrucao:
        return """
Exemplo de tabuada em Python:

for i in range(1,11):
    print(i)
"""

    else:
        return "Ainda não sei gerar esse código."


def analisar_codigo(codigo):

    if "print(" not in codigo:
        return "⚠ Talvez você tenha esquecido de usar print()"

    elif "==" in codigo:
        return "✔ Parece que você está usando comparação."

    elif "for" in codigo:
        return "✔ Você está usando um loop."

    else:
        return "Código analisado. Parece correto."


print(Fore.GREEN + "🤖 Assistente Python iniciado!")
print(Fore.YELLOW + "Digite 'ajuda' para ver os comandos ou 'sair' para encerrar.\n")

while True:

    pergunta = input(Fore.CYAN + "Você: ").lower()

    if pergunta == "sair":
        print(Fore.RED + "Assistente: Até logo! Bons estudos em Python 🚀")
        break

    resposta = responder(pergunta)

    print(Fore.MAGENTA + "Assistente:", resposta)