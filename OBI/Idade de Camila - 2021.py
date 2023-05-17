# Cibele = Mais velha
# Camila = Média
# Celeste = Mais nova

P1 = int(input())
P2 = int(input())
P3 = int(input())

if P1 == P2 == P3:  # Caso todas tenham a mesma idade
    Ca = P1
    print(Ca)

else:
    x = P1 + P2 + P3  # Todas as idades juntas

    Ci = 0
    Ce = 0

# Idade da mais nova

    if P1 < P2 and P1 < P3:
        Ce += P1
    elif P2 < P1 and P2 < P3:
        Ce += P2
    elif P3 < P1 and P3 < P2:
        Ce += P3
    elif P1 == P2 or P1 == P3:
        Ce += P1
    elif P2 == P1 or P2 == P3:
        Ce += P2
    elif P3 == P1 or P3 == P2:
        Ce += P3

# Idade da mais velha

    if P1 > P2 and P1 > P3:
        Ci += P1
    elif P2 > P1 and P2 > P3:
        Ci += P2
    elif P3 > P1 and P3 > P2:
        Ci += P3
    elif P1 == P2 or P1 == P3:
        Ce += P1
    elif P2 == P1 or P2 == P3:
        Ce += P2
    elif P3 == P1 or P3 == P2:
        Ce += P3

    y = Ce + Ci  # Idade da mais nova com a mais velha

    Ca = x - y   # Idade dela é a diferença da total - (a da mais nova + a da mais velha)

    print(Ca)
