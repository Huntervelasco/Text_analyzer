
def texto(text):
    text = text.lower().replace(",", " ").replace(".", " ").replace("?", " ").replace("¿", " ").replace("(", " ").replace(
        ")", " ").replace(":", " ").replace(
        ";", " ").replace("!", " ")
    text = text.split()
    return text


def contador_palabras(lista_palabras):
    word_count = {}

    for word in lista_palabras:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count



def palabra_mayor(diccionario):
    max_word = None
    max_count = 0
    for word in diccionario:
        if diccionario[word] > max_count:
            max_word = word
            max_count = diccionario[word]


    print(f"\nLa palabra mas repetida es: {max_word}")
    print(f"Numero de veces: {max_count}")








print("Bienvenidx!, Este es un analizador de texto...\n")
x = input("Ingresa el texto que analizaré...: ")

y = texto(x)
count = 0
for i in y:
    count += 1

print(f"\n--¡Texto analizado!---\nTotal de palabras : {count}\n")
conta = contador_palabras(y)
print("Frecuencia de cada palabra: ")
for word in conta:
    print(word, ":", conta[word])
palabra_mayor(conta)


