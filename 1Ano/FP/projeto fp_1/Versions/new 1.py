import random

# Lista de palavras para o jogo da forca
palavras = ["python", "programacao", "computador", "jogo", "desenvolvimento"]

# Escolhe uma palavra aleatoriamente
palavra = random.choice(palavras).lower()  # Converte a palavra para minúsculas
letras_corretas = set()
letras_erradas = set()
tentativas_maximas = 7

def mostrar_forca(erros):
    desenho_forca = [
        """
           ______
          |      |
                 |
                 |
                 |
                 |
        """,
        """
           ______
          |      |
          O      |
                 |
                 |
                 |
        """,
        """
           ______
          |      |
          O      |
          |      |
                 |
                 |
        """,
        """
           ______
          |      |
          O      |
         /|      |
                 |
                 |
        """,
        """
           ______
          |      |
          O      |
         /|\\    |
                 |
                 |
        """,
        """
           ______
          |      |
          O      |
         /|\\    |
         /       |
                 |
        """,
        """
           ______
          |      |
          O      |
         /|\\    |
         / \\    |
                 |
        """
    ]

    return desenho_forca[erros]

def mostrar_palavra(palavra, letras_corretas):
    resultado = ''
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

def remove_acentos(palavra):
    # Função para remover acentos e cedilhas
    acentos = {'á': 'a', 'à': 'a', 'â': 'a', 'ã': 'a', 'é': 'e', 'è': 'e', 'ê': 'e', 'í': 'i', 'ì': 'i', 'î': 'i',
               'ó': 'o', 'ò': 'o', 'ô': 'o', 'õ': 'o', 'ú': 'u', 'ù': 'u', 'û': 'u', 'ç': 'c'}
    for acento, letra in acentos.items():
        palavra = palavra.replace(acento, letra)
    return palavra

while True:
    print("\n" + mostrar_forca(len(letras_erradas)))
    print(mostrar_palavra(palavra, letras_corretas))
    print("Letras erradas:", ' '.join(sorted(letras_erradas)))
    letras_restantes = set(palavra) - letras_corretas
    print("Letras restantes:", ' '.join(sorted(letras_restantes)))
    
    if mostrar_palavra(palavra, letras_corretas) == palavra:
        print("\nParabéns, você ganhou! A palavra era:", palavra)
        break
    
    if len(letras_erradas) == tentativas_maximas:
        print("\nVocê perdeu! A palavra era:", palavra)
        break

    letra = input("Adivinhe uma letra: ").lower()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Por favor, insira uma única letra válida.")
        continue
    
    letra = remove_acentos(letra)
    
    if letra in letras_corretas or letra in letras_erradas:
        print("Você já adivinhou esta letra.")
        continue
    
    if letra in palavra:
        letras_corretas.add(letra)
    else:
        letras_erradas.add(letra)
