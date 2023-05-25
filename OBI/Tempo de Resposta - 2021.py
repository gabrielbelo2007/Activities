numero_registros = int(input())
dict_registros = {}

tempo_total = 0
tempo_amigo = 0

contador = 0
contador1 = 2
copia_registros = []
copia_registros_num = []

amigos_recebidos = []
amigos_enviados = []
amigos_respondidos = set()
amigos_nao_respondidos = set()


while numero_registros > 0:
    registro = input()
    copia_registros += [registro]
    copia_registros_num += registro
    numero_registros -= 1

    chave, valor = registro.split()
    valor = int(valor)

    if chave not in dict_registros:
        dict_registros[chave] = []
    dict_registros[chave].append(valor)

for chave in dict_registros:  # Salva oq recebeu, oq enviou e o tempo

    if chave == "R":
        for recebido in dict_registros[chave]:
            amigos_recebidos.append(recebido)

    elif chave == "E":
        for enviado in dict_registros[chave]:
            amigos_enviados.append(enviado)

    else:
        for tempo in dict_registros[chave]:
            tempo_total += tempo

amigos_recebidos.sort()
amigos_enviados.sort()

if len(amigos_recebidos) != len(amigos_enviados):  # Verifica se respondeu tudo q recebeu
    indice = 0

    for valor in amigos_recebidos:
        if valor in amigos_enviados and indice < len(amigos_enviados):
            amigos_enviados[indice] = amigos_enviados[indice] + 1
            amigos_respondidos.add(valor)
            indice += 1
        else:
            amigos_respondidos.remove(valor)
            amigos_nao_respondidos.add(valor)
            indice += 1
else:
    amigos_respondidos = amigos_recebidos



x = 0
teste = []
z = copia_registros
while x < 1:
    numero_E = str(copia_registros_num[contador1])
    tamanho_registro = len(copia_registros[0])

    if tamanho_registro > 3:
        contador1 += 1
        numero_E += str(copia_registros_num[contador1])
        contador1 += 3
    else:
        contador1 += 3

    f = "E " + numero_E
    descontar_T = copia_registros_num.count("T")

    for valor in copia_registros:
        while valor != f:
            tempo_amigo += 1
            break
        else:
            if len(copia_registros) > 1:
                copia_registros.pop(0)
            tempo_amigo -= descontar_T
            tempo_amigo += tempo_total
    else:
        for amigo in amigos_recebidos:
            teste += amigo, tempo_amigo
            tempo_amigo = 0

if contador > len(z):
    x += 1


"""
print(dict_registros)
print(tempo_total)
print(amigos_recebidos, amigos_enviados)
print(amigos_respondidos, amigos_nao_respondidos)
"""
