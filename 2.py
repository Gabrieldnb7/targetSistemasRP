# Contador de caracter a em uma string

texto = str(input("Digite uma frase: "))
if "a"  in texto or "A"  in texto:
    print(f"O caractere A aparece {texto.count("A")} vezes")
    print(f"O caractere a aparece {texto.count("a")} vezes")
else:
    print("Os caracteres a e A não aparecem na frase.")