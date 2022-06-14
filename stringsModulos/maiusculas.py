
def maiusculas(frase):
    count = ""
    for char in frase:
        if char.isupper():
            count += char
    return count


print(maiusculas(input()))