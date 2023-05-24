numero_registros = int(input())
dict_registros = {}

tempo_total = 0
tempo_amigo = 0

#  copia_registros = ""

amigos_recebidos = []
amigos_enviados = []
amigos_respondidos = set()
amigos_nao_respondidos = set()


while numero_registros > 0:
    registro = input()
#   copia_registros += registro + ","
    numero_registros -= 1

    chave, valor = registro.split()
    valor = int(valor)

    if chave not in dict_registros:
        dict_registros[chave] = []
    dict_registros[chave].append(valor)

for chave in dict_registros:  # Salva oq recebeu, oq enviou e o tempo

    if chave == "R":
        for valor in dict_registros[chave]:
            amigos_recebidos.append(valor)

    elif chave == "E":
        for valor in dict_registros[chave]:
            amigos_enviados.append(valor)

    else:
        for valor in dict_registros[chave]:
            tempo_total += valor

if len(amigos_recebidos) != len(amigos_enviados):  # Verifica se respondeu tudo q recebeu
    contador = 0

    for valor in amigos_recebidos:
        if valor in amigos_enviados and contador < len(amigos_enviados):
            amigos_enviados[contador] = amigos_enviados[contador] + 1
            amigos_respondidos.add(valor)
            contador += 1
        else:
            amigos_respondidos.remove(valor)
            amigos_nao_respondidos.add(valor)
            contador += 1

print(dict_registros)
print(tempo_total)
print(amigos_recebidos, amigos_enviados)
print(amigos_respondidos, amigos_nao_respondidos)

for valor in amigos_recebidos:
    print(valor, tempo_amigo)


"""
copia_registros = copia_registros.split(",")
copia_registros.pop()
print(copia_registros)

for valor in copia_registros:  # R 3
    if valor == "R" or "E":
        x = valor  # R 3
        copia_registros.remove(valor)  # registros sem R 3
        len(valor)
        if len == 3:
            for valor1 in copia_registros:
                if valor1 == "E" and x[2]:
                    print()
                else:
                    tempo_amigo += 1
            
# Vai remover todos os valores R, então é problema se ela enviar mais de uma mensagem
"""