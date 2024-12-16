def achar_palavra(texto, palavra):
    inicio = texto.rfind(palavra)
    if inicio == -1:
        return "Palavra não encontrada"
    fim = inicio + len(palavra)
    return texto[inicio: fim]

texto = input("Digite uma frase: ")
substituir = input("Qual palavra deseja substituir?")
substituicao = input("Qual palavra será usada como substituição?")

ocorrencia = achar_palavra(texto, substituir)

if ocorrencia != "Palavra não encontrada":
    novo_texto = texto.replace(ocorrencia, substituicao,1)
else:
        print(ocorrencia)
