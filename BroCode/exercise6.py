def achar_palavra(texto, palavra):
    inicio = texto.rfind(palavra)
    if inicio == -1:
        return "Palavra não encontrada"
    else:
        fim = inicio + len(palavra)
        return texto[inicio: fim]

texto = "Python é fácil de aprender. Python é versátil. Python é poderoso."


palavra_substituir = "Python"
nova_palavra = "Programa"


ultima_ocorrencia = achar_palavra(texto, palavra_substituir)

if ultima_ocorrencia != "Palavra não encontrada":
    texto_corrigido = texto.replace(ultima_ocorrencia, nova_palavra)
    print(texto_corrigido)
else:
    print("Palavra não encontrada.")
