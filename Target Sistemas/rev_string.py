def inverte_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

texto = input("Informe uma string: ")
print(f"String invertida: {inverte_string(texto)}")
