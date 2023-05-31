import copy

numero_registros = int(input())
dict_registros = {}

tempo_total = 0
tempo_amigo = 0

contador = 0
contador1 = 2
registros = []
registros_num = []

amigos_recebidos = []
amigos_enviados = []
amigos_respondidos = set()
amigos_nao_respondidos = set()

while numero_registros > 0:
    registro = input()
    registros += [registro]
    registros_num += registro
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

# Criar a lista com todos os amigos e seus tempos

copia_registros = copy.deepcopy(registros)  # Copia de todos os registros
lista_amigos_tempo = []

while len(copia_registros) > 0:
    letra_E = str(registros_num[contador])  # Confere a primeira letra de cada registro
    numero_E = str(registros_num[contador1])  # Confere o número do amigo de cada registro
    tamanho_registro = len(copia_registros[0])  # Confere o tamanho do registro, se amigo é 3 ou 30

    if tamanho_registro > 3:  # Caso o amigo seja com unidade e dezena
        contador += 4
        contador1 += 1
        numero_E += str(registros_num[contador1])
        contador1 += 3
    else:  # Caso o amigo seja só unidade
        contador += 3
        contador1 += 3

    f = "E " + numero_E  # Cria o registro de enviado com o número do amigo
    if letra_E == "E":  # Confere se o valor que está sendo chegado é um valor de enviado
        copia_registros.pop(0)
        continue

    descontar_T = registros_num.count("T")  # Retira os segundos adicionais quando o valor é T

    contar_E = copia_registros.count(f)  # Contar quantos Enviados teve para o msm amigo

    if numero_E in amigos_nao_respondidos:  # Confere se esse amigo foi respondido
        lista_amigos_tempo += numero_E, tempo_amigo
        if len(copia_registros) > 1:
            copia_registros.pop(0)
            continue

    else:
        while contar_E > 0:  # Conta quantos segundos teve para cada amigo
            for valor in copia_registros:
                if valor != f:
                    tempo_amigo += 1
                elif valor == f and contar_E > 1:
                    tempo_amigo += 1
                    contar_E -= 1
                elif contar_E == 1:
                    contar_E -= 1
                    break

        else:  # Adiciona na lista o amigo e o seu tempo
            if len(copia_registros) > 1:
                copia_registros.pop(0)
            tempo_amigo -= descontar_T
            tempo_amigo += tempo_total  # Precisa resolver esse tempo total !!!
            lista_amigos_tempo += [numero_E + " " + str(tempo_amigo)]
            tempo_amigo = 0

print(lista_amigos_tempo)
