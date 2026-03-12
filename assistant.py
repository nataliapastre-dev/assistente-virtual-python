def responder(pergunta):

    if "erro" in pergunta:
        return "Verifique a indentação ou erros de sintaxe."

    elif "print" in pergunta:
        return "print() exibe informações na tela."

    elif "loop" in pergunta:
        return "Loops repetem blocos de código."

    elif "lista" in pergunta:
        return "Listas armazenam múltiplos valores."

    else:
        return "Ainda estou aprendendo."