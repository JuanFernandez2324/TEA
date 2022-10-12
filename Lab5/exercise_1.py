texto = "X-DSPAM-Confinde: 0.8475"
inicio = texto.find(":")
final = len(texto)
numero = texto[inicio:final]
print(inicio,final)
print(numero)
print(type(numero))
